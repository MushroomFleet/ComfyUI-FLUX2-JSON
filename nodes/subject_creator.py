"""
FLUX2_SubjectCreator - Define individual subjects with detailed properties
"""

from .base import FLUX2BaseNode, FLUX2Types, FLUX2Presets


class FLUX2_SubjectCreator(FLUX2BaseNode):
    """
    Create individual subject objects with detailed specifications.
    Each subject can have description, position, action, pose, and colors.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        # Get position vocabulary for hints
        positions = FLUX2Presets.POSITION_VOCABULARY
        
        return {
            "required": {
                "description": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "Detailed subject description (e.g., 'Minimalist ceramic coffee mug with matte finish')"
                }),
            },
            "optional": {
                "position": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "e.g., 'Center foreground', 'Left side midground'"
                }),
                "position_horizontal": ([""] + positions["horizontal"], {
                    "default": ""
                }),
                "position_vertical": ([""] + positions["vertical"], {
                    "default": ""
                }),
                "position_depth": ([""] + positions["depth"], {
                    "default": ""
                }),
                "action": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "What the subject is doing (e.g., 'Walking toward camera')"
                }),
                "pose": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "Static positioning (e.g., 'Standing upright', 'Leaning against wall')"
                }),
                "color_1": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "#HEXCODE or color name"
                }),
                "color_2": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "#HEXCODE or color name"
                }),
                "color_3": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "#HEXCODE or color name"
                }),
                "color_4": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "#HEXCODE or color name"
                }),
            }
        }
    
    RETURN_TYPES = (FLUX2Types.SUBJECT_OBJECT,)
    RETURN_NAMES = ("subject",)
    FUNCTION = "create_subject"
    
    CATEGORY = "FLUX2_Prompt_Builder/Subjects"
    
    def create_subject(self,
                      description,
                      position="",
                      position_horizontal="",
                      position_vertical="",
                      position_depth="",
                      action="",
                      pose="",
                      color_1="",
                      color_2="",
                      color_3="",
                      color_4=""):
        """
        Create a subject object with all specified properties.
        
        Args:
            description: Detailed subject description (required)
            position: Manual position description (overrides helpers)
            position_horizontal: Horizontal position helper
            position_vertical: Vertical position helper
            position_depth: Depth position helper
            action: Dynamic action description
            pose: Static pose description
            color_1-4: Color specifications (hex or names)
        
        Returns:
            Subject object dictionary
        """
        
        if not description or not description.strip():
            raise ValueError("Subject description is required")
        
        # Build position from helpers if manual position not provided
        final_position = position.strip() if position else ""
        
        if not final_position:
            # Build from position helpers
            position_parts = []
            if position_horizontal:
                position_parts.append(position_horizontal)
            if position_vertical:
                position_parts.append(position_vertical)
            if position_depth:
                position_parts.append(position_depth)
            
            if position_parts:
                final_position = " ".join(position_parts)
        
        # Collect colors
        colors = []
        for color in [color_1, color_2, color_3, color_4]:
            if color and color.strip():
                color_clean = color.strip()
                # Validate and format hex colors
                if color_clean.startswith('#') or all(c in '0123456789ABCDEFabcdef' for c in color_clean.replace('#', '')):
                    color_clean = self.format_hex_color(color_clean)
                colors.append(color_clean)
        
        # Create subject using base class helper
        subject = FLUX2Types.create_subject(
            description=description.strip(),
            position=final_position if final_position else None,
            action=action.strip() if action else None,
            pose=pose.strip() if pose else None,
            color_palette=colors if colors else None
        )
        
        return (subject,)
    
    @classmethod
    def VALIDATE_INPUTS(cls, description, **kwargs):
        """Validate required fields"""
        if not description or not description.strip():
            return "Description is required for subject creation"
        return True


# For display in UI
FLUX2_SubjectCreator.DESCRIPTION = """
Create individual subjects with detailed specifications.

Required:
- description: Detailed subject description

Optional:
- position: Where in frame (use helpers or manual)
- action: Dynamic movement or activity
- pose: Static positioning or body language
- colors: Up to 4 color specifications (hex or names)

Position Helpers:
- Horizontal: left, center, right, etc.
- Vertical: top, middle, bottom, etc.
- Depth: foreground, midground, background

Example:
Description: "Minimalist ceramic coffee mug with matte finish"
Position: "Center foreground"
Colors: "#000000" (matte black)

Output: Subject object for use in Subject Array
"""
