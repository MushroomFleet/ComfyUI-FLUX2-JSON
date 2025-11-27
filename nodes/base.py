"""
Base class and utilities for FLUX.2 Prompt Builder nodes
"""

import json
from typing import Dict, List, Any, Optional, Union


class FLUX2BaseNode:
    """
    Base class for all FLUX2 prompt builder nodes.
    Provides common functionality for validation, formatting, and data handling.
    """
    
    CATEGORY = "FLUX2_Prompt_Builder"
    RETURN_TYPES = ()
    FUNCTION = "execute"
    
    @classmethod
    def INPUT_TYPES(cls):
        """Override this in subclasses to define inputs"""
        return {}
    
    def execute(self, **kwargs):
        """Override this in subclasses to implement node logic"""
        raise NotImplementedError("Subclasses must implement execute()")
    
    @staticmethod
    def validate_hex_color(color: str) -> bool:
        """Validate hex color format"""
        if not color:
            return False
        color = color.strip()
        if color.startswith('#'):
            color = color[1:]
        if len(color) not in (3, 6):
            return False
        try:
            int(color, 16)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def format_hex_color(color: str) -> str:
        """Format hex color consistently with # prefix"""
        if not color:
            return ""
        color = color.strip()
        if not color.startswith('#'):
            color = f"#{color}"
        return color.upper()
    
    @staticmethod
    def remove_empty_fields(data: Dict) -> Dict:
        """Remove None, empty string, and empty list values from dictionary"""
        if not isinstance(data, dict):
            return data
        
        cleaned = {}
        for key, value in data.items():
            # Skip None values
            if value is None:
                continue
            # Skip empty strings
            if isinstance(value, str) and not value.strip():
                continue
            # Skip empty lists
            if isinstance(value, list) and len(value) == 0:
                continue
            # Recursively clean nested dicts
            if isinstance(value, dict):
                cleaned_nested = FLUX2BaseNode.remove_empty_fields(value)
                if cleaned_nested:  # Only add if not empty after cleaning
                    cleaned[key] = cleaned_nested
            # Clean lists of dicts
            elif isinstance(value, list):
                if all(isinstance(item, dict) for item in value):
                    cleaned_list = [FLUX2BaseNode.remove_empty_fields(item) for item in value]
                    cleaned_list = [item for item in cleaned_list if item]  # Remove empty dicts
                    if cleaned_list:
                        cleaned[key] = cleaned_list
                else:
                    cleaned[key] = value
            else:
                cleaned[key] = value
        
        return cleaned
    
    @staticmethod
    def format_json_output(data: Dict, pretty: bool = True) -> str:
        """Format dictionary as JSON string"""
        if pretty:
            return json.dumps(data, indent=2, ensure_ascii=False)
        return json.dumps(data, ensure_ascii=False)
    
    @staticmethod
    def merge_color_palettes(global_palette: Optional[List[str]], 
                            local_palette: Optional[List[str]]) -> Optional[List[str]]:
        """
        Merge color palettes with local taking precedence.
        If local exists, use it. Otherwise use global.
        """
        if local_palette:
            return local_palette
        return global_palette


# Custom type definitions for ComfyUI
class FLUX2Types:
    """Custom data types for FLUX2 nodes"""
    
    SUBJECT_OBJECT = "FLUX2_SUBJECT"
    SUBJECT_ARRAY = "FLUX2_SUBJECT_ARRAY"
    CAMERA_OBJECT = "FLUX2_CAMERA"
    COLOR_ARRAY = "FLUX2_COLOR_ARRAY"
    JSON_OBJECT = "FLUX2_JSON"
    
    @staticmethod
    def create_subject(description: str, 
                       position: Optional[str] = None,
                       action: Optional[str] = None,
                       pose: Optional[str] = None,
                       color_palette: Optional[List[str]] = None) -> Dict:
        """Create a subject object with validation"""
        subject = {"description": description}
        
        if position:
            subject["position"] = position
        if action:
            subject["action"] = action
        if pose:
            subject["pose"] = pose
        if color_palette:
            subject["color_palette"] = color_palette
        
        return subject
    
    @staticmethod
    def create_camera(angle: Optional[str] = None,
                     distance: Optional[str] = None,
                     lens: Optional[str] = None,
                     lens_mm: Optional[int] = None,
                     f_number: Optional[str] = None,
                     iso: Optional[int] = None,
                     depth_of_field: Optional[str] = None,
                     focus: Optional[str] = None,
                     **kwargs) -> Dict:
        """Create a camera object with validation"""
        camera = {}
        
        if angle:
            camera["angle"] = angle
        if distance:
            camera["distance"] = distance
        if lens:
            camera["lens"] = lens
        
        # Handle both lens_mm and lens-mm (from presets)
        lens_val = lens_mm or kwargs.get("lens-mm")
        if lens_val is not None:
            camera["lens-mm"] = lens_val
        
        # Handle both f_number and f-number (from presets)
        f_val = f_number or kwargs.get("f-number")
        if f_val:
            camera["f-number"] = f_val
        
        if iso is not None:
            camera["ISO"] = iso
        if depth_of_field:
            camera["depth_of_field"] = depth_of_field
        if focus:
            camera["focus"] = focus
        
        return camera


# Preset libraries
class FLUX2Presets:
    """Preset libraries for common configurations"""
    
    SCENE_TYPES = {
        "Studio": "Professional photography studio with seamless backdrop",
        "Interior": "Indoor space with natural or artificial lighting",
        "Exterior": "Outdoor location with natural environment",
        "Product Stage": "Minimal product photography setup with clean surface",
        "Workshop": "Industrial or craft workspace with tools and materials",
        "Office": "Modern office environment with desks and equipment",
        "Kitchen": "Culinary space with counters and appliances",
        "Living Room": "Comfortable residential living space",
        "Urban Street": "City street with buildings and urban elements",
        "Natural Landscape": "Outdoor natural environment with terrain and vegetation",
    }
    
    STYLE_CATEGORIES = {
        "Photorealistic": [
            "Ultra-realistic product photography with commercial quality",
            "Photorealistic CGI rendering with ray-traced lighting",
            "High-end editorial photography with professional finish",
            "Documentary-style photojournalism with natural authenticity",
            "Architectural photography with precise technical detail",
        ],
        "Film Photography": [
            "Analog film photography, shot on Kodak Portra 400",
            "Vintage film photo with natural grain, shot on Fuji Velvia 50",
            "Black and white film photography, Ilford HP5 Plus",
            "Instant film aesthetic, Polaroid SX-70 style",
            "Medium format film, Hasselblad with Kodak Ektar 100",
        ],
        "Digital Eras": [
            "Modern digital photography, shot on Sony A7IV, clean sharp",
            "Early 2000s digital camera aesthetic with slight noise",
            "1990s digicam style with CCD sensor characteristics",
            "Smartphone photography style, computational processing",
        ],
        "Artistic": [
            "Impressionist painting with visible brushstrokes",
            "Oil painting with rich colors and texture",
            "Watercolor illustration with soft flowing colors",
            "Digital illustration with clean vector aesthetics",
            "Minimalist design with geometric shapes",
        ],
        "Cinematic": [
            "Cinematic movie still with dramatic lighting",
            "Film noir aesthetic with high contrast shadows",
            "Wes Anderson style with symmetrical composition and pastel colors",
            "Blade Runner inspired with neon and atmospheric haze",
        ],
        "Technical": [
            "Technical blueprint style with precise measurements",
            "Scientific documentation with clinical accuracy",
            "X-ray imaging style with translucent structures",
            "Infrared photography with surreal color shifts",
        ],
    }
    
    MOOD_PRESETS = [
        "Clean, professional, minimalist",
        "Warm, inviting, cozy",
        "Energetic and vibrant",
        "Calm and peaceful",
        "Dramatic and intense",
        "Mysterious and intriguing",
        "Playful and whimsical",
        "Elegant and sophisticated",
        "Melancholic and nostalgic",
        "Bold and confident",
        "Serene and tranquil",
        "Tense and suspenseful",
        "Joyful and uplifting",
        "Dark and moody",
        "Bright and cheerful",
    ]
    
    CAMERA_PRESETS = {
        "Portrait": {
            "angle": "Eye level, slight low angle",
            "distance": "Medium shot",
            "lens-mm": 85,
            "f-number": "f/2.0",
            "ISO": 200,
            "depth_of_field": "Shallow, background softly blurred",
            "focus": "Sharp focus on subject's eyes"
        },
        "Product Photography": {
            "angle": "Slight overhead angle, 30 degrees",
            "distance": "Medium shot",
            "lens-mm": 85,
            "f-number": "f/5.6",
            "ISO": 200,
            "depth_of_field": "Moderate depth, product sharp",
            "focus": "Sharp focus on product details"
        },
        "Landscape": {
            "angle": "Eye level or slightly elevated",
            "distance": "Wide shot",
            "lens-mm": 24,
            "f-number": "f/11",
            "ISO": 100,
            "depth_of_field": "Deep, everything in focus",
            "focus": "Infinity focus, entire scene sharp"
        },
        "Macro": {
            "angle": "Perpendicular to subject",
            "distance": "Extreme close-up",
            "lens-mm": 100,
            "f-number": "f/2.8",
            "ISO": 400,
            "depth_of_field": "Very shallow, narrow plane of focus",
            "focus": "Sharp on main detail, background melts away"
        },
        "Street Photography": {
            "angle": "Eye level, candid perspective",
            "distance": "Medium to full shot",
            "lens-mm": 35,
            "f-number": "f/5.6",
            "ISO": 400,
            "depth_of_field": "Moderate depth, subject and context visible",
            "focus": "Zone focus on subject"
        },
        "Wide Angle": {
            "angle": "Low angle or eye level",
            "distance": "Wide shot",
            "lens-mm": 16,
            "f-number": "f/8",
            "ISO": 200,
            "depth_of_field": "Deep, expansive focus",
            "focus": "Hyperfocal, near to far"
        },
    }
    
    POSITION_VOCABULARY = {
        # Horizontal positions
        "horizontal": [
            "far left",
            "left side",
            "left of center",
            "center",
            "right of center",
            "right side",
            "far right"
        ],
        # Vertical positions
        "vertical": [
            "top",
            "upper third",
            "middle",
            "lower third",
            "bottom"
        ],
        # Depth positions
        "depth": [
            "foreground",
            "midground",
            "background"
        ],
        # Combined examples
        "examples": [
            "Center foreground",
            "Left side midground",
            "Right upper third background",
            "Far right foreground",
            "Center background, upper third",
        ]
    }
