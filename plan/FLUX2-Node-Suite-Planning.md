# FLUX.2 JSON Prompt Builder - Custom Node Suite Planning Document

**Project:** ComfyUI Custom Nodes for FLUX.2 Structured JSON Prompting  
**Version:** 1.0 Planning Phase  
**Date:** 2024

---

## Executive Summary

This document outlines a comprehensive suite of custom nodes for ComfyUI that enable visual, modular construction of FLUX.2 JSON prompts. The node architecture mirrors the FLUX.2 JSON schema, providing a no-code interface for building complex, production-grade prompts.

### Core Objective

Transform the FLUX.2 JSON prompting micro-course into a visual node-based workflow system where users can:
- Build JSON prompts through node connections instead of manual JSON editing
- Achieve reproducible, version-controlled prompt engineering
- Enable non-technical users to leverage advanced FLUX.2 capabilities
- Create reusable prompt templates and components

---

## Architecture Overview

### Design Philosophy

1. **Modular Composition:** Each JSON field becomes a dedicated node
2. **Visual Clarity:** Node outputs clearly show what they contribute
3. **Type Safety:** Proper data types and validation at node level
4. **Composability:** Nodes can be combined, saved as presets, and reused
5. **Progressive Disclosure:** Simple nodes for beginners, advanced options available

### Node Categories

The suite is organized into 7 primary categories:

```
FLUX2_Prompt_Builder/
├── Core/              # Foundation nodes (scene, style, mood)
├── Subjects/          # Subject definition and control
├── Visual/            # Color, lighting, composition
├── Camera/            # Photography simulation
├── Advanced/          # Multi-reference, upsampling, utilities
├── Presets/           # Template and preset loaders
└── Output/            # Final JSON assembly and formatting
```

---

## Node Mapping: Course to Implementation

### Module 1: Foundations (Lessons 1-3)
**Teaches:** Core concepts, schema understanding, conversion skills

#### Required Nodes:

**1. FLUX2_PromptAssembler** (Core Output Node)
- **Purpose:** Master node that collects all inputs and outputs final JSON
- **Inputs:** 
  - scene (STRING)
  - subjects (SUBJECT_ARRAY)
  - style (STRING)
  - color_palette (COLOR_ARRAY)
  - lighting (STRING)
  - mood (STRING)
  - background (STRING)
  - composition (STRING)
  - camera (CAMERA_OBJECT)
- **Outputs:**
  - json_string (STRING) - formatted JSON
  - json_object (DICT) - Python dict for processing
- **Features:**
  - Pretty-print formatting
  - Validation and error checking
  - Optional field filtering (removes empty fields)
  - Export to file option

**2. FLUX2_SceneBuilder** (Core)
- **Purpose:** Define overall scene context
- **Inputs:**
  - scene_type (DROPDOWN: "Studio", "Interior", "Exterior", "Abstract", "Custom")
  - description (STRING, multiline)
  - environment_details (STRING, optional)
- **Outputs:**
  - scene (STRING)
- **Presets:** Common scene types with descriptions

**3. FLUX2_StyleSelector** (Core)
- **Purpose:** Choose artistic style and rendering approach
- **Inputs:**
  - style_category (DROPDOWN: "Photorealistic", "Digital Art", "Film Photography", "Artistic", "Custom")
  - style_details (STRING, multiline)
  - quality_level (DROPDOWN: "Commercial", "Editorial", "Artistic", "Experimental")
- **Outputs:**
  - style (STRING)
- **Presets:** 50+ style templates

**4. FLUX2_MoodController** (Core)
- **Purpose:** Set emotional tone
- **Inputs:**
  - mood_category (DROPDOWN with common moods)
  - custom_mood (STRING, optional)
  - intensity (SLIDER: 0-100)
- **Outputs:**
  - mood (STRING)
- **Features:** Mood combination suggestions

---

### Module 2: Core JSON Techniques (Lessons 4-6)
**Teaches:** Subject control, camera parameters, composition

#### Required Nodes:

**5. FLUX2_SubjectCreator** (Subjects)
- **Purpose:** Define individual subject with all properties
- **Inputs:**
  - description (STRING, multiline, required)
  - position (STRING with helper dropdown)
  - action (STRING, optional)
  - pose (STRING, optional)
  - subject_colors (COLOR_ARRAY input, optional)
  - priority (INT: 1-10, for ordering)
- **Outputs:**
  - subject (SUBJECT_OBJECT)
- **Features:**
  - Visual preview of position grid
  - Common pose library
  - Action verb suggestions

**6. FLUX2_SubjectArray** (Subjects)
- **Purpose:** Collect multiple subjects into ordered array
- **Inputs:**
  - subject_1 (SUBJECT_OBJECT, optional)
  - subject_2 (SUBJECT_OBJECT, optional)
  - subject_3 (SUBJECT_OBJECT, optional)
  - subject_4 (SUBJECT_OBJECT, optional)
  - subject_5 (SUBJECT_OBJECT, optional)
- **Outputs:**
  - subjects (SUBJECT_ARRAY)
- **Features:**
  - Automatically filters null inputs
  - Maintains priority ordering
  - Shows subject count

**7. FLUX2_PositionHelper** (Subjects)
- **Purpose:** Visual positioning assistant
- **Inputs:**
  - grid_position (GRID_SELECTOR: 3x3 grid)
  - depth (DROPDOWN: "Foreground", "Midground", "Background")
  - offset (STRING, optional)
- **Outputs:**
  - position (STRING)
- **Features:**
  - Interactive visual grid
  - Generates natural language position descriptions
  - Relative positioning support

**8. FLUX2_CameraRig** (Camera)
- **Purpose:** Complete camera parameter control
- **Inputs:**
  - angle (DROPDOWN + custom)
  - distance (DROPDOWN: shot types)
  - lens_mm (INT: 16-200, slider)
  - f_number (DROPDOWN: f/1.4 - f/16)
  - iso (INT: 100-3200)
  - depth_of_field (STRING)
  - focus (STRING)
- **Outputs:**
  - camera (CAMERA_OBJECT)
- **Presets:**
  - Portrait setup
  - Product photography
  - Landscape
  - Macro
  - Street photography

**9. FLUX2_CameraPresets** (Camera)
- **Purpose:** Load common camera configurations
- **Inputs:**
  - preset (DROPDOWN: 20+ preset types)
  - allow_override (BOOLEAN)
- **Outputs:**
  - camera (CAMERA_OBJECT)
- **Presets Library:**
  - Canon 5D Mark IV portrait
  - Sony A7IV product
  - Fujifilm X-T5 street
  - Hasselblad medium format
  - iPhone 15 Pro style
  - Vintage film cameras

**10. FLUX2_CompositionGuide** (Visual)
- **Purpose:** Apply composition rules
- **Inputs:**
  - rule (DROPDOWN: "Rule of Thirds", "Golden Ratio", "Centered", "Diagonal", etc.)
  - custom_composition (STRING, optional)
- **Outputs:**
  - composition (STRING)
- **Features:**
  - Visual guide overlay preview
  - Common composition patterns

---

### Module 3: Advanced Color Control (Lessons 7-9)
**Teaches:** Hex colors, palettes, gradients, brand consistency

#### Required Nodes:

**11. FLUX2_HexColorPicker** (Visual)
- **Purpose:** Select and manage hex colors
- **Inputs:**
  - color_1 (COLOR_PICKER with hex display)
  - color_2 (COLOR_PICKER, optional)
  - color_3 (COLOR_PICKER, optional)
  - color_4 (COLOR_PICKER, optional)
  - include_color_names (BOOLEAN)
- **Outputs:**
  - color_palette (COLOR_ARRAY)
- **Features:**
  - Visual color preview
  - Hex code display and copy
  - Color harmony suggestions
  - Import from brand guidelines (hex list)

**12. FLUX2_ColorPaletteGenerator** (Visual)
- **Purpose:** Generate harmonious color palettes
- **Inputs:**
  - base_color (COLOR_PICKER)
  - harmony_type (DROPDOWN: "Monochromatic", "Analogous", "Complementary", "Triadic", "Split-Complementary")
  - num_colors (INT: 2-8)
- **Outputs:**
  - color_palette (COLOR_ARRAY)
- **Features:**
  - Real-time palette preview
  - Export palette for reuse
  - Accessibility checker (contrast ratios)

**13. FLUX2_GradientBuilder** (Visual)
- **Purpose:** Create gradient specifications
- **Inputs:**
  - start_color (COLOR_PICKER)
  - end_color (COLOR_PICKER)
  - gradient_type (DROPDOWN: "Linear", "Radial", "Conical")
  - direction (STRING, optional)
- **Outputs:**
  - gradient_description (STRING)
- **Use:** For subject colors or backgrounds with gradients

**14. FLUX2_BrandColors** (Visual)
- **Purpose:** Load and manage brand color libraries
- **Inputs:**
  - brand_preset (DROPDOWN: common brands + custom)
  - custom_hex_list (STRING: comma-separated)
- **Outputs:**
  - color_palette (COLOR_ARRAY)
  - brand_name (STRING)
- **Presets:**
  - Major tech brands (Apple, Google, Microsoft, etc.)
  - Social media (Twitter, Instagram, Facebook, etc.)
  - Custom brand library loader

---

### Module 4: Multi-Subject Composition (Lessons 10-12)
**Teaches:** Positioning, interactions, complex scenes

#### Required Nodes:

**15. FLUX2_SceneLayoutPlanner** (Advanced)
- **Purpose:** Plan multi-subject layouts visually
- **Inputs:**
  - layout_type (DROPDOWN: "Grid", "Layered", "Diagonal", "Circular", "Custom")
  - num_subjects (INT: 1-10)
- **Outputs:**
  - position_array (STRING_ARRAY) - suggested positions for each subject
- **Features:**
  - Visual layout preview
  - Exports position descriptions
  - Composition rule integration

**16. FLUX2_SubjectRelations** (Subjects)
- **Purpose:** Define relationships between subjects
- **Inputs:**
  - subject_a (SUBJECT_OBJECT)
  - subject_b (SUBJECT_OBJECT)
  - relationship (DROPDOWN: "next to", "behind", "in front of", "above", "below")
  - distance (STRING: optional modifier)
- **Outputs:**
  - updated_subjects (SUBJECT_ARRAY with modified positions)
- **Features:**
  - Relative positioning calculator
  - Spatial reasoning validation

**17. FLUX2_IncrementalBuilder** (Advanced)
- **Purpose:** Build scenes step-by-step with versioning
- **Inputs:**
  - base_prompt (JSON_OBJECT)
  - new_subject (SUBJECT_OBJECT, optional)
  - modifications (STRING, optional)
  - version_number (INT)
- **Outputs:**
  - updated_prompt (JSON_OBJECT)
  - version_history (STRING_ARRAY)
- **Features:**
  - Track changes across iterations
  - Rollback to previous versions
  - Compare versions side-by-side

---

### Module 5: Photorealism & Camera Simulation (Lessons 13-15)
**Teaches:** Advanced camera work, lighting, atmosphere

#### Required Nodes:

**18. FLUX2_LightingRig** (Visual)
- **Purpose:** Professional lighting setup
- **Inputs:**
  - setup_type (DROPDOWN: "Three-point", "Natural", "Studio", "Dramatic", "Custom")
  - light_quality (DROPDOWN: "Hard", "Soft", "Diffused")
  - color_temperature (INT: Kelvin, 2000-10000)
  - custom_description (STRING, optional)
- **Outputs:**
  - lighting (STRING)
- **Presets:**
  - Studio product photography
  - Natural window light
  - Golden hour
  - Neon nightscape
  - Candlelight
  - Overcast daylight

**19. FLUX2_AtmosphericEffects** (Visual)
- **Purpose:** Add environmental atmosphere
- **Inputs:**
  - effect_type (DROPDOWN: "Fog", "Haze", "Volumetric light", "Rain", "Snow", "Dust particles")
  - intensity (SLIDER: 0-100)
  - color_tint (COLOR_PICKER, optional)
- **Outputs:**
  - atmospheric_description (STRING)
- **Integration:** Adds to lighting or mood fields

**20. FLUX2_FilmStockSimulator** (Camera)
- **Purpose:** Simulate specific film stocks and eras
- **Inputs:**
  - film_era (DROPDOWN: "Modern Digital", "2000s Digicam", "90s Film", "80s Vintage", "70s", "60s")
  - film_stock (DROPDOWN based on era: "Kodak Portra 400", "Fuji Velvia 50", etc.)
  - grain_amount (SLIDER: 0-100)
- **Outputs:**
  - style_modifier (STRING)
  - camera_modifier (CAMERA_OBJECT with ISO/grain)
- **Features:**
  - Authentic film characteristics
  - Color cast simulation
  - Grain and texture patterns

**21. FLUX2_LensCharacteristics** (Camera)
- **Purpose:** Add lens-specific rendering qualities
- **Inputs:**
  - lens_type (DROPDOWN: "Prime", "Zoom", "Macro", "Fisheye", "Tilt-shift")
  - aberration (BOOLEAN: chromatic aberration)
  - vignetting (SLIDER: 0-100)
  - bokeh_shape (DROPDOWN: "Circular", "Hexagonal", "Octagonal")
- **Outputs:**
  - lens_description (STRING)
- **Integration:** Enhances camera object

---

### Module 6: Production Workflows (Lessons 16-18)
**Teaches:** Multi-reference, upsampling, automation

#### Required Nodes:

**22. FLUX2_MultiReferenceManager** (Advanced)
- **Purpose:** Manage multiple reference images for compositing
- **Inputs:**
  - reference_1 (IMAGE)
  - ref_1_role (STRING: "Subject style", "Color palette", "Composition", "Background")
  - reference_2 through reference_8 (IMAGE, optional)
  - ref_2-8_role (STRING, optional)
  - weight_distribution (STRING: how to balance references)
- **Outputs:**
  - reference_description (STRING)
  - reference_count (INT)
- **Features:**
  - Visual thumbnail preview
  - Role-based weighting
  - Reference image analysis hints

**23. FLUX2_PromptUpsampler** (Advanced)
- **Purpose:** Enable/configure prompt upsampling
- **Inputs:**
  - base_prompt (JSON_OBJECT)
  - enable_upsampling (BOOLEAN)
  - upsampling_focus (DROPDOWN: "Visual detail", "Atmospheric", "Technical", "Balanced")
- **Outputs:**
  - enhanced_prompt (JSON_OBJECT)
  - upsampling_note (STRING)
- **Features:**
  - Preview upsampling suggestions
  - Control upsampling direction

**24. FLUX2_BatchVariator** (Advanced)
- **Purpose:** Generate prompt variations for batch processing
- **Inputs:**
  - base_prompt (JSON_OBJECT)
  - vary_field (DROPDOWN: all JSON fields)
  - variations (STRING_ARRAY: different values to try)
  - batch_size (INT)
- **Outputs:**
  - prompt_array (JSON_ARRAY)
- **Features:**
  - A/B testing support
  - Systematic exploration
  - Export batch queue

**25. FLUX2_TemplateLoader** (Presets)
- **Purpose:** Load and save complete prompt templates
- **Inputs:**
  - template_category (DROPDOWN: "Product", "Portrait", "Landscape", "Abstract", etc.)
  - template_name (DROPDOWN: specific templates)
  - custom_path (STRING: file path for custom templates)
- **Outputs:**
  - template_prompt (JSON_OBJECT)
- **Features:**
  - Built-in template library
  - Save current workflow as template
  - Template marketplace integration (future)

**26. FLUX2_PromptLibrary** (Presets)
- **Purpose:** Manage reusable prompt components
- **Inputs:**
  - component_type (DROPDOWN: "Scene", "Subject", "Style", "Camera", "Lighting")
  - component_name (DROPDOWN: saved components)
  - save_current (BOOLEAN)
  - new_component_name (STRING)
- **Outputs:**
  - component (appropriate type)
- **Features:**
  - Personal library management
  - Search and filter
  - Import/export library

---

### Module 7: Specialized Applications (Lessons 19-21)
**Teaches:** Typography, infographics, sequential art

#### Required Nodes:

**27. FLUX2_TypographyDesigner** (Advanced)
- **Purpose:** Design text-heavy images with layout control
- **Inputs:**
  - title_text (STRING)
  - subtitle_text (STRING, optional)
  - body_text (STRING, optional)
  - text_layout (DROPDOWN: "Poster", "Magazine", "Advertisement", "Infographic")
  - typography_style (STRING)
- **Outputs:**
  - scene (STRING with typography specifications)
  - composition (STRING with text layout)
- **Features:**
  - Text hierarchy helper
  - Font style suggestions
  - Layout grid templates

**28. FLUX2_InfographicBuilder** (Advanced)
- **Purpose:** Structure infographic generations
- **Inputs:**
  - infographic_type (DROPDOWN: "Vertical", "Horizontal", "Grid", "Timeline", "Comparison")
  - title (STRING)
  - num_sections (INT: 2-8)
  - section_content (STRING_ARRAY)
  - icon_style (STRING)
  - data_viz_type (DROPDOWN: "Charts", "Icons", "Illustrations", "Mixed")
- **Outputs:**
  - infographic_prompt (JSON_OBJECT)
- **Features:**
  - Section layout calculator
  - Data visualization hints
  - Color scheme for data categories

**29. FLUX2_ComicPanelCreator** (Advanced)
- **Purpose:** Create consistent sequential art panels
- **Inputs:**
  - character_description (STRING, persistent)
  - panel_action (STRING)
  - panel_dialogue (STRING, optional)
  - panel_number (INT)
  - art_style (STRING: comic style)
- **Outputs:**
  - panel_prompt (JSON_OBJECT)
- **Features:**
  - Character consistency helper
  - Panel layout suggestions
  - Speech bubble positioning
  - Action lines and effects

**30. FLUX2_SequenceManager** (Advanced)
- **Purpose:** Manage multi-panel sequences
- **Inputs:**
  - sequence_name (STRING)
  - panel_prompts (JSON_ARRAY)
  - maintain_consistency (BOOLEAN)
  - shared_elements (STRING: characters, locations, etc.)
- **Outputs:**
  - sequence_queue (JSON_ARRAY)
- **Features:**
  - Consistency checking across panels
  - Character/location library per sequence
  - Batch generation queue

---

### Module 8: Utilities & Helpers
**Supporting nodes for enhanced workflow**

#### Required Nodes:

**31. FLUX2_PromptValidator** (Output)
- **Purpose:** Validate JSON prompt structure and suggest improvements
- **Inputs:**
  - prompt (JSON_OBJECT)
  - strict_mode (BOOLEAN)
- **Outputs:**
  - is_valid (BOOLEAN)
  - errors (STRING_ARRAY)
  - warnings (STRING_ARRAY)
  - suggestions (STRING_ARRAY)
- **Features:**
  - Schema validation
  - Conflict detection
  - Best practice checking
  - Performance optimization hints

**32. FLUX2_PromptAnalyzer** (Output)
- **Purpose:** Analyze prompt complexity and predict results
- **Inputs:**
  - prompt (JSON_OBJECT)
- **Outputs:**
  - complexity_score (INT: 1-10)
  - field_count (INT)
  - analysis_report (STRING)
  - estimated_generation_time (STRING)
- **Features:**
  - Complexity metrics
  - Token usage estimation
  - Field coverage analysis

**33. FLUX2_PromptComparator** (Output)
- **Purpose:** Compare two prompts to see differences
- **Inputs:**
  - prompt_a (JSON_OBJECT)
  - prompt_b (JSON_OBJECT)
- **Outputs:**
  - diff_report (STRING)
  - changed_fields (STRING_ARRAY)
  - similarity_score (FLOAT: 0-1)
- **Features:**
  - Visual diff display
  - Highlight changes
  - Merge suggestions

**34. FLUX2_NaturalLanguageParser** (Advanced)
- **Purpose:** Convert natural language prompts to JSON structure
- **Inputs:**
  - natural_prompt (STRING, multiline)
  - parsing_mode (DROPDOWN: "Strict", "Balanced", "Creative")
- **Outputs:**
  - parsed_prompt (JSON_OBJECT)
  - confidence (FLOAT: 0-1)
  - ambiguities (STRING_ARRAY)
- **Features:**
  - AI-assisted parsing (local or API)
  - Ambiguity highlighting
  - Suggest fields from text

**35. FLUX2_PromptExporter** (Output)
- **Purpose:** Export prompts in various formats
- **Inputs:**
  - prompt (JSON_OBJECT)
  - format (DROPDOWN: "JSON", "YAML", "Natural Language", "API Call", "Template")
  - include_metadata (BOOLEAN)
- **Outputs:**
  - exported_text (STRING)
  - file_path (STRING, if saved)
- **Features:**
  - Multiple export formats
  - Metadata inclusion (date, version, author)
  - API-ready formatting

**36. FLUX2_RandomPromptGenerator** (Advanced)
- **Purpose:** Generate random prompts for exploration
- **Inputs:**
  - category (DROPDOWN: "Product", "Portrait", "Landscape", "Abstract", "Any")
  - complexity (DROPDOWN: "Simple", "Medium", "Complex")
  - randomness_seed (INT)
- **Outputs:**
  - random_prompt (JSON_OBJECT)
- **Features:**
  - Coherent random generation
  - Discovery of new combinations
  - Seeded for reproducibility

**37. FLUX2_BackgroundRemover** (Visual)
- **Purpose:** Specify background removal/replacement
- **Inputs:**
  - removal_mode (DROPDOWN: "Remove", "Replace", "Blur", "Keep")
  - replacement_description (STRING, optional)
  - edge_treatment (DROPDOWN: "Sharp", "Soft", "Natural")
- **Outputs:**
  - background (STRING with removal spec)
- **Integration:** Connects to background field

---

## Implementation Roadmap

### Phase 1: Core Foundation (Weeks 1-2)
**Priority:** Essential nodes for basic functionality

**Nodes to implement:**
1. FLUX2_PromptAssembler (Critical - master output)
2. FLUX2_SceneBuilder
3. FLUX2_StyleSelector
4. FLUX2_SubjectCreator
5. FLUX2_SubjectArray
6. FLUX2_CameraRig

**Deliverables:**
- Basic prompt construction possible
- Simple workflows functional
- Documentation for core nodes
- Example workflows for each node

**Success Criteria:**
- Can build product photography prompt via nodes
- JSON output is valid and well-formed
- Nodes have proper input/output types

---

### Phase 2: Visual Control (Weeks 3-4)
**Priority:** Color, lighting, composition

**Nodes to implement:**
7. FLUX2_HexColorPicker
8. FLUX2_ColorPaletteGenerator
9. FLUX2_LightingRig
10. FLUX2_CompositionGuide
11. FLUX2_MoodController
12. FLUX2_PositionHelper

**Deliverables:**
- Complete visual control toolkit
- Color harmony tools working
- Lighting presets library
- Position visual grid functional

**Success Criteria:**
- Can specify exact brand colors
- Professional lighting setups achievable
- Visual positioning tools aid composition

---

### Phase 3: Advanced Camera & Photography (Weeks 5-6)
**Priority:** Photorealism and professional control

**Nodes to implement:**
13. FLUX2_CameraPresets
14. FLUX2_LensCharacteristics
15. FLUX2_FilmStockSimulator
16. FLUX2_AtmosphericEffects

**Deliverables:**
- Complete camera simulation
- Film stock presets library (30+ stocks)
- Lens effect controls
- Atmospheric enhancement tools

**Success Criteria:**
- Can replicate real camera setups
- Film photography styles achievable
- Professional photorealism possible

---

### Phase 4: Production & Workflow Tools (Weeks 7-8)
**Priority:** Professional workflow support

**Nodes to implement:**
17. FLUX2_TemplateLoader
18. FLUX2_PromptLibrary
19. FLUX2_BatchVariator
20. FLUX2_IncrementalBuilder
21. FLUX2_MultiReferenceManager
22. FLUX2_PromptUpsampler

**Deliverables:**
- Template system functional
- Library management working
- Batch processing supported
- Version control for prompts
- Multi-reference system complete

**Success Criteria:**
- Can save and reload templates
- Batch variations generate correctly
- Multi-reference properly configured
- Team collaboration possible

---

### Phase 5: Specialized Applications (Weeks 9-10)
**Priority:** Niche use cases

**Nodes to implement:**
23. FLUX2_TypographyDesigner
24. FLUX2_InfographicBuilder
25. FLUX2_ComicPanelCreator
26. FLUX2_SequenceManager
27. FLUX2_BrandColors
28. FLUX2_GradientBuilder

**Deliverables:**
- Typography tools complete
- Infographic builder functional
- Sequential art support
- Brand asset tools

**Success Criteria:**
- Can design text-heavy images
- Infographic structure generates correctly
- Comic panels maintain consistency
- Brand guidelines enforceable

---

### Phase 6: Utilities & Polish (Weeks 11-12)
**Priority:** Quality of life and advanced features

**Nodes to implement:**
29. FLUX2_PromptValidator
30. FLUX2_PromptAnalyzer
31. FLUX2_PromptComparator
32. FLUX2_NaturalLanguageParser
33. FLUX2_PromptExporter
34. FLUX2_RandomPromptGenerator
35. FLUX2_BackgroundRemover
36. FLUX2_SceneLayoutPlanner
37. FLUX2_SubjectRelations

**Deliverables:**
- All utility nodes complete
- Validation and analysis tools
- Natural language conversion
- Export system for multiple formats
- Complete node suite documentation

**Success Criteria:**
- Prompts validate automatically
- Natural language parsing works
- Export to multiple formats
- Random generation for exploration
- Full node suite is cohesive

---

## Technical Implementation Details

### Node Base Class Structure

```python
class FLUX2BaseNode:
    """Base class for all FLUX2 prompt builder nodes"""
    
    CATEGORY = "FLUX2_Prompt_Builder"
    RETURN_TYPES = ()
    FUNCTION = "execute"
    
    @classmethod
    def INPUT_TYPES(cls):
        return {}
    
    def execute(self, **kwargs):
        pass
    
    def validate_inputs(self, **kwargs):
        """Validate node inputs"""
        pass
    
    def format_output(self, data):
        """Format output data consistently"""
        pass
```

### Custom Data Types

We need to define custom types for ComfyUI:

```python
# Custom type definitions
SUBJECT_OBJECT = "SUBJECT_OBJECT"
SUBJECT_ARRAY = "SUBJECT_ARRAY"
CAMERA_OBJECT = "CAMERA_OBJECT"
COLOR_ARRAY = "COLOR_ARRAY"
JSON_OBJECT = "JSON_OBJECT"
JSON_ARRAY = "JSON_ARRAY"
```

### Data Structure Standards

**SUBJECT_OBJECT structure:**
```python
{
    "description": str,
    "position": str (optional),
    "action": str (optional),
    "pose": str (optional),
    "color_palette": list[str] (optional)
}
```

**CAMERA_OBJECT structure:**
```python
{
    "angle": str (optional),
    "distance": str (optional),
    "lens": str (optional),
    "lens-mm": int (optional),
    "f-number": str (optional),
    "ISO": int (optional),
    "depth_of_field": str (optional),
    "focus": str (optional)
}
```

**COLOR_ARRAY structure:**
```python
[
    "#HEXCODE",  # Hex format
    "color name",  # Name format
    "descriptive color #HEX"  # Mixed format
]
```

**JSON_OBJECT structure:**
```python
{
    "scene": str (optional),
    "subjects": list[SUBJECT_OBJECT] (optional),
    "style": str (optional),
    "color_palette": COLOR_ARRAY (optional),
    "lighting": str (optional),
    "mood": str (optional),
    "background": str (optional),
    "composition": str (optional),
    "camera": CAMERA_OBJECT (optional)
}
```

---

## Node Design Guidelines

### Visual Design Principles

1. **Color Coding:**
   - Core nodes: Blue (#4A90E2)
   - Subject nodes: Green (#27AE60)
   - Visual nodes: Purple (#9B59B6)
   - Camera nodes: Orange (#E67E22)
   - Advanced nodes: Red (#E74C3C)
   - Output nodes: Gray (#95A5A6)

2. **Size & Layout:**
   - Consistent width: 300px default
   - Expandable for complex inputs
   - Collapsible sections for advanced options
   - Clear visual hierarchy

3. **Input/Output Labeling:**
   - Clear, descriptive labels
   - Type indicators visible
   - Optional inputs marked clearly
   - Tooltips for complex fields

### User Experience Principles

1. **Progressive Disclosure:**
   - Basic options visible by default
   - Advanced options collapsible
   - Presets available for quick use
   - Custom options for power users

2. **Discoverability:**
   - Descriptive node names
   - Category organization clear
   - Search-friendly naming
   - Example values provided

3. **Error Prevention:**
   - Input validation at node level
   - Type checking automatic
   - Helpful error messages
   - Suggestion system for fixes

4. **Efficiency:**
   - Presets for common use cases
   - Copy/paste support
   - Template system integrated
   - Keyboard shortcuts where possible

---

## Testing Strategy

### Unit Testing (Per Node)

Each node requires:
- Input validation tests
- Output format tests
- Edge case handling
- Null input handling
- Type checking validation

**Example test cases for FLUX2_SubjectCreator:**
```python
def test_subject_creator_basic():
    # Test with only required fields
    result = node.execute(description="Red apple")
    assert result["description"] == "Red apple"
    assert "position" not in result

def test_subject_creator_full():
    # Test with all fields
    result = node.execute(
        description="Red apple",
        position="Center foreground",
        action="Rolling",
        color_palette=["#FF0000"]
    )
    assert all keys exist
    
def test_subject_creator_validation():
    # Test validation errors
    with pytest.raises(ValueError):
        node.execute()  # Missing required description
```

### Integration Testing (Node Combinations)

Test common workflows:
- Scene + Subject + Style → Assembler
- Camera + Lighting + Composition → Complete setup
- Multiple Subjects → Subject Array → Assembler
- Color Picker → Subject → Assembler

**Example integration test:**
```python
def test_product_photography_workflow():
    scene = scene_builder.execute(scene_type="Studio")
    subject = subject_creator.execute(
        description="Coffee mug",
        color_palette=["#000000"]
    )
    camera = camera_rig.execute(lens_mm=85, f_number="f/5.6")
    
    result = assembler.execute(
        scene=scene,
        subjects=[subject],
        camera=camera
    )
    
    assert validate_json(result)
    assert "scene" in result
    assert len(result["subjects"]) == 1
    assert result["camera"]["lens-mm"] == 85
```

### User Acceptance Testing

Real-world scenarios:
1. New user creates first product shot
2. Designer implements brand guidelines
3. Photographer replicates film stock
4. Artist creates sequential panels
5. Team collaborates on templates

---

## Documentation Requirements

### Per-Node Documentation

Each node needs:

1. **Purpose Statement:** Clear one-sentence description
2. **Input Reference:** Every input with type and description
3. **Output Reference:** Every output with type and description
4. **Usage Examples:** 2-3 common use cases
5. **Tips & Tricks:** Best practices and pro tips
6. **Related Nodes:** Suggestions for combinations

**Example format:**

```markdown
# FLUX2_SubjectCreator

## Purpose
Creates a subject object with detailed description and positioning for use in FLUX.2 prompts.

## Inputs
- **description** (STRING, required): Detailed description of the subject
- **position** (STRING, optional): Where in frame the subject appears
- **action** (STRING, optional): What the subject is doing
- **pose** (STRING, optional): Static positioning or body language
- **subject_colors** (COLOR_ARRAY, optional): Colors specific to this subject

## Outputs
- **subject** (SUBJECT_OBJECT): Complete subject specification

## Examples

### Example 1: Simple Product
```
description: "Ceramic coffee mug with matte finish"
position: "Center foreground"
color_palette: ["#000000"]
```

### Example 2: Character with Action
```
description: "Young woman in casual attire"
position: "Right side of frame"
action: "Walking toward camera"
pose: "Confident stride, head slightly tilted"
```

## Tips
- Be specific in descriptions for better results
- Use position helpers for complex layouts
- Color palette here overrides global colors
- Priority field determines rendering order

## Related Nodes
- FLUX2_SubjectArray (collect multiple subjects)
- FLUX2_PositionHelper (visual positioning aid)
- FLUX2_HexColorPicker (choose exact colors)
```

### Global Documentation

**Required documents:**

1. **Getting Started Guide**
   - Installation instructions
   - First workflow tutorial
   - Basic node overview
   - Common patterns

2. **Complete Node Reference**
   - All 37 nodes documented
   - Organized by category
   - Search functionality
   - Cross-references

3. **Workflow Examples**
   - 20+ pre-built workflows
   - Various complexity levels
   - Different use cases
   - Downloadable JSON files

4. **Best Practices Guide**
   - When to use which nodes
   - Optimization tips
   - Common pitfalls
   - Performance considerations

5. **API Reference**
   - Custom type definitions
   - Node base classes
   - Extension guidelines
   - Contributing guide

---

## Quality Assurance Checklist

### Before Release - Per Node

- [ ] Inputs validated and type-checked
- [ ] Outputs formatted consistently
- [ ] Error handling implemented
- [ ] Default values sensible
- [ ] Tooltips and help text complete
- [ ] Visual design consistent
- [ ] Performance optimized
- [ ] Unit tests pass (>90% coverage)
- [ ] Documentation complete
- [ ] Examples provided

### Before Release - Full Suite

- [ ] All 37 nodes implemented
- [ ] Integration tests pass
- [ ] Example workflows tested
- [ ] Documentation complete and accurate
- [ ] Installation process smooth
- [ ] No dependency conflicts
- [ ] Performance benchmarks met
- [ ] User testing completed
- [ ] Bug tracker established
- [ ] Version control in place

---

## Future Enhancements (Post-V1)

### Version 1.1 Ideas

1. **Visual Prompt Builder GUI**
   - Standalone UI for prompt construction
   - Real-time preview
   - Drag-and-drop elements

2. **AI Assistant Integration**
   - Natural language to node workflow
   - Optimization suggestions
   - Automatic error fixing

3. **Cloud Library**
   - Community templates
   - Preset marketplace
   - Collaborative workflows

4. **Advanced Analytics**
   - Prompt performance tracking
   - A/B testing automation
   - Success rate analysis

5. **Mobile Companion App**
   - Remote workflow triggering
   - Preview and approval
   - Library management

### Version 2.0 Vision

1. **Multi-Model Support**
   - Adapt to other image generators
   - Model-specific optimizations
   - Cross-model workflows

2. **Video Extension**
   - Sequence management for video
   - Keyframe interpolation
   - Motion prompting

3. **3D Integration**
   - Camera path planning
   - 3D scene layout
   - Lighting simulation

---

## Resource Requirements

### Development Team

- **Lead Developer:** Node architecture, core implementation
- **UI/UX Designer:** Node visual design, user experience
- **Documentation Writer:** All documentation and tutorials
- **QA Tester:** Testing, bug tracking, user feedback

### Tools & Infrastructure

- **Development:** Python, ComfyUI SDK, Git
- **Testing:** pytest, ComfyUI test environment
- **Documentation:** Markdown, GitHub Pages/ReadTheDocs
- **Community:** Discord server, GitHub Discussions, Reddit

### Timeline

- **Total Duration:** 12 weeks for V1.0
- **Per Phase:** 2 weeks average
- **Testing:** Ongoing throughout
- **Documentation:** Parallel to development
- **Beta Testing:** Week 11-12

---

## Success Metrics

### User Adoption
- **Week 1:** 100 users
- **Month 1:** 1,000 users
- **Month 3:** 5,000 users
- **Month 6:** 10,000+ users

### Engagement
- **Daily Active Users:** >20% of installs
- **Workflows Created:** Average 10 per user
- **Template Shares:** 500+ community templates

### Quality
- **Bug Reports:** <5 per 1000 users
- **User Satisfaction:** >4.5/5 stars
- **Documentation Completeness:** 100%
- **Test Coverage:** >90%

---

## Conclusion

This comprehensive suite of 37 custom nodes transforms FLUX.2's JSON prompting system into a visual, modular workflow that makes advanced prompting accessible to all skill levels. By mapping each capability from the micro-course to specific nodes, we create a complete ecosystem for professional image generation.

The phased implementation ensures core functionality arrives early while advanced features develop over time. The focus on documentation, testing, and user experience will drive adoption and create a thriving community around the tools.

**Next Steps:**
1. Review and approve this planning document
2. Set up development environment
3. Begin Phase 1 implementation
4. Establish testing framework
5. Start documentation structure

---

**Ready to proceed with implementation?** Let's start building the FLUX.2 JSON Prompt Builder node suite!
