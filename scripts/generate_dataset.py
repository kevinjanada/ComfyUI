#!/usr/bin/env python3
"""
Dataset Generation Automation for ComfyUI Character Training

Automates the generation of 200 images (for later curation to 30-40)
using workflow JSON files with random seeds.

Usage:
    python3 generate_dataset.py --config configs/hikariAI.yaml
    python3 generate_dataset.py --config configs/hikariAI.yaml --resume
    python3 generate_dataset.py --status
"""

import argparse
import json
import os
import random
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime, timedelta


class ComfyUIClient:
    """Client for interacting with ComfyUI API"""
    
    def __init__(self, host="127.0.0.1", port=8188):
        self.host = host
        self.port = port
        self.base_url = f"http://{host}:{port}"
    
    def check_connection(self):
        """Check if ComfyUI server is running"""
        try:
            req = urllib.request.Request(f"{self.base_url}/system_stats")
            with urllib.request.urlopen(req, timeout=5) as response:
                return True
        except:
            return False
    
    def queue_prompt(self, workflow):
        """Queue a workflow for execution"""
        data = json.dumps({"prompt": workflow}).encode('utf-8')
        req = urllib.request.Request(
            f"{self.base_url}/prompt",
            data=data,
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read())
    
    def get_history(self, prompt_id):
        """Get execution history for a prompt"""
        req = urllib.request.Request(f"{self.base_url}/history/{prompt_id}")
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read())
    
    def is_prompt_complete(self, prompt_id):
        """Check if a prompt has completed execution"""
        try:
            history = self.get_history(prompt_id)
            if prompt_id in history:
                outputs = history[prompt_id].get('outputs', {})
                # Check if any node has images output
                for node_id, node_output in outputs.items():
                    if 'images' in node_output:
                        return True
            return False
        except:
            return False


class DatasetGenerator:
    """Main class for generating character datasets"""
    
    def __init__(self, config_path, resume=False):
        self.config = self.load_config(config_path)
        self.client = ComfyUIClient(
            host=self.config['comfyui']['host'],
            port=self.config['comfyui']['port']
        )
        self.state_file = Path(self.config['character']['output_dir']) / ".generation_state.json"
        self.state = self.load_state() if resume else self.create_new_state()
        
    def load_config(self, config_path):
        """Load YAML config file"""
        # Simple YAML parser for our specific format
        config = {}
        current_section = None
        current_subsection = None
        
        with open(config_path, 'r') as f:
            for line in f:
                line = line.rstrip()
                if not line or line.startswith('#'):
                    continue
                
                # Check for section headers
                if line.endswith(':') and not line.strip().startswith('-'):
                    indent = len(line) - len(line.lstrip())
                    key = line.strip().rstrip(':')
                    
                    if indent == 0:
                        current_section = key
                        config[current_section] = {}
                        current_subsection = None
                    elif indent == 2:
                        current_subsection = key
                        config[current_section][current_subsection] = {}
                    elif indent == 4:
                        config[current_section][current_subsection][key] = {}
                
                # Check for key-value pairs
                elif ':' in line and not line.strip().startswith('-'):
                    indent = len(line) - len(line.lstrip())
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # Remove inline comments
                    if '#' in value:
                        value = value.split('#')[0].strip()
                    
                    # Strip quotes if present
                    if (value.startswith('"') and value.endswith('"')) or \
                       (value.startswith("'") and value.endswith("'")):
                        value = value[1:-1]
                    
                    # Try to convert value
                    if value.isdigit():
                        value = int(value)
                    elif value.lower() == 'true':
                        value = True
                    elif value.lower() == 'false':
                        value = False
                    
                    if indent == 2 and current_section:
                        config[current_section][key] = value
                    elif indent == 4 and current_subsection:
                        config[current_section][current_subsection][key] = value
                    elif indent == 6:
                        # Deep nesting
                        if isinstance(config[current_section][current_subsection], dict):
                            config[current_section][current_subsection][key] = value
        
        return config
    
    def create_new_state(self):
        """Create initial state"""
        return {
            'character': self.config['character']['name'],
            'started_at': datetime.now().isoformat(),
            'completed': False,
            'poses': {}
        }
    
    def load_state(self):
        """Load generation state from file"""
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return self.create_new_state()
    
    def save_state(self):
        """Save generation state to file"""
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def load_workflow(self, workflow_path, output_subdir=None):
        """Load workflow JSON file and convert to API format if needed"""
        with open(workflow_path, 'r') as f:
            workflow = json.load(f)
        
        # Check if it's already in API format
        if self.is_api_format(workflow):
            return workflow
        
        # Convert from visual format to API format
        print("Converting workflow from visual format to API format...")
        return self.convert_to_api_format(workflow, output_subdir)
    
    def is_api_format(self, workflow):
        """Check if workflow is already in API format"""
        # API format has numeric string keys and class_type
        for key in list(workflow.keys())[:3]:
            if isinstance(key, str) and key.isdigit():
                if isinstance(workflow[key], dict) and 'class_type' in workflow[key]:
                    return True
        return False
    
    def convert_to_api_format(self, workflow, output_subdir=None):
        """Convert visual workflow format to API format"""
        if 'nodes' not in workflow:
            print("Warning: Unknown workflow format, returning as-is")
            return workflow
        
        api_workflow = {}
        node_id_map = {}  # Map visual node IDs to API node IDs
        
        # First pass: create API nodes
        for node in workflow['nodes']:
            node_id = str(node['id'])
            node_id_map[node['id']] = node_id
            
            node_type = node.get('type', 'Unknown')
            
            # Initialize inputs dict
            inputs = {}
            
            # Map widget values to inputs based on node type
            widgets = node.get('widgets_values', [])
            
            if node_type == 'KSampler':
                if len(widgets) >= 7:
                    inputs['seed'] = widgets[0]
                    inputs['control_after_generate'] = widgets[1]
                    inputs['steps'] = widgets[2]
                    inputs['cfg'] = widgets[3]
                    inputs['sampler_name'] = widgets[4]
                    inputs['scheduler'] = widgets[5]
                    inputs['denoise'] = widgets[6]
            
            elif node_type == 'CheckpointLoaderSimple':
                if len(widgets) >= 1:
                    inputs['ckpt_name'] = widgets[0]
            
            elif node_type == 'CLIPTextEncode':
                if len(widgets) >= 1:
                    inputs['text'] = widgets[0]
            
            elif node_type == 'EmptyLatentImage':
                if len(widgets) >= 3:
                    inputs['width'] = widgets[0]
                    inputs['height'] = widgets[1]
                    inputs['batch_size'] = widgets[2]
            
            elif node_type == 'VAEDecode':
                pass  # No widgets, only inputs from links
            
            elif node_type == 'SaveImage':
                if len(widgets) >= 1:
                    prefix = widgets[0]
                    # Add subdirectory to filename prefix
                    if output_subdir:
                        prefix = f"{output_subdir}/{prefix}"
                    inputs['filename_prefix'] = prefix
            
            elif node_type == 'PreviewImage':
                pass  # No widgets
            
            elif node_type == 'Note':
                # Skip Note nodes - they're UI-only
                continue
            
            api_workflow[node_id] = {
                'class_type': node_type,
                'inputs': inputs
            }
        
        # Second pass: resolve links
        if 'links' in workflow:
            for link in workflow['links']:
                # link format: [link_id, origin_node_id, origin_slot, target_node_id, target_slot, type]
                if len(link) >= 5:
                    origin_id = link[1]
                    origin_slot = link[2]
                    target_id = link[3]
                    target_slot = link[4]
                    
                    origin_node_id = str(origin_id)
                    target_node_id = str(target_id)
                    
                    if target_node_id not in api_workflow:
                        continue
                    
                    target_node = api_workflow[target_node_id]
                    target_type = target_node['class_type']
                    
                    # Map slot index to input name based on node type
                    input_name = self.get_input_name(target_type, target_slot)
                    if input_name:
                        target_node['inputs'][input_name] = [origin_node_id, origin_slot]
        
        return api_workflow
    
    def get_input_name(self, node_type, slot_index):
        """Get input parameter name for a node type and slot index"""
        input_maps = {
            'KSampler': {0: 'model', 1: 'positive', 2: 'negative', 3: 'latent_image'},
            'VAEDecode': {0: 'samples', 1: 'vae'},
            'CLIPTextEncode': {0: 'clip'},
            'SaveImage': {0: 'images'},
            'PreviewImage': {0: 'images'},
        }
        
        if node_type in input_maps:
            return input_maps[node_type].get(slot_index)
        
        # Generic fallback
        return f"input_{slot_index}"
    
    def modify_seed(self, workflow, seed):
        """Modify the seed in workflow (supports both API and visual formats)"""
        # API format: numeric keys with class_type
        for node_id, node in workflow.items():
            if isinstance(node, dict):
                if node.get('class_type') == 'KSampler':
                    if 'inputs' in node:
                        node['inputs']['seed'] = seed
                        return workflow
        
        # Visual format: has nodes array
        if 'nodes' in workflow:
            for node in workflow['nodes']:
                if node.get('type') == 'KSampler':
                    widgets = node.get('widgets_values', [])
                    if len(widgets) > 0:
                        widgets[0] = seed
                        return workflow
        
        print(f"Warning: Could not find KSampler node to modify seed")
        return workflow
    
    def calculate_batches(self, total_needed, batch_size):
        """Calculate number of batches needed"""
        return (total_needed + batch_size - 1) // batch_size
    
    def format_eta(self, seconds):
        """Format seconds as human-readable time"""
        return str(timedelta(seconds=int(seconds)))
    
    def print_progress(self, pose_name, current_batch, total_batches, images_done, total_images, start_time):
        """Print progress bar"""
        elapsed = time.time() - start_time
        if images_done > 0:
            avg_time_per_image = elapsed / images_done
            remaining_images = total_images - images_done
            eta_seconds = avg_time_per_image * remaining_images
            eta = self.format_eta(eta_seconds)
        else:
            eta = "calculating..."
        
        progress = (images_done / total_images) * 100
        bar_width = 40
        filled = int(bar_width * images_done / total_images)
        bar = '█' * filled + '░' * (bar_width - filled)
        
        print(f"\r[{pose_name}] Batch {current_batch}/{total_batches} | Images: {images_done}/{total_images} | ETA: {eta}")
        print(f"[{bar}] {progress:.1f}%", end='', flush=True)
    
    def generate_pose(self, pose_name, workflow_path, target_images, batch_size):
        """Generate images for a specific pose"""
        print(f"\n{'='*60}")
        print(f"Generating {pose_name.upper()} - Target: {target_images} images")
        print(f"{'='*60}\n")
        
        # Check if this pose was already completed
        if pose_name in self.state['poses']:
            completed = self.state['poses'][pose_name].get('completed', 0)
            if completed >= target_images:
                print(f"✓ {pose_name} already completed ({completed}/{target_images} images)")
                return
            print(f"Resuming {pose_name}: {completed}/{target_images} images already generated")
        else:
            self.state['poses'][pose_name] = {'completed': 0, 'batches_done': 0}
            completed = 0
        
        # Load workflow with output subdirectory for organized saving
        output_subdir = f"{self.config['character']['name']}/{len(self.state['poses']):02d}_{pose_name}"
        workflow = self.load_workflow(workflow_path, output_subdir)
        
        # Calculate remaining
        remaining = target_images - completed
        total_batches = self.calculate_batches(target_images, batch_size)
        batches_done = self.state['poses'][pose_name].get('batches_done', 0)
        
        # Create output directory
        output_dir = Path(self.config['character']['output_dir']) / f"{len(self.state['poses']):02d}_{pose_name}"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        start_time = time.time()
        
        # Generate batches
        for batch_num in range(batches_done + 1, total_batches + 1):
            current_batch_size = min(batch_size, remaining)
            
            # Generate random seed
            seed = random.randint(0, 2**32 - 1)
            
            # Modify workflow with new seed
            modified_workflow = self.modify_seed(workflow.copy(), seed)
            
            # Queue prompt
            try:
                print(f"\nQueueing batch {batch_num}/{total_batches} (seed: {seed})...")
                response = self.client.queue_prompt(modified_workflow)
                prompt_id = response.get('prompt_id')
                
                if not prompt_id:
                    print(f"✗ Failed to queue batch {batch_num}")
                    continue
                
                # Wait for completion
                check_interval = self.config['comfyui'].get('check_interval', 5)
                print(f"Waiting for completion...")
                
                while True:
                    time.sleep(check_interval)
                    if self.client.is_prompt_complete(prompt_id):
                        break
                    print(".", end='', flush=True)
                
                print(f"\n✓ Batch {batch_num} completed ({current_batch_size} images)")
                
                # Update state
                completed += current_batch_size
                remaining -= current_batch_size
                self.state['poses'][pose_name]['completed'] = completed
                self.state['poses'][pose_name]['batches_done'] = batch_num
                self.save_state()
                
                # Show progress
                self.print_progress(pose_name, batch_num, total_batches, completed, target_images, start_time)
                
            except Exception as e:
                print(f"\n✗ Error in batch {batch_num}: {e}")
                print("Saving state and continuing...")
                self.save_state()
                continue
        
        print(f"\n\n✓ {pose_name.upper()} complete! Generated {completed}/{target_images} images")
        print(f"  Output: {output_dir}")
    
    def run(self):
        """Main generation loop"""
        print("="*60)
        print(f"Dataset Generation: {self.config['character']['name']}")
        print("="*60)
        
        # Check ComfyUI connection
        print("\nChecking ComfyUI connection...")
        if not self.client.check_connection():
            print("✗ ERROR: Cannot connect to ComfyUI!")
            print(f"  Tried: {self.client.base_url}")
            print("\nPlease make sure ComfyUI is running:")
            print("  python main.py --listen 0.0.0.0 --port 8188")
            sys.exit(1)
        print("✓ ComfyUI is running")
        
        # Get distribution
        distribution = self.config['generation']['distribution']
        workflows = self.config['workflows']
        batch_size = self.config['generation']['batch_size']
        
        # Generate each pose sequentially
        pose_order = ['portrait', 'standing', 'action']  # Order matters for consistency
        
        for pose_name in pose_order:
            if pose_name not in distribution or pose_name not in workflows:
                print(f"Skipping {pose_name} (not configured)")
                continue
            
            target = distribution[pose_name]
            workflow_path = workflows[pose_name]
            
            # Verify workflow exists
            if not Path(workflow_path).exists():
                print(f"✗ ERROR: Workflow not found: {workflow_path}")
                continue
            
            self.generate_pose(pose_name, workflow_path, target, batch_size)
        
        # Mark as complete
        self.state['completed'] = True
        self.state['completed_at'] = datetime.now().isoformat()
        self.save_state()
        
        # Print summary
        print("\n" + "="*60)
        print("DATASET GENERATION COMPLETE!")
        print("="*60)
        total_images = sum(pose.get('completed', 0) for pose in self.state['poses'].values())
        print(f"Total images generated: {total_images}")
        print(f"Output directory: {self.config['character']['output_dir']}")
        print("\nNext step: Manually curate the 30-40 best images for LoRA training")
        print("="*60)


def main():
    parser = argparse.ArgumentParser(
        description='Automate dataset generation for ComfyUI character training'
    )
    parser.add_argument(
        '--config', '-c',
        required=True,
        help='Path to YAML config file'
    )
    parser.add_argument(
        '--resume', '-r',
        action='store_true',
        help='Resume interrupted generation'
    )
    parser.add_argument(
        '--status', '-s',
        action='store_true',
        help='Show generation status'
    )
    
    args = parser.parse_args()
    
    if args.status:
        # Show status
        if not Path(args.config).exists():
            print(f"Config not found: {args.config}")
            sys.exit(1)
        
        generator = DatasetGenerator(args.config, resume=False)
        print(f"\nStatus for: {generator.config['character']['name']}")
        print("-" * 40)
        
        if generator.state['poses']:
            total_completed = 0
            total_target = 0
            for pose_name, data in generator.state['poses'].items():
                completed = data.get('completed', 0)
                target = generator.config['generation']['distribution'].get(pose_name, 0)
                total_completed += completed
                total_target += target
                status = "✓" if completed >= target else "○"
                print(f"{status} {pose_name}: {completed}/{target}")
            
            print("-" * 40)
            print(f"Total: {total_completed}/{total_target} images")
            
            if generator.state.get('completed'):
                print("\n✓ Generation completed!")
        else:
            print("No generation has started yet")
        
        return
    
    # Run generation
    if not Path(args.config).exists():
        print(f"Config not found: {args.config}")
        sys.exit(1)
    
    generator = DatasetGenerator(args.config, resume=args.resume)
    
    if args.resume:
        print("Resuming from previous state...")
    
    try:
        generator.run()
    except KeyboardInterrupt:
        print("\n\n⚠ Interrupted by user")
        print("Progress has been saved. Use --resume to continue.")
        sys.exit(0)


if __name__ == "__main__":
    main()
