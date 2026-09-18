import bpy
import bpy.utils.previews
import os
from ..core.status_manager import status, ConnectionState
from ..utils.logger import logger
from ..utils.text_wrap import draw_wrapped_label
from .. import bl_info

STUDIO_URL = "https://studio.tripo3d.ai/workspace/generate"
TUTORIAL_URL = bl_info.get("doc_url", "")

# Sidebar chrome that eats into the width available to a label: the region
# margins the panel layout reserves plus the inset a box() draws with.
PANEL_MARGIN_PX = 28.0
BOX_INSET_PX = 14.0

_custom_icons = None


def _content_width_px(context):
    """Return the pixel width a label inside a panel box can use."""
    region = context.region
    ui_scale = context.preferences.system.ui_scale
    width = region.width if region else 200
    return max(40.0, width - (PANEL_MARGIN_PX + BOX_INSET_PX) * ui_scale)


class VIEW3D_PT_TripoPanel(bpy.types.Panel):
    bl_label = "Tripo bridge"
    bl_idname = "VIEW3D_PT_tripo"
    bl_space_type = 'VIEW_3D'         # Space type: 3D Viewport
    bl_region_type = 'UI'             # Region type: Sidebar
    bl_category = "Tripo"             # Tab name (right-side panel label)

    def draw(self, context):
        layout = self.layout
        ui_scale = context.preferences.system.ui_scale
        content_px = _content_width_px(context)

        # Tripo Studio link
        box = layout.box()
        row = box.row(align=True)

        global _custom_icons
        if _custom_icons and "tripo_icon" in _custom_icons:
            icon = _custom_icons["tripo_icon"].icon_id
            op = row.operator("wm.url_open", text=bpy.app.translations.pgettext("Open Tripo Studio"), icon_value=icon)
        else:
            op = row.operator("wm.url_open", text=bpy.app.translations.pgettext("Open Tripo Studio"), icon='WORLD')
        op.url = STUDIO_URL  # type: ignore

        # Tutorial link question-mark icon
        if TUTORIAL_URL:
            op = row.operator("wm.url_open", text="", icon='QUESTION')
            op.url = TUTORIAL_URL

        # Connection status
        box = layout.box()
        draw_wrapped_label(
            box, bpy.app.translations.pgettext("Connection Status:"), content_px, ui_scale
        )
        row = box.row()
        if status.state == ConnectionState.CONNECTED:
            row.alert = False
            state_text = bpy.app.translations.pgettext_iface("Connected", "Tripo bridge")
            state_icon = 'WORLD_DATA'
        elif status.state == ConnectionState.LISTENING:
            row.alert = False
            state_text = bpy.app.translations.pgettext_iface("Waiting for connection", "Tripo bridge")
            state_icon = 'REC'
        else:
            row.alert = True
            state_text = bpy.app.translations.pgettext_iface("Disconnected", "Tripo bridge")
            state_icon = 'CANCEL'
        draw_wrapped_label(row, state_text, content_px, ui_scale, icon=state_icon)

        if status.last_log:
            draw_wrapped_label(
                box, bpy.app.translations.pgettext("Last Log:"), content_px, ui_scale
            )
            log_text = bpy.app.translations.pgettext_iface(
                status.last_log, "Tripo bridge"
            ).format(**status.last_log_params)[:240]
            draw_wrapped_label(box, log_text, content_px, ui_scale)

classes = (
    VIEW3D_PT_TripoPanel,
)


def register():
    global _custom_icons
    _custom_icons = bpy.utils.previews.new()
    
    addon_dir = os.path.dirname(os.path.dirname(__file__))
    icons_dir = os.path.join(addon_dir, "assets")
    icon_path = os.path.join(icons_dir, "logo.png")
    
    if os.path.exists(icon_path):
        _custom_icons.load("tripo_icon", icon_path, 'IMAGE')
        logger.debug(f"Custom icon loaded: {icon_path}")
    else:
        logger.warning(f"Icon file not found: {icon_path}")
    
    for cls in classes:
        bpy.utils.register_class(cls)
    logger.debug("Sidebar panel registered.")


def unregister():
    global _custom_icons
    if _custom_icons:
        bpy.utils.previews.remove(_custom_icons)
        _custom_icons = None
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    logger.debug("Sidebar panel unregistered.")
