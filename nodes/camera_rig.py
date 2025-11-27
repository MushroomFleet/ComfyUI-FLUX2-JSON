"""
FLUX2_CameraRig - Complete camera parameter control for photorealistic results
"""

from .base import FLUX2BaseNode, FLUX2Types, FLUX2Presets


class FLUX2_CameraRig(FLUX2BaseNode):
    """
    Complete camera parameter control for photorealistic image generation.
    Simulates real photography equipment and settings.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (["None"] + list(FLUX2Presets.CAMERA_PRESETS.keys()), {
                    "default": "None"
                }),
            },
            "optional": {
                "angle": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "e.g., 'Eye level', 'High angle looking down'"
                }),
                "angle_preset": (["", "Eye level", "High angle", "Low angle", "Bird's eye view", 
                                 "Worm's eye view", "Dutch angle (tilted)"], {
                    "default": ""
                }),
                "distance": (["", "Extreme close-up", "Close-up", "Medium shot", 
                            "Full shot", "Wide shot", "Extreme wide shot"], {
                    "default": ""
                }),
                "lens_mm": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 400,
                    "step": 1,
                    "display": "slider"
                }),
                "lens_description": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "e.g., 'Wide angle lens', 'Macro lens'"
                }),
                "f_number": (["", "f/1.4", "f/1.8", "f/2.0", "f/2.8", "f/4", 
                            "f/5.6", "f/8", "f/11", "f/16"], {
                    "default": ""
                }),
                "iso": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 6400,
                    "step": 100,
                    "display": "slider"
                }),
                "depth_of_field": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "e.g., 'Shallow, background blurred'"
                }),
                "depth_preset": (["", "Very shallow (bokeh)", "Shallow", "Moderate", 
                                "Deep", "Everything sharp"], {
                    "default": ""
                }),
                "focus": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "placeholder": "e.g., 'Sharp focus on subject'"
                }),
                "override_preset": ("BOOLEAN", {
                    "default": False
                }),
            }
        }
    
    RETURN_TYPES = (FLUX2Types.CAMERA_OBJECT, "STRING")
    RETURN_NAMES = ("camera", "camera_summary")
    FUNCTION = "setup_camera"
    
    CATEGORY = "FLUX2_Prompt_Builder/Camera"
    
    def setup_camera(self,
                    preset="None",
                    angle="",
                    angle_preset="",
                    distance="",
                    lens_mm=0,
                    lens_description="",
                    f_number="",
                    iso=0,
                    depth_of_field="",
                    depth_preset="",
                    focus="",
                    override_preset=False):
        """
        Setup camera parameters from preset or custom values.
        
        Args:
            preset: Camera preset (Portrait, Product Photography, etc.)
            angle: Camera angle description
            angle_preset: Camera angle preset
            distance: Shot distance/framing
            lens_mm: Lens focal length (0 = not specified)
            lens_description: Lens type description
            f_number: Aperture setting
            iso: ISO sensitivity (0 = not specified)
            depth_of_field: Depth of field description
            depth_preset: DOF preset
            focus: Focus description
            override_preset: If True, custom values override preset
        
        Returns:
            Tuple of (camera_object, summary_string)
        """
        
        # Start with preset if selected and not overridden
        if preset != "None" and not override_preset:
            camera_data = FLUX2Presets.CAMERA_PRESETS.get(preset, {}).copy()
        else:
            camera_data = {}
        
        # Override or set individual parameters
        # Angle
        final_angle = angle.strip() if angle else angle_preset
        if final_angle:
            camera_data["angle"] = final_angle
        
        # Distance
        if distance:
            camera_data["distance"] = distance
        
        # Lens
        if lens_description:
            camera_data["lens"] = lens_description.strip()
        if lens_mm > 0:
            camera_data["lens-mm"] = lens_mm
        
        # F-number
        if f_number:
            camera_data["f-number"] = f_number
        
        # ISO
        if iso > 0:
            camera_data["ISO"] = iso
        
        # Depth of field
        final_dof = depth_of_field.strip() if depth_of_field else depth_preset
        if final_dof:
            camera_data["depth_of_field"] = final_dof
        
        # Focus
        if focus:
            camera_data["focus"] = focus.strip()
        
        # Create camera object using base class helper
        camera = FLUX2Types.create_camera(**camera_data)
        
        # Generate summary
        summary_lines = []
        if preset != "None" and not override_preset:
            summary_lines.append(f"Preset: {preset}")
        
        if camera:
            if "angle" in camera:
                summary_lines.append(f"Angle: {camera['angle']}")
            if "distance" in camera:
                summary_lines.append(f"Distance: {camera['distance']}")
            if "lens-mm" in camera:
                summary_lines.append(f"Lens: {camera['lens-mm']}mm")
            elif "lens" in camera:
                summary_lines.append(f"Lens: {camera['lens']}")
            if "f-number" in camera:
                summary_lines.append(f"Aperture: {camera['f-number']}")
            if "ISO" in camera:
                summary_lines.append(f"ISO: {camera['ISO']}")
            if "depth_of_field" in camera:
                summary_lines.append(f"DOF: {camera['depth_of_field']}")
        
        summary = "\n".join(summary_lines) if summary_lines else "No camera parameters set"
        
        return (camera, summary)


# For display in UI
FLUX2_CameraRig.DESCRIPTION = """
Complete camera parameter control for photorealistic results.

Use Presets for quick setups:
- Portrait: 85mm, f/2.0, shallow DOF
- Product Photography: 85mm, f/5.6, moderate DOF
- Landscape: 24mm, f/11, deep DOF
- Macro: 100mm, f/2.8, very shallow DOF
- Street Photography: 35mm, f/5.6, moderate DOF

Or customize individual parameters:
- angle: Camera viewing angle
- distance: Shot framing (close-up, wide, etc.)
- lens_mm: Focal length (16-400mm)
- f_number: Aperture (affects depth of field)
- iso: Light sensitivity (affects grain)
- depth_of_field: How much is in focus
- focus: What to focus on

Lens Guide:
- 16-24mm: Ultra-wide, slight distortion
- 35-50mm: Natural perspective
- 85-135mm: Portrait, flattering compression
- 200mm+: Telephoto, extreme compression

Aperture Guide:
- f/1.4-2.0: Very shallow DOF (portraits)
- f/2.8-5.6: Moderate DOF (products)
- f/8-16: Deep DOF (landscapes)

Output: Camera object for prompt assembly
"""


# Simple camera preset loader
class FLUX2_CameraPreset(FLUX2BaseNode):
    """
    Quick camera preset loader without customization options.
    Perfect for fast workflow when you want standard camera setups.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (list(FLUX2Presets.CAMERA_PRESETS.keys()), {
                    "default": "Portrait"
                }),
            }
        }
    
    RETURN_TYPES = (FLUX2Types.CAMERA_OBJECT,)
    RETURN_NAMES = ("camera",)
    FUNCTION = "load_preset"
    
    CATEGORY = "FLUX2_Prompt_Builder/Camera"
    
    def load_preset(self, preset="Portrait"):
        """Load a camera preset directly."""
        camera_data = FLUX2Presets.CAMERA_PRESETS.get(preset, {})
        camera = FLUX2Types.create_camera(**camera_data)
        return (camera,)
