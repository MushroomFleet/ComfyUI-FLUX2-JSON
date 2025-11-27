# Lesson 2: The JSON Schema Anatomy

**Module 1: Foundations** | Lesson 2 of 22

---

## TL;DR

The FLUX.2 JSON schema consists of 9 core fields that control different aspects of generation. This lesson provides a complete reference for every field, their data types, when to use them, and how they interact. Think of this as your technical specification guide.

---

## The Complete Schema

Here's the full JSON structure with all available fields:

```json
{
  "scene": "string",
  "subjects": [
    {
      "description": "string",
      "position": "string",
      "action": "string",
      "pose": "string",
      "color_palette": ["array", "of", "strings"]
    }
  ],
  "style": "string",
  "color_palette": ["array", "of", "strings"],
  "lighting": "string",
  "mood": "string",
  "background": "string",
  "composition": "string",
  "camera": {
    "angle": "string",
    "distance": "string",
    "lens": "string",
    "lens-mm": number,
    "f-number": "string",
    "ISO": number,
    "depth_of_field": "string",
    "focus": "string"
  }
}
```

**Important:** All fields are optional. Use only what you need.

---

## Field-by-Field Breakdown

### 1. `scene` (string)

**Purpose:** Sets the overall context and environment for your image.

**What it controls:**
- General setting (indoor/outdoor, location type)
- Environmental context
- Spatial parameters
- Foundational atmosphere

**Best practices:**
- Be specific but not overly detailed
- Focus on the "where" and "what kind of space"
- Save specific details for `background` field

**Examples:**

```json
// ✅ Good
"scene": "Professional photography studio with seamless white backdrop"
"scene": "Bustling Tokyo street market at dusk"
"scene": "Minimalist Scandinavian living room with hardwood floors"

// ❌ Too vague
"scene": "A nice place"
"scene": "Indoors"

// ⚠️ Too detailed (save for other fields)
"scene": "Studio with specific Canon lighting equipment positioned at 45-degree angles with softboxes and a person standing..."
```

**When to use:**
- Always use for establishing context
- Essential for multi-element scenes
- Skip only for abstract/minimal compositions

---

### 2. `subjects` (array of objects)

**Purpose:** Define individual elements in your scene with granular control.

**Structure:** Array of subject objects, each with:

#### 2a. `subjects[].description` (string) - REQUIRED

**What it controls:**
- What the subject IS
- Physical characteristics
- Material properties
- Details and features

```json
"description": "Minimalist ceramic coffee mug with smooth matte finish"
"description": "Vintage leather-bound journal with brass corner protectors"
"description": "Sleek humanoid robot with articulated joints and LED indicators"
```

#### 2b. `subjects[].position` (string) - RECOMMENDED

**What it controls:**
- Where in the frame
- Spatial relationships to other subjects
- Foreground/midground/background placement

```json
"position": "Center foreground, slightly left of frame"
"position": "Right side on concrete surface"
"position": "Background, upper third of composition"
"position": "Floating in midground, centered"
```

**Positioning vocabulary:**
- **Horizontal:** left, center, right, far left, far right
- **Vertical:** top, middle, bottom, upper third, lower third
- **Depth:** foreground, midground, background
- **Relative:** "to the left of subject 1", "behind the main subject"

#### 2c. `subjects[].action` (string) - OPTIONAL

**What it controls:**
- Dynamic elements
- Movement or activity
- Interaction with environment or other subjects

```json
"action": "Pouring coffee into a cup"
"action": "Walking toward the camera"
"action": "Examining a mechanical part"
"action": "Steam rising from the surface"
```

**Note:** Use `action` for dynamic elements, `pose` for static positioning.

#### 2d. `subjects[].pose` (string) - OPTIONAL

**What it controls:**
- Static positioning of the subject
- Body language (for characters)
- Orientation and stance

```json
"pose": "Sitting cross-legged on the floor"
"pose": "Standing upright, arms at sides"
"pose": "Leaning against the wall"
"pose": "Stationary on surface"
```

#### 2e. `subjects[].color_palette` (array) - RECOMMENDED

**What it controls:**
- Colors specific to THIS subject
- Overrides global `color_palette` for this element
- Supports hex codes and color names

```json
"color_palette": ["#FF5733", "#C70039"]
"color_palette": ["matte black ceramic", "brushed steel accents"]
"color_palette": ["#4A90E2", "white", "#2C3E50"]
```

**Subject best practices:**
- One subject object per distinct element
- Order matters: first subject is typically primary/foreground
- Be consistent with subject descriptions across iterations

---

### 3. `style` (string)

**Purpose:** Control the artistic rendering approach and overall aesthetic.

**What it controls:**
- Rendering technique
- Artistic movement or genre
- Quality level and finish
- Visual treatment

**Categories and examples:**

```json
// Photorealism
"style": "Ultra-realistic product photography with commercial quality"
"style": "Photorealistic CGI rendering with ray-traced lighting"
"style": "Analog film photography, shot on Kodak Portra 400"

// Digital art
"style": "Digital illustration with clean vector aesthetics"
"style": "3D rendered with Blender Cycles, photorealistic materials"

// Artistic movements
"style": "Impressionist painting with visible brushstrokes"
"style": "Art Nouveau poster design with flowing organic lines"

// Photography styles
"style": "Editorial fashion photography, high contrast"
"style": "Documentary street photography, candid and natural"
"style": "Studio product photography with clean lighting"

// Vintage/retro
"style": "1980s vintage photograph with film grain"
"style": "Early 2000s digital camera aesthetic"
```

**Combining style elements:**
```json
"style": "Cinematic CGI rendering with photorealistic materials and atmospheric depth"
```

---

### 4. `color_palette` (array) - Global

**Purpose:** Define the overall color scheme for the entire image.

**What it controls:**
- Global color harmony
- Brand color enforcement
- Mood through color
- Accent colors

**Syntax options:**

```json
// Hex codes (most precise)
"color_palette": ["#FF5733", "#C70039", "#900C3F", "#581845"]

// Color names (less precise but intuitive)
"color_palette": ["deep blue", "golden yellow", "charcoal gray"]

// Mixed approach
"color_palette": ["#4A90E2", "warm white", "#2C3E50", "soft gold"]

// With descriptive modifiers
"color_palette": ["matte black", "brushed gold #FFD700", "concrete gray"]
```

**Color palette strategies:**

```json
// Monochromatic
"color_palette": ["#1A1A1A", "#4A4A4A", "#7A7A7A", "#AAAAAA"]

// Complementary
"color_palette": ["#0066CC", "#FF6600"]

// Analogous
"color_palette": ["#FF5733", "#FF8D33", "#FFC133"]

// Triadic
"color_palette": ["#FF0000", "#00FF00", "#0000FF"]

// Brand-specific
"color_palette": ["#1DA1F2", "#14171A", "#657786"] // Twitter brand colors
```

**Interaction with subjects:**
- Global palette sets overall scheme
- Subject-specific `color_palette` overrides for that element
- Both can coexist harmoniously

---

### 5. `lighting` (string)

**Purpose:** Define how the scene is illuminated.

**What it controls:**
- Light source types and positions
- Shadow characteristics
- Lighting mood and intensity
- Technical photography lighting

**Lighting vocabulary:**

```json
// Natural lighting
"lighting": "Soft morning sunlight from window on left"
"lighting": "Golden hour backlight creating rim lighting"
"lighting": "Overcast daylight, even and diffused"
"lighting": "Dappled sunlight through tree canopy"

// Studio lighting
"lighting": "Three-point softbox setup creating soft highlights"
"lighting": "Key light from upper right, fill light from left, rim light behind"
"lighting": "Single dramatic spotlight from above, deep shadows"

// Ambient/environmental
"lighting": "Warm Edison bulb overhead, blue accent from window"
"lighting": "Neon signs casting colorful reflections"
"lighting": "Soft ambient room lighting, no harsh shadows"

// Technical specifications
"lighting": "5600K daylight balanced, diffused through silk, 1/125 shutter"
```

**Lighting characteristics to specify:**
- **Direction:** overhead, side, backlit, front-lit
- **Quality:** hard, soft, diffused, harsh
- **Color temperature:** warm, cool, neutral, specific Kelvin
- **Intensity:** bright, subtle, dramatic, even
- **Shadows:** deep, soft, minimal, harsh

---

### 6. `mood` (string)

**Purpose:** Set the emotional tone and atmosphere.

**What it controls:**
- Emotional resonance
- Atmospheric quality
- Psychological impact
- Tonal character

**Mood examples:**

```json
// Positive moods
"mood": "Energetic and vibrant"
"mood": "Calm and peaceful"
"mood": "Joyful and playful"
"mood": "Inspiring and uplifting"

// Neutral/professional moods
"mood": "Clean, professional, minimalist"
"mood": "Clinical and precise"
"mood": "Sophisticated and elegant"

// Dramatic moods
"mood": "Mysterious and intriguing"
"mood": "Tense and suspenseful"
"mood": "Melancholic and nostalgic"

// Complex compound moods
"mood": "Nostalgic yet hopeful, with subtle whimsy"
"mood": "Serene but slightly eerie, dreamlike quality"
```

**Mood vs. Style vs. Lighting:**
- **Style** = HOW it's rendered (photorealistic, painted, etc.)
- **Lighting** = WHERE light comes from and its properties
- **Mood** = WHAT it FEELS like emotionally

---

### 7. `background` (string)

**Purpose:** Describe environmental details behind or around subjects.

**What it controls:**
- Environmental context beyond main subjects
- Setting details and props
- Atmospheric elements
- Depth and layering

**Background strategies:**

```json
// Minimal/clean
"background": "Seamless white studio backdrop"
"background": "Soft gradient from light gray to white"

// Detailed environmental
"background": "Weathered brick wall with vintage posters and graffiti"
"background": "Floor-to-ceiling bookshelves filled with leather-bound volumes"
"background": "Dense jungle foliage with filtered sunlight"

// Blurred/atmospheric
"background": "Softly blurred city lights at night, bokeh effect"
"background": "Out-of-focus forest trees creating green haze"

// Architectural
"background": "Industrial warehouse with exposed beams and concrete"
"background": "Modern minimalist interior with large windows"
```

**Background detail levels:**

```json
// Low detail (emphasizes subjects)
"background": "Neutral gray backdrop, minimal distraction"

// Medium detail (contextual)
"background": "Coffee shop interior with wooden tables and hanging plants"

// High detail (story-rich)
"background": "Cluttered workshop with vintage tools hanging on pegboard, oil-stained workbench covered in blueprints and mechanical parts, morning light through dusty windows"
```

---

### 8. `composition` (string)

**Purpose:** Control framing, layout, and visual organization.

**What it controls:**
- Framing rules and guidelines
- Visual balance
- Leading lines and flow
- Cropping and aspect

**Composition techniques:**

```json
// Classic rules
"composition": "Rule of thirds, subject on right vertical line"
"composition": "Centered symmetrical composition"
"composition": "Golden ratio spiral leading to focal point"

// Dynamic compositions
"composition": "Diagonal leading lines from lower left to upper right"
"composition": "Triangular composition with three main elements"
"composition": "Layered depth with clear foreground, midground, background"

// Framing devices
"composition": "Natural framing through doorway or window"
"composition": "Negative space emphasizing subject isolation"
"composition": "Tight crop on subject, minimal surrounding space"

// Advanced techniques
"composition": "Dutch angle (tilted) for dynamic energy"
"composition": "Worm's eye view looking upward"
"composition": "Bird's eye view, flat lay arrangement"
```

---

### 9. `camera` (object)

**Purpose:** Simulate photography equipment and parameters for photorealistic control.

**Sub-fields:**

#### 9a. `camera.angle` (string)

```json
"angle": "Eye level, straight on"
"angle": "High angle looking down"
"angle": "Low angle looking up"
"angle": "45-degree angle from upper right"
"angle": "Bird's eye view, directly overhead"
"angle": "Worm's eye view from ground level"
```

#### 9b. `camera.distance` (string)

```json
"distance": "Extreme close-up (macro)"
"distance": "Close-up"
"distance": "Medium shot"
"distance": "Full shot"
"distance": "Wide shot"
"distance": "Extreme wide shot"
```

#### 9c. `camera.lens` / `camera.lens-mm` (string / number)

```json
// By description
"lens": "Wide angle lens creating slight distortion"
"lens": "Standard prime lens, natural perspective"
"lens": "Telephoto lens with compression effect"
"lens": "Macro lens for extreme close-up detail"

// By focal length (more precise)
"lens-mm": 16    // Ultra-wide
"lens-mm": 24    // Wide angle
"lens-mm": 35    // Wide-normal
"lens-mm": 50    // Standard/"normal"
"lens-mm": 85    // Portrait
"lens-mm": 135   // Telephoto
"lens-mm": 200   // Long telephoto
```

**Focal length effects:**
- **16-24mm:** Wide field of view, slight distortion, deep depth
- **35-50mm:** Natural perspective, versatile
- **85-135mm:** Portrait flattering, background compression
- **200mm+:** Extreme compression, shallow depth

#### 9d. `camera.f-number` (string)

Controls aperture and depth of field:

```json
"f-number": "f/1.4"    // Very shallow DOF, extreme blur
"f-number": "f/1.8"    // Shallow DOF, portrait-like
"f-number": "f/2.8"    // Moderate shallow DOF
"f-number": "f/5.6"    // Balanced DOF
"f-number": "f/8"      // Deep DOF, most in focus
"f-number": "f/11"     // Very deep DOF
"f-number": "f/16"     // Maximum depth
```

#### 9e. `camera.ISO` (number)

Controls light sensitivity and grain:

```json
"ISO": 100    // Minimal grain, bright conditions
"ISO": 200    // Clean, versatile
"ISO": 400    // Slight grain, indoor natural light
"ISO": 800    // Visible grain, low light
"ISO": 1600   // Pronounced grain, very low light
"ISO": 3200+  // Heavy grain, artistic or necessary
```

#### 9f. `camera.depth_of_field` (string)

```json
"depth_of_field": "Shallow, background heavily blurred"
"depth_of_field": "Moderate, subject sharp, background softened"
"depth_of_field": "Deep, everything in sharp focus"
"depth_of_field": "Bokeh effect with circular highlights"
```

#### 9g. `camera.focus` (string)

```json
"focus": "Sharp focus on subject's eyes"
"focus": "Focus on foreground product, background soft"
"focus": "Entire scene in sharp focus"
"focus": "Selective focus on left subject only"
```

**Camera object best practices:**
- Combine multiple parameters for photorealism
- `lens-mm` + `f-number` = natural photography feel
- Higher specificity = more predictable results

**Complete camera example:**

```json
"camera": {
  "angle": "Slight low angle, eye level with subject",
  "distance": "Medium shot",
  "lens-mm": 85,
  "f-number": "f/2.8",
  "ISO": 200,
  "depth_of_field": "Shallow, background gently blurred",
  "focus": "Sharp focus on subject in foreground"
}
```

---

## Field Interactions and Hierarchies

### Specificity Hierarchy

When fields overlap, more specific overrides more general:

```json
{
  "color_palette": ["#FF0000", "#0000FF"],  // ← Global: applies to everything
  "subjects": [
    {
      "description": "Coffee mug",
      "color_palette": ["#000000"]  // ← Overrides global for this subject
    }
  ]
}
```

**Result:** Mug is black, rest of scene uses red/blue palette.

### Complementary Fields

Some fields naturally work together:

```json
{
  "mood": "Energetic and vibrant",      // ← Sets emotional tone
  "lighting": "Bright overhead light",   // ← Supports that mood
  "color_palette": ["#FF5733", "#FFC300"]  // ← Reinforces with warm colors
}
```

### Conflicting Instructions

Avoid contradictory specifications:

```json
// ❌ Conflict
{
  "lighting": "Dark, moody shadows",
  "mood": "Bright and cheerful"
}

// ✅ Aligned
{
  "lighting": "Soft, warm glow",
  "mood": "Cozy and inviting"
}
```

---

## Required vs. Optional Fields

### Truly Required
**None.** Every field is optional.

### Highly Recommended
For coherent results, include at least:
- `scene` OR `subjects[].description`
- One of: `style`, `mood`, or `lighting`

### Minimal viable prompts:

```json
// Absolutely minimal
{
  "subjects": [{"description": "Red apple"}]
}

// Practical minimum
{
  "scene": "Kitchen counter",
  "subjects": [{"description": "Red apple"}],
  "style": "Product photography"
}
```

---

## Building Your Field Strategy

### Start Simple, Expand Deliberately

**Phase 1:** Core identification
```json
{
  "scene": "...",
  "subjects": [{"description": "..."}],
  "style": "..."
}
```

**Phase 2:** Add control
```json
{
  "scene": "...",
  "subjects": [{
    "description": "...",
    "position": "...",
    "color_palette": ["..."]
  }],
  "style": "...",
  "lighting": "..."
}
```

**Phase 3:** Refinement
```json
{
  "scene": "...",
  "subjects": [{
    "description": "...",
    "position": "...",
    "action": "...",
    "color_palette": ["..."]
  }],
  "style": "...",
  "color_palette": ["..."],
  "lighting": "...",
  "mood": "...",
  "camera": {
    "lens-mm": ...,
    "f-number": "..."
  }
}
```

---

## Common Patterns and Templates

### Pattern 1: Product Photography

```json
{
  "scene": "Professional studio setup",
  "subjects": [{
    "description": "[product details]",
    "position": "Center, slight angle",
    "color_palette": ["[brand colors]"]
  }],
  "style": "Commercial product photography",
  "lighting": "Three-point softbox with soft shadows",
  "background": "Seamless backdrop",
  "camera": {
    "lens-mm": 85,
    "f-number": "f/5.6"
  }
}
```

### Pattern 2: Portrait

```json
{
  "scene": "[environment context]",
  "subjects": [{
    "description": "[person details]",
    "position": "[rule of thirds placement]",
    "pose": "[body language]"
  }],
  "style": "Editorial portrait photography",
  "lighting": "[lighting setup]",
  "mood": "[emotional tone]",
  "background": "[out of focus details]",
  "camera": {
    "angle": "Eye level",
    "lens-mm": 85,
    "f-number": "f/2.0",
    "depth_of_field": "Shallow bokeh"
  }
}
```

### Pattern 3: Landscape/Scene

```json
{
  "scene": "[detailed location]",
  "style": "[artistic approach]",
  "color_palette": ["[atmospheric colors]"],
  "lighting": "[time of day, quality]",
  "mood": "[emotional atmosphere]",
  "composition": "[layout rule]",
  "camera": {
    "angle": "[perspective]",
    "lens-mm": 24,
    "f-number": "f/11",
    "depth_of_field": "Deep, everything sharp"
  }
}
```

---

## Practice Exercise

### Challenge: Build a Complete Prompt

Create a JSON prompt for: **A tech product advertisement showing a smartwatch on a minimalist desk setup with laptop and coffee.**

**Requirements:**
- Smartwatch should be black (#000000)
- Laptop in background, silver (#C0C0C0)
- Coffee mug, white ceramic
- Clean, modern, professional mood
- Overhead natural lighting
- Shallow depth of field focusing on watch

### Starter Template:

```json
{
  "scene": "",
  "subjects": [
    {"description": "", "position": "", "color_palette": []},
    {"description": "", "position": "", "color_palette": []},
    {"description": "", "position": "", "color_palette": []}
  ],
  "style": "",
  "lighting": "",
  "mood": "",
  "background": "",
  "camera": {
    "angle": "",
    "lens-mm": ,
    "f-number": ""
  }
}
```

### Sample Solution:

```json
{
  "scene": "Minimalist desk workspace with clean lines",
  "subjects": [
    {
      "description": "Modern smartwatch with digital display",
      "position": "Center foreground on desk surface",
      "color_palette": ["#000000"]
    },
    {
      "description": "Sleek laptop, partially visible",
      "position": "Background right side",
      "color_palette": ["#C0C0C0"]
    },
    {
      "description": "White ceramic coffee mug with coffee",
      "position": "Left midground",
      "color_palette": ["white ceramic"]
    }
  ],
  "style": "Commercial tech product photography",
  "color_palette": ["#000000", "#C0C0C0", "white", "warm wood tones"],
  "lighting": "Soft natural light from above, diffused through window",
  "mood": "Clean, modern, professional, focused",
  "background": "Minimalist wooden desk surface, soft neutral backdrop",
  "composition": "Rule of thirds, watch on right vertical line",
  "camera": {
    "angle": "Slight overhead angle, 30 degrees",
    "lens-mm": 85,
    "f-number": "f/2.8",
    "depth_of_field": "Shallow, watch sharp, laptop and mug soft",
    "focus": "Sharp on smartwatch face and band"
  }
}
```

---

## Quick Reference Card

**Essential Fields for Production Work:**

| Field | Purpose | When to Use |
|-------|---------|-------------|
| `scene` | Context | Always for multi-element scenes |
| `subjects[]` | Element control | When precision matters |
| `subjects[].color_palette` | Exact colors | Brand work, specific colors |
| `style` | Rendering | Define aesthetic direction |
| `lighting` | Illumination | Photorealism, mood control |
| `camera.lens-mm` | Perspective | Natural photography feel |
| `camera.f-number` | Depth of field | Subject isolation |

**Remember:** Start with 3-4 fields, expand as needed.

---

## What's Next

In **Lesson 3: From Natural Language to JSON**, we'll practice converting traditional prompts into structured JSON, developing your "translation" skills.

You'll learn:
- Step-by-step conversion methodology
- Identifying which natural language elements map to which fields
- Common pitfalls and how to avoid them
- Building conversion templates for efficiency

---

**[← Previous: Lesson 1](01-introduction-to-structured-prompting.md)** | **[Next: Lesson 3 - Natural Language to JSON →](03-natural-language-to-json.md)**
