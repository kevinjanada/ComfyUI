# Characters Directory

This directory contains character specifications for LoRA training dataset generation.

## Structure

Each character has their own folder containing:
- **`spec.md`** - Complete character specification (visual identity, prompts, settings)
- **`README.md`** - Generation notes, results, and training outcomes

## Available Characters

### Anime Style (Animagine XL 4.0)
- **[hikariAI](hikariAI/)** - AI crypto market scout
- **[aika](aika/)** - Crypto analyst
- **[luna](luna/)** - 3D stylized character (Juggernaut XL)

## How to Use

1. **View a spec**: `cat characters/hikariAI/spec.md`
2. **Generate dataset**: Use scripts with character name matching folder name
3. **Reference**: Link to spec when generating workflows with LLM

## Related Files

- **Workflows**: `user/default/workflows/[character]_[pose]_animagine.json`
- **Generated images**: `output/[character]/`
- **Embeddings**: `embeddings/[character]/`
- **Clusters**: `output/[character]/clusters/`
- **Example specs**: `SKILLS/examples/` (kept for reference)

## Creating New Characters

1. Create new folder: `mkdir characters/yourCharacter`
2. Write spec using template: `SKILLS/ANIME_CHARACTER_SPEC_TEMPLATE.md`
3. Generate workflows using: `SKILLS/ANIME_WORKFLOW_GENERATOR_PROMPT.md`
4. Validate with: `SKILLS/ANIME_VALIDATION_GUIDE.md`
5. Generate dataset: `python3 scripts/generate_dataset.py --config scripts/configs/yourCharacter.yaml`

## See Also

- **SKILLS/** - Skill system documentation and templates
- **scripts/README.md** - Complete automation workflow
- **QUICK_START_GUIDE.md** - Getting started guide
