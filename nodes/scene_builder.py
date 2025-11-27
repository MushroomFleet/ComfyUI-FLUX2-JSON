"""
FLUX2_SceneBuilder - Define the overall scene context and environment
"""

from .base import FLUX2BaseNode, FLUX2Presets


class FLUX2_SceneBuilder(FLUX2BaseNode):
    """
    Define the overall scene context and environment.
    Sets the foundational setting for your image.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        scene_type_options = ["Custom"] + list(FLUX2Presets.SCENE_TYPES.keys())
        
        return {
            "required": {
                "scene_type": (scene_type_options, {
                    "default": "Custom"
                }),
            },
            "optional": {
                "custom_description": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "Enter custom scene description..."
                }),
                "environment_details": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "Additional environmental details (optional)..."
                }),
                "time_of_day": (["", "Morning", "Afternoon", "Evening", "Night", "Golden Hour", "Blue Hour", "Custom"], {
                    "default": ""
                }),
                "custom_time_of_day": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "Enter custom time of day..."
                }),
                "weather": (["", "Clear", "Cloudy", "Overcast", "Rainy", "Foggy", "Snowy", "Custom"], {
                    "default": ""
                }),
                "custom_weather": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "Enter custom weather conditions..."
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("scene",)
    FUNCTION = "build_scene"
    
    CATEGORY = "FLUX2_Prompt_Builder/Core"
    
    def build_scene(self, 
                    scene_type="Custom",
                    custom_description="",
                    environment_details="",
                    time_of_day="",
                    custom_time_of_day="",
                    weather="",
                    custom_weather=""):
        """
        Build scene description from inputs.
        
        Args:
            scene_type: Preset scene type or Custom
            custom_description: Custom scene description (used if scene_type is Custom)
            environment_details: Additional environmental context
            time_of_day: Time of day setting
            custom_time_of_day: Custom time of day (used when time_of_day is "Custom")
            weather: Weather conditions
            custom_weather: Custom weather description (used when weather is "Custom")
        
        Returns:
            Complete scene description string
        """
        
        # Start with base scene description
        if scene_type == "Custom":
            if not custom_description:
                scene = "General scene"
            else:
                scene = custom_description.strip()
        else:
            # Use preset
            scene = FLUX2Presets.SCENE_TYPES.get(scene_type, "")
        
        # Build additional context parts
        context_parts = []
        
        # Handle time of day - use custom_time_of_day if "Custom" is selected
        final_time = custom_time_of_day.strip() if time_of_day == "Custom" else time_of_day
        if final_time:
            context_parts.append(f"{final_time.lower()} lighting")
        
        # Handle weather - use custom_weather if "Custom" is selected
        final_weather = custom_weather.strip() if weather == "Custom" else weather
        if final_weather:
            context_parts.append(f"{final_weather.lower()} conditions")
        
        if environment_details:
            context_parts.append(environment_details.strip())
        
        # Combine scene with context
        if context_parts:
            context = ", ".join(context_parts)
            scene = f"{scene}, {context}"
        
        return (scene,)
    
    @classmethod
    def VALIDATE_INPUTS(cls, scene_type, custom_description, **kwargs):
        """Validate that custom scenes have descriptions"""
        if scene_type == "Custom" and not custom_description:
            return "Custom scene type requires a custom_description"
        return True
    
    # Description for display in UI
    DESCRIPTION = """
Define the overall scene context and environment.

Use presets for common scene types or create custom descriptions.
Add environmental details like time of day and weather for more control.

Examples:
- Studio: Professional photography studio setup
- Interior: Indoor residential or commercial space
- Exterior: Outdoor location with natural elements
- Custom: Your own unique scene description

Output: Scene description string for prompt assembly
"""
