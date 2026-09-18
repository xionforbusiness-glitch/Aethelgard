import bpy
import json
import shutil

import time
import uuid

from pathlib import Path
from hashlib import md5
from ..utils.logger import logger


class ModelImporter:
    """Imports 3D model files in various formats."""
    
    SUPPORTED_FORMATS = {
        'obj', 'fbx', 'glb', 'gltf', 'usdz', 'stl'
    }
    
    IMAGE_FORMATS = {
        'png', 'jpg', 'jpeg', 'tga', 'bmp', 'tiff', 'exr'
    }
    
    @classmethod
    def import_model(cls, file_path, file_format, model_name=None):
        """Import a model file according to its format."""
        file_path = Path(file_path)
        
        if not file_path.exists():
            raise FileNotFoundError(f"Model file does not exist: {file_path}")
        
        # Record objects present before the import
        previous_objects = set(bpy.data.objects)
        previous_images = set(bpy.data.images)
        
        try:
            if file_format == "obj":
                bpy.ops.wm.obj_import(filepath=str(file_path))
            elif file_format in {"gltf", "glb"}:
                bpy.ops.import_scene.gltf(filepath=str(file_path))
            elif file_format == "fbx":
                cls._import_fbx_safe(file_path, previous_objects)
            elif file_format == "stl":
                bpy.ops.wm.stl_import(filepath=str(file_path))
            elif file_format == "usdz":
                cls._import_usdz_safe(file_path, previous_images)
            else:
                raise ValueError(f"Unsupported format: {file_format}")
                
        except Exception as e:
            logger.error(f"Failed to import model {file_path}: {e}")
            return None, []
        
        # Collect objects and images added by the import
        new_objects = list(set(bpy.data.objects) - previous_objects)
        new_images = list(set(bpy.data.images) - previous_images)

        # Replace the wrapper root node name with the frontend-supplied model name;
        # child node names are not affected.
        cls._rename_imported_root(new_objects, model_name)

        # Fix material color-space settings on the imported objects
        cls._fix_material_colorspaces(new_objects)
        
        return new_objects, new_images

    @classmethod
    def _rename_imported_root(cls, objects, model_name):
        """Rename the imported wrapper root node to the model name provided by the frontend."""
        if not isinstance(model_name, str) or not model_name.strip():
            logger.warning(f"Skipping imported root rename: invalid model name {model_name!r}")
            return

        desired_name = model_name.strip()
        imported_objects = set(objects)
        root_objects = [
            obj for obj in objects
            if obj.parent is None or obj.parent not in imported_objects
        ]

        def is_parent_node(obj):
            return obj.name == "ParentNode" or obj.name.startswith("ParentNode.")

        parent_node_roots = [obj for obj in root_objects if is_parent_node(obj)]
        parent_nodes = [obj for obj in objects if is_parent_node(obj)]

        logger.info(
            f"Resolving imported root name {desired_name!r}: "
            f"objects={[obj.name for obj in objects]}, "
            f"top-level={[obj.name for obj in root_objects]}"
        )

        if len(parent_node_roots) == 1:
            root = parent_node_roots[0]
        elif len(root_objects) == 1:
            root = root_objects[0]
        elif len(parent_nodes) == 1:
            root = parent_nodes[0]
            logger.warning(
                f"Using non-top-level ParentNode as imported root: {root.name}"
            )
        else:
            logger.warning(
                "Could not identify a unique imported root node; "
                f"keeping original names for {len(root_objects)} top-level objects"
            )
            return

        original_name = root.name
        root.name = desired_name
        logger.info(
            f"Renamed imported root: {original_name!r} -> {root.name!r} "
            f"(requested: {desired_name!r})"
        )
    
    @classmethod
    def _import_fbx_safe(cls, fbx_path, previous_objects):
        """Import an FBX file safely, shrinking empty-node display sizes."""

        bpy.ops.import_scene.fbx(filepath=str(fbx_path))
        
        new_objects = list(set(bpy.data.objects) - previous_objects)
        
        for obj in new_objects:
            if obj.type == 'EMPTY':
                obj.empty_display_size = 0.0001
                logger.debug(f"Set empty display size to 0.0001 for: {obj.name}")
    
    @classmethod
    def _import_usdz_safe(cls, usdz_path, previous_images):
        """Import a USDZ file safely, removing spurious empty objects."""
        # Save the current environment texture
        original_env = cls._get_current_environment_texture()

        # Import the USDZ
        texture_dir = usdz_path.with_suffix("")
        bpy.ops.wm.usd_import(
            filepath=str(usdz_path),
            import_textures_mode="IMPORT_COPY",
            import_textures_dir=str(texture_dir)
        )
        
        # Collect images added by the import
        new_images = list(set(bpy.data.images) - previous_images)

        # Remove spurious empty objects and process textures
        cls._cleanup_imported_scene(original_env, new_images)
    
    @classmethod
    def _get_current_environment_texture(cls):
        """Return the environment texture currently used by any scene world, or None."""
        for scene in bpy.data.scenes:
            if scene.world and scene.world.use_nodes and scene.world.node_tree:
                for node in scene.world.node_tree.nodes:
                    if node.type == 'TEX_ENVIRONMENT' and node.image:
                        return node.image
        return None
    
    @classmethod
    def _cleanup_imported_scene(cls, original_env_texture, new_images=None):
        """Clean up the imported scene: remove empty objects and process textures."""
        # Find and remove parentless empty objects
        imported_objects = [obj for obj in bpy.data.objects if obj.parent is None]
        
        for obj in imported_objects[:]:
            if obj.type == 'EMPTY' and not obj.children:
                logger.info(f"Removing empty object: {obj.name}")
                bpy.data.objects.remove(obj, do_unlink=True)
        
        # Process newly imported textures
        cls._process_imported_textures(original_env_texture, new_images)
    
    @classmethod
    def _process_imported_textures(cls, original_env_texture, new_images=None):
        """Process imported texture assets: rename files and pack into the blend."""
        # Only process newly imported images; fall back to all images for backwards compatibility.
        images_to_process = new_images if new_images is not None else bpy.data.images
        
        for image in images_to_process:
            if not image.filepath:
                continue
                
            # Skip the environment texture
            if image == original_env_texture:
                continue

            # Handle HDR files
            if image.filepath.lower().endswith('.hdr'):
                cls._handle_hdr_texture(image, original_env_texture)
                continue

            # Rename other textures to avoid name conflicts
            cls._rename_texture_file(image)

        # Pack all assets
        bpy.ops.file.pack_all()
        logger.info("Assets packaged into Blend file")
    
    @classmethod
    def _handle_hdr_texture(cls, hdr_image, original_env):
        """Remove an imported HDR texture that should not override the existing environment."""
        if hdr_image != original_env:
            logger.info(f"Removing imported HDR texture: {hdr_image.name}")
            # Clear material references before removing the image
            for material in bpy.data.materials:
                if material.use_nodes and material.node_tree:
                    for node in material.node_tree.nodes:
                        if node.type == 'TEX_ENVIRONMENT' and node.image == hdr_image:
                            node.image = None
            bpy.data.images.remove(hdr_image)
    
    @classmethod
    def _rename_texture_file(cls, image):
        """Rename a texture file with a short UUID prefix to avoid name collisions."""
        import re

        try:
            original_path = Path(bpy.path.abspath(image.filepath))

            # Skip paths that are too long to rename safely
            if len(str(original_path)) > 240:
                logger.warning(f"Path too long, skipping rename: {original_path.name}")
                return

            if not original_path.exists():
                logger.warning(f"Texture file does not exist, skipping: {original_path.name}")
                return

            # Already renamed: filename starts with 8 hex chars + underscore
            if re.match(r'^[0-9a-f]{8}_', original_path.name):
                logger.debug(f"Texture already renamed, skipping: {original_path.name}")
                return

            # Generate a new name using an 8-char short UUID prefix
            new_name = f"{uuid.uuid4().hex[:8]}_{original_path.name}"
            new_path = original_path.parent / new_name

            # Move the file and update Blender's reference
            shutil.move(str(original_path), str(new_path))
            image.filepath = str(new_path)
            image.name = new_name
            image.reload()

            logger.info(f"Texture renamed: {original_path.name} → {new_name}")
            
        except OSError as e:
            logger.error(f"File system error, rename failed for {image.name}: {e}")
        except Exception as e:
            logger.error(f"Failed to rename texture {image.name}: {e}")
    
    @classmethod
    def _fix_material_colorspaces(cls, objects):
        """Correct color-space settings on all image textures connected to imported materials."""
        COLOR_INPUTS = {"Base Color", "Emission"}
        DATA_INPUTS = {"Roughness", "Metallic", "Normal", "Alpha", "Specular"}

        def find_image_node(socket, visited=None):
            """Recursively walk upstream links to find the TEX_IMAGE node driving *socket*."""
            if visited is None:
                visited = set()

            if not socket or not socket.is_linked:
                return None

            link = socket.links[0]
            node = link.from_node

            if node in visited:
                return None
            visited.add(node)

            if node.type == 'TEX_IMAGE':
                return node

            # Recurse into the node's inputs
            for inp in node.inputs:
                img_node = find_image_node(inp, visited)
                if img_node:
                    return img_node

            return None

        for obj in objects:
            if not obj.data or not hasattr(obj.data, 'materials'):
                continue

            for mat in obj.data.materials:
                if not mat or not mat.use_nodes or not mat.node_tree:
                    continue

                principled_node = next(
                    (n for n in mat.node_tree.nodes if n.type == 'BSDF_PRINCIPLED'),
                    None
                )

                if not principled_node:
                    continue

                # Walk each Principled BSDF input and correct color-space
                for socket in principled_node.inputs:
                    img_node = find_image_node(socket)
                    if not img_node or not img_node.image:
                        continue
                    
                    img = img_node.image
                    socket_name = socket.name
                    
                    if socket_name in COLOR_INPUTS:
                        if img.colorspace_settings.name != 'sRGB':
                            img.colorspace_settings.name = 'sRGB'
                            logger.info(f"  {socket_name} → {img.name}: sRGB")
                    elif socket_name in DATA_INPUTS:
                        if img.colorspace_settings.name != 'Non-Color':
                            img.colorspace_settings.name = 'Non-Color'
                            logger.info(f"  {socket_name} → {img.name}: Non-Color")


class ModelCacheManager:
    """Manages the temporary cache directory used for in-flight model files."""

    def __init__(self, cache_dir=None):
        self.cache_dir = Path(cache_dir) if cache_dir else Path(bpy.app.tempdir)

    def save_file(self, filename, content):
        """Write *content* to the cache directory and return the resulting path."""
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        file_path = self.cache_dir / filename
        file_path.write_bytes(content)
        return file_path

    def cleanup_file(self, file_path, max_retries=5):
        """Delete a cached file, retrying on transient PermissionError."""
        for attempt in range(max_retries):
            try:
                Path(file_path).unlink(missing_ok=True)
                break
            except PermissionError:
                if attempt < max_retries - 1:
                    time.sleep(0.1)
                else:
                    logger.warning(f"Could not delete cache file: {file_path}")

    def save_event_cache(self, event_data):
        """Persist event data to the cache directory as JSON."""
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        cache_file = self.cache_dir / "model_event_cache.json"
        cache_file.write_text(json.dumps(event_data, indent=2))
        return cache_file


class MaterialBuilder:
    """Builds PBR materials from a set of texture images."""

    @staticmethod
    def create_pbr_material(obj, texture_images, material_name=None):
        """Create and assign a PBR material with the given textures to *obj*."""
        if not obj or not texture_images:
            return None

        if material_name is None:
            material_name = f"pbr_{md5(obj.name.encode()).hexdigest()[:8]}"

        # Create new material
        material = bpy.data.materials.new(name=material_name)
        material.use_nodes = True

        # Clear default nodes
        node_tree = material.node_tree
        if not node_tree:
            return None
        node_tree.nodes.clear()

        # Create nodes
        bsdf_node = node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
        output_node = node_tree.nodes.new(type='ShaderNodeOutputMaterial')

        # Position nodes
        bsdf_node.location = (0, 0)
        output_node.location = (300, 0)

        # Link nodes
        node_tree.links.new(bsdf_node.outputs['BSDF'], output_node.inputs['Surface'])

        # Add texture nodes
        texture_nodes = {}
        texture_types = {
            'diffuse': ('Base Color', 'RGBA'),
            'albedo': ('Base Color', 'RGBA'),
            'basecolor': ('Base Color', 'RGBA'),
            'metallic': ('Metallic', 'VALUE'),
            'roughness': ('Roughness', 'VALUE'),
            'normal': ('Normal', 'VECTOR')
        }

        y_offset = 0
        for texture_type, (input_name, socket_type) in texture_types.items():
            texture_node = node_tree.nodes.new(type='ShaderNodeTexImage')
            texture_node.location = (-300, y_offset)
            texture_nodes[texture_type] = texture_node
            y_offset -= 280

            # Wire to the corresponding BSDF input
            if socket_type == 'VECTOR' and input_name == 'Normal':
                normal_map_node = node_tree.nodes.new(type='ShaderNodeNormalMap')
                normal_map_node.location = (-100, y_offset + 140)
                node_tree.links.new(texture_node.outputs['Color'], normal_map_node.inputs['Color'])
                node_tree.links.new(normal_map_node.outputs['Normal'], bsdf_node.inputs[input_name])
            else:
                node_tree.links.new(texture_node.outputs[socket_type], bsdf_node.inputs[input_name])

        # Assign textures
        MaterialBuilder._assign_textures(texture_nodes, texture_images)

        # Apply to object
        if obj.data.materials:
            obj.data.materials[0] = material
        else:
            obj.data.materials.append(material)

        return material

    @staticmethod
    def _assign_textures(texture_nodes, texture_images):
        """Match texture images to node slots by filename keywords."""
        texture_mappings = {
            'diffuse': ['diffuse', 'albedo', 'basecolor', 'color'],
            'metallic': ['metallic', 'metalness'],
            'roughness': ['roughness', 'gloss'],
            'normal': ['normal', 'normals']
        }

        # These texture types must use Non-Color color-space
        non_color_types = {'metallic', 'roughness', 'normal'}

        for image in texture_images:
            image_name_lower = image.name.lower()

            for texture_type, keywords in texture_mappings.items():
                if texture_type in texture_nodes:
                    if any(keyword in image_name_lower for keyword in keywords):
                        texture_nodes[texture_type].image = image
                        # Set color-space
                        if texture_type in non_color_types:
                            image.colorspace_settings.name = 'Non-Color'
                        break


class ModelLoader:
    """Top-level loader: routes files to the right importer and manages the cache."""

    def __init__(self, cache_manager=None):
        self.cache_manager = cache_manager or ModelCacheManager()

    def _import_model_file(self, file_path, file_format, model_name=None):
        """Import a model file and return the first resulting object."""
        objects, _images = ModelImporter.import_model(file_path, file_format, model_name)
        if objects:
            return objects[0]
        return None

    def _import_image_file(self, file_path):
        """Load an image into Blender's data block."""
        try:
            return bpy.data.images.load(str(file_path))
        except Exception as e:
            logger.error(f"Failed to load image {file_path}: {e}")
            return None

    def _is_model_file(self, file_data):
        """Return True if *file_data* describes a supported model format."""
        fmt = file_data['format'].lower()
        return fmt in ModelImporter.SUPPORTED_FORMATS

    def _is_image_file(self, file_data):
        """Return True if *file_data* describes a supported image format."""
        fmt = file_data['format'].lower()
        return fmt in ModelImporter.IMAGE_FORMATS

    def load_from_bytes(self, data_bytes: bytes, filename: str, file_format: str, md5_hex: str | None = None):
        """Load a model from raw bytes.

        Must be called from the Blender main thread (schedule via
        bpy.app.timers.register). Writes the data to the cache then delegates
        to the existing import logic.
        """
        file_path = None
        try:
            # Write to the cache directory
            file_path = self.cache_manager.save_file(filename, data_bytes)

            # Optional MD5 integrity check
            if md5_hex:
                import hashlib
                if hashlib.md5(data_bytes).hexdigest() != md5_hex:
                    raise ValueError("MD5 mismatch for binary payload")

            file_format = file_format.lower()
            if file_format not in ModelImporter.SUPPORTED_FORMATS:
                raise ValueError(f"Unsupported format: {file_format}")

            ModelImporter.import_model(file_path, file_format)

        except Exception as e:
            logger.error(f"load_from_bytes failed for {filename}: {e}")
            raise
        finally:
            # Clean up the temporary cache file
            if file_path is not None:
                try:
                    self.cache_manager.cleanup_file(file_path)
                except Exception:
                    pass

loader = ModelLoader()
