WEB_DIRECTORY = "js"

from .murmur_picker import MurmurPicker

NODE_CLASS_MAPPINGS = {
    "MurmurPicker": MurmurPicker,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MurmurPicker": "🫳 MURMUR Picker",
}

__all__ = [
    "WEB_DIRECTORY",
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]
