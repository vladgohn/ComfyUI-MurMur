class MurmurPicker:
    CATEGORY = "MURMUR"
    FUNCTION = "pass_hex"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("hex",)
    OUTPUT_NODE = False

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "hex": (
                    "STRING",
                    {
                        "default": "#4F86F7",
                        "multiline": False,
                    },
                ),
            }
        }

    @classmethod
    def IS_CHANGED(cls, hex):
        return hex

    def pass_hex(self, hex):
        value = str(hex or "").strip() or "#4F86F7"
        if not value.startswith("#"):
            value = f"#{value}"
        return (value,)
