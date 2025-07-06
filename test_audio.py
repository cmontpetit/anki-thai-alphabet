#!/usr/bin/env python3
"""
Test script for gTTS audio generation
Generates audio files for a few Thai consonants to test the functionality
"""

try:
    from gtts import gTTS
    import os
    import time
    
    print("Testing gTTS audio generation...")
    
    # Test consonants
    test_consonants = [
        ("ก", "กอ ไก่"),
        ("ข", "ขอ ไข่"),
        ("ด", "ดอ เด็ก")
    ]
    
    # Create test sounds directory
    test_dir = "test_sounds"
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
        print(f"Created test directory: {test_dir}")
    
    print(f"Generating test audio files for {len(test_consonants)} consonants...")
    
    for consonant, name in test_consonants:
        try:
            filename = f"{test_dir}/{consonant}_test.mp3"
            
            # Create gTTS object with Thai language
            tts = gTTS(text=name, lang='th', slow=False)
            
            # Save the audio file
            tts.save(filename)
            
            print(f"✓ {consonant} - Generated {filename}")
            
            # Small delay
            time.sleep(0.5)
            
        except Exception as e:
            print(f"✗ {consonant} - Error: {e}")
    
    print(f"\nTest complete! Check the '{test_dir}/' directory for generated files.")
    print("If this works, you can run the full script: python generate_thai_deck.py")
    
except ImportError:
    print("Error: gTTS is not installed.")
    print("To install gTTS, run: pip install gTTS")
    print("Or install all requirements: pip install -r requirements.txt") 