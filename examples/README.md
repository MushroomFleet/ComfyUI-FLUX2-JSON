# Example Workflows for FLUX.2 JSON Prompt Builder

This directory contains example ComfyUI workflows demonstrating the FLUX.2 Prompt Builder nodes.

## Available Examples

### 1. basic_product_shot.json
Simple product photography setup with single subject.

**Features demonstrated:**
- SceneBuilder with preset
- Single SubjectCreator
- CameraRig preset
- StyleSelector
- Basic PromptAssembler

**Use case:** Product catalog images

---

### 2. multi_subject_workspace.json
Complex scene with multiple subjects (laptop, coffee, plant).

**Features demonstrated:**
- Multiple SubjectCreator nodes
- SubjectArray for organization
- Position helpers
- Color specification
- Multi-subject composition

**Use case:** Lifestyle photography, tech workspace shots

---

### 3. portrait_setup.json
Professional portrait photography configuration.

**Features demonstrated:**
- Portrait camera preset
- Depth of field control
- Lighting considerations
- Mood setting

**Use case:** Professional portraits, headshots

---

### 4. custom_scene_advanced.json
Advanced workflow with all optional parameters.

**Features demonstrated:**
- Custom scene descriptions
- Environmental details (time of day, weather)
- Manual position descriptions
- Camera parameter fine-tuning
- Style modifiers

**Use case:** Learning advanced techniques

---

## How to Use

1. **Import into ComfyUI:**
   - File → Load
   - Navigate to this examples directory
   - Select desired workflow JSON

2. **Examine the Setup:**
   - Review node connections
   - Check parameter values
   - Read node descriptions

3. **Customize:**
   - Modify descriptions
   - Change colors
   - Adjust camera settings
   - Experiment!

4. **Generate:**
   - Connect to your FLUX.2 generation nodes
   - Copy JSON output from PromptAssembler
   - Generate images

---

## Learning Path

**Beginner:** Start with `basic_product_shot.json`
- Understand basic node connections
- Learn preset usage
- See minimal viable workflow

**Intermediate:** Try `multi_subject_workspace.json`
- Multiple subjects
- Position helpers
- Subject organization

**Advanced:** Explore `custom_scene_advanced.json`
- All optional parameters
- Fine-grained control
- Custom descriptions

---

## Creating Your Own

1. Start with an example as template
2. Replace descriptions with your subject
3. Adjust camera for your needs
4. Modify colors to match brand
5. Save your workflow for reuse

---

## Notes

- These workflows require FLUX.2 Prompt Builder nodes installed
- JSON outputs are ready to use with FLUX.2
- Modify freely to suit your needs
- Share your creations with the community!

---

For more information, see the main README.md
