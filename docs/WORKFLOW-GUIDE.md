# FLUX.2 JSON Prompt Builder - Visual Workflow Guide

## Basic Workflow Diagram

```
┌─────────────────────┐
│  FLUX2_SceneBuilder │
│       🏗️            │
│                     │
│ Preset: "Studio"    │
│ Time: "Morning"     │
└──────────┬──────────┘
           │ scene
           │
           ▼
┌─────────────────────┐
│ FLUX2_StyleSelector │
│       🎨            │
│                     │
│ Category:           │
│ "Photorealistic"    │
└──────────┬──────────┘
           │ style
           │
           ▼
┌─────────────────────┐        ┌─────────────────────┐
│ FLUX2_SubjectCreator│        │ FLUX2_SubjectCreator│
│       👤            │        │       👤            │
│                     │        │                     │
│ Desc: "Coffee mug"  │        │ Desc: "Laptop"      │
│ Pos: "Center"       │        │ Pos: "Right"        │
│ Color: "#000000"    │        │ Color: "#C0C0C0"    │
└──────────┬──────────┘        └──────────┬──────────┘
           │ subject_1                    │ subject_2
           │                              │
           └──────────┬───────────────────┘
                      ▼
           ┌─────────────────────┐
           │ FLUX2_SubjectArray  │
           │       📋            │
           │                     │
           │ Collects subjects   │
           │ Shows summary       │
           └──────────┬──────────┘
                      │ subjects
                      │
                      ▼
           ┌─────────────────────┐
           │   FLUX2_CameraRig   │
           │       📷            │
           │                     │
           │ Preset: "Product    │
           │ Photography"        │
           └──────────┬──────────┘
                      │ camera
                      │
    ┌─────────────────┴─────────────────┐
    │                                     │
    │  All inputs connect here            │
    ▼                                     ▼
┌───────────────────────────────────────────┐
│       FLUX2_PromptAssembler 🎯           │
│                                           │
│  ┌─────────────────────────────────────┐ │
│  │  Final JSON Output                  │ │
│  │  {                                  │ │
│  │    "scene": "...",                  │ │
│  │    "subjects": [...],               │ │
│  │    "style": "...",                  │ │
│  │    "camera": {...}                  │ │
│  │  }                                  │ │
│  └─────────────────────────────────────┘ │
│                                           │
│  Copy this JSON to FLUX.2 →              │
└───────────────────────────────────────────┘
```

---

## Node Connection Reference

### Input → Output Connections

```
SceneBuilder.scene → PromptAssembler.scene
StyleSelector.style → PromptAssembler.style
SubjectCreator.subject → SubjectArray.subject_N
SubjectArray.subjects → PromptAssembler.subjects
CameraRig.camera → PromptAssembler.camera
```

---

## Workflow Variations

### 1. Minimal Workflow (Single Subject)

```
SceneBuilder → PromptAssembler
               ↑
SubjectCreator ┘
```

**Use case:** Simple, single-subject images

---

### 2. Standard Workflow (Multi-Subject)

```
SceneBuilder ────┐
StyleSelector ───┼──→ PromptAssembler
SubjectArray ────┤
CameraRig ───────┘
    ↑
    │
SubjectCreator (x3)
```

**Use case:** Product photography, lifestyle shots

---

### 3. Advanced Workflow (Full Control)

```
SceneBuilder ────┐
StyleSelector ───┤
SubjectArray ────┤
CameraRig ───────┼──→ PromptAssembler
[mood input] ────┤
[lighting input] ┤
[background] ────┤
[composition] ───┘
    ↑
    │
SubjectCreator (x8)
```

**Use case:** Professional, production-grade images

---

## Node Categories & Colors

```
┌──────────────────────┐
│   Core Nodes (Blue)  │
├──────────────────────┤
│ • PromptAssembler    │ 🎯
│ • SceneBuilder       │ 🏗️
│ • StyleSelector      │ 🎨
└──────────────────────┘

┌──────────────────────┐
│ Subject Nodes (Green)│
├──────────────────────┤
│ • SubjectCreator     │ 👤
│ • SubjectArray       │ 📋
└──────────────────────┘

┌──────────────────────┐
│ Camera Nodes (Orange)│
├──────────────────────┤
│ • CameraRig          │ 📷
└──────────────────────┘
```

---

## Data Flow Types

```
STRING ───────────────→  Simple text
SUBJECT_OBJECT ───────→  Single subject
SUBJECT_ARRAY ────────→  Multiple subjects
CAMERA_OBJECT ────────→  Camera parameters
JSON_OBJECT ──────────→  Complete prompt
```

---

## Common Workflow Patterns

### Pattern A: Quick Product Shot

```
1. Add SceneBuilder (Studio preset)
2. Add SubjectCreator (product description)
3. Add CameraRig (Product Photography preset)
4. Add PromptAssembler
5. Connect all outputs
6. Generate!

Time: ~2 minutes
```

---

### Pattern B: Multi-Product Composition

```
1. Add SceneBuilder
2. Add 3x SubjectCreator (one per product)
3. Add SubjectArray
4. Add CameraRig
5. Add StyleSelector
6. Add PromptAssembler
7. Connect all
8. Generate!

Time: ~5 minutes
```

---

### Pattern C: Styled Portrait

```
1. Add SceneBuilder (Interior preset)
2. Add SubjectCreator (person description)
3. Add CameraRig (Portrait preset)
4. Add StyleSelector (Film Photography)
5. Add PromptAssembler with mood input
6. Generate!

Time: ~3 minutes
```

---

## Troubleshooting Workflows

### Issue: No output from PromptAssembler
```
Check:
1. Is at least one input connected?
2. Are all connected nodes executed?
3. Is remove_empty disabled if testing?

Solution:
- Ensure scene OR subjects is connected
- Execute workflow (Queue Prompt)
```

---

### Issue: Subject not appearing
```
Check:
1. Is SubjectCreator connected to SubjectArray?
2. Is SubjectArray connected to PromptAssembler?
3. Does subject have a description?

Solution:
- Verify connection chain
- Check subject description field
```

---

### Issue: Camera settings not applying
```
Check:
1. Is CameraRig connected to PromptAssembler?
2. Is a preset selected or custom values entered?
3. Is override_preset correctly set?

Solution:
- Select a preset OR enter custom values
- Check override_preset if mixing both
```

---

## Advanced Connection Patterns

### Modular Template System

```
Save as separate groups:

[Product Setup]         [Portrait Setup]
├─ SceneBuilder        ├─ SceneBuilder
├─ CameraRig           ├─ CameraRig
└─ StyleSelector       └─ StyleSelector

Reuse these groups + new subjects!
```

---

### Batch Variation System

```
Same subjects + different styles:

SubjectArray ───┬──→ PromptAssembler #1
                │     (Style: Photorealistic)
                │
                ├──→ PromptAssembler #2
                │     (Style: Film)
                │
                └──→ PromptAssembler #3
                      (Style: Artistic)

Generate 3 variations from one subject setup!
```

---

## Node Execution Order

ComfyUI automatically determines execution order, but understanding it helps:

```
1. Leaf nodes execute first:
   - SceneBuilder
   - StyleSelector
   - SubjectCreator nodes
   - CameraRig

2. Collection nodes next:
   - SubjectArray (waits for all SubjectCreators)

3. Assembler last:
   - PromptAssembler (waits for all inputs)
```

---

## Performance Tips

### Efficient Workflows

✅ **DO:**
- Reuse SubjectArray for multiple prompts
- Group common settings (scene + camera)
- Use presets for speed
- Save successful workflows

❌ **DON'T:**
- Create duplicate nodes unnecessarily
- Connect unused nodes
- Over-complicate simple scenes

---

## Workflow Templates

### Template 1: E-commerce Product
```
Nodes: 4
Time: 2 min
Output: Clean product shot

SceneBuilder: "Product Stage"
SubjectCreator: Product description
CameraRig: "Product Photography"
PromptAssembler: Collect
```

### Template 2: Tech Workspace
```
Nodes: 7
Time: 5 min
Output: Multi-item scene

SceneBuilder: "Office"
SubjectCreator x3: Laptop, coffee, phone
SubjectArray: Collect
CameraRig: Custom overhead
StyleSelector: "Photorealistic"
PromptAssembler: Full setup
```

### Template 3: Portrait
```
Nodes: 5
Time: 3 min
Output: Professional portrait

SceneBuilder: "Studio" or "Interior"
SubjectCreator: Person details
CameraRig: "Portrait"
StyleSelector: "Film Photography"
PromptAssembler: + mood input
```

---

## Quick Reference Card

```
┌────────────────────────────────────────┐
│ Essential Connections                  │
├────────────────────────────────────────┤
│ SceneBuilder → PromptAssembler.scene   │
│ StyleSelector → PromptAssembler.style  │
│ SubjectArray → PromptAssembler.subjects│
│ CameraRig → PromptAssembler.camera     │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│ Minimum Viable Workflow                │
├────────────────────────────────────────┤
│ 1. SubjectCreator                      │
│ 2. PromptAssembler                     │
│ → Connect subject → PromptAssembler    │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│ Recommended Workflow                   │
├────────────────────────────────────────┤
│ 1. SceneBuilder                        │
│ 2. SubjectCreator(s)                   │
│ 3. SubjectArray (if multiple)          │
│ 4. CameraRig                           │
│ 5. StyleSelector                       │
│ 6. PromptAssembler                     │
└────────────────────────────────────────┘
```

---

## Success Checklist

Before generating, verify:

- [ ] At least one input connected to PromptAssembler
- [ ] All SubjectCreators have descriptions
- [ ] SubjectArray connected if using multiple subjects
- [ ] Camera or Style specified for quality
- [ ] PromptAssembler set to pretty_print=True
- [ ] Workflow executed (Queue Prompt clicked)
- [ ] JSON output visible in PromptAssembler

---

## Next Steps After Phase 1

Phase 2 will add visual tools:

```
Future nodes to connect:

HexColorPicker ────→ SubjectCreator.colors
                  └→ PromptAssembler.color_palette

LightingRig ───────→ PromptAssembler.lighting

CompositionGuide ──→ PromptAssembler.composition

MoodController ────→ PromptAssembler.mood
```

Stay tuned! 🚀

---

*For more details, see the main README.md*
