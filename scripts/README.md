# Dataset Generation Automation

Automated generation of 200+ images for LoRA training using ComfyUI workflows with random seeds.

## Overview

This system automates the "Generate Many, Keep Best" strategy:
1. **Generates 200 images** (following 40/40/20 distribution)
2. **Random seeds** for variety
3. **Sequential execution** (portrait → standing → action) to manage RAM
4. **Progress tracking** with resume capability
5. **Organized output** into pose-specific folders

## Quick Start

```bash
# 1. Make sure ComfyUI is running
python main.py --listen 0.0.0.0 --port 8188

# 2. Generate dataset
python3 scripts/generate_dataset.py --config scripts/configs/hikariAI.yaml

# 3. Check progress
python3 scripts/generate_dataset.py --config scripts/configs/hikariAI.yaml --status

# 4. Resume if interrupted
python3 scripts/generate_dataset.py --config scripts/configs/hikariAI.yaml --resume
```

## Complete Workflow

### Phase 1: Generate Images (Standard Library)

No dependencies needed - uses only Python standard library.

### Phase 2: Cluster Images (Requires Dependencies)

Install clustering dependencies:
```bash
cd scripts
pip install -r requirements.txt
```

**Dependencies (~1.5GB download):**
- `open-clip-torch` - CLIP ViT-L/14 model
- `insightface` - Face detection
- `onnxruntime-gpu` - ONNX runtime
- `hdbscan` - Clustering algorithm
- `scikit-learn` - Preprocessing
- `numpy`, `Pillow`, `tqdm` - Utilities

## Configuration

### Creating a New Config

Copy `scripts/configs/hikariAI.yaml` and modify:

```yaml
character:
  name: "your_character"
  output_dir: "output/your_character"
  
generation:
  batch_size: 2  # Images per API call
  distribution:
    portrait: 80   # 40%
    standing: 80   # 40%
    action: 40     # 20%
  
workflows:
  portrait: "user/default/workflows/yourchar_portrait_animagine.json"
  standing: "user/default/workflows/yourchar_standing_animagine.json"
  action: "user/default/workflows/yourchar_action_animagine.json"

comfyui:
  host: "127.0.0.1"
  port: 8188
```

### Important Notes

- **Sequential Execution**: Only one pose type runs at a time (RAM management)
- **Random Seeds**: Each batch gets a random seed for variety
- **Resume Capability**: All scripts support `--resume` to continue from interruption
- **State Files**: Progress tracked in JSON files
- **Phase 1 (Standard Library)**: No dependencies for generation
- **Phase 2 (Clustering)**: Requires pip install for embeddings/clustering

## Workflow Requirements

Your workflow JSON files must:
1. Have a `KSampler` node with seed input
2. Use `SaveImage` node (not PreviewImage)
3. Be valid ComfyUI workflow exports

## Output Structure

### Generated Images
```
output/
└── hikariAI/
    ├── .generation_state.json    # Progress tracking
    ├── 01_portrait/
    │   ├── hikariAI_portrait_animagine_00001.png
    │   ├── hikariAI_portrait_animagine_00002.png
    │   └── ...
    ├── 02_standing/
    │   └── ...
    └── 03_action/
        └── ...
```

### Embeddings (after Phase 2)
```
embeddings/
└── hikariAI/
    ├── 01_portrait/
    │   ├── hikariAI_portrait_00001.npy       # 768-dim embedding
    │   ├── hikariAI_portrait_00001.json      # Metadata
    │   └── ...
    ├── manifest.json                          # Master list
```

### Clusters (after Phase 3)
```
output/
└── hikariAI/
    ├── 01_portrait/
    ├── 02_standing/
    ├── 03_action/
    └── clusters/               # Cluster results
        ├── cluster_0/              # Symlinks to best images
        │   ├── image_001.png -> ../../01_portrait/...
        │   └── ...
        ├── cluster_1/              # Alternative style
        ├── cluster_-1/             # Outliers
        ├── assignments.json        # Image->cluster mapping
        ├── clusters.json           # Cluster contents
        ├── stats.json              # Statistics
        └── manifest.json           # Complete manifest
```

## After Generation: Automated Clustering

Once you have 200+ images, use the automated clustering system to find similar images:

### Step 1: Install Dependencies

```bash
cd scripts
pip install -r requirements.txt
```

This downloads ~1.5GB of models:
- CLIP ViT-L/14 (~1GB)
- InsightFace models (~400MB)

### Step 2: Extract Embeddings

Extract face-focused CLIP embeddings from all images (~10-15 min for 200 images):

```bash
python3 extract_embeddings.py --character hikariAI
```

**What it does:**
- Detects faces using InsightFace
- Extracts CLIP ViT-L/14 embeddings
- Face crop: 70% weight, Full image: 30% weight
- Saves to `embeddings/hikariAI/`

**Resume capability:** Can interrupt and resume with `--resume` flag

### Step 3: Cluster Images

Automatically group similar images using HDBSCAN (~30 seconds):

```bash
python3 cluster_images.py --character hikariAI
```

**What it does:**
- Auto-detects optimal number of clusters
- Groups images by face consistency
- Creates symlinks in `output/hikariAI/clusters/`
- Identifies outliers (noise)

**Adjusting clustering parameters:**

If default settings don't work well, tune these:

```bash
# More strict clustering (fewer, tighter clusters)
python3 cluster_images.py --character hikariAI --min-cluster-size 15 --min-samples 8

# More lenient clustering (more, looser clusters)
python3 cluster_images.py --character hikariAI --min-cluster-size 5 --min-samples 3
```

**Parameter guide:**
- `--min-cluster-size`: Minimum images per cluster (default: 10)
  - Higher = fewer, more consistent clusters
  - Lower = more clusters, might include outliers
- `--min-samples`: Minimum samples for core points (default: 5)
  - Higher = stricter cluster membership
  - Lower = more images included in clusters

**Output structure:**
```
output/
└── hikariAI/
    ├── 01_portrait/        # Generated images
    ├── 02_standing/
    ├── 03_action/
    └── clusters/           # Cluster results
        ├── cluster_0/          # Most consistent group
        │   ├── image_001.png -> ../../01_portrait/...
        │   └── ...
        ├── cluster_1/          # Alternative style
        ├── cluster_-1/         # Outliers
        ├── assignments.json    # Image -> cluster mapping
        ├── clusters.json       # Cluster contents
        └── stats.json          # Cluster statistics
```

**Understanding cluster_-1 (Outliers):**
- Contains images that don't fit any cluster well
- These are "noise" in the dataset
- Some may actually be good - review individually
- Usually has lower consistency scores

### Step 4: View Results

```bash
python3 view_clusters.py --character hikariAI
```

**Example output:**
```
============================================================
Image Clustering Results: hikariAI
============================================================

Total Images Processed: 204
Clusters Found: 2
Outliers (Noise): 129

Cluster 0: (15 images)
  Consistency Score: 0.731
  Face Detection Rate: 0.0%
  Location: output/hikariAI/clusters/cluster_0/

Cluster 1: (60 images)
  Consistency Score: 0.706
  Face Detection Rate: 0.0%
  Location: output/hikariAI/clusters/cluster_1/

🏆 Best Cluster: Cluster 0
   Highest consistency score: 0.731
   This cluster has the most consistent character appearance
```

**Understanding the metrics:**
- **Consistency Score** (0-1): Higher = images in cluster are more similar
- **Face Detection Rate**: % of images where a face was detected
- **Outliers**: Images that don't fit well in any cluster

**Good results look like:**
- 2-5 clusters found
- At least one cluster with 20+ images
- Consistency score > 0.7

**Bad results indicate:**
- Everything in outliers: Images too diverse, need more generations
- Only 1 cluster: Images very similar (might be OK) or not enough variety
- Very low consistency (< 0.5): Character appearance varies too much

### Step 5: View Clusters in Smart Gallery

**Access the web UI:**
```
http://localhost:8189/galleryout/
```

Navigate to: `hikariAI` → `clusters` → `cluster_0` (or `cluster_1`, etc.)

**Why use the gallery?**
- See all images at once with thumbnails
- Check metadata/prompts for each image
- Download individual images
- Compare clusters side-by-side in different browser tabs

**The clusters directory contains:**
```
output/hikariAI/clusters/
├── cluster_0/          ← Start here (highest consistency)
│   └── [symlinks to best images]
├── cluster_1/          ← Alternative style/angle
├── cluster_-1/         ← Outliers (noise, inconsistent)
├── stats.json          ← Cluster statistics
└── assignments.json    ← Which image is in which cluster
```

**What to look for:**
1. **cluster_0** usually has the most consistent character appearance
2. **cluster_1, 2, etc.** might have different styles or poses
3. **cluster_-1** contains outliers - review individually, some might be good

### Step 6: Select Best Images

**Goal: Pick 30-40 most consistent images from ONE cluster**

**Recommended approach:**

1. **Open gallery** and browse each cluster
2. **Pick ONE cluster** with the most consistent character appearance
3. **Select 30-40 images** from that cluster:
   - Good face consistency
   - No weird artifacts
   - Variety of poses/expressions
   - At least 10 images per pose type (portrait/standing/action)

**Quick selection from command line:**
```bash
# List images in best cluster (usually cluster_0)
ls -la output/hikariAI/clusters/cluster_0/

# Copy to training folder
mkdir -p datasets/hikariAI/train
ls output/hikariAI/clusters/cluster_0/ | head -40 | while read f; do
    cp -L "output/hikariAI/clusters/cluster_0/$f" datasets/hikariAI/train/
done
```

**Note:** The `-L` flag copies the actual file (follows symlink), not the symlink itself.

### Step 7: Create Captions

Create caption files (one .txt per image) with the trigger token:

```bash
# Automated caption creation
for img in datasets/hikariAI/train/*.png; do
    base=$(basename "$img" .png)
    echo "hikariAI, AI crypto market scout, 1girl" > "datasets/hikariAI/train/${base}.txt"
done
```

**Caption format:**
```
hikariAI, 1girl, short neon blue hair, electric yellow eyes...
```

- **First token** = trigger token (must match your training config)
- **Keep it simple** - 5-15 tags is usually enough
- **Be consistent** - use same tags across all images

### Step 8: Train LoRA

Use Kohya_ss or your preferred trainer:

```bash
# Example with kohya_ss
python train_network.py \
    --pretrained_model_name_or_path="stabilityai/stable-diffusion-xl-base-1.0" \
    --train_data_dir="datasets/hikariAI/train" \
    --output_dir="models/lora" \
    --network_module=networks.lora \
    --network_dim=32 \
    --network_alpha=16 \
    --resolution=1024 \
    --train_batch_size=2 \
    --max_train_epochs=10 \
    --learning_rate=1e-4 \
    --lr_scheduler="cosine_with_restarts" \
    --optimizer_type="AdamW8bit"
```

### Step 7: Train LoRA

Use Kohya_ss or your preferred trainer with the curated dataset.

## Troubleshooting

**"Cannot connect to ComfyUI"**
- Make sure ComfyUI is running on the configured host/port
- Default: `http://127.0.0.1:8188`

**"Workflow not found"**
- Check that workflow paths are correct relative to ComfyUI root
- Verify JSON files exist

**Generation interrupted**
- Use `--resume` flag to continue from last saved state
- Progress is saved after each batch

**Out of memory**
- Reduce `batch_size` in config
- Ensure only one workflow runs at a time (sequential by design)

### Clustering Issues

**"No clusters found"**
- Increase `--min-cluster-size` (try 5 instead of 10)
- You need at least `min-cluster-size * 2` images

**"Everything in cluster_-1"**
- Lower `--min-samples` (try 3 instead of 5)
- Increase `--min-cluster-size` for stricter clustering
- Your images might be too diverse (need more generations)

**"Only 1-2 clusters found"**
- Lower `--min-cluster-size` to find smaller groups
- Images might be very similar (good problem to have!)

**Images not showing in gallery**
- Restart smart-comfyui-gallery to pick up new symlinks
- Check that symlinks point to valid files: `ls -la output/[character]/clusters/cluster_0/`
- Gallery scans on startup - wait for "Full scan completed" message

### ROCm Support (AMD GPUs on Arch Linux)

If you're using AMD GPUs with ROCm instead of NVIDIA/CUDA, you'll need `onnxruntime-rocm` instead of `onnxruntime-gpu`.

#### Installation

```bash
pip uninstall onnxruntime-gpu
pip install onnxruntime-rocm
```

#### Arch Linux: Executable Stack Fix

On Arch Linux with hardened kernel (PaX/grsecurity), you may encounter this error:

```
ImportError: cannot enable executable stack as shared object requires: Invalid argument
```

**Solution:** Clear the executable stack flag on all onnxruntime .so files:

```bash
# Option 1: Use the helper script (recommended)
python3 scripts/fix_onnxruntime_rocm.py

# Option 2: Manual fix
# Find all .so files and clear executable stack flag
for so in $(python -c "import onnxruntime; print(onnxruntime.__path__[0])")/capi/*.so; do
    patchelf --clear-execstack "$so"
done

# Verify it works
python -c "import onnxruntime; print(onnxruntime.get_available_providers())"
# Should show: ['MIGraphXExecutionProvider', 'ROCMExecutionProvider', 'CPUExecutionProvider']
```

**Note:** You may need to re-run this fix after upgrading `onnxruntime-rocm`.

## Examples

### Generate hikariAI dataset:
```bash
python3 scripts/generate_dataset.py --config scripts/configs/hikariAI.yaml
```

### Generate Aika dataset:
```bash
python3 scripts/generate_dataset.py --config scripts/configs/aika.yaml
```

### Check status of any generation:
```bash
python3 scripts/generate_dataset.py --config scripts/configs/hikariAI.yaml --status
```

## Features

### Image Generation
✓ Pure Python (standard library only)  
✓ Automatic progress tracking  
✓ Resume from interruption  
✓ ETA calculation  
✓ Sequential execution (RAM-friendly)  
✓ Random seed generation  
✓ Progress bars  
✓ Status checking  
✓ Error recovery  

### Image Clustering
✓ Face-focused CLIP embeddings (ViT-L/14)  
✓ InsightFace detection (confidence threshold: 0.5)  
✓ 70/30 weighting (face/full image)  
✓ Automatic HDBSCAN clustering  
✓ Outlier detection  
✓ Consistency scoring  
✓ Symlink organization  
✓ Resume capability  
✓ Best cluster recommendation
