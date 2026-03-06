#!/usr/bin/env python3
"""
Extract face-focused CLIP embeddings from generated images

Usage:
    python3 extract_embeddings.py --character hikariAI
    python3 extract_embeddings.py --character hikariAI --resume
"""

import argparse
import json
import sys
from pathlib import Path
from tqdm import tqdm
import numpy as np

# Add parent directory to path for utils
sys.path.insert(0, str(Path(__file__).parent))
from utils import FaceDetector, CLIPEmbedder


def get_image_files(character_dir):
    """Get all image files for a character"""
    image_files = []
    output_dir = Path('output') / character_dir
    
    if not output_dir.exists():
        print(f"Error: Output directory not found: {output_dir}")
        return []
    
    # Find all PNG files in subdirectories
    for subdir in sorted(output_dir.iterdir()):
        if subdir.is_dir():
            for img_file in subdir.glob('*.png'):
                image_files.append(img_file)
    
    return sorted(image_files)


def extract_embedding(image_path, face_detector, clip_embedder, embedding_dir):
    """Extract embedding for a single image"""
    # Create paths
    rel_path = image_path.relative_to(Path('output'))
    embedding_path = embedding_dir / f"{image_path.stem}.npy"
    metadata_path = embedding_dir / f"{image_path.stem}.json"
    
    # Check if already exists
    if embedding_path.exists() and metadata_path.exists():
        return True, "Already exists"
    
    try:
        # Detect face
        face_result = face_detector.detect_face(image_path)
        
        # Load full image
        from PIL import Image
        full_image = Image.open(image_path).convert('RGB')
        
        # Get combined embedding
        if face_result['has_face']:
            embedding = clip_embedder.get_combined_embedding(
                face_result['face_image'],
                full_image,
                face_weight=0.7
            )
        else:
            # No face detected, use full image only
            embedding = clip_embedder.get_embedding(full_image)
        
        # Save embedding
        np.save(embedding_path, embedding)
        
        # Save metadata
        metadata = {
            'image_path': str(rel_path),
            'has_face': face_result['has_face'],
            'face_bbox': face_result['bbox'],
            'face_confidence': face_result['confidence'],
            'embedding_dim': len(embedding),
            'face_weight': 0.7 if face_result['has_face'] else 0.0
        }
        
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        return True, "Success"
        
    except Exception as e:
        return False, str(e)


def main():
    parser = argparse.ArgumentParser(
        description='Extract CLIP embeddings from generated images'
    )
    parser.add_argument(
        '--character', '-c',
        required=True,
        help='Character name (e.g., hikariAI)'
    )
    parser.add_argument(
        '--resume', '-r',
        action='store_true',
        help='Resume from interrupted extraction'
    )
    
    args = parser.parse_args()
    
    # Setup paths
    character = args.character
    output_dir = Path('output') / character
    embedding_dir = Path('embeddings') / character
    
    print("="*60)
    print(f"Extracting Embeddings: {character}")
    print("="*60)
    
    # Check if output exists
    if not output_dir.exists():
        print(f"Error: No output directory found: {output_dir}")
        print("Please generate images first using generate_dataset.py")
        sys.exit(1)
    
    # Create embedding directory
    embedding_dir.mkdir(parents=True, exist_ok=True)
    
    # Get all image files
    image_files = get_image_files(character)
    if not image_files:
        print("No images found to process")
        sys.exit(1)
    
    print(f"\nFound {len(image_files)} images")
    
    # Check for existing embeddings
    if args.resume:
        existing = list(embedding_dir.glob('*.npy'))
        print(f"Found {len(existing)} existing embeddings")
        print("Resuming extraction...\n")
    else:
        print("Starting fresh extraction...\n")
    
    # Initialize models
    print("Loading models...")
    face_detector = FaceDetector(det_thresh=0.5, min_face_size=100)
    clip_embedder = CLIPEmbedder(model_name='ViT-L-14', pretrained='openai')
    print("✓ Models loaded\n")
    
    # Process images
    successful = 0
    failed = 0
    with_face = 0
    
    with tqdm(image_files, desc="Extracting embeddings") as pbar:
        for img_path in pbar:
            # Check if already exists
            embedding_path = embedding_dir / f"{img_path.stem}.npy"
            if embedding_path.exists():
                successful += 1
                # Load metadata to count faces
                metadata_path = embedding_dir / f"{img_path.stem}.json"
                if metadata_path.exists():
                    with open(metadata_path) as f:
                        meta = json.load(f)
                        if meta.get('has_face'):
                            with_face += 1
                continue
            
            # Extract embedding
            success, message = extract_embedding(
                img_path, face_detector, clip_embedder, embedding_dir
            )
            
            if success:
                successful += 1
                # Check if face was detected
                metadata_path = embedding_dir / f"{img_path.stem}.json"
                if metadata_path.exists():
                    with open(metadata_path) as f:
                        meta = json.load(f)
                        if meta.get('has_face'):
                            with_face += 1
            else:
                failed += 1
                pbar.write(f"Failed: {img_path.name} - {message}")
    
    # Create manifest
    manifest = {
        'character': character,
        'total_images': len(image_files),
        'successful_extractions': successful,
        'failed_extractions': failed,
        'images_with_faces': with_face,
        'embedding_dir': str(embedding_dir),
        'embeddings': []
    }
    
    for emb_file in sorted(embedding_dir.glob('*.npy')):
        metadata_file = emb_file.with_suffix('.json')
        if metadata_file.exists():
            with open(metadata_file) as f:
                meta = json.load(f)
                manifest['embeddings'].append({
                    'embedding_file': str(emb_file.name),
                    'metadata_file': str(metadata_file.name),
                    'image_path': meta['image_path'],
                    'has_face': meta['has_face']
                })
    
    manifest_path = embedding_dir / 'manifest.json'
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    # Print summary
    print("\n" + "="*60)
    print("EXTRACTION COMPLETE")
    print("="*60)
    print(f"Total images: {len(image_files)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Images with faces: {with_face} ({with_face/len(image_files)*100:.1f}%)")
    print(f"\nEmbeddings saved to: {embedding_dir}")
    print(f"Manifest: {manifest_path}")
    print("\nNext step: Run cluster_images.py")
    print("="*60)


if __name__ == "__main__":
    main()
