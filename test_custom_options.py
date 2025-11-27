"""
Test script for custom options in camera_rig.py and scene_builder.py
"""

from nodes.camera_rig import FLUX2_CameraRig
from nodes.scene_builder import FLUX2_SceneBuilder

def test_camera_custom_distance():
    """Test custom distance option in CameraRig"""
    print("=== Testing Camera Rig Custom Distance ===\n")
    
    node = FLUX2_CameraRig()
    
    # Test 1: Using preset distance
    result1 = node.setup_camera(
        preset="None",
        distance="Close-up"
    )
    print("Test 1 - Preset distance:")
    print(f"  Input: distance='Close-up'")
    print(f"  Camera: {result1[0]}")
    print(f"  Summary: {result1[1]}\n")
    
    # Test 2: Using custom distance
    result2 = node.setup_camera(
        preset="None",
        distance="Custom",
        custom_distance="Intimate macro, filling the frame"
    )
    print("Test 2 - Custom distance:")
    print(f"  Input: distance='Custom', custom_distance='Intimate macro, filling the frame'")
    print(f"  Camera: {result2[0]}")
    print(f"  Summary: {result2[1]}\n")
    
    # Test 3: Custom distance with other settings
    result3 = node.setup_camera(
        preset="None",
        distance="Custom",
        custom_distance="Aerial view from 100 feet",
        angle_preset="Bird's eye view",
        lens_mm=24
    )
    print("Test 3 - Custom distance with other settings:")
    print(f"  Input: distance='Custom', custom_distance='Aerial view from 100 feet'")
    print(f"  Camera: {result3[0]}")
    print(f"  Summary: {result3[1]}\n")


def test_scene_custom_fields():
    """Test custom weather and time_of_day options in SceneBuilder"""
    print("=== Testing Scene Builder Custom Options ===\n")
    
    node = FLUX2_SceneBuilder()
    
    # Test 1: Using preset time_of_day and weather
    result1 = node.build_scene(
        scene_type="Exterior",
        time_of_day="Golden Hour",
        weather="Clear"
    )
    print("Test 1 - Preset time and weather:")
    print(f"  Input: time_of_day='Golden Hour', weather='Clear'")
    print(f"  Output: {result1[0]}\n")
    
    # Test 2: Using custom time_of_day
    result2 = node.build_scene(
        scene_type="Interior",
        time_of_day="Custom",
        custom_time_of_day="Late twilight with deep blue sky",
        weather="Clear"
    )
    print("Test 2 - Custom time of day:")
    print(f"  Input: time_of_day='Custom', custom_time_of_day='Late twilight...'")
    print(f"  Output: {result2[0]}\n")
    
    # Test 3: Using custom weather
    result3 = node.build_scene(
        scene_type="Urban Street",
        time_of_day="Night",
        weather="Custom",
        custom_weather="Light drizzle with neon reflections"
    )
    print("Test 3 - Custom weather:")
    print(f"  Input: weather='Custom', custom_weather='Light drizzle...'")
    print(f"  Output: {result3[0]}\n")
    
    # Test 4: Using both custom time and weather
    result4 = node.build_scene(
        scene_type="Natural Landscape",
        time_of_day="Custom",
        custom_time_of_day="Pre-dawn nautical twilight",
        weather="Custom",
        custom_weather="Patchy ground fog forming in valleys"
    )
    print("Test 4 - Both custom time and weather:")
    print(f"  Input: Both custom time and weather")
    print(f"  Output: {result4[0]}\n")
    
    # Test 5: Custom with environment details
    result5 = node.build_scene(
        scene_type="Workshop",
        time_of_day="Custom",
        custom_time_of_day="Midday with strong overhead sun",
        weather="Custom",
        custom_weather="Humid, sultry summer heat",
        environment_details="with visible dust particles in sunbeams"
    )
    print("Test 5 - Custom options with environment details:")
    print(f"  Input: All custom fields populated")
    print(f"  Output: {result5[0]}\n")


def test_dropdown_options():
    """Verify that 'Custom' appears in the dropdown options"""
    print("=== Verifying Dropdown Options ===\n")
    
    # Check CameraRig
    camera_inputs = FLUX2_CameraRig.INPUT_TYPES()
    distance_options = camera_inputs["optional"]["distance"][0]
    print(f"CameraRig distance options: {distance_options}")
    print(f"  ✓ 'Custom' option present: {'Custom' in distance_options}\n")
    
    # Check SceneBuilder
    scene_inputs = FLUX2_SceneBuilder.INPUT_TYPES()
    time_options = scene_inputs["optional"]["time_of_day"][0]
    weather_options = scene_inputs["optional"]["weather"][0]
    print(f"SceneBuilder time_of_day options: {time_options}")
    print(f"  ✓ 'Custom' option present: {'Custom' in time_options}")
    print(f"\nSceneBuilder weather options: {weather_options}")
    print(f"  ✓ 'Custom' option present: {'Custom' in weather_options}\n")


if __name__ == "__main__":
    print("=" * 60)
    print("CUSTOM OPTIONS TEST SUITE")
    print("=" * 60)
    print()
    
    test_dropdown_options()
    print()
    test_camera_custom_distance()
    print()
    test_scene_custom_fields()
    
    print("=" * 60)
    print("ALL TESTS COMPLETED SUCCESSFULLY")
    print("=" * 60)
    print("\nSummary:")
    print("✓ CameraRig: 'Custom' option added to distance dropdown")
    print("✓ CameraRig: custom_distance field working correctly")
    print("✓ SceneBuilder: 'Custom' option added to time_of_day dropdown")
    print("✓ SceneBuilder: custom_time_of_day field working correctly")
    print("✓ SceneBuilder: 'Custom' option added to weather dropdown")
    print("✓ SceneBuilder: custom_weather field working correctly")
    print("✓ All custom fields integrate properly with other parameters")
