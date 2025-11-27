# Agent System Prompts Guide

**Two specialized agents for converting natural language to FLUX.2 JSON prompts**

---

## 📋 Overview

We've created two expert agent system prompts that convert natural language prompts into structured FLUX.2 JSON. Each serves a different use case:

1. **JSON-Plan-Expert** - Creates educational workflow plans (like the Godzilla example)
2. **JSON-Direct-Expert** - Produces immediate JSON output (quick conversion)

---

## 🎯 JSON-Plan-Expert

**File:** [JSON-Plan-Expert.md](JSON-Plan-Expert.md)

### Purpose
Creates comprehensive markdown documentation showing how to build prompts using ComfyUI's FLUX.2 Prompt Builder nodes. Output is educational and workflow-focused.

### Use Cases
- ✅ Teaching users how to use the ComfyUI nodes
- ✅ Creating detailed workflow documentation
- ✅ Building reusable prompt examples
- ✅ Explaining the "why" behind decisions
- ✅ Providing variations and experiments
- ✅ Educational content creation

### Output Format
Complete markdown document with:
- Original prompt analysis
- Step-by-step node configuration
- ASCII workflow diagrams
- Final JSON output
- Decision explanations
- Variations to try
- Learning exercises

### Example Output Structure
```markdown
# [Title] - Converting Natural Language to Structured JSON

## 📝 Original Prompt
[Original text]

## 🎯 Step 1: Analyze Components
[Breakdown]

## 🛠️ Step 2: Build with ComfyUI Nodes
[Workflow diagram]

## 📦 Step 3: Configure Each Node
[Detailed settings]

## 🎨 Step 4: Final JSON Output
[Complete JSON]

## 💡 Key Decisions Explained
[Why certain choices]

## 🔧 Variations
[Alternative approaches]
```

### When to Use
- Creating tutorials or guides
- Documenting complex workflows
- Teaching prompt engineering
- Building example libraries
- Explaining the ComfyUI interface

### Example Prompt to Agent
```
Convert this prompt to a ComfyUI workflow plan:
"A steaming cup of coffee on a rustic wooden table with morning sunlight"
```

**Agent produces:** 4000+ word markdown guide with node-by-node instructions

---

## ⚡ JSON-Direct-Expert

**File:** [JSON-Direct-Expert.md](JSON-Direct-Expert.md)

### Purpose
Converts natural language directly to clean, valid FLUX.2 JSON. Output is ready to use immediately without ComfyUI.

### Use Cases
- ✅ Quick prompt conversion
- ✅ API/script integration
- ✅ Batch processing
- ✅ Direct FLUX.2 usage
- ✅ Non-ComfyUI workflows
- ✅ Rapid prototyping

### Output Format
Concise response with:
- Brief interpretation (2-3 sentences)
- Valid JSON output
- Optional technical notes

### Example Output Structure
```
[Brief analysis]

{
  "scene": "...",
  "subjects": [...],
  "camera": {...}
}

Technical notes: [Key decisions]
```

### When to Use
- Need immediate JSON output
- Bypassing ComfyUI interface
- Integrating into scripts/tools
- Quick experimentation
- Production pipelines

### Example Prompt to Agent
```
Convert to JSON:
"A steaming cup of coffee on a rustic wooden table with morning sunlight"
```

**Agent produces:** ~30 lines of clean JSON ready to use

---

## 🔄 Comparison

| Aspect | JSON-Plan-Expert | JSON-Direct-Expert |
|--------|------------------|-------------------|
| **Output Type** | Markdown documentation | Pure JSON |
| **Length** | 2000-5000+ words | 50-200 words |
| **Purpose** | Educational | Functional |
| **Audience** | Learners, documenters | Developers, users |
| **Use Case** | Teaching/examples | Production/quick use |
| **Node Focus** | Yes (ComfyUI) | No (direct conversion) |
| **Workflow Diagram** | Yes (ASCII art) | No |
| **Explanations** | Extensive | Minimal |
| **Variations** | Multiple suggested | None (single output) |
| **Time to Create** | Detailed/slower | Fast |

---

## 🎓 How to Use These Agents

### Setting Up JSON-Plan-Expert

1. **Copy the system prompt:** Use the content from `JSON-Plan-Expert.md`
2. **Paste into your LLM interface:** Claude, GPT-4, etc.
3. **Provide natural language prompt:** Any descriptive image prompt
4. **Receive:** Complete markdown tutorial

**Example conversation:**
```
[System]: [Paste JSON-Plan-Expert.md content]

[User]: Convert this to a workflow plan:
"A vintage 1960s photograph of a diner at night with neon signs"

[Agent]: [Creates 3000+ word markdown guide with node configurations]
```

### Setting Up JSON-Direct-Expert

1. **Copy the system prompt:** Use the content from `JSON-Direct-Expert.md`
2. **Paste into your LLM interface**
3. **Provide natural language prompt**
4. **Receive:** Clean JSON output

**Example conversation:**
```
[System]: [Paste JSON-Direct-Expert.md content]

[User]: A vintage 1960s photograph of a diner at night with neon signs

[Agent]: 
Vintage diner scene with night photography. Era-appropriate technical settings.

{
  "scene": "1960s American roadside diner exterior at night",
  "subjects": [
    {
      "description": "Chrome and glass diner with red vinyl booths visible through windows",
      "position": "center frame",
      "color_palette": ["#FF0000", "#SILVER"]
    },
    {
      "description": "Neon signs glowing in blue and red",
      "position": "flanking diner entrance",
      "color_palette": ["#0000FF", "#FF0000"]
    }
  ],
  "style": "Vintage color photography with Kodachrome film aesthetic",
  "lighting": "Neon lights and warm interior glow against dark night sky",
  "mood": "Nostalgic, Americana, cinematic",
  "camera": {
    "angle": "Eye level, straight on",
    "distance": "Wide shot",
    "lens-mm": 35,
    "f-number": "f/4",
    "ISO": 800
  }
}

Technical notes: ISO 800 for night shooting, f/4 balancing depth and light gathering.
```

---

## 🛠️ Both Agents Share

### Common Knowledge
Both agents understand:
- Complete FLUX.2 JSON schema
- All field specifications and data types
- Camera parameter ranges
- Color hex code conversion
- Position vocabulary
- Photography terminology
- Era-specific technical matching

### Formatting Rules
Both enforce:
- `lens-mm` as number: `85` not `"85"`
- `f-number` as string: `"f/2.8"` not `2.8`
- `ISO` as number: `400` not `"400"`
- Hex codes uppercase: `#FF5733` not `#ff5733`
- Correct field naming (hyphens vs underscores)
- Valid JSON syntax
- Only fields with meaningful values

### Quality Standards
Both ensure:
- Schema compliance
- Proper data types
- No syntax errors
- Meaningful content
- Omit empty fields
- At least one subject with description

---

## 💡 Best Practices

### Using JSON-Plan-Expert
**Do:**
- Use for creating tutorials
- Reference for learning node system
- Build example libraries
- Document complex workflows

**Don't:**
- Use when you just need JSON quickly
- Use for batch processing
- Use in automated pipelines

### Using JSON-Direct-Expert
**Do:**
- Use for quick conversions
- Integrate into scripts/APIs
- Rapid prototyping
- Direct FLUX.2 usage

**Don't:**
- Use when learning the node system
- Use for creating documentation
- Use when teaching others

---

## 🎯 Example Use Cases

### Use Case 1: Building Documentation
**Goal:** Create tutorial showing how to make vintage film prompts

**Agent:** JSON-Plan-Expert  
**Input:** "1960s Kodachrome photograph of a beach scene"  
**Output:** Complete markdown guide with node workflow

**Why:** Educational value, shows ComfyUI process, includes variations

---

### Use Case 2: Quick Image Generation
**Goal:** Convert 50 natural language prompts to JSON for batch processing

**Agent:** JSON-Direct-Expert  
**Input:** List of 50 descriptions  
**Output:** 50 clean JSON objects

**Why:** Fast, no extra documentation, ready for API

---

### Use Case 3: Learning the System
**Goal:** Understand how to structure complex multi-subject scenes

**Agent:** JSON-Plan-Expert  
**Input:** Complex scene description  
**Output:** Step-by-step breakdown with explanations

**Why:** Educational, shows decision-making process, suggests experiments

---

### Use Case 4: Production Pipeline
**Goal:** Integrate prompt conversion into image generation workflow

**Agent:** JSON-Direct-Expert  
**Input:** User-provided descriptions  
**Output:** Valid JSON for FLUX.2 API

**Why:** Minimal output, fast, production-ready

---

## 📊 Decision Matrix

**Choose JSON-Plan-Expert when:**
- [ ] Creating documentation
- [ ] Teaching/learning
- [ ] Building examples
- [ ] Explaining workflow
- [ ] ComfyUI interface is relevant
- [ ] You want variations and alternatives
- [ ] Output will be saved and referenced

**Choose JSON-Direct-Expert when:**
- [ ] Need immediate JSON
- [ ] Bypassing ComfyUI
- [ ] Batch processing
- [ ] API integration
- [ ] Quick experimentation
- [ ] Production pipeline
- [ ] Only need the JSON output

---

## 🔗 Integration Examples

### Using with ComfyUI
1. Use **JSON-Plan-Expert** to understand workflow
2. Build the workflow in ComfyUI interface
3. Use **JSON-Direct-Expert** for quick JSON variations
4. Test different prompts rapidly

### Using with Scripts
```python
# Example integration with JSON-Direct-Expert output
import json

natural_prompt = "A red sports car on a mountain road"
# Get JSON from agent (paste agent's JSON output)
flux_json = {
  "scene": "Winding mountain road with scenic vista",
  "subjects": [
    {
      "description": "Sleek red sports car with aerodynamic design",
      "position": "center foreground on road",
      "color_palette": ["#DC143C", "#1A1A1A"]
    }
  ],
  "camera": {
    "lens-mm": 24,
    "f-number": "f/8"
  }
}

# Use with FLUX.2 API
response = flux_api.generate(json_prompt=json.dumps(flux_json))
```

### Using for Documentation
1. Collect natural language prompts
2. Run through **JSON-Plan-Expert**
3. Save markdown outputs as examples
4. Build documentation library
5. Reference in tutorials

---

## 📝 Files Location

Both agent system prompts are located at:
```
Documentation/04_Planning/
├── JSON-Plan-Expert.md      ← Educational workflow agent
└── JSON-Direct-Expert.md    ← Direct conversion agent
```

---

## 🎉 Quick Start

### To Create Educational Documentation:
1. Copy content from [JSON-Plan-Expert.md](JSON-Plan-Expert.md)
2. Use as system prompt in LLM
3. Provide natural language prompt
4. Get complete workflow guide

### To Get Quick JSON:
1. Copy content from [JSON-Direct-Expert.md](JSON-Direct-Expert.md)
2. Use as system prompt in LLM
3. Provide natural language prompt
4. Get clean JSON output

---

## 🤝 Both Agents Can

- Convert any natural language prompt
- Handle complex multi-subject scenes
- Extract and convert colors to hex codes
- Infer appropriate camera settings
- Match technical parameters to eras
- Understand photography terminology
- Follow FLUX.2 schema exactly
- Produce valid, working output

---

## 📚 Related Documentation

- [Godzilla Example](../03_Reference/t2i-Godzilla-example.md) - Example output from JSON-Plan-Expert
- [JSON Schema Anatomy](../02_Learning_Materials/02-json-schema-anatomy.md) - Complete field reference
- [ComfyUI Package](../../ComfyUI_Package/ComfyUI_FLUX2_Prompt_Builder/) - The node system

---

## 🎯 Summary

Two agents, two purposes:

**JSON-Plan-Expert** = Education + Workflow + Documentation  
**JSON-Direct-Expert** = Speed + Production + Clean JSON

Choose based on your goal: learning or building?

---

**Both agents are ready to convert your natural language prompts to structured FLUX.2 JSON!** 🚀

*Last updated: November 27, 2024*
