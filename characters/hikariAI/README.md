# hikariAI - AI Crypto Market Scout

## Overview
- **Token:** hikariAI
- **Style:** Modern Anime (Animagine XL 4.0)
- **Role:** AI crypto market scout who detects trading opportunities early

## Character Details
- **Hair:** Short neon blue, dynamic spiky style
- **Eyes:** Electric yellow with star highlights
- **Signature:** Glowing cyber visor over one eye
- **Outfit:** Futuristic trading jacket (electric blue + neon purple)
- **Environment:** Holographic interfaces, floating candlestick charts

## Files
- **`spec.md`** - Complete character specification with prompts and settings
- **Workflows**: 
  - `user/default/workflows/hikariAI_portrait_animagine.json`
  - `user/default/workflows/hikariAI_standing_animagine.json`
  - `user/default/workflows/hikariAI_action_animagine.json`

## Generation Results

### Dataset Statistics
- **Total Generated:** 204 images
- **Clusters Found:** 2
- **Best Cluster:** cluster_0 (15 images, consistency: 0.731)

### Cluster Analysis
```
Cluster 0: 15 images - Consistency: 0.731
Cluster 1: 60 images - Consistency: 0.706
Outliers: 129 images
```

### Selected for Training
- **Images:** 30-40 from cluster_0
- **Distribution:** Portrait 40%, Standing 40%, Action 20%
- **Location:** `output/hikariAI/clusters/cluster_0/`

## Training Notes

### Caption Format
```
hikariAI, AI crypto market scout
```

### Training Configuration
- **Model:** SDXL Base
- **Network Dim:** 32
- **Network Alpha:** 16
- **Resolution:** 1024x1024
- **Epochs:** 10

### Results
- **Training Date:** 
- **Final Loss:**
- **Model Quality:**

## See Also
- [Spec](spec.md) - Full character specification
- [Skill Guide](../SKILLS/ANIME_CHARACTER_SKILL.md) - Anime generation guide
- [Automation](../scripts/README.md) - Batch generation workflow
