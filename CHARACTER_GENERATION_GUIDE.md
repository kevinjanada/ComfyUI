# SDXL Character Generation - Phase 1 Complete!

## What We Set Up:

### 1. Models Downloaded:
- **Base Model**: `sd_xl_base_1.0.safetensors` (6.5GB) in `/models/checkpoints/`
- **VAE**: `sdxl_vae.safetensors` (320MB) in `/models/vae/`

### 2. Workflow Created:
- **File**: `workflows/sdxl_character_generation.json`
- A basic text-to-image workflow optimized for stylized 3D characters

## How to Use:

### Load the Workflow:
1. Open ComfyUI at `http://localhost:8188`
2. Click **Load** button (top right)
3. Select `workflows/sdxl_character_generation.json`

### Generate Images:
1. **CheckpointLoaderSimple** node already has `sd_xl_base_1.0.safetensors` selected
2. **Modify the Positive Prompt** (CLIPTextEncode node, top):
   - Default: "3d render of a stylized character, cute cartoon style..."
   - Customize to describe your desired character
3. **Adjust Settings** (KSampler node):
   - **Steps**: 30 (lower for faster, higher for quality)
   - **CFG**: 7.0 (guidance scale, higher = more prompt adherence)
   - **Sampler**: euler (try dpmpp_2m for different results)
4. Click **Queue Prompt** to generate!

### Prompt Tips for Stylized 3D Characters:

**Positive Keywords:**
- `3d render`, `blender render`, `octane render`
- `stylized`, `cartoon`, `chibi`, `stylized character`
- `vibrant colors`, `soft lighting`, `volumetric lighting`
- `high quality`, `detailed`, `masterpiece`, `best quality`

**Negative Keywords** (already included):
- `2d`, `flat`, `painting`, `drawing`, `sketch`
- `realistic`, `photorealistic`
- `bad anatomy`, `blurry`, `low quality`

### Example Prompts to Try:

1. **Cute Robot:**
   ```
   3d render of a cute robot character, round body, big eyes, metallic blue and orange colors, friendly expression, blender render, soft studio lighting, toy-like, vinyl figure, isometric view, white background
   ```

2. **Fantasy Character:**
   ```
   3d render of a stylized wizard character, pointy hat, flowing robes in purple and gold, magical staff, big expressive eyes, cartoon style, octane render, magical particles, rim lighting
   ```

3. **Animal Character:**
   ```
   3d render of a stylized fox character, orange fur, fluffy tail, big ears, wearing a scarf, cute expression, Pixar style, soft lighting, detailed fur, white background
   ```

## Next Steps (Phase 2):

Once you find a character design you like:
1. Save multiple images of that character with different poses/expressions
2. We'll use those to train a custom LoRA
3. Install Kohya_ss for training
4. Train your LoRA with ~15-20 images

## Troubleshooting:

### Out of Memory:
- Reduce batch size to 1
- Lower resolution (768x768 or 896x896)
- Use `--normalvram` or `--lowvram` flags when starting ComfyUI

### ROCm Issues:
Make sure PyTorch with ROCm is properly installed:
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm7.1
```

## Files Structure:
```
/home/kevin/ComfyUI/
├── models/
│   ├── checkpoints/
│   │   └── sd_xl_base_1.0.safetensors
│   └── vae/
│       └── sdxl_vae.safetensors
└── workflows/
    └── sdxl_character_generation.json
```

---

**Ready to generate!** Open ComfyUI, load the workflow, and start experimenting with prompts. Save any designs you like - we'll train a LoRA on them in Phase 2!
