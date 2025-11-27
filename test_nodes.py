"""
Test suite for FLUX.2 JSON Prompt Builder - Phase 1 Core Nodes

Run with: python test_nodes.py
"""

import sys
import os

# Add the package to path for testing
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from nodes.base import FLUX2BaseNode, FLUX2Types, FLUX2Presets
from nodes.scene_builder import FLUX2_SceneBuilder
from nodes.style_selector import FLUX2_StyleSelector
from nodes.subject_creator import FLUX2_SubjectCreator
from nodes.subject_array import FLUX2_SubjectArray
from nodes.camera_rig import FLUX2_CameraRig
from nodes.prompt_assembler import FLUX2_PromptAssembler

import json


def test_scene_builder():
    """Test SceneBuilder node"""
    print("\n" + "="*60)
    print("Testing FLUX2_SceneBuilder")
    print("="*60)
    
    node = FLUX2_SceneBuilder()
    
    # Test with preset
    result = node.build_scene(
        scene_type="Studio",
        time_of_day="Morning",
        weather="Clear"
    )
    print(f"✓ Preset scene: {result[0]}")
    
    # Test with custom
    result = node.build_scene(
        scene_type="Custom",
        custom_description="Futuristic laboratory with holographic displays"
    )
    print(f"✓ Custom scene: {result[0]}")
    
    print("✓ SceneBuilder tests passed!")


def test_style_selector():
    """Test StyleSelector node"""
    print("\n" + "="*60)
    print("Testing FLUX2_StyleSelector")
    print("="*60)
    
    node = FLUX2_StyleSelector()
    
    # Test with preset
    result = node.select_style(
        style_category="Photorealistic",
        quality_level="Commercial quality"
    )
    print(f"✓ Preset style: {result[0]}")
    
    # Test with custom
    result = node.select_style(
        style_category="Custom",
        custom_style="Cyberpunk neon aesthetic with dramatic lighting"
    )
    print(f"✓ Custom style: {result[0]}")
    
    print("✓ StyleSelector tests passed!")


def test_subject_creator():
    """Test SubjectCreator node"""
    print("\n" + "="*60)
    print("Testing FLUX2_SubjectCreator")
    print("="*60)
    
    node = FLUX2_SubjectCreator()
    
    # Test basic subject
    result = node.create_subject(
        description="Minimalist ceramic coffee mug with matte finish"
    )
    print(f"✓ Basic subject: {result[0]}")
    
    # Test full subject with all fields
    result = node.create_subject(
        description="Vintage leather-bound journal",
        position_horizontal="center",
        position_depth="foreground",
        action="Pages fluttering in breeze",
        color_1="#8B4513",
        color_2="#FFD700"
    )
    print(f"✓ Full subject: {json.dumps(result[0], indent=2)}")
    
    # Test with hex color validation
    result = node.create_subject(
        description="Red sports car",
        color_1="FF0000",  # Without #
        color_2="#00FF00"  # With #
    )
    print(f"✓ Color formatting: {result[0]['color_palette']}")
    
    print("✓ SubjectCreator tests passed!")


def test_subject_array():
    """Test SubjectArray node"""
    print("\n" + "="*60)
    print("Testing FLUX2_SubjectArray")
    print("="*60)
    
    # Create some subjects
    creator = FLUX2_SubjectCreator()
    
    subject1 = creator.create_subject(
        description="Coffee mug",
        color_1="#000000"
    )[0]
    
    subject2 = creator.create_subject(
        description="Laptop",
        color_1="#C0C0C0"
    )[0]
    
    subject3 = creator.create_subject(
        description="Plant",
        color_1="#228B22"
    )[0]
    
    # Test array collection
    array_node = FLUX2_SubjectArray()
    subjects, count, summary = array_node.collect_subjects(
        subject_1=subject1,
        subject_2=subject2,
        subject_3=subject3
    )
    
    print(f"✓ Collected {count} subjects")
    print(f"✓ Summary:\n{summary}")
    print(f"✓ Array: {json.dumps(subjects, indent=2)}")
    
    print("✓ SubjectArray tests passed!")


def test_camera_rig():
    """Test CameraRig node"""
    print("\n" + "="*60)
    print("Testing FLUX2_CameraRig")
    print("="*60)
    
    node = FLUX2_CameraRig()
    
    # Test with preset
    camera, summary = node.setup_camera(preset="Portrait")
    print(f"✓ Preset camera:\n{summary}")
    print(f"  Camera object: {json.dumps(camera, indent=2)}")
    
    # Test with custom parameters
    camera, summary = node.setup_camera(
        preset="None",
        angle_preset="Eye level",
        distance="Medium shot",
        lens_mm=50,
        f_number="f/2.8",
        iso=400,
        depth_preset="Shallow"
    )
    print(f"\n✓ Custom camera:\n{summary}")
    
    # Test preset with override
    camera, summary = node.setup_camera(
        preset="Product Photography",
        lens_mm=100,  # Override lens
        override_preset=True
    )
    print(f"\n✓ Override camera:\n{summary}")
    
    print("✓ CameraRig tests passed!")


def test_prompt_assembler():
    """Test PromptAssembler node (integration test)"""
    print("\n" + "="*60)
    print("Testing FLUX2_PromptAssembler (Integration)")
    print("="*60)
    
    # Build a complete prompt
    scene_node = FLUX2_SceneBuilder()
    style_node = FLUX2_StyleSelector()
    subject_node = FLUX2_SubjectCreator()
    array_node = FLUX2_SubjectArray()
    camera_node = FLUX2_CameraRig()
    assembler = FLUX2_PromptAssembler()
    
    # Create components
    scene = scene_node.build_scene(
        scene_type="Studio",
        time_of_day="Morning"
    )[0]
    
    style = style_node.select_style(
        style_category="Photorealistic",
        quality_level="Commercial quality"
    )[0]
    
    subject1 = subject_node.create_subject(
        description="Black ceramic coffee mug with matte finish",
        position_horizontal="center",
        position_depth="foreground",
        color_1="#000000"
    )[0]
    
    subject2 = subject_node.create_subject(
        description="Silver laptop in background",
        position_horizontal="right side",
        position_depth="background",
        color_1="#C0C0C0"
    )[0]
    
    subjects = array_node.collect_subjects(
        subject_1=subject1,
        subject_2=subject2
    )[0]
    
    camera = camera_node.setup_camera(preset="Product Photography")[0]
    
    # Assemble
    json_string, json_object = assembler.assemble_prompt(
        scene=scene,
        subjects=subjects,
        style=style,
        camera=camera,
        mood="Clean, professional, minimalist",
        lighting="Soft three-point studio lighting",
        pretty_print=True,
        remove_empty=True
    )
    
    print("✓ Complete JSON Prompt:")
    print(json_string)
    
    # Validate it's valid JSON
    try:
        json.loads(json_string)
        print("\n✓ JSON is valid!")
    except json.JSONDecodeError as e:
        print(f"\n✗ JSON validation failed: {e}")
        return False
    
    print("✓ PromptAssembler tests passed!")


def test_base_utilities():
    """Test base class utilities"""
    print("\n" + "="*60)
    print("Testing Base Class Utilities")
    print("="*60)
    
    # Test hex color validation
    assert FLUX2BaseNode.validate_hex_color("#FF0000") == True
    assert FLUX2BaseNode.validate_hex_color("FF0000") == True
    assert FLUX2BaseNode.validate_hex_color("#FFF") == True
    assert FLUX2BaseNode.validate_hex_color("ZZZZZZ") == False
    print("✓ Hex color validation works")
    
    # Test hex color formatting
    assert FLUX2BaseNode.format_hex_color("ff0000") == "#FF0000"
    assert FLUX2BaseNode.format_hex_color("#ff0000") == "#FF0000"
    print("✓ Hex color formatting works")
    
    # Test empty field removal
    data = {
        "field1": "value",
        "field2": "",
        "field3": None,
        "field4": [],
        "field5": ["item"],
        "nested": {
            "a": "value",
            "b": "",
            "c": None
        }
    }
    cleaned = FLUX2BaseNode.remove_empty_fields(data)
    assert "field1" in cleaned
    assert "field2" not in cleaned
    assert "field3" not in cleaned
    assert "field4" not in cleaned
    assert "field5" in cleaned
    assert cleaned["nested"] == {"a": "value"}
    print("✓ Empty field removal works")
    
    print("✓ Base utilities tests passed!")


def test_presets():
    """Test preset libraries"""
    print("\n" + "="*60)
    print("Testing Preset Libraries")
    print("="*60)
    
    # Test scene presets
    assert "Studio" in FLUX2Presets.SCENE_TYPES
    assert len(FLUX2Presets.SCENE_TYPES) >= 5
    print(f"✓ Scene presets: {len(FLUX2Presets.SCENE_TYPES)} available")
    
    # Test style presets
    assert "Photorealistic" in FLUX2Presets.STYLE_CATEGORIES
    assert len(FLUX2Presets.STYLE_CATEGORIES) >= 5
    print(f"✓ Style categories: {len(FLUX2Presets.STYLE_CATEGORIES)} available")
    
    # Test camera presets
    assert "Portrait" in FLUX2Presets.CAMERA_PRESETS
    assert len(FLUX2Presets.CAMERA_PRESETS) >= 5
    print(f"✓ Camera presets: {len(FLUX2Presets.CAMERA_PRESETS)} available")
    
    # Test mood presets
    assert len(FLUX2Presets.MOOD_PRESETS) >= 10
    print(f"✓ Mood presets: {len(FLUX2Presets.MOOD_PRESETS)} available")
    
    print("✓ Preset libraries tests passed!")


def run_all_tests():
    """Run all tests"""
    print("\n" + "#"*60)
    print("# FLUX.2 JSON Prompt Builder - Test Suite")
    print("# Phase 1: Core Foundation")
    print("#"*60)
    
    try:
        test_base_utilities()
        test_presets()
        test_scene_builder()
        test_style_selector()
        test_subject_creator()
        test_subject_array()
        test_camera_rig()
        test_prompt_assembler()
        
        print("\n" + "="*60)
        print("✓ ALL TESTS PASSED!")
        print("="*60)
        print("\nPhase 1 nodes are ready to use!")
        return True
        
    except Exception as e:
        print("\n" + "="*60)
        print(f"✗ TEST FAILED: {e}")
        print("="*60)
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
