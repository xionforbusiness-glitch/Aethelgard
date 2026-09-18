"""Internationalisation (i18n) support module."""
import bpy
from .dictionary import dictionary


def register():
    # Registered unconditionally: Blender picks the matching language itself and
    # falls back to the English msgids when there is no entry for the current one.
    try:
        bpy.app.translations.register(__name__, dictionary)
    except Exception as e:
        print(f"Tripo bridge: Failed to register translations: {e}")


def unregister():
    try:
        bpy.app.translations.unregister(__name__)
    except Exception:
        pass
