# 🦖 Godzilla Example - Converting Natural Language to Structured JSON Prompts

**From traditional prompt to FLUX.2 JSON using the Prompt Builder nodes**

---

## 📝 Original Natural Language Prompt

```
A towering Godzilla suit with rough, charcoal-gray rubber scales and visible seams stands amid a miniature Tokyo cityscape of balsa wood buildings and cardboard skyscrapers, filmed in oversaturated 1960s color film with harsh studio lighting casting dramatic shadows, practical pyrotechnic explosions creating orange fireballs and billowing smoke, the camera at low angles to emphasize the monster's imposing stature while capturing the distinctive stiff, lumbering movement of the actor inside 
the heavy costume, power lines made of thread stretched across the set, tiny model trains and cars scattered among the destruction, all bathed in the distinctive warm, slightly faded Eastmancolor palette with visible film grain.
```

---

## 🎯 Step 1: Analyze the Prompt Components

Let's break down what this prompt is describing:

### **Scene Elements:**
- Miniature Tokyo cityscape
- Balsa wood buildings
- Cardboard skyscrapers
- Model trains and cars
- Thread power lines
- Practical pyrotechnic effects

### **Main Subject:**
- Godzilla suit (practical effect)
- Charcoal-gray rubber scales
- Visible seams
- Stiff, lumbering movement

### **Style & Era:**
- 1960s tokusatsu/kaiju film
- Eastmancolor film stock
- Oversaturated colors
- Visible film grain
- Faded, warm palette

### **Camera & Lighting:**
- Low angle shots
- Harsh studio lighting
- Dramatic shadows
- Emphasizing imposing stature

### **Atmosphere:**
- Orange fireballs
- Billowing smoke
- Destruction aesthetic
- Vintage practical effects

---

## 🛠️ Step 2: Build with ComfyUI Nodes

### **Workflow Setup**

```
[FLUX2_SceneBuilder]
    ↓ scene
[FLUX2_SubjectCreator] × 2
    ↓ subject
[FLUX2_SubjectArray]
    ↓ subjects
[FLUX2_StyleSelector]
    ↓ style
[FLUX2_CameraRig]
    ↓ camera
[FLUX2_PromptAssembler] → JSON Output
```

---

## 📦 Step 3: Configure Each Node

### **Node 1: FLUX2_SceneBuilder**

**Configuration:**
- **Scene Type:** Custom
- **Custom Scene:** `Miniature film set of Tokyo cityscape with balsa wood buildings and cardboard skyscrapers`
- **Time of Day:** *Leave empty* (not relevant for studio set)
- **Weather:** *Leave empty* (indoor set)

**Output Preview:**
```json
{
  "scene": "Miniature film set of Tokyo cityscape with balsa wood buildings and cardboard skyscrapers"
}
```

---

### **Node 2: FLUX2_SubjectCreator (Godzilla)**

**Configuration:**
- **Description:** `Towering Godzilla suit with rough charcoal-gray rubber scales and visible seams, stiff lumbering movement of actor inside heavy costume`
- **Horizontal Position:** Center
- **Vertical Position:** Center
- **Depth Position:** Foreground
- **Action/Pose:** `Standing imposingly amid destruction`
- **Color 1:** `#36454F` (charcoal gray)

**Output Preview:**
```json
{
  "description": "Towering Godzilla suit with rough charcoal-gray rubber scales and visible seams, stiff lumbering movement of actor inside heavy costume",
  "position": "center foreground",
  "action": "Standing imposingly amid destruction",
  "color_palette": ["#36454F"]
}
```

---

### **Node 3: FLUX2_SubjectCreator (Set Dressing)**

**Configuration:**
- **Description:** `Practical pyrotechnic explosions with orange fireballs and billowing smoke, thread power lines, tiny model trains and cars scattered among destruction`
- **Horizontal Position:** *Leave empty*
- **Vertical Position:** *Leave empty*
- **Depth Position:** Midground
- **Color 1:** `#FF8C00` (orange fire)
- **Color 2:** `#808080` (smoke gray)

**Output Preview:**
```json
{
  "description": "Practical pyrotechnic explosions with orange fireballs and billowing smoke, thread power lines, tiny model trains and cars scattered among destruction",
  "position": "midground",
  "color_palette": ["#FF8C00", "#808080"]
}
```

---

### **Node 4: FLUX2_SubjectArray**

**Configuration:**
- **Subject 1:** Connect from Godzilla SubjectCreator
- **Subject 2:** Connect from Set Dressing SubjectCreator
- **Subject 3-8:** *Leave disconnected*

**Output Preview:**
```json
{
  "subjects": [
    {
      "description": "Towering Godzilla suit...",
      "position": "center foreground",
      "action": "Standing imposingly amid destruction",
      "color_palette": ["#36454F"]
    },
    {
      "description": "Practical pyrotechnic explosions...",
      "position": "midground",
      "color_palette": ["#FF8C00", "#808080"]
    }
  ]
}
```

---

### **Node 5: FLUX2_StyleSelector**

**Configuration:**
- **Style Category:** Film Photography
- **Style Preset:** Vintage Film
- **Quality Level:** Artistic
- **Custom Modifiers:** `1960s tokusatsu kaiju film, oversaturated Eastmancolor film stock, warm faded palette, visible film grain, practical effects aesthetic`

**Output Preview:**
```json
{
  "style": "Vintage Film with 1960s tokusatsu kaiju film, oversaturated Eastmancolor film stock, warm faded palette, visible film grain, practical effects aesthetic - Artistic quality"
}
```

---

### **Node 6: FLUX2_CameraRig**

**Configuration:**
- **Camera Preset:** Custom
- **Angle:** `Dramatic low angle looking up to emphasize imposing monster stature`
- **Distance:** `Medium shot capturing full suit and set`
- **Lens (mm):** 35 *(wide angle for dramatic perspective)*
- **F-Number:** f/8 *(deep depth for miniature set)*
- **ISO:** 400 *(vintage film stock sensitivity)*
- **Depth of Field:** `Deep depth of field maintaining focus across miniature set`
- **Focus:** `Sharp focus on Godzilla suit with visible practical effects`

**Additional Settings:**
- **Lighting (in PromptAssembler):** `Harsh studio lighting casting dramatic shadows across miniature set`
- **Mood (in PromptAssembler):** `Destructive, imposing, vintage monster movie spectacle`

**Output Preview:**
```json
{
  "camera": {
    "angle": "Dramatic low angle looking up to emphasize imposing monster stature",
    "distance": "Medium shot capturing full suit and set",
    "lens-mm": 35,
    "f-number": "f/8",
    "iso": 400,
    "depth_of_field": "Deep depth of field maintaining focus across miniature set",
    "focus": "Sharp focus on Godzilla suit with visible practical effects"
  }
}
```

---

### **Node 7: FLUX2_PromptAssembler**

**Configuration:**
- **Scene:** Connect from SceneBuilder
- **Subjects:** Connect from SubjectArray
- **Style:** Connect from StyleSelector
- **Lighting:** `Harsh studio lighting casting dramatic shadows across miniature set`
- **Mood:** `Destructive, imposing, vintage monster movie spectacle`
- **Background:** `Miniature Tokyo under destruction with smoke and fire effects`
- **Composition:** `Low angle hero shot emphasizing scale and power`
- **Camera:** Connect from CameraRig
- **Remove Empty Fields:** Yes *(recommended)*
- **Pretty Print:** Yes *(for readability)*

---

## 🎨 Step 4: Final JSON Output

```json
{
  "scene": "Miniature film set of Tokyo cityscape with balsa wood buildings and cardboard skyscrapers",
  "subjects": [
    {
      "description": "Towering Godzilla suit with rough charcoal-gray rubber scales and visible seams, stiff lumbering movement of actor inside heavy costume",
      "position": "center foreground",
      "action": "Standing imposingly amid destruction",
      "color_palette": ["#36454F"]
    },
    {
      "description": "Practical pyrotechnic explosions with orange fireballs and billowing smoke, thread power lines, tiny model trains and cars scattered among destruction",
      "position": "midground",
      "color_palette": ["#FF8C00", "#808080"]
    }
  ],
  "style": "Vintage Film with 1960s tokusatsu kaiju film, oversaturated Eastmancolor film stock, warm faded palette, visible film grain, practical effects aesthetic - Artistic quality",
  "lighting": "Harsh studio lighting casting dramatic shadows across miniature set",
  "mood": "Destructive, imposing, vintage monster movie spectacle",
  "background": "Miniature Tokyo under destruction with smoke and fire effects",
  "composition": "Low angle hero shot emphasizing scale and power",
  "camera": {
    "angle": "Dramatic low angle looking up to emphasize imposing monster stature",
    "distance": "Medium shot capturing full suit and set",
    "lens-mm": 35,
    "f-number": "f/8",
    "iso": 400,
    "depth_of_field": "Deep depth of field maintaining focus across miniature set",
    "focus": "Sharp focus on Godzilla suit with visible practical effects"
  }
}
```

---

## 🎬 Visual Workflow Diagram

```
┌─────────────────────────┐
│  FLUX2_SceneBuilder     │
│  "Miniature Tokyo set"  │
└────────────┬────────────┘
             │
             │ scene
             ↓
┌─────────────────────────┐     ┌─────────────────────────┐
│  SubjectCreator #1      │     │  SubjectCreator #2      │
│  "Godzilla suit"        │     │  "Pyro effects & set"   │
└────────────┬────────────┘     └────────────┬────────────┘
             │                               │
             └───────────┬───────────────────┘
                         │ subject
                         ↓
             ┌───────────────────────┐
             │  FLUX2_SubjectArray   │
             │  Combines subjects    │
             └──────────┬────────────┘
                        │ subjects
                        ↓
┌─────────────────────────┐
│  FLUX2_StyleSelector    │
│  "Vintage Film"         │
│  + 60s tokusatsu mods   │
└────────────┬────────────┘
             │ style
             ↓
┌─────────────────────────┐
│  FLUX2_CameraRig        │
│  Low angle, 35mm, f/8   │
└────────────┬────────────┘
             │ camera
             ↓
┌─────────────────────────────────────────────────────┐
│              FLUX2_PromptAssembler                  │
│  Inputs: scene, subjects, style, camera             │
│  + lighting, mood, background, composition          │
│  Output: Complete JSON prompt                       │
└─────────────────────────────────────────────────────┘
                         │
                         ↓
                   [JSON Output]
                         │
                         ↓
                  [FLUX.2 Model]
```

---

## 💡 Key Decisions Explained

### **Why Split Into Two Subjects?**

1. **Godzilla (Subject 1)**
   - Primary focus
   - Specific colors and characteristics
   - Clear position and action

2. **Set Dressing (Subject 2)**
   - Environmental effects
   - Secondary visual elements
   - Supports the main subject

**Alternative:** Could create 3 subjects (Godzilla, City Set, Pyrotechnics) for even more control.

---

### **Why Custom Style Modifiers?**

The "Vintage Film" preset gives us the foundation, but custom modifiers add:
- Specific era (1960s)
- Specific technique (tokusatsu)
- Specific film stock (Eastmancolor)
- Specific aesthetic qualities (oversaturated, faded, grain)

---

### **Why These Camera Settings?**

- **35mm lens:** Wide enough for dramatic perspective
- **f/8:** Deep depth keeps miniatures in focus
- **ISO 400:** Matches vintage film stocks
- **Low angle:** Classic kaiju film technique
- **Manual angle description:** Captures the specific framing intent

---

## 🎯 Benefits of the Structured Approach

### **Compared to Natural Language:**

**Original Prompt Issues:**
- ❌ 256 words in one long run-on sentence
- ❌ Mixed concerns (subject, camera, style, lighting)
- ❌ Ambiguous priorities
- ❌ Hard to modify specific elements
- ❌ Difficult to reuse components

**Structured JSON Benefits:**
- ✅ Clear separation of concerns
- ✅ Explicit priorities (subjects ordered)
- ✅ Easy to modify individual elements
- ✅ Reusable components (camera preset, style)
- ✅ Precise color control (hex codes)
- ✅ Better model understanding

---

## 🔧 Variations & Experiments

### **Variation 1: Different Era**
Change StyleSelector modifiers:
```
"1950s black and white tokusatsu, high contrast dramatic lighting, silver nitrate film grain"
```

### **Variation 2: Modern Take**
Change StyleSelector to:
```
"Modern practical effects with 4K digital capture, maintaining vintage aesthetic with intentional film grain and color grading"
```

### **Variation 3: More Destruction**
Add a third subject:
```
"Collapsing buildings with detailed destruction debris, falling miniature rubble, tilting structures"
```

### **Variation 4: Different Angle**
Change CameraRig angle:
```
"Bird's eye view looking down at monster and cityscape, emphasizing scale of destruction"
```

---

## 📚 What You Learned

### **Conversion Process:**
1. ✅ Analyze natural language prompt
2. ✅ Identify distinct components (scene, subjects, style, camera)
3. ✅ Map to appropriate nodes
4. ✅ Configure each node with specific details
5. ✅ Assemble into structured JSON

### **Node Usage:**
- ✅ SceneBuilder for environment
- ✅ SubjectCreator for distinct elements
- ✅ SubjectArray to combine multiple subjects
- ✅ StyleSelector with custom modifiers for era/aesthetic
- ✅ CameraRig for technical specifications
- ✅ PromptAssembler for additional context

### **Best Practices:**
- ✅ Use hex codes for precise colors
- ✅ Split complex scenes into multiple subjects
- ✅ Add custom modifiers to presets
- ✅ Be specific with camera angles
- ✅ Include era-specific technical details

---

## 🚀 Try It Yourself

### **Exercise 1: Simpler Version**
Build a basic Godzilla prompt with:
- Just the Godzilla subject
- Scene preset: "Interior"
- Style preset: "Film Photography - Vintage Film"
- Camera preset: "Wide Angle"

### **Exercise 2: Add Your Twist**
Modify the example to create:
- Godzilla vs. Mothra scene
- Underwater kaiju battle
- Space monster on alien planet
- Modern city destruction (CGI aesthetic)

### **Exercise 3: Different Genre**
Apply the same structured approach to:
- Ray Harryhausen stop-motion scene
- 1950s B-movie sci-fi
- Ultraman-style tokusatsu
- Pacific Rim style mech battle

---

## 📖 Related Documentation

### **Learn More:**
- [Introduction to Structured Prompting](../02_Learning_Materials/01-introduction-to-structured-prompting.md) - Why JSON?
- [JSON Schema Anatomy](../02_Learning_Materials/02-json-schema-anatomy.md) - Field reference
- [Workflow Patterns](./WORKFLOW-PATTERNS.md) - More examples

### **Node Reference:**
- [Package README](../../ComfyUI_Package/ComfyUI_FLUX2_Prompt_Builder/README.md) - Complete API

### **Installation:**
- [Getting Started](../01_Getting_Started/README.md) - Setup guide

---

## 🎉 Result

By converting the natural language prompt to structured JSON, you've gained:

✅ **Better Control** - Modify any element independently  
✅ **Reusability** - Save camera/style presets for future use  
✅ **Clarity** - Clear hierarchy of elements  
✅ **Precision** - Exact colors and technical specs  
✅ **Flexibility** - Easy to experiment with variations  

**Happy prompting!** 🦖✨

---

**Example Type:** Text-to-Image Complex Scene  
**Difficulty:** Intermediate  
**Techniques Used:** Multi-subject composition, custom style modifiers, precise camera control, color specification  
**Estimated Build Time:** 10-15 minutes  

*Last updated: November 27, 2024*
