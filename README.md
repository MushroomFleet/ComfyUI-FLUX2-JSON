# FLUX.2 JSON Prompt Builder for ComfyUI

![godzilla-flux2-json](https://raw.githubusercontent.com/MushroomFleet/ComfyUI-FLUX2-JSON/refs/heads/main/examples/id6_00001_.png)
![Akira-Insert-Character](https://raw.githubusercontent.com/MushroomFleet/ComfyUI-FLUX2-JSON/refs/heads/main/examples/ComfyUI_temp_ttbdg_00004_.png)
![akira-bike-char-custom](https://github.com/MushroomFleet/ComfyUI-FLUX2-JSON/blob/main/examples/ComfyUI_temp_bancn_00006_.png)

A comprehensive suite of custom nodes for building structured JSON prompts for FLUX.2 image generation with precision and control.

## 🚀 Phase 1: Core Foundation (v1.0.0)

This initial release includes 6 essential nodes for basic FLUX.2 prompt construction:

- **FLUX2_PromptAssembler** 🎯 - Master output node for final JSON assembly
- **FLUX2_SceneBuilder** 🏗️ - Define scene context and environment
- **FLUX2_StyleSelector** 🎨 - Choose artistic style and rendering
- **FLUX2_SubjectCreator** 👤 - Create individual subjects with properties
- **FLUX2_SubjectArray** 📋 - Collect multiple subjects into arrays
- **FLUX2_CameraRig** 📷 - Complete camera parameter control

---

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "FLUX2 Prompt Builder"
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/MushroomFleet/ComfyUI-FLUX2-JSON.git
```

3. Restart ComfyUI

### Method 3: Direct Download

1. Download this repository as ZIP
2. Extract to `ComfyUI/custom_nodes/ComfyUI_FLUX2_Prompt_Builder/`
3. Restart ComfyUI

---

## 🎯 Quick Start

### Basic Product Photography Workflow

```
1. Add FLUX2_SceneBuilder node
   - Set scene_type: "Product Stage"

2. Add FLUX2_SubjectCreator node
   - description: "Minimalist ceramic coffee mug"
   - position: "Center foreground"
   - color_1: "#000000"

3. Add FLUX2_CameraRig node
   - preset: "Product Photography"

4. Add FLUX2_StyleSelector node
   - style_category: "Photorealistic"

5. Add FLUX2_PromptAssembler node
   - Connect all outputs to corresponding inputs
   - Copy the json_string output

6. Use the JSON in your FLUX.2 generation workflow
```

---

## 📚 Node Documentation

### FLUX2_PromptAssembler 🎯

**Purpose:** Master node that collects all prompt components and outputs final JSON.

**Inputs:**
- `scene` (optional): Scene description from SceneBuilder
- `subjects` (optional): Subject array from SubjectArray
- `style` (optional): Style description from StyleSelector
- `color_palette` (optional): Global color palette (array)
- `lighting` (optional): Lighting description (string)
- `mood` (optional): Mood description (string)
- `background` (optional): Background details (string)
- `composition` (optional): Composition rules (string)
- `camera` (optional): Camera object from CameraRig
- `pretty_print` (boolean): Format JSON with indentation
- `remove_empty` (boolean): Remove empty/null fields

**Outputs:**
- `json_string`: Formatted JSON text (copy this to FLUX.2)
- `json_object`: Python dict for further processing

**Usage:**
This is your final node. Connect all your prompt components here and copy the JSON output to use with FLUX.2.

---

### FLUX2_SceneBuilder 🏗️

**Purpose:** Define the overall scene context and environment.

**Inputs:**
- `scene_type` (required): Preset scene type or "Custom"
  - Options: Studio, Interior, Exterior, Product Stage, Workshop, Office, Kitchen, Living Room, Urban Street, Natural Landscape
- `custom_description` (optional): Custom scene description
- `environment_details` (optional): Additional environmental context
- `time_of_day` (optional): Morning, Afternoon, Evening, Night, Golden Hour, Blue Hour
- `weather` (optional): Clear, Cloudy, Overcast, Rainy, Foggy, Snowy

**Outputs:**
- `scene`: Complete scene description string

**Example:**
```
scene_type: "Studio"
time_of_day: "Morning"
weather: "Clear"
→ Output: "Professional photography studio with seamless backdrop, morning lighting, clear conditions"
```

---

### FLUX2_StyleSelector 🎨

**Purpose:** Choose artistic style and rendering approach.

**Inputs:**
- `style_category` (required): Main style category
  - Options: Photorealistic, Film Photography, Digital Eras, Artistic, Cinematic, Technical
- `style_preset` (optional): Specific preset within category
- `custom_style` (optional): Custom style description
- `quality_level` (optional): Commercial quality, Editorial quality, Artistic expression, Experimental
- `additional_modifiers` (optional): Extra style details

**Outputs:**
- `style`: Complete style description string

**Categories:**
- **Photorealistic**: Commercial, editorial, documentary photography
- **Film Photography**: Kodak Portra 400, Fuji Velvia 50, Ilford HP5+, etc.
- **Digital Eras**: Modern digital, 2000s digicam, 90s aesthetic
- **Artistic**: Painting styles, illustrations, minimalist design
- **Cinematic**: Movie-inspired looks, film noir, Wes Anderson style
- **Technical**: Blueprint, scientific, x-ray, infrared

---

### FLUX2_SubjectCreator 👤

**Purpose:** Create individual subjects with detailed specifications.

**Inputs:**
- `description` (required): Detailed subject description
- `position` (optional): Manual position description
- `position_horizontal` (optional): left, center, right, etc.
- `position_vertical` (optional): top, middle, bottom, etc.
- `position_depth` (optional): foreground, midground, background
- `action` (optional): Dynamic action description
- `pose` (optional): Static pose description
- `color_1` through `color_4` (optional): Color specifications (hex or names)

**Outputs:**
- `subject`: Subject object for use in SubjectArray

**Example:**
```
description: "Vintage leather-bound journal with brass corners"
position_horizontal: "center"
position_depth: "foreground"
color_1: "#8B4513"
color_2: "#FFD700"
→ Creates subject object with all properties
```

**Position Helpers:**
- Horizontal: far left, left side, center, right side, far right
- Vertical: top, upper third, middle, lower third, bottom
- Depth: foreground, midground, background

---

### FLUX2_SubjectArray 📋

**Purpose:** Collect multiple subjects into an ordered array.

**Inputs:**
- `subject_1` through `subject_8` (optional): Subject objects from SubjectCreator

**Outputs:**
- `subjects`: Array of subject objects for prompt assembly
- `subject_count`: Number of subjects in array
- `summary`: Quick overview of all subjects

**Usage:**
Connect multiple SubjectCreator nodes to different input slots. Empty slots are automatically filtered out. Order matters—subject_1 is typically the primary/foreground element.

---

### FLUX2_CameraRig 📷

**Purpose:** Complete camera parameter control for photorealistic results.

**Inputs:**
- `preset` (required): Camera preset or "None"
  - Options: Portrait, Product Photography, Landscape, Macro, Street Photography, Wide Angle
- `angle` (optional): Camera viewing angle
- `angle_preset` (optional): Eye level, High angle, Low angle, etc.
- `distance` (optional): Shot framing (Close-up, Wide shot, etc.)
- `lens_mm` (optional): Focal length (0-400mm)
- `lens_description` (optional): Lens type description
- `f_number` (optional): Aperture (f/1.4 - f/16)
- `iso` (optional): ISO sensitivity (0-6400)
- `depth_of_field` (optional): DOF description
- `depth_preset` (optional): Very shallow, Shallow, Moderate, Deep, etc.
- `focus` (optional): Focus description
- `override_preset` (optional): Custom values override preset

**Outputs:**
- `camera`: Camera object for prompt assembly
- `camera_summary`: Text summary of settings

**Presets:**
- **Portrait**: 85mm, f/2.0, shallow DOF, eye-level angle
- **Product Photography**: 85mm, f/5.6, moderate DOF, slight overhead
- **Landscape**: 24mm, f/11, deep DOF, wide shot
- **Macro**: 100mm, f/2.8, very shallow DOF, extreme close-up
- **Street Photography**: 35mm, f/5.6, moderate DOF, eye level
- **Wide Angle**: 16mm, f/8, deep DOF, expansive

**Lens Guide:**
- 16-24mm: Ultra-wide, landscapes
- 35-50mm: Natural perspective, versatile
- 85-135mm: Portrait, flattering
- 200mm+: Telephoto, compression

**Aperture Guide:**
- f/1.4-2.0: Very shallow DOF (portraits)
- f/2.8-5.6: Moderate DOF (products)
- f/8-16: Deep DOF (landscapes)

---

## 🎨 Example Workflows

### Example 1: Simple Product Shot

**Goal:** Black coffee mug on white background

```
SceneBuilder:
  scene_type: "Studio"
  
SubjectCreator:
  description: "Minimalist ceramic coffee mug with matte finish"
  position_horizontal: "center"
  position_depth: "foreground"
  color_1: "#000000"
  
StyleSelector:
  style_category: "Photorealistic"
  quality_level: "Commercial quality"
  
CameraRig:
  preset: "Product Photography"
  
PromptAssembler:
  [Connect all above outputs]
```

**Generated JSON:**
```json
{
  "scene": "Professional photography studio with seamless backdrop",
  "subjects": [
    {
      "description": "Minimalist ceramic coffee mug with matte finish",
      "position": "center foreground",
      "color_palette": ["#000000"]
    }
  ],
  "style": "Ultra-realistic product photography with commercial quality, commercial quality",
  "camera": {
    "angle": "Slight overhead angle, 30 degrees",
    "distance": "Medium shot",
    "lens-mm": 85,
    "f-number": "f/5.6",
    "ISO": 200,
    "depth_of_field": "Moderate depth, product sharp",
    "focus": "Sharp focus on product details"
  }
}
```

---

### Example 2: Multi-Subject Scene

**Goal:** Tech workspace with laptop, coffee, and plant

```
SceneBuilder:
  scene_type: "Office"
  time_of_day: "Morning"
  
SubjectCreator #1 (Laptop):
  description: "Sleek modern laptop, open with glowing screen"
  position_horizontal: "right side"
  position_depth: "midground"
  color_1: "#C0C0C0"
  
SubjectCreator #2 (Coffee):
  description: "White ceramic coffee mug with steam rising"
  position_horizontal: "left side"
  position_depth: "foreground"
  color_1: "#FFFFFF"
  
SubjectCreator #3 (Plant):
  description: "Small succulent plant in terracotta pot"
  position_horizontal: "far left"
  position_depth: "midground"
  color_1: "#228B22"
  color_2: "#D2691E"
  
SubjectArray:
  subject_1: [Coffee - foreground priority]
  subject_2: [Laptop]
  subject_3: [Plant]
  
StyleSelector:
  style_category: "Photorealistic"
  additional_modifiers: "Clean, minimalist aesthetic"
  
CameraRig:
  preset: "Product Photography"
  
PromptAssembler:
  [Connect all outputs]
```

---

## 🔧 Advanced Tips

### Color Management

**Hex Colors:**
- Always use 6-digit hex codes: `#FF0000` not `#F00`
- Format automatically corrects to uppercase with # prefix
- Validation ensures proper hex format

**Color Strategies:**
- Use subject-specific colors for precise control
- Global color_palette sets overall mood
- Subject colors override global palette

### Position Strategies

**Using Position Helpers:**
```
position_horizontal: "center"
position_vertical: "upper third"
position_depth: "foreground"
→ Generates: "center upper third foreground"
```

**Manual Position:**
```
position: "Center foreground on polished concrete surface"
→ Uses exactly as written
```

### Camera Tips

**Start with Presets:**
- Use presets as starting points
- Enable `override_preset` to customize
- Adjust individual parameters as needed

**Photorealism Formula:**
```
Realistic focal length (35-85mm)
+ Appropriate aperture (f/2.8-8)
+ Proper ISO (100-400)
+ Clear focus description
= Photorealistic results
```

---

## 🛠️ Troubleshooting

### "Subject description is required"
**Solution:** SubjectCreator requires a description. Fill in the description field.

### JSON output is empty
**Solution:** Check that `remove_empty` is set appropriately. If all fields are empty, the output will be `{}`.

### Camera preset not applying
**Solution:** Make sure `override_preset` is False. If True, manual settings override the preset.

### Colors not appearing
**Solution:** Ensure hex codes start with `#` and are valid 6-digit hex (e.g., `#FF0000`).

---

## 📅 Roadmap

### Phase 2: Visual Control (Coming Soon)
- FLUX2_HexColorPicker: Visual color selection
- FLUX2_ColorPaletteGenerator: Harmony-based palettes
- FLUX2_LightingRig: Professional lighting setups
- FLUX2_CompositionGuide: Composition rules
- FLUX2_MoodController: Emotional tone control

### Phase 3: Advanced Camera (Future)
- FLUX2_LensCharacteristics: Lens effects
- FLUX2_FilmStockSimulator: Film emulation
- FLUX2_AtmosphericEffects: Environmental atmosphere

### Phase 4+: Production Tools (Future)
- Template system
- Batch processing
- Multi-reference management
- Natural language conversion
- And much more!

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

MIT License - See LICENSE file for details

---

## 📚 Citation

### Academic Citation

If you use this codebase in your research or project, please cite:

```bibtex
@software{comfyui_flux2_json,
  title = {ComfyUI FLUX2 JSON: building structured JSON prompts for FLUX.2},
  author = {[Drift Johnson]},
  year = {2025},
  url = {https://github.com/MushroomFleet/ComfyUI-FLUX2-JSON},
  version = {1.0.0}
}
```

### Donate:


[![Ko-Fi](https://cdn.ko-fi.com/cdn/kofi3.png?v=3)](https://ko-fi.com/driftjohnson)

---

## 💬 Support

- **Issues:** [GitHub Issues](https://github.com/MushroomFleet/ComfyUI-FLUX2-JSON/issues)
- **Discussions:** [GitHub Discussions](https://github.com/MushroomFleet/ComfyUI-FLUX2-JSON/discussions)
- **Documentation:** [Full Course](link-to-course-docs)

---

## 🙏 Acknowledgments

- Built for the FLUX.2 image generation model
- Inspired by the FLUX.2 JSON prompting capabilities
- Community feedback and testing

---

## 📊 Version History

### v1.0.0 (Phase 1) - Initial Release
- Core foundation nodes (6 nodes)
- Basic prompt assembly
- Scene, style, subject, camera control
- Preset libraries
- Documentation

---

**Ready to build precise, professional prompts for FLUX.2? Install now and start creating!** 🚀




