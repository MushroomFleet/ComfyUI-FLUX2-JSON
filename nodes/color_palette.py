"""
FLUX2_ColorPalette - Create color palettes from hex color codes
"""

from .base import FLUX2BaseNode, FLUX2Types


class FLUX2_ColorPalette(FLUX2BaseNode):
    """
    Create a color palette from up to 4 hex color codes.
    Output is compatible with prompt_assembler's color_palette input.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "color_1": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "e.g., #FF0000 or FF0000"
                }),
                "color_2": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "e.g., #00FF00 or 00FF00"
                }),
                "color_3": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "e.g., #0000FF or 0000FF"
                }),
                "color_4": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "e.g., #FFFF00 or FFFF00"
                }),
            }
        }
    
    RETURN_TYPES = (FLUX2Types.COLOR_ARRAY, "STRING")
    RETURN_NAMES = ("color_palette", "palette_preview")
    FUNCTION = "create_palette"
    
    CATEGORY = "FLUX2_Prompt_Builder/Utilities"
    
    def create_palette(self,
                      color_1="",
                      color_2="",
                      color_3="",
                      color_4=""):
        """
        Create a color palette from hex color inputs.
        
        Args:
            color_1: First hex color
            color_2: Second hex color
            color_3: Third hex color
            color_4: Fourth hex color
        
        Returns:
            Tuple of (color_array, preview_string)
        """
        
        colors = []
        invalid_colors = []
        
        # Process each color input
        for i, color in enumerate([color_1, color_2, color_3, color_4], 1):
            if not color or not color.strip():
                continue
            
            color = color.strip()
            
            # Validate the color
            if self.validate_hex_color(color):
                # Format and add to palette
                formatted = self.format_hex_color(color)
                colors.append(formatted)
            else:
                # Track invalid colors for preview
                invalid_colors.append(f"Color {i}: '{color}' (invalid)")
        
        # Create preview string
        if colors:
            preview_lines = [f"Valid colors ({len(colors)}):"]
            preview_lines.extend([f"  {i+1}. {color}" for i, color in enumerate(colors)])
        else:
            preview_lines = ["No valid colors provided"]
        
        if invalid_colors:
            preview_lines.append("\nInvalid colors skipped:")
            preview_lines.extend([f"  {ic}" for ic in invalid_colors])
        
        preview = "\n".join(preview_lines)
        
        # Return empty list if no valid colors
        if not colors:
            colors = []
        
        return (colors, preview)
    
    # Description for display in UI
    DESCRIPTION = """
Create a color palette from hex color codes.

Input Format:
- Accepts hex colors with or without # prefix
- Examples: #FF0000, FF0000, #f00, f00
- 3-digit (#RGB) or 6-digit (#RRGGBB) formats supported

The palette will:
- Automatically validate each color
- Format with # prefix and uppercase
- Skip empty or invalid colors
- Output as COLOR_ARRAY for prompt_assembler

Connect output to prompt_assembler's color_palette input.
"""


# Preset color palette builder
class FLUX2_ColorPalettePreset(FLUX2BaseNode):
    """
    Quick color palette selection from common presets.
    Pre-defined palettes for common color schemes.
    """
    
    # Common color palette presets
    PALETTE_PRESETS = {
        "Vibrant Primary": ["#FF0000", "#00FF00", "#0000FF", "#FFFF00"],
        "Pastel Spring": ["#FFB3BA", "#BAFFC9", "#BAE1FF", "#FFFFBA"],
        "Earth Tones": ["#8B4513", "#D2691E", "#CD853F", "#DEB887"],
        "Ocean Blues": ["#000080", "#0000CD", "#4169E1", "#87CEEB"],
        "Sunset Warm": ["#FF4500", "#FF6347", "#FFD700", "#FFA500"],
        "Monochrome Gray": ["#2F2F2F", "#5F5F5F", "#8F8F8F", "#CFCFCF"],
        "Neon Cyberpunk": ["#FF00FF", "#00FFFF", "#FF0080", "#8000FF"],
        "Forest Green": ["#228B22", "#32CD32", "#90EE90", "#98FB98"],
        "Royal Purple": ["#4B0082", "#8B008B", "#9370DB", "#DDA0DD"],
        "Fire Red": ["#8B0000", "#DC143C", "#FF6347", "#FFA07A"],
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (list(cls.PALETTE_PRESETS.keys()), {
                    "default": "Vibrant Primary"
                }),
            }
        }
    
    RETURN_TYPES = (FLUX2Types.COLOR_ARRAY, "STRING")
    RETURN_NAMES = ("color_palette", "palette_info")
    FUNCTION = "load_preset"
    
    CATEGORY = "FLUX2_Prompt_Builder/Utilities"
    
    def load_preset(self, preset="Vibrant Primary"):
        """Load a preset color palette."""
        colors = self.PALETTE_PRESETS.get(preset, [])
        
        # Create info string
        info_lines = [f"Preset: {preset}"]
        info_lines.append(f"Colors ({len(colors)}):")
        info_lines.extend([f"  {i+1}. {color}" for i, color in enumerate(colors)])
        info = "\n".join(info_lines)
        
        return (colors, info)
    
    # Description for display in UI
    DESCRIPTION = """
Quick color palette selection from presets.

Available Presets:
- Vibrant Primary: Bold primary colors
- Pastel Spring: Soft, gentle tones
- Earth Tones: Natural browns and tans
- Ocean Blues: Cool water-inspired blues
- Sunset Warm: Warm oranges and yellows
- Monochrome Gray: Grayscale palette
- Neon Cyberpunk: Bright neon colors
- Forest Green: Natural greens
- Royal Purple: Rich purple tones
- Fire Red: Warm red spectrum

Connect output to prompt_assembler's color_palette input.
"""
