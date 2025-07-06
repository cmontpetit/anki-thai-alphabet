#!/usr/bin/env python3
"""
Installation and setup script for Thai Consonants Anki Deck
Handles dependency installation and runs the deck generation
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required Python packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "gTTS"])
        print("✓ gTTS installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing gTTS: {e}")
        return False

def check_gtts():
    """Check if gTTS is available"""
    try:
        import gtts
        return True
    except ImportError:
        return False

def main():
    """Main installation and setup function"""
    print("Thai Consonants Anki Deck - Setup")
    print("=" * 40)
    
    # Check if gTTS is already installed
    if check_gtts():
        print("✓ gTTS is already installed")
    else:
        print("gTTS not found. Installing...")
        if not install_requirements():
            print("\nInstallation failed. Please install manually:")
            print("pip install gTTS")
            return
    
    # Run the main deck generation script
    print("\n" + "=" * 40)
    print("Running deck generation...")
    
    try:
        # Import and run the main script
        from generate_thai_deck import main as run_deck_generation
        run_deck_generation()
    except ImportError as e:
        print(f"Error importing deck generation script: {e}")
        print("Please ensure all files are in the same directory")
    except Exception as e:
        print(f"Error running deck generation: {e}")

if __name__ == "__main__":
    main() 