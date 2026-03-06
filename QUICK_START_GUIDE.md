# Quick Start Guide - Character Dataset Generation 🚀

Generate consistent characters for AI training using our Skill System workflow.

```
┌─────────────────────────────────────────────────────────────┐
│           SKILL SYSTEM WORKFLOW                             │
│     Generate Consistent Characters for AI Training          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 1: DEFINE CHARACTER                                  │
│                                                             │
│  ┌──────────────┐    ┌──────────────┐                      │
│  │ Choose Style │───▶│ Fill Spec    │                      │
│  │  • 3D or     │    │ Template:    │                      │
│  │    Anime     │    │ SKILLS/      │                      │
│  └──────────────┘    │ *_CHARACTER_ │                      │
│                      │ _SPEC_       │                      │
│                      │ _TEMPLATE.md │                      │
│                      └──────────────┘                      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 2: GENERATE WORKFLOWS                                │
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │ Copy LLM     │───▶│ Paste to     │───▶│ Get 7 JSON   │  │
│  │ Prompt:      │    │ ChatGPT/     │    │ Workflow     │  │
│  │ SKILLS/      │    │ Claude       │    │ Files        │  │
│  │ *_WORKFLOW_  │    │              │    │              │  │
│  │ _GENERATOR_  │    │              │    │              │  │
│  │ _PROMPT.md   │    │              │    │              │  │
│  └──────────────┘    └──────────────┘    └──────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 3: VALIDATE                                          │
│                                                             │
│  ┌──────────────────────────────────────────┐              │
│  │ Run 10-Point Checklist                   │              │
│  │ SKILLS/*_VALIDATION_GUIDE.md             │              │
│  │  □ Gender tag first (anime)?             │              │
│  │  □ No weight syntax?                     │              │
│  │  □ Quality tags at end?                  │              │
│  │  □ Correct settings?                     │              │
│  │  □ Valid JSON?                           │              │
│  └──────────────────────────────────────────┘              │
└─────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 4: GENERATE                                          │
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │ Load in      │───▶│ Generate     │───▶│ Curate 30-40 │  │
│  │ ComfyUI      │    │ Images       │    │ Best Images  │  │
│  │ user/default │    │ 2-4 at a     │    │              │  │
│  │ /workflows/  │    │ time         │    │              │  │
│  └──────────────┘    └──────────────┘    └──────────────┘  │
└─────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 5: AUTO-CLUSTER (NEW!)                               │
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │ Extract      │───▶│ Cluster with │───▶│ View in      │  │
│  │ Embeddings   │    │ HDBSCAN      │    │ Gallery      │  │
│  │ (CLIP+Face)  │    │ Auto-groups  │    │ Pick Best    │  │
│  └──────────────┘    │ Similar      │    │ Cluster      │  │
│                      │ Images       │    │              │  │
│                      └──────────────┘    └──────────────┘  │
└─────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 6: TRAIN                                             │
│                                                             │
│  ┌──────────────────────────────────────────┐              │
│  │ Train LoRA with Kohya_ss                 │              │
│  │  • Create captions: TOKEN, role          │              │
│  │  • Organize dataset folder               │              │
│  │  • Run training                          │              │
│  └──────────────────────────────────────────┘              │
└─────────────────────────────────────────────────────────────┘
```

## 🎨 Choose Your Character Style

### Option A: 3D Stylized (JuggernautXL)
- **Best for:** Semi-realistic 3D characters with tech aesthetic
- **Examples:** Nova (AI researcher), Athena (DeFi strategist)
- **Model:** `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` (~6.7GB)
- **Settings:** Steps=35, CFG=7, Weighted prompts `(token:1.2)`
- **Style:** Stylized 3D fintech characters

### Option B: Anime/Manga (Animagine XL 4.0)
- **Best for:** Anime-style characters
- **Examples:** hikariAI (crypto market scout), Aika (crypto analyst)
- **Model:** `animagine-xl-4.0-opt.safetensors` (~6.5GB)
- **Settings:** Steps=28, CFG=5, Tag-based prompts (no weights)
- **Style:** Modern 2020s anime aesthetic

## 📦 Prerequisites

**Models required:**
- Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors (for 3D)
- animagine-xl-4.0-opt.safetensors (for Anime)

**Verify workflows exist:**
```
user/default/workflows/
├── nova_juggernaut.json
├── athena_juggernaut.json
├── hikariAI_portrait_animagine.json
├── hikariAI_standing_animagine.json
├── hikariAI_action_animagine.json
├── aika_portrait_animagine.json
├── aika_standing_animagine.json
└── aika_action_animagine.json
```

## ⚡ Quick Start - Use Existing Characters

### 3D Stylized:
1. **Nova** (AI researcher): Load `nova_juggernaut.json`
2. **Athena** (DeFi strategist): Load `athena_juggernaut.json`
3. See prompts in: `CHARACTERS.md`

### Anime:
1. **hikariAI** (crypto market scout):
   - Portrait: `hikariAI_portrait_animagine.json`
   - Standing: `hikariAI_standing_animagine.json`
   - Action: `hikariAI_action_animagine.json`
2. **Aika** (crypto analyst):
   - Portrait: `aika_portrait_animagine.json`
   - Standing: `aika_standing_animagine.json`
   - Action: `aika_action_animagine.json`

See full specs: `characters/hikariAI/spec.md`, `characters/aika/spec.md`

## ⚙️ Settings Comparison

| Feature | 3D Stylized | Anime |
|---------|-------------|-------|
| **Model** | Juggernaut-XL_v9 | animagine-xl-4.0-opt |
| **Prompt** | Natural language | Tag-based |
| **Weights** | `(token:1.2)` | ❌ Not used |
| **Steps** | 35 | 28 |
| **CFG** | 7 | 5 |
| **Sampler** | dpmpp_2m | euler_ancestral |
| **Resolution** | 1024×1024 | 1024×1024 |
| **BREAK** | ✅ Required | ❌ Not used |
| **Quality Tags** | Throughout | At END only |

## 📊 Dataset Curation Strategy

### The "Generate Many, Keep Best" Approach

**Step 1: Generate 100-200+ images**
- Run multiple batches with different seeds
- Cover all poses: portrait, waist-up, full body, action
- Don't stop at 30-40 - generate many more

**Step 2: Auto-Cluster with AI (NEW!)**

Let the computer find your best images automatically:

```bash
# Install dependencies (one time)
cd scripts && pip install -r requirements.txt

# Extract face-focused embeddings
python3 extract_embeddings.py --character hikariAI

# Cluster similar images automatically
python3 cluster_images.py --character hikariAI

# View results
python3 view_clusters.py --character hikariAI
```

**What happens:**
- CLIP + InsightFace extracts embeddings from all images
- HDBSCAN groups similar faces into clusters
- Creates symlinks in `output/hikariAI/clusters/cluster_0/`
- You get 2-5 clusters + outliers

**Step 3: Pick the best cluster (30-40 images)**

Browse clusters in smart-comfyui-gallery at `http://localhost:8189/galleryout/`

**Selection criteria:**
- ✅ **Pick ONE cluster** - Usually cluster_0 (highest consistency)
- ✅ **30-40 images** - Don't mix clusters!
- ✅ **Variety in poses** - Front, 3/4, side views, different actions
- ✅ **Good anatomy** - Avoid obviously broken hands/proportions

**Why pick ONE cluster:**
Each cluster represents a consistent "look" for your character. Mixing clusters mixes different styles/angles and confuses the LoRA training.

Think of it like teaching someone to recognize a friend - show them many photos from different angles, but all of the SAME person. The clustering does the hard work of grouping "same person" photos for you!

### Image Distribution Target

| Pose Type | Percentage | Count | Priority |
|-----------|-----------|-------|----------|
| **Portrait** | 40% | 12-16 | Face consistency is critical |
| **Waist-Up** | 40% | 12-16 | Shows outfit details |
| **Full Body** | 20% | 6-8 | Environmental context |

**Pro tip:** You can fix minor issues in Photoshop/GIMP before training. Focus on getting the character's core identity consistent.

## 📚 Essential Documentation

### For 3D Stylized:
- `SKILLS/JUGGERNAUT_CHARACTER_SKILL.md` - Complete guide
- `SKILLS/CHARACTER_SPEC_TEMPLATE.md` - Character template
- `SKILLS/WORKFLOW_GENERATOR_PROMPT.md` - LLM prompt
- `SKILLS/VALIDATION_GUIDE.md` - 10-point checklist

### For Anime:
- `SKILLS/ANIME_CHARACTER_SKILL.md` - Complete guide
- `SKILLS/ANIME_CHARACTER_SPEC_TEMPLATE.md` - Character template
- `SKILLS/ANIME_WORKFLOW_GENERATOR_PROMPT.md` - LLM prompt
- `SKILLS/ANIME_VALIDATION_GUIDE.md` - 10-point checklist
- `SKILLS/ANIME_PROMPT_TEMPLATES.md` - Pre-built poses

### Automation Scripts:
- `scripts/README.md` - Complete automation workflow
- `scripts/generate_dataset.py` - Batch image generation
- `scripts/extract_embeddings.py` - Face-focused embeddings
- `scripts/cluster_images.py` - HDBSCAN clustering
- `scripts/view_clusters.py` - View cluster statistics

## 🆘 Common Issues

**"Which model should I use?"**
→ Check your workflow JSON - it specifies the model name

**"Images don't look right"**
→ Run the validation checklist for your chosen style

**"Workflow won't load"**
→ Check JSON syntax, ensure model file exists in `models/checkpoints/`

**"Out of memory"**
→ Reduce batch size to 1, restart ComfyUI, close other applications

**"Clustering takes too long"**
→ First run downloads ~1.5GB models. After that it's fast (~1 min for 200 images)

**"Clusters not showing in gallery"**
→ Restart smart-comfyui-gallery to pick up new symlinks

## 💡 Pro Tips

**Use the clustering!** Don't manually review 200+ images:
```bash
cd scripts
python3 extract_embeddings.py --character hikariAI
python3 cluster_images.py --character hikariAI
python3 view_clusters.py --character hikariAI
# Then browse http://localhost:8189/galleryout/ → hikariAI → clusters → cluster_0
```

**Check cluster stats:** Look for consistency score > 0.7 and 20+ images in a cluster

**Mixing clusters = bad training:** Pick images from ONE cluster only

**cluster_-1 = outliers:** Some might be good, but review individually

## 🎯 Ready? Let's Go!

1. **Pick your style** (3D or Anime)
2. **Choose a character** (existing or create new)
3. **Follow the Skill System Workflow** above
4. **Generate 200+ images** with automation scripts
5. **Auto-cluster and pick best 30-40 images**
6. **Train your LoRA!**

**Questions?** Check the detailed skill documentation in `SKILLS/` folder.

**Need help?** The LLM workflow generator will ask clarifying questions and guide you through creating your character!

**Want automation?** See `scripts/README.md` for the complete automated workflow including batch generation and AI-powered clustering.
