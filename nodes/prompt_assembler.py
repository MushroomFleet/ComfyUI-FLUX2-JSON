"""
FLUX2_PromptAssembler - Master node for assembling complete JSON prompts
"""

from .base import FLUX2BaseNode, FLUX2Types


class FLUX2_PromptAssembler(FLUX2BaseNode):
    """
    Master node that collects all prompt components and outputs final JSON.
    This is the terminal node in most FLUX2 prompt building workflows.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "scene": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "subjects": (FLUX2Types.SUBJECT_ARRAY, {
                    "default": None
                }),
                "style": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "color_palette": (FLUX2Types.COLOR_ARRAY, {
                    "default": None
                }),
                "lighting": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "mood": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "background": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "composition": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "camera": (FLUX2Types.CAMERA_OBJECT, {
                    "default": None
                }),
                "pretty_print": ("BOOLEAN", {
                    "default": True
                }),
                "remove_empty": ("BOOLEAN", {
                    "default": True
                }),
            }
        }
    
    RETURN_TYPES = ("STRING", FLUX2Types.JSON_OBJECT)
    RETURN_NAMES = ("json_string", "json_object")
    FUNCTION = "assemble_prompt"
    OUTPUT_NODE = True
    
    CATEGORY = "FLUX2_Prompt_Builder/Core"
    
    def assemble_prompt(self, 
                       scene="",
                       subjects=None,
                       style="",
                       color_palette=None,
                       lighting="",
                       mood="",
                       background="",
                       composition="",
                       camera=None,
                       pretty_print=True,
                       remove_empty=True):
        """
        Assemble all components into final JSON prompt.
        
        Args:
            scene: Overall scene description
            subjects: Array of subject objects
            style: Artistic style
            color_palette: Global color palette
            lighting: Lighting description
            mood: Emotional tone
            background: Background details
            composition: Composition rules
            camera: Camera object with parameters
            pretty_print: Format JSON with indentation
            remove_empty: Remove empty/null fields from output
        
        Returns:
            Tuple of (json_string, json_object)
        """
        
        # Build the prompt dictionary
        prompt = {}
        
        # Add fields in standard order
        if scene:
            prompt["scene"] = scene.strip()
        
        if subjects:
            prompt["subjects"] = subjects
        
        if style:
            prompt["style"] = style.strip()
        
        if color_palette:
            prompt["color_palette"] = color_palette
        
        if lighting:
            prompt["lighting"] = lighting.strip()
        
        if mood:
            prompt["mood"] = mood.strip()
        
        if background:
            prompt["background"] = background.strip()
        
        if composition:
            prompt["composition"] = composition.strip()
        
        if camera:
            prompt["camera"] = camera
        
        # Remove empty fields if requested
        if remove_empty:
            prompt = self.remove_empty_fields(prompt)
        
        # Format as JSON string
        json_string = self.format_json_output(prompt, pretty=pretty_print)
        
        # Return both string and dict
        return (json_string, prompt)
    
    @classmethod
    def IS_CHANGED(cls, **kwargs):
        # Always execute to ensure updates propagate
        return float("nan")


# For display in UI
FLUX2_PromptAssembler.DESCRIPTION = """
Master node for assembling complete FLUX.2 JSON prompts.

Connect all your prompt components (scene, subjects, style, camera, etc.) 
to this node to generate the final JSON output.

Outputs:
- json_string: Formatted JSON text (copy this to FLUX.2)
- json_object: Python dict for further processing

Options:
- pretty_print: Format with indentation for readability
- remove_empty: Automatically remove empty/null fields
"""
