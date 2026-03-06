#!/usr/bin/env python3
"""
Fix onnxruntime-rocm executable stack issue on Arch Linux

This script clears the executable stack flag from all onnxruntime .so files,
which is required on Arch Linux with hardened kernel (PaX/grsecurity).

Usage:
    python3 scripts/fix_onnxruntime_rocm.py
"""

import subprocess
import sys
from pathlib import Path


def get_onnxruntime_path():
    """Get the path to onnxruntime installation"""
    try:
        import onnxruntime
        return Path(onnxruntime.__path__[0])
    except ImportError:
        print("Error: onnxruntime not installed")
        print("Please install first: pip install onnxruntime-rocm")
        sys.exit(1)


def check_patchelf():
    """Check if patchelf is available"""
    try:
        subprocess.run(['patchelf', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def fix_so_files(onnxruntime_path):
    """Clear executable stack flag on all .so files"""
    capi_dir = onnxruntime_path / 'capi'
    
    if not capi_dir.exists():
        print(f"Error: capi directory not found at {capi_dir}")
        sys.exit(1)
    
    so_files = list(capi_dir.glob('*.so'))
    
    if not so_files:
        print("No .so files found to fix")
        return
    
    print(f"Found {len(so_files)} .so files to fix")
    print("")
    
    fixed_count = 0
    for so_file in so_files:
        print(f"Fixing: {so_file.name}")
        try:
            subprocess.run(
                ['patchelf', '--clear-execstack', str(so_file)],
                check=True,
                capture_output=True
            )
            fixed_count += 1
        except subprocess.CalledProcessError as e:
            print(f"  Error: {e}")
    
    print("")
    print(f"✓ Fixed {fixed_count}/{len(so_files)} files")


def test_import():
    """Test that onnxruntime can be imported"""
    print("")
    print("Testing import...")
    try:
        import onnxruntime as ort
        print("✓ onnxruntime imported successfully!")
        print(f"  Version: {ort.__version__}")
        print(f"  Available providers: {ort.get_available_providers()}")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False


def main():
    print("="*60)
    print("Fixing onnxruntime-rocm executable stack issue")
    print("="*60)
    print("")
    
    # Check patchelf
    if not check_patchelf():
        print("Error: patchelf not found")
        print("Please install: sudo pacman -S patchelf")
        sys.exit(1)
    
    print("✓ patchelf is available")
    
    # Get onnxruntime path
    try:
        ort_path = get_onnxruntime_path()
        print(f"✓ Found onnxruntime at: {ort_path}")
    except SystemExit:
        sys.exit(1)
    
    # Fix .so files
    print("")
    fix_so_files(ort_path)
    
    # Test import
    if test_import():
        print("")
        print("="*60)
        print("SUCCESS!")
        print("="*60)
        print("\nonnxruntime-rocm is now working with ROCm GPU acceleration.")
        print("You can now run: python3 extract_embeddings.py --character <name>")
    else:
        print("")
        print("="*60)
        print("FAILED")
        print("="*60)
        print("\nThe fix didn't work. Try:")
        print("1. Reinstall onnxruntime-rocm: pip install --force-reinstall onnxruntime-rocm")
        print("2. Check for other errors above")
        print("3. Use CPU version instead: pip install onnxruntime")
        sys.exit(1)


if __name__ == "__main__":
    main()
