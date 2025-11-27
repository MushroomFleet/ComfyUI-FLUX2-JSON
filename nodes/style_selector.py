"""
FLUX2_StyleSelector - Choose artistic style and rendering approach
"""

from .base import FLUX2BaseNode, FLUX2Presets


class FLUX2_StyleSelector(FLUX2BaseNode):
    """
    Choose artistic style and rendering approach.
    Controls how the image is rendered and its aesthetic direction.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        style_categories = ["Custom"] + list(FLUX2Presets.STYLE_CATEGORIES.keys())
        
        return {
            "required": {
                "style_category": (style_categories, {
                    "default": "Photorealistic"
                }),
            },
            "optional": {
                "style_preset": ([""], {
                    "default": ""
                }),
                "custom_style": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "Enter custom style description..."
                }),
                "quality_level": (["", "Commercial quality", "Editorial quality", "Artistic expression", "Experimental"], {
                    "default": ""
                }),
                "additional_modifiers": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "Additional style details (optional)..."
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("style",)
    FUNCTION = "select_style"
    
    CATEGORY = "FLUX2_Prompt_Builder/Core"
    
    def select_style(self,
                    style_category="Photorealistic",
                    style_preset="",
                    custom_style="",
                    quality_level="",
                    additional_modifiers=""):
        """
        Build style description from selections.
        
        Args:
            style_category: Main style category
            style_preset: Specific preset within category
            custom_style: Custom style description
            quality_level: Quality/finish level
            additional_modifiers: Extra style details
        
        Returns:
            Complete style description string
        """
        
        # Start with base style
        if style_category == "Custom":
            if not custom_style:
                style = "Professional rendering"
            else:
                style = custom_style.strip()
        else:
            # Get presets for this category
            presets = FLUX2Presets.STYLE_CATEGORIES.get(style_category, [])
            
            if style_preset and presets:
                # Try to find matching preset
                matching = [p for p in presets if style_preset.lower() in p.lower()]
                if matching:
                    style = matching[0]
                elif presets:
                    style = presets[0]  # Default to first preset
                else:
                    style = f"{style_category} style"
            elif presets:
                style = presets[0]  # Default to first preset
            else:
                style = f"{style_category} style"
        
        # Add quality level if specified
        if quality_level:
            style = f"{style}, {quality_level.lower()}"
        
        # Add additional modifiers
        if additional_modifiers:
            style = f"{style}, {additional_modifiers.strip()}"
        
        return (style,)
    
    @classmethod
    def get_style_presets(cls, style_category):
        """Get available presets for a category (for UI updates)"""
        return FLUX2Presets.STYLE_CATEGORIES.get(style_category, [])


# For display in UI
FLUX2_StyleSelector.DESCRIPTION = """
Choose artistic style and rendering approach.

Categories:
- Photorealistic: Commercial, editorial, documentary photography
- Film Photography: Analog film stocks and vintage cameras
- Digital Eras: Modern digital, 2000s digicam, 90s aesthetic
- Artistic: Painting styles, illustrations, minimalist design
- Cinematic: Movie-inspired looks and dramatic lighting
- Technical: Blueprint, scientific, x-ray, infrared

Add quality level and modifiers for fine control.

Output: Style description string for prompt assembly
"""


# Extended style selector with dynamic preset loading
class FLUX2_StyleSelectorAdvanced(FLUX2BaseNode):
    """
    Advanced style selector with dynamic preset updates.
    Automatically updates available presets based on category selection.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "style_category": (list(FLUX2Presets.STYLE_CATEGORIES.keys()), {
                    "default": "Photorealistic"
                }),
                "preset_index": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 10,
                    "step": 1
                }),
            },
            "optional": {
                "custom_override": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "Override with custom style..."
                }),
                "quality_suffix": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "e.g., 'with commercial quality'"
                }),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("style", "preset_list")
    FUNCTION = "select_style_advanced"
    
    CATEGORY = "FLUX2_Prompt_Builder/Core"
    
    def select_style_advanced(self,
                            style_category="Photorealistic",
                            preset_index=0,
                            custom_override="",
                            quality_suffix=""):
        """
        Advanced style selection with preset info.
        
        Returns both the selected style and a list of available presets.
        """
        
        # If custom override provided, use it
        if custom_override:
            style = custom_override.strip()
            if quality_suffix:
                style = f"{style}, {quality_suffix.strip()}"
            preset_list = "Custom style"
            return (style, preset_list)
        
        # Get presets for category
        presets = FLUX2Presets.STYLE_CATEGORIES.get(style_category, [])
        
        if not presets:
            style = f"{style_category} style"
            preset_list = "No presets available"
        else:
            # Clamp index to valid range
            idx = max(0, min(preset_index, len(presets) - 1))
            style = presets[idx]
            
            # Add quality suffix if provided
            if quality_suffix:
                style = f"{style}, {quality_suffix.strip()}"
            
            # Create preset list for reference
            preset_list = "\n".join([f"{i}: {p[:60]}..." if len(p) > 60 else f"{i}: {p}" 
                                    for i, p in enumerate(presets)])
        
        return (style, preset_list)
