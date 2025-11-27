"""
FLUX.2 JSON Prompt Builder - Custom Nodes for ComfyUI
Version: 1.0.0 (Phase 1 - Core Foundation)

A comprehensive suite of custom nodes for building structured JSON prompts
for FLUX.2 image generation with precision and control.

Phase 1 includes:
- FLUX2_PromptAssembler: Master output node
- FLUX2_SceneBuilder: Scene context definition
- FLUX2_StyleSelector: Artistic style control
- FLUX2_SubjectCreator: Individual subject specification
- FLUX2_SubjectArray: Multi-subject collection
- FLUX2_CameraRig: Photography parameters

Author: Claude & Team
License: MIT
"""

from .nodes.prompt_assembler import FLUX2_PromptAssembler
from .nodes.scene_builder import FLUX2_SceneBuilder
from .nodes.style_selector import FLUX2_StyleSelector
from .nodes.subject_creator import FLUX2_SubjectCreator
from .nodes.subject_array import FLUX2_SubjectArray
from .nodes.camera_rig import FLUX2_CameraRig
from .nodes.color_palette import FLUX2_ColorPalette, FLUX2_ColorPalettePreset

# Node class mappings for ComfyUI registration
NODE_CLASS_MAPPINGS = {
    "FLUX2_PromptAssembler": FLUX2_PromptAssembler,
    "FLUX2_SceneBuilder": FLUX2_SceneBuilder,
    "FLUX2_StyleSelector": FLUX2_StyleSelector,
    "FLUX2_SubjectCreator": FLUX2_SubjectCreator,
    "FLUX2_SubjectArray": FLUX2_SubjectArray,
    "FLUX2_CameraRig": FLUX2_CameraRig,
    "FLUX2_ColorPalette": FLUX2_ColorPalette,
    "FLUX2_ColorPalettePreset": FLUX2_ColorPalettePreset,
}

# Display name mappings for ComfyUI interface
NODE_DISPLAY_NAME_MAPPINGS = {
    "FLUX2_PromptAssembler": "FLUX2 Prompt Assembler 🎯",
    "FLUX2_SceneBuilder": "FLUX2 Scene Builder 🏗️",
    "FLUX2_StyleSelector": "FLUX2 Style Selector 🎨",
    "FLUX2_SubjectCreator": "FLUX2 Subject Creator 👤",
    "FLUX2_SubjectArray": "FLUX2 Subject Array 📋",
    "FLUX2_CameraRig": "FLUX2 Camera Rig 📷",
    "FLUX2_ColorPalette": "FLUX2 Color Palette 🎨",
    "FLUX2_ColorPalettePreset": "FLUX2 Color Palette Preset 🌈",
}

# Version and metadata
__version__ = "1.0.0"
__author__ = "Claude & Team"
__description__ = "FLUX.2 JSON Prompt Builder - Phase 1: Core Foundation"

print(f"\n{'='*60}")
print(f"FLUX.2 JSON Prompt Builder v{__version__}")
print(f"Phase 1: Core Foundation - 8 nodes loaded")
print(f"{'='*60}\n")
