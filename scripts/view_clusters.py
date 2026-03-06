#!/usr/bin/env python3
"""
View clustering results and show cluster information

Usage:
    python3 view_clusters.py --character hikariAI
"""

import argparse
import json
import sys
from pathlib import Path


def load_cluster_data(character):
    """Load clustering results"""
    clusters_dir = Path('output') / character / 'clusters'
    
    # Check if clustering was done
    manifest_path = clusters_dir / 'manifest.json'
    if not manifest_path.exists():
        print(f"Error: No clustering results found for {character}")
        print(f"Run: python3 cluster_images.py --character {character}")
        sys.exit(1)
    
    with open(manifest_path) as f:
        manifest = json.load(f)
    
    # Load stats
    stats_path = clusters_dir / 'stats.json'
    with open(stats_path) as f:
        stats = json.load(f)
    
    return manifest, stats


def display_results(character, manifest, stats):
    """Display clustering results"""
    
    print("="*60)
    print(f"Image Clustering Results: {character}")
    print("="*60)
    
    print(f"\nTotal Images Processed: {manifest['total_images']}")
    print(f"Clusters Found: {manifest['num_clusters']}")
    print(f"Outliers (Noise): {manifest['num_outliers']}")
    
    print(f"\nClustering Parameters:")
    print(f"  Algorithm: {manifest['clustering_params']['algorithm']}")
    print(f"  Min cluster size: {manifest['clustering_params']['min_cluster_size']}")
    print(f"  Min samples: {manifest['clustering_params']['min_samples']}")
    
    # Sort clusters by consistency score (highest first)
    sorted_clusters = sorted(
        stats.items(),
        key=lambda x: x[1]['consistency_score'],
        reverse=True
    )
    
    print("\n" + "="*60)
    print("CLUSTER DETAILS")
    print("="*60)
    
    best_cluster = None
    best_score = 0
    
    for cluster_name, cluster_stats in sorted_clusters:
        label = cluster_stats['label']
        
        if label == -1:
            print(f"\n📦 CLUSTER {label} (OUTLIERS)")
            print("-"*60)
        else:
            print(f"\n⭐ CLUSTER {label}")
            print("-"*60)
        
        print(f"  Images: {cluster_stats['num_images']}")
        print(f"  Consistency Score: {cluster_stats['consistency_score']:.3f}")
        print(f"  Face Detection Rate: {cluster_stats['face_detection_rate']*100:.1f}%")
        print(f"  Images with Faces: {cluster_stats['images_with_faces']}/{cluster_stats['num_images']}")
        print(f"  Location: {cluster_stats['directory']}")
        
        if label != -1 and cluster_stats['consistency_score'] > best_score:
            best_score = cluster_stats['consistency_score']
            best_cluster = label
    
    # Recommendation
    if best_cluster is not None:
        print("\n" + "="*60)
        print("RECOMMENDATION")
        print("="*60)
        print(f"\n🏆 Best Cluster: Cluster {best_cluster}")
        print(f"   Highest consistency score: {best_score:.3f}")
        print(f"   This cluster has the most consistent character appearance")
        print(f"\n   View at: output/{character}/clusters/cluster_{best_cluster}/")
    
    # Instructions
    print("\n" + "="*60)
    print("NEXT STEPS")
    print("="*60)
    print("\n1. Browse clusters using your file manager:")
    print(f"   output/{character}/clusters/")
    print("\n2. Review each cluster folder:")
    print("   - cluster_0/, cluster_1/, etc. = Different character styles")
    print("   - cluster_-1/ = Outliers (review separately)")
    print("\n3. Pick your favorite cluster based on:")
    print("   - Face consistency")
    print("   - Art style coherence")
    print("   - Overall character likeness")
    print("\n4. Manually curate 30-40 images from your chosen cluster")
    print("   Or continue to automated dataset creation")
    print("="*60)


def list_cluster_images(character, cluster_id, max_show=10):
    """List images in a specific cluster"""
    clusters_dir = Path('output') / character / 'clusters'
    cluster_dir = clusters_dir / f"cluster_{cluster_id}"
    
    if not cluster_dir.exists():
        print(f"Error: Cluster {cluster_id} not found")
        return
    
    # Load clusters.json to get full paths
    clusters_path = clusters_dir / 'clusters.json'
    with open(clusters_path) as f:
        clusters_data = json.load(f)
    
    cluster_key = f"cluster_{cluster_id}"
    if cluster_key not in clusters_data:
        print(f"Error: No data for cluster {cluster_id}")
        return
    
    images = clusters_data[cluster_key]['images']
    
    print(f"\nCluster {cluster_id} - {len(images)} images:")
    print("-"*60)
    
    for i, img_path in enumerate(images[:max_show]):
        print(f"  {i+1}. {img_path}")
    
    if len(images) > max_show:
        print(f"  ... and {len(images) - max_show} more")
    
    print(f"\nFull cluster: output/{character}/clusters/cluster_{cluster_id}/")


def main():
    parser = argparse.ArgumentParser(
        description='View image clustering results'
    )
    parser.add_argument(
        '--character', '-c',
        required=True,
        help='Character name (e.g., hikariAI)'
    )
    parser.add_argument(
        '--list-cluster', '-l',
        type=int,
        help='List images in a specific cluster ID'
    )
    parser.add_argument(
        '--max-show',
        type=int,
        default=10,
        help='Max images to show when listing cluster (default: 10)'
    )
    
    args = parser.parse_args()
    
    character = args.character
    
    # Load clustering data
    manifest, stats = load_cluster_data(character)
    
    # Either show full results or list specific cluster
    if args.list_cluster is not None:
        list_cluster_images(character, args.list_cluster, args.max_show)
    else:
        display_results(character, manifest, stats)


if __name__ == "__main__":
    main()
