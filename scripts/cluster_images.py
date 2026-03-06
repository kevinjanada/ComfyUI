#!/usr/bin/env python3
"""
Cluster images using HDBSCAN based on face-focused CLIP embeddings

Usage:
    python3 cluster_images.py --character hikariAI
    python3 cluster_images.py --character hikariAI --min-cluster-size 10
"""

import argparse
import json
import sys
from pathlib import Path
import numpy as np
from sklearn.preprocessing import normalize


def load_embeddings(embedding_dir):
    """Load all embeddings and metadata"""
    manifest_path = embedding_dir / 'manifest.json'
    
    if not manifest_path.exists():
        print(f"Error: Manifest not found: {manifest_path}")
        print("Please run extract_embeddings.py first")
        sys.exit(1)
    
    with open(manifest_path) as f:
        manifest = json.load(f)
    
    embeddings = []
    metadata_list = []
    
    print(f"Loading {len(manifest['embeddings'])} embeddings...")
    
    for item in manifest['embeddings']:
        emb_path = embedding_dir / item['embedding_file']
        meta_path = embedding_dir / item['metadata_file']
        
        # Load embedding
        embedding = np.load(emb_path)
        embeddings.append(embedding)
        
        # Load metadata
        with open(meta_path) as f:
            metadata = json.load(f)
            metadata['embedding_file'] = item['embedding_file']
            metadata_list.append(metadata)
    
    return np.array(embeddings), metadata_list


def perform_clustering(embeddings, min_cluster_size=10, min_samples=5):
    """Perform HDBSCAN clustering"""
    from hdbscan import HDBSCAN
    
    print(f"\nClustering with HDBSCAN...")
    print(f"  Min cluster size: {min_cluster_size}")
    print(f"  Min samples: {min_samples}")
    
    # Normalize embeddings
    embeddings_normalized = normalize(embeddings, norm='l2')
    
    # Run HDBSCAN
    clusterer = HDBSCAN(
        min_cluster_size=min_cluster_size,
        min_samples=min_samples,
        metric='euclidean',
        cluster_selection_method='eom'
    )
    
    labels = clusterer.fit_predict(embeddings_normalized)
    
    return labels, clusterer


def create_cluster_structure(character, labels, metadata_list, min_cluster_size):
    """Create cluster folders with symlinks"""
    clusters_dir = Path('output') / character / 'clusters'
    clusters_dir.mkdir(parents=True, exist_ok=True)
    
    # Get unique clusters
    unique_labels = set(labels)
    n_clusters = len([l for l in unique_labels if l >= 0])
    n_outliers = list(labels).count(-1)
    
    print(f"\nFound {n_clusters} clusters + {n_outliers} outliers")
    
    # Create cluster directories
    clusters = {}
    for label in unique_labels:
        cluster_name = f"cluster_{label}"
        cluster_dir = clusters_dir / cluster_name
        cluster_dir.mkdir(exist_ok=True)
        clusters[label] = {
            'dir': cluster_dir,
            'images': [],
            'label': label
        }
    
    # Assign images to clusters
    assignments = {}
    for i, (label, metadata) in enumerate(zip(labels, metadata_list)):
        # Use absolute path for the source image
        img_path = Path('output') / metadata['image_path']
        abs_img_path = img_path.resolve()
        
        # Create symlink
        cluster_dir = clusters[label]['dir']
        link_path = cluster_dir / img_path.name
        
        # Remove existing symlink if any
        if link_path.exists() or link_path.is_symlink():
            link_path.unlink()
        
        # Create absolute symlink (more reliable than relative)
        try:
            link_path.symlink_to(abs_img_path)
        except Exception as e:
            print(f"Warning: Could not create symlink for {img_path.name}: {e}")
        
        # Store assignment
        assignments[metadata['image_path']] = int(label)
        clusters[label]['images'].append(metadata)
    
    return clusters, assignments, n_clusters, n_outliers


def calculate_cluster_stats(clusters, embeddings, labels):
    """Calculate statistics for each cluster"""
    stats = {}
    
    for label, cluster_data in clusters.items():
        # Convert numpy int64 to Python int for JSON serialization
        label = int(label)
        cluster_name = f"cluster_{label}"
        images = cluster_data['images']
        
        if not images:
            continue
        
        # Get embeddings for this cluster
        cluster_mask = labels == label
        cluster_embeddings = embeddings[cluster_mask]
        
        # Calculate centroid
        centroid = np.mean(cluster_embeddings, axis=0)
        
        # Calculate average distance to centroid
        distances = np.linalg.norm(cluster_embeddings - centroid, axis=1)
        avg_distance = float(np.mean(distances))
        
        # Calculate face detection rate
        with_face = sum(1 for img in images if img.get('has_face', False))
        face_rate = with_face / len(images) if images else 0
        
        # Calculate consistency score (inverse of avg distance)
        # Lower distance = higher consistency
        consistency = max(0, 1 - avg_distance)
        
        stats[cluster_name] = {
            'label': label,
            'num_images': len(images),
            'avg_distance_to_centroid': round(avg_distance, 4),
            'consistency_score': round(consistency, 4),
            'face_detection_rate': round(face_rate, 4),
            'images_with_faces': with_face,
            'directory': str(cluster_data['dir'])
        }
    
    return stats


def main():
    parser = argparse.ArgumentParser(
        description='Cluster images based on face-focused embeddings'
    )
    parser.add_argument(
        '--character', '-c',
        required=True,
        help='Character name (e.g., hikariAI)'
    )
    parser.add_argument(
        '--min-cluster-size',
        type=int,
        default=10,
        help='Minimum images per cluster (default: 10)'
    )
    parser.add_argument(
        '--min-samples',
        type=int,
        default=5,
        help='Minimum samples for core points (default: 5)'
    )
    
    args = parser.parse_args()
    
    character = args.character
    embedding_dir = Path('embeddings') / character
    
    print("="*60)
    print(f"Clustering Images: {character}")
    print("="*60)
    
    # Load embeddings
    embeddings, metadata_list = load_embeddings(embedding_dir)
    
    if len(embeddings) < args.min_cluster_size * 2:
        print(f"Error: Not enough images for clustering")
        print(f"  Found: {len(embeddings)}")
        print(f"  Need at least: {args.min_cluster_size * 2}")
        sys.exit(1)
    
    # Perform clustering
    labels, clusterer = perform_clustering(
        embeddings,
        min_cluster_size=args.min_cluster_size,
        min_samples=args.min_samples
    )
    
    # Create cluster structure
    clusters, assignments, n_clusters, n_outliers = create_cluster_structure(
        character, labels, metadata_list, args.min_cluster_size
    )
    
    # Calculate statistics
    stats = calculate_cluster_stats(clusters, embeddings, labels)
    
    # Save assignments
    assignments_path = Path('output') / character / 'clusters' / 'assignments.json'
    with open(assignments_path, 'w') as f:
        json.dump(assignments, f, indent=2)
    
    # Save clusters
    clusters_data = {}
    for label, cluster_data in clusters.items():
        cluster_name = f"cluster_{label}"
        clusters_data[cluster_name] = {
            'label': int(label),
            'num_images': len(cluster_data['images']),
            'images': [m['image_path'] for m in cluster_data['images']]
        }
    
    clusters_path = Path('output') / character / 'clusters' / 'clusters.json'
    with open(clusters_path, 'w') as f:
        json.dump(clusters_data, f, indent=2)
    
    # Save stats
    stats_path = Path('output') / character / 'clusters' / 'stats.json'
    with open(stats_path, 'w') as f:
        json.dump(stats, f, indent=2)
    
    # Create manifest
    manifest = {
        'character': character,
        'total_images': len(embeddings),
        'num_clusters': n_clusters,
        'num_outliers': n_outliers,
        'clustering_params': {
            'min_cluster_size': args.min_cluster_size,
            'min_samples': args.min_samples,
            'algorithm': 'HDBSCAN'
        },
        'clusters_dir': str(Path('output') / character / 'clusters')
    }
    
    manifest_path = Path('output') / character / 'clusters' / 'manifest.json'
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    # Print summary
    print("\n" + "="*60)
    print("CLUSTERING COMPLETE")
    print("="*60)
    print(f"Total images: {len(embeddings)}")
    print(f"Clusters found: {n_clusters}")
    print(f"Outliers (noise): {n_outliers}")
    print(f"\nCluster statistics:")
    print("-"*60)
    
    # Sort clusters by consistency score
    sorted_clusters = sorted(stats.items(), key=lambda x: x[1]['consistency_score'], reverse=True)
    
    for cluster_name, cluster_stats in sorted_clusters:
        label = cluster_stats['label']
        if label == -1:
            print(f"\nCluster {label} (Outliers):")
        else:
            print(f"\nCluster {label}:")
        print(f"  Images: {cluster_stats['num_images']}")
        print(f"  Consistency: {cluster_stats['consistency_score']:.3f}")
        print(f"  Face detection: {cluster_stats['face_detection_rate']*100:.1f}%")
        print(f"  Location: {cluster_stats['directory']}")
    
    print(f"\nClusters saved to: {Path('output') / character / 'clusters'}")
    print("\nNext step: Review clusters and pick the best one")
    print("  Or run: python3 view_clusters.py --character", character)
    print("="*60)


if __name__ == "__main__":
    main()
