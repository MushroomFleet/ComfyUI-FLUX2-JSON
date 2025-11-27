# Quick Installation & Setup Guide

## FLUX.2 JSON Prompt Builder for ComfyUI

**Version:** 1.0.0 (Phase 1)  
**Installation Time:** < 2 minutes  
**Difficulty:** Beginner-friendly

---

## Prerequisites

- ✅ ComfyUI installed and working
- ✅ Basic familiarity with ComfyUI interface
- ✅ FLUX.2 model access (for generation)

That's it! No additional dependencies needed.

---

## Installation Methods

### Method 1: ComfyUI Manager (Easiest) 🎯

**Coming Soon!** Will be available once published.

1. Open ComfyUI
2. Click ComfyUI Manager button
3. Search "FLUX2 Prompt Builder"
4. Click Install
5. Restart ComfyUI

---

### Method 2: Git Clone (Recommended) 💻

```bash
# Navigate to ComfyUI custom nodes directory
cd /path/to/ComfyUI/custom_nodes/

# Clone the repository
git clone https://github.com/yourusername/ComfyUI_FLUX2_Prompt_Builder.git

# Restart ComfyUI
```

**Advantages:**
- Easy updates via `git pull`
- Version control
- Can contribute back

---

### Method 3: Manual Download (Simple) 📦

1. **Download the package:**
   - Visit the GitHub releases page
   - Download `ComfyUI_FLUX2_Prompt_Builder.zip`
   - Or use the package in `/outputs/`

2. **Extract to ComfyUI:**
   ```
   ComfyUI/
   └── custom_nodes/
       └── ComfyUI_FLUX2_Prompt_Builder/   ← Extract here
           ├── __init__.py
           ├── nodes/
           └── ...
   ```

3. **Restart ComfyUI**

---

## Verification

### Step 1: Check Installation

After restarting ComfyUI, look for this in the console:

```
============================================================
FLUX.2 JSON Prompt Builder v1.0.0
Phase 1: Core Foundation - 6 nodes loaded
============================================================
```

If you see this, installation succeeded! ✅

---

### Step 2: Find the Nodes

1. Right-click in ComfyUI canvas
2. Navigate to: **Add Node** → **FLUX2_Prompt_Builder**
3. You should see 6 nodes:
   - Core/
     - FLUX2 Prompt Assembler 🎯
     - FLUX2 Scene Builder 🏗️
     - FLUX2 Style Selector 🎨
   - Subjects/
     - FLUX2 Subject Creator 👤
     - FLUX2 Subject Array 📋
   - Camera/
     - FLUX2 Camera Rig 📷

---

### Step 3: Quick Test

**Let's build your first prompt!**

1. **Add these nodes:**
   - FLUX2 Scene Builder
   - FLUX2 Subject Creator
   - FLUX2 Prompt Assembler

2. **Configure:**
   - Scene Builder: Select "Studio"
   - Subject Creator: Enter "Red apple on white plate"
   - Connect Scene → Assembler.scene
   - Connect Subject → Assembler.subjects

3. **Execute:**
   - Click "Queue Prompt"
   - Check Prompt Assembler output

4. **You should see:**
   ```json
   {
     "scene": "Professional photography studio...",
     "subjects": [
       {
         "description": "Red apple on white plate"
       }
     ]
   }
   ```

✅ **Success!** You're ready to use the nodes.

---

## First Workflow: Product Photography

Let's create a complete product shot prompt.

### Step-by-Step Setup

**1. Add Nodes (Right-click → Add Node → FLUX2_Prompt_Builder):**
- FLUX2 Scene Builder (Core)
- FLUX2 Subject Creator (Subjects)
- FLUX2 Camera Rig (Camera)
- FLUX2 Style Selector (Core)
- FLUX2 Prompt Assembler (Core)

**2. Arrange Nodes:**
```
[SceneBuilder]  [SubjectCreator]  [CameraRig]  [StyleSelector]
      ↓               ↓                ↓            ↓
      └───────────────┴────────────────┴────────────┘
                          ↓
                  [PromptAssembler]
```

**3. Configure Each Node:**

**Scene Builder:**
- scene_type: "Product Stage"

**Subject Creator:**
- description: "Minimalist ceramic coffee mug with matte finish"
- position_horizontal: "center"
- position_depth: "foreground"
- color_1: "#000000"

**Camera Rig:**
- preset: "Product Photography"

**Style Selector:**
- style_category: "Photorealistic"
- quality_level: "Commercial quality"

**4. Connect Outputs to Prompt Assembler:**
- SceneBuilder.scene → PromptAssembler.scene
- SubjectCreator.subject → PromptAssembler.subjects
- CameraRig.camera → PromptAssembler.camera
- StyleSelector.style → PromptAssembler.style

**5. Execute:**
- Click "Queue Prompt"
- View json_string output in PromptAssembler

**6. Copy JSON to FLUX.2:**
- Use the JSON with your FLUX.2 generation workflow

---

## Workflow Templates

### Template Files Location

Find example workflows in:
```
ComfyUI_FLUX2_Prompt_Builder/
└── examples/
    ├── README.md
    ├── basic_product_shot.json
    ├── multi_subject_workspace.json
    └── portrait_setup.json
```

### Loading Templates

1. File → Load
2. Navigate to examples folder
3. Select a JSON workflow
4. Examine and modify as needed

---

## Common Issues & Solutions

### Issue 1: Nodes Not Appearing

**Problem:** Can't find FLUX2 nodes in Add Node menu

**Solutions:**
- ✅ Restart ComfyUI completely
- ✅ Check console for error messages
- ✅ Verify folder is in `custom_nodes/`
- ✅ Check folder name is exactly `ComfyUI_FLUX2_Prompt_Builder`

---

### Issue 2: Import Errors

**Problem:** Console shows import errors

**Solutions:**
- ✅ Ensure `__init__.py` exists in main folder
- ✅ Verify all files in `nodes/` folder
- ✅ Check Python version (3.8+ required)
- ✅ Try deleting `.pyc` files and restart

---

### Issue 3: Node Execution Fails

**Problem:** Nodes show errors when executed

**Solutions:**
- ✅ Check all required inputs are provided
- ✅ Verify connections are correct type
- ✅ Review error message in console
- ✅ Try simple workflow first (Scene + Subject + Assembler)

---

### Issue 4: JSON Output Empty

**Problem:** PromptAssembler outputs `{}`

**Solutions:**
- ✅ Connect at least one input
- ✅ Check `remove_empty` setting
- ✅ Verify connected nodes executed
- ✅ Check for required fields (e.g., subject description)

---

## Configuration Tips

### Optimal Settings

**For Quick Prototyping:**
- Use presets extensively
- Enable `remove_empty` in Assembler
- Use `pretty_print` for readability

**For Production:**
- Customize all parameters
- Validate JSON before generation
- Save workflows for reuse

**For Experimentation:**
- Try different presets
- Combine multiple styles
- Test various camera angles

---

## Performance Notes

### Node Performance
- All nodes execute in <0.1 seconds
- No heavy computation
- Zero dependencies means stable
- Works on any ComfyUI install

### Workflow Tips
- Reuse Subject Arrays for multiple prompts
- Group common settings
- Save successful workflows
- Use presets for speed

---

## Integration with FLUX.2

### Connecting to FLUX.2

**Option A: Manual Copy**
1. Execute workflow
2. Copy JSON from PromptAssembler
3. Paste into FLUX.2 prompt field

**Option B: Direct Connection** (Future)
- Connect PromptAssembler.json_string to FLUX.2 prompt input
- Seamless workflow

---

## Learning Path

### Week 1: Basics
- ✅ Install nodes
- ✅ Create simple prompts
- ✅ Understand node connections
- ✅ Try all presets

### Week 2: Intermediate
- ✅ Multi-subject scenes
- ✅ Custom camera settings
- ✅ Position helpers
- ✅ Color specifications

### Week 3: Advanced
- ✅ Complete workflows
- ✅ Custom descriptions
- ✅ Fine camera control
- ✅ Template creation

---

## Resources

### Documentation
- 📖 [Main README](README.md) - Complete guide
- 📖 [Workflow Guide](WORKFLOW-GUIDE.md) - Visual workflows
- 📖 [Phase 1 Complete](PHASE-1-COMPLETE.md) - Implementation details

### Examples
- 📁 `examples/` - Workflow templates
- 🎯 Basic product shot
- 🎯 Multi-subject workspace
- 🎯 Portrait setup

### Testing
- 🧪 `test_nodes.py` - Run tests
- ✅ All tests pass out of the box

---

## Getting Help

### Self-Service
1. Check README.md troubleshooting section
2. Review example workflows
3. Run test suite: `python test_nodes.py`
4. Check console for errors

### Community Support
- GitHub Issues - Bug reports
- GitHub Discussions - Questions
- Discord - ComfyUI community
- Reddit - r/comfyui

---

## Next Steps

### After Installation
1. ✅ Complete quick test workflow
2. ✅ Try example templates
3. ✅ Create your first product shot
4. ✅ Experiment with presets
5. ✅ Share your results!

### Looking Ahead
- **Phase 2**: Visual color pickers, lighting rigs
- **Phase 3**: Advanced camera effects, film simulation  
- **Phase 4**: Batch processing, templates
- Stay tuned! 🚀

---

## Quick Reference

### Essential Keyboard Shortcuts
- `Space` - Add Node menu
- `Ctrl+C` / `Cmd+C` - Copy selected
- `Ctrl+V` / `Cmd+V` - Paste
- `Ctrl+S` / `Cmd+S` - Save workflow
- `Ctrl+O` / `Cmd+O` - Load workflow

### Node Categories
```
FLUX2_Prompt_Builder/
├── Core/          # Foundation nodes
├── Subjects/      # Subject control
└── Camera/        # Photography
```

### Minimum Workflow
```
SubjectCreator → PromptAssembler
```

### Recommended Workflow
```
SceneBuilder ──┐
SubjectCreator ┼→ PromptAssembler
CameraRig ─────┤
StyleSelector ─┘
```

---

## Success Checklist

Before you start creating:

- [ ] ComfyUI running smoothly
- [ ] Nodes installed and visible
- [ ] Quick test completed successfully
- [ ] Example workflow loaded
- [ ] JSON output visible
- [ ] Ready to create! 🎨

---

## Welcome Message

**Congratulations on installing FLUX.2 JSON Prompt Builder!** 🎉

You now have access to precise, modular control over FLUX.2 prompt generation. Start simple with presets, then explore advanced customization as you get comfortable.

**Happy prompting!** 🚀

---

*For detailed documentation, see README.md*  
*For workflow examples, see WORKFLOW-GUIDE.md*  
*For technical details, see PHASE-1-COMPLETE.md*
