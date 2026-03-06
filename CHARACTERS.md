# Nova & Athena LoRA Dataset Generation Guide (SDXL)

This document defines **how to generate the dataset images** for training LoRAs for the characters **Nova (AI Market Analyst)** and **Athena (Quant Strategist)**.

Goal: produce **30–40 clean training images per character** with consistent identity but varied poses and scenes.

---

# Global Style Rules

Art style (must remain consistent):

stylized 3D fintech character

Image resolution:

1024x1024

Sampler suggestion:

DPM++ 2M Karras  
Steps: 30  
CFG: 6

---

# Negative Prompt

Use the same negative prompt for every generation.

bad anatomy, bad hands, extra fingers, distorted face, blurry, low quality, text, watermark, logo, multiple characters, duplicate body parts

---

# Character Identity Lock

These traits must **NOT change** across images.

## Nova

Identity:

- female AI trading analyst
- short silver hair
- glowing teal eyes
- circular holographic halo behind head
- black fintech bodysuit with glowing circuit patterns

Color palette:

teal #00F0FF  
purple #6B4DFF  
black #0B0F1A

Signature elements:

- holographic candlestick charts
- teal lighting
- fintech holographic interfaces

---

## Athena

Identity:

- AI quant strategist
- long white or platinum hair
- glowing gold eyes
- neural crown interface
- white strategist robe with gold accents

Color palette:

gold #FFD700  
white #F4F6F8  
navy #0A1A33

Signature elements:

- quant data streams
- neural analysis interface
- gold lighting

---

# Dataset Generation Strategy

Generate **80–100 candidate images**.

After filtering, keep **30–40 images**.

Only vary:

- pose
- camera angle
- lighting
- environment

Never change:

- hairstyle
- outfit
- face structure
- color palette
- core accessories

---

# Dataset Composition

Recommended final dataset:

Portrait shots: 15  
Waist-up shots: 15  
Full-body shots: 10

---

# Nova Dataset Generation Prompts

## Portrait

novatraderAI, female AI trading analyst, glowing teal eyes, circular holographic halo behind head, short silver hair, black fintech bodysuit with glowing circuits, teal lighting, stylized 3D fintech character, portrait shot, minimal background

---

## Neutral Pose

novatraderAI, female AI trading analyst standing confidently, glowing teal eyes, circular holographic halo, black fintech bodysuit with circuit patterns, teal and purple lighting, stylized 3D fintech character

---

## Chart Analysis

novatraderAI analyzing holographic candlestick charts, glowing teal eyes, circular holographic halo interface behind head, futuristic trading interface, teal neon lighting, stylized 3D fintech character

---

## Explaining Trade

novatraderAI pointing at resistance level on holographic trading chart, glowing teal eyes, circular halo interface, fintech AI bodysuit, teal lighting, stylized 3D fintech character

---

## Market Scan

novatraderAI observing floating crypto market data streams, holographic candlestick charts, glowing teal eyes, teal neon lighting, stylized 3D fintech character

---

## Side Angle

novatraderAI side profile analyzing financial data streams, glowing teal eyes, circular holographic halo, teal lighting, stylized 3D fintech character

---

## Trading Desk

novatraderAI sitting at futuristic trading desk with holographic charts, glowing teal eyes, circular halo interface, teal lighting, stylized 3D fintech character

---

# Athena Dataset Generation Prompts

## Portrait

athenaquantAI, AI quant strategist, glowing gold eyes, neural crown interface, long platinum hair, white strategist robe with gold accents, gold lighting, stylized 3D fintech character, portrait shot

---

## Strategic Analysis

athenaquantAI analyzing advanced market data streams, glowing gold eyes, neural crown interface, gold quant interface floating around her, stylized 3D fintech character

---

## Macro Market View

athenaquantAI observing global market data holograms, neural crown interface, gold lighting, white strategist robe, stylized 3D fintech character

---

## Quant Calculation

athenaquantAI surrounded by floating quant analysis equations and market indicators, glowing gold eyes, neural crown interface, stylized 3D fintech character

---

## Confident Pose

athenaquantAI standing with arms crossed, analyzing market volatility data streams, glowing gold eyes, neural crown interface, gold lighting, stylized 3D fintech character

---

## Side Angle

athenaquantAI side profile reviewing financial data interface, neural crown interface, glowing gold eyes, stylized 3D fintech character

---

## Strategy Console

athenaquantAI operating advanced quant analysis console, neural crown interface, gold data streams, stylized 3D fintech character

---

# Dataset Filtering Checklist

Delete images if they contain:

- distorted hands
- broken faces
- different hairstyles
- different outfits
- missing halo or crown
- artifacts
- multiple characters

---

# Caption Format

Each image should have a short caption file.

Example:

novatraderAI, female AI trading analyst

or

athenaquantAI, AI quant strategist

Avoid long captions.

---

# Dataset Folder Structure

nova_dataset/
  0001.png
  0001.txt
  0002.png
  0002.txt
  ...

athena_dataset/
  0001.png
  0001.txt
  0002.png
  0002.txt
  ...

---

# LoRA Testing Prompts

Test simple prompts first.

Nova:

novatraderAI portrait

Athena:

athenaquantAI portrait

Then test complex prompts.

Example:

novatraderAI explaining bitcoin breakout with holographic candlestick chart

athenaquantAI analyzing crypto market volatility with quant data streams
