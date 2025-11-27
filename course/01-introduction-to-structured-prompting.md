# Lesson 1: Introduction to Structured Prompting

**Module 1: Foundations** | Lesson 1 of 22

---

## TL;DR

FLUX.2 introduces JSON structured prompting—a way to control image generation with the precision of code. Instead of hoping the AI interprets your natural language correctly, you specify exactly what goes where, in what color, with what lighting. This lesson covers why structured prompting matters and when to use it.

---

## The Problem with Traditional Prompting

Let's start with a real-world scenario. You're a product designer creating marketing materials for a new coffee mug line. You need:

- Two mugs (one black #000000, one yellow #FFD700)
- Specific positioning (black on left, yellow on right)
- Steam rising from the black mug only
- Professional studio lighting setup
- Consistent output for client revisions

### Traditional Natural Language Approach

```
"Two coffee mugs on a concrete surface, one black and one yellow, 
with steam rising from the black one, professional studio lighting"
```

**Problems you'll encounter:**

1. **Color Inconsistency:** "Black" might render as charcoal, dark gray, or true black across different generations
2. **Positioning Ambiguity:** Which mug is on the left? AI decides randomly
3. **Element Uncertainty:** Steam might appear on both mugs, neither, or somewhere else entirely
4. **Revision Chaos:** Change one detail, everything else shifts unpredictably

**Result:** You'll generate 20+ images hoping one matches your needs.

---

## The Structured Prompting Solution

Now let's solve this with JSON structured prompting:

```json
{
  "scene": "Professional studio product photography with polished concrete surface",
  "subjects": [
    {
      "description": "Minimalist ceramic coffee mug with steam rising",
      "position": "Left side on concrete surface",
      "color_palette": ["#000000"]
    },
    {
      "description": "Minimalist ceramic coffee mug, matching design",
      "position": "Right side on concrete surface",
      "color_palette": ["#FFD700"]
    }
  ],
  "style": "Ultra-realistic product photography",
  "lighting": "Three-point softbox setup with soft highlights",
  "camera": {
    "angle": "45-degree angle",
    "lens-mm": 85,
    "f-number": "f/5.6"
  }
}
```

**What you gain:**

✅ **Exact colors** via hex codes  
✅ **Precise positioning** per subject  
✅ **Isolated control** - change one element without affecting others  
✅ **Reproducibility** - same structure = consistent results  
✅ **Documentation** - JSON serves as a specification

---

## Understanding the Paradigm Shift

### Traditional Prompting: The "Request" Model

You're making a request to an AI system:

> "Please create an image with these characteristics..."

The AI interprets your natural language, fills in gaps with assumptions, and produces its best guess. You're **describing an outcome** and hoping.

### Structured Prompting: The "Specification" Model

You're providing a technical specification:

> "This image shall contain exactly these elements, positioned precisely here, colored exactly this..."

The AI follows your blueprint. You're **defining a system** with precision.

**Think of it like this:**

| Traditional | Structured |
|-------------|-----------|
| Asking a friend to paint | Providing architectural blueprints |
| "Make it blue-ish" | `"color": "#0066CC"` |
| "Put the car somewhere on the right" | `"position": "right foreground"` |
| Hope it looks professional | `"style": "commercial product photography"` |

---

## When to Use Structured Prompting

### ✅ Use JSON Structured Prompts When:

1. **Precision Matters**
   - Brand work requiring exact colors
   - Product photography needing consistent layouts
   - Client work with specific requirements

2. **Multiple Elements Need Control**
   - Scenes with 3+ distinct subjects
   - Each element needs different styling
   - Precise positioning is critical

3. **Reproducibility Is Required**
   - Creating image series with consistency
   - A/B testing variations
   - Production pipelines and automation

4. **Documentation Is Valuable**
   - Collaborative workflows
   - Version control of prompts
   - Handoff to other team members

### ⚠️ Natural Language Still Works When:

1. **Exploration Phase**
   - Initial concept development
   - Creative experimentation
   - When you're not sure what you want yet

2. **Simple, Single-Subject Scenes**
   - Portrait with standard composition
   - Single object product shots
   - Landscapes and environments

3. **Artistic Freedom Is Desired**
   - Abstract art
   - Creative interpretations welcome
   - "Surprise me" scenarios

---

## The Anatomy of Control

Structured prompting gives you discrete control over distinct aspects:

```json
{
  "scene": "← Overall context and setting",
  "subjects": "← Individual elements with per-subject control",
  "style": "← Artistic direction and rendering approach",
  "color_palette": "← Global color scheme",
  "lighting": "← Illumination setup",
  "mood": "← Emotional tone",
  "background": "← Environmental details",
  "composition": "← Layout and framing rules",
  "camera": "← Photography simulation parameters"
}
```

**Each field is optional.** Start simple, add complexity as needed.

---

## Practical Example: Evolution of a Prompt

Let's watch a prompt evolve from simple to sophisticated:

### Stage 1: Minimal Natural Language
```
"A robot in a workshop"
```
*Result: Unpredictable style, colors, positioning, and mood*

### Stage 2: Detailed Natural Language
```
"A friendly blue robot with glowing eyes standing in a cluttered workshop 
with tools on the walls, warm lighting, cinematic style"
```
*Result: Better, but "blue" is ambiguous, positioning varies, tools placement random*

### Stage 3: Basic Structured Prompt
```json
{
  "scene": "Cluttered workshop interior",
  "subjects": [{
    "description": "Friendly robot with glowing eyes",
    "color_palette": ["#4169E1"]
  }],
  "style": "Cinematic rendering",
  "lighting": "Warm overhead lighting"
}
```
*Result: Consistent blue, but we can do better*

### Stage 4: Comprehensive Structured Prompt
```json
{
  "scene": "Industrial workshop with vintage tools and workbenches",
  "subjects": [{
    "description": "Humanoid robot with expressive glowing eyes and weathered metal surface",
    "position": "Center foreground, standing at workbench",
    "color_palette": ["#4169E1", "#C0C0C0"],
    "action": "Examining a small mechanical part"
  }],
  "style": "Cinematic CGI with photorealistic materials",
  "color_palette": ["#4169E1", "#8B4513", "#C0C0C0", "#FFD700"],
  "lighting": "Warm Edison bulb overhead, blue accent light from window",
  "mood": "Nostalgic, industrious, slightly whimsical",
  "background": "Walls covered with hanging vintage tools, blueprints, oil-stained workbench",
  "composition": "Rule of thirds, robot slightly off-center left",
  "camera": {
    "angle": "Eye level, slight low angle",
    "lens-mm": 50,
    "f-number": "f/2.8",
    "depth_of_field": "Shallow, background slightly soft"
  }
}
```
*Result: Exactly what you envisioned, reproducible, modifiable*

---

## The Learning Curve

Don't worry if structured prompting feels complex at first. Here's the progression:

**Week 1:** Copy examples, modify one field at a time  
**Week 2:** Understand which fields affect what  
**Week 3:** Build prompts from scratch for simple scenes  
**Week 4:** Master complex multi-subject compositions  
**Week 5:** Develop your own templates and patterns

---

## Key Principles to Remember

### 1. Start Simple, Add Complexity
Begin with 3-4 fields. Add more as you need finer control.

### 2. Each Field Is Independent
Changing `lighting` doesn't affect `subjects[0].color_palette`. This isolation is powerful.

### 3. Natural Language Still Lives Inside
Notice the fields still contain natural language descriptions. JSON provides structure, English provides nuance.

### 4. Templates Are Your Friend
Build a library of JSON templates for common scenarios (product shots, portraits, landscapes).

### 5. Version Control Your Prompts
JSON files work beautifully with Git. Track changes, revert experiments, collaborate easily.

---

## Common Misconceptions

### ❌ "I need to use JSON for everything now"
**Reality:** Use the right tool for the job. Exploring? Natural language. Producing? Structure.

### ❌ "JSON prompting is only for technical people"
**Reality:** If you can fill out a form, you can use JSON prompts. The syntax becomes natural quickly.

### ❌ "More fields = better results"
**Reality:** Use only what you need. Over-specification can be as problematic as under-specification.

### ❌ "I have to memorize all the fields"
**Reality:** Keep a reference template. Copy, modify, iterate.

---

## Practice Exercise

Let's solidify your understanding. Take this natural language prompt:

```
"A vintage red bicycle leaning against a yellow wall with morning sunlight, 
film photography style, shallow depth of field"
```

### Your Task:
Convert this to a basic JSON structure. Include:
- `scene`
- `subjects` (at least the bicycle)
- `style`
- `lighting`
- `camera` (at least lens and f-number)

### Starter Template:
```json
{
  "scene": "",
  "subjects": [
    {
      "description": "",
      "position": "",
      "color_palette": []
    }
  ],
  "style": "",
  "lighting": "",
  "camera": {
    "lens-mm": ,
    "f-number": ""
  }
}
```

**Hints:**
- "Vintage red" → hex code like #DC143C
- "Yellow wall" → hex code like #FFD700
- "Film photography" → style field
- "Shallow depth of field" → f-number like f/1.8

### Sample Solution:
```json
{
  "scene": "Urban exterior with textured stucco wall",
  "subjects": [
    {
      "description": "Vintage road bicycle with classic frame design",
      "position": "Leaning against wall, left side of frame",
      "color_palette": ["#DC143C"]
    }
  ],
  "style": "Analog film photography, natural grain",
  "color_palette": ["#DC143C", "#FFD700"],
  "lighting": "Soft morning sunlight from left, creating gentle shadows",
  "background": "Yellow stucco wall with subtle texture",
  "camera": {
    "lens-mm": 50,
    "f-number": "f/1.8",
    "depth_of_field": "Shallow, wall softly blurred"
  }
}
```

---

## What's Next

In **Lesson 2: The JSON Schema Anatomy**, we'll dissect every field in the JSON structure, understanding exactly what each one controls and how they interact.

You'll learn:
- The complete field reference
- Required vs. optional fields
- How fields cascade and override
- Building your first template library

---

## Quick Reference

**When to use structured prompting:**
- Precision color requirements
- Multi-element scenes
- Production workflows
- Client/commercial work

**When natural language is fine:**
- Creative exploration
- Simple single-subject scenes
- Rapid prototyping
- Artistic freedom desired

**Core benefit:**
JSON gives you **reproducible, precise, modifiable** control over every aspect of generation.

---

**[← Back to Course Overview](00-course-overview.md)** | **[Next: Lesson 2 - JSON Schema Anatomy →](02-json-schema-anatomy.md)**
