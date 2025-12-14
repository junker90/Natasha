#!/usr/bin/env python3
"""
File Listing Utility for Natasha Case Repository

This script lists all files and directories in a specified folder.
Usage: python list_files.py [folder_path]
"""

import sys
from pathlib import Path


def list_files(folder_path="."):
    """
    List all files and directories in the specified folder.
    
    Args:
        folder_path (str): Path to the folder to list (default: current directory)
    """
    try:
        # Convert to Path object for better handling
        path = Path(folder_path).resolve()
        
        if not path.exists():
            print(f"Error: Path '{folder_path}' does not exist.")
            return 1
        
        if not path.is_dir():
            print(f"Error: '{folder_path}' is not a directory.")
            return 1
        
        # Print header
        print(f"\n{'='*80}")
        print(f"Listing files in: {path}")
        print(f"{'='*80}\n")
        
        # Collect and sort directories and files separately
        directories = []
        files = []
        
        for item in path.iterdir():
            if item.is_dir():
                directories.append(item)
            else:
                files.append(item)
        
        if not directories and not files:
            print("(Empty directory)")
            return 0
        
        # Sort each category alphabetically (case-insensitive)
        directories.sort(key=lambda x: x.name.lower())
        files.sort(key=lambda x: x.name.lower())
        
        # Print directories first
        if directories:
            print("DIRECTORIES:")
            print("-" * 80)
            for dir_item in directories:
                print(f"  📁 {dir_item.name}/")
            print()
        
        # Print files
        if files:
            print("FILES:")
            print("-" * 80)
            for file_item in files:
                size = file_item.stat().st_size
                size_str = format_size(size)
                print(f"  📄 {file_item.name:<50} ({size_str})")
            print()
        
        # Print summary
        print(f"{'='*80}")
        print(f"Total: {len(directories)} directories, {len(files)} files")
        print(f"{'='*80}\n")
        
        return 0
        
    except PermissionError:
        print(f"Error: Permission denied to access '{folder_path}'.")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1


def format_size(size_bytes):
    """
    Format file size in human-readable format using binary units.
    
    Args:
        size_bytes (int): Size in bytes
        
    Returns:
        str: Formatted size string
    """
    for unit in ['B', 'KiB', 'MiB', 'GiB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TiB"


def main():
    """Main entry point for the script."""
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
    else:
        folder_path = "."
    
    sys.exit(list_files(folder_path))


if __name__ == "__main__":
    main()
