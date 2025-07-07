#!/usr/bin/env python3
"""
Thai Consonants Anki Deck Generator
Generates a complete deck of Thai consonant cards for Anki
"""

import csv
import os
from gtts import gTTS
import time

# Thai consonants data
# Format: (consonant, name, paiboon_pronunciation_with_tone, class, initial_sound, final_sound, meaning, notes)
THAI_CONSONANTS = [
    ("ค", "คอ ควาย", "khaawᴹ khwaaiᴹ", "Low", "kh-", "-k", "buffalo", "Low-class consonant."),
    ("ฅ", "ฅอ คน", "khaawᴹ khohnᴹ", "Low", "kh-", "-k", "person", "Rare/obsolete. Low-class consonant."),
    ("ฆ", "ฆอ ระฆัง", "khaawᴹ raᴴ kangᴹ", "Low", "kh-", "-k", "bell", "Low-class consonant."),
    ("ง", "งอ งู", "ngaawᴹ nguuᴹ", "Low", "ng-", "-ng", "snake", "Low-class consonant."),
    ("ช", "ชอ ช้าง", "chaawᴹ changᴴ", "Low", "ch-", "-t", "elephant", "Low-class consonant."),
    ("ซ", "ซอ โซ่", "saawᴹ sohᶠ", "Low", "s-", "-t", "chain", "Low-class consonant."),
    ("ฌ", "ฌอ เฌอ", "chaawᴹ chuuhrᴹ", "Low", "ch-", "-t", "tree", "Low-class consonant."),
    ("ญ", "ญอ หญิง", "yaawᴹ yingᴿ", "Low", "y-", "-n", "woman", "Low-class consonant."),
    ("ฑ", "ฑอ มณโฑ", "thaawᴹ mohnᴹ thohᴹ", "Low", "th-", "-t", "Mandodari", "Low-class consonant."),
    ("ฒ", "ฒอ ผู้เฒ่า", "thaawᴹ phuuᶠ thaoᶠ", "Low", "th-", "-t", "elder", "Low-class consonant."),
    ("ณ", "ณอ เณร", "naawᴹ naehnᴹ", "Low", "n-", "-n", "novice monk", "Low-class consonant."),
    ("ท", "ทอ ทหาร", "thaawᴹ tha-haanᴿ", "Low", "th-", "-t", "soldier", "Low-class consonant."),
    ("ธ", "ธอ ธง", "thaawᴹ thongᴹ", "Low", "th-", "-t", "flag", "Low-class consonant."),
    ("น", "นอ หนู", "naawᴹ nuuᴿ", "Low", "n-", "-n", "mouse", "Low-class consonant."),
    ("พ", "พอ พาน", "phaawᴹ phaanᴹ", "Low", "ph-", "-p", "tray", "Low-class consonant."),
    ("ฟ", "ฟอ ฟัน", "faawᴹ fanᴹ", "Low", "f-", "-p", "teeth", "Low-class consonant."),
    ("ภ", "ภอ สำเภา", "phaawᴹ samᴿ paoᴹ", "Low", "ph-", "-p", "junk", "Low-class consonant."),
    ("ม", "มอ ม้า", "maawᴹ maaᴴ", "Low", "m-", "-m", "horse", "Low-class consonant."),
    ("ย", "ยอ ยักษ์", "yaawᴹ yakᴴ", "Low", "y-", "-n", "giant", "Low-class consonant."),
    ("ร", "รอ เรือ", "raawᴹ reuuaᴹ", "Low", "r-", "-n", "boat", "Low-class consonant."),
    ("ล", "ลอ ลิง", "laawᴹ lingᴹ", "Low", "l-", "-n", "monkey", "Low-class consonant."),
    ("ว", "วอ แหวน", "waawᴹ waaenᴿ", "Low", "w-", "-n", "ring", "Low-class consonant."),
    ("ฬ", "ฬอ จุฬา", "laawᴹ jooᴸ laaᴹ", "Low", "l-", "-n", "kite", "Low-class consonant."),
    ("ฮ", "ฮอ นกฮูก", "haawᴹ nohkᴴ huukᶠ", "Low", "h-", "-k", "owl", "Low-class consonant."),
    ("ก", "กอ ไก่", "gaawᴹ gaiᴸ", "Mid", "g-", "-k", "chicken", "Mid-class consonant."),
    ("จ", "จอ จาน", "jaawᴹ jaanᴹ", "Mid", "j-", "-n", "plate", "Mid-class consonant."),
    ("ฎ", "ฎอ ชฎา", "daawᴹ cha-daaᴹ", "Mid", "d-", "-n", "headdress", "Mid-class consonant."),
    ("ฏ", "ฏอ ปฏัก", "dtaawᴹ bpaᴸ dtakᴸ", "Mid", "dt-", "-k", "goad", "Mid-class consonant."),
    ("ด", "ดอ เด็ก", "daawᴹ dekᴸ", "Mid", "d-", "-k", "child", "Mid-class consonant."),
    ("ต", "ตอ เต่า", "dtaawᴹ dtaoᴸ", "Mid", "dt-", "-k", "turtle", "Mid-class consonant."),
    ("บ", "บอ ใบไม้", "baawᴹ baiᴹ maiᴴ", "Mid", "b-", "-p", "leaf", "Mid-class consonant."),
    ("ป", "ปอ ปลา", "bpaawᴹ bplaaᴹ", "Mid", "bp-", "-p", "fish", "Mid-class consonant."),
    ("อ", "ออ อ่าง", "aawᴹ aangᴹ", "Mid", "ʔ-", "-", "basin", "Mid-class consonant."),
    ("ข", "ขอ ไข่", "khaawᴿ khaiᴸ", "High", "kh-", "-k", "egg", "High-class consonant."),
    ("ฃ", "ฃอ ขวด", "khaawᴿ khuaatᴸ", "High", "kh-", "-k", "bottle", "Rare/obsolete. High-class consonant."),
    ("ฉ", "ฉอ ฉิ่ง", "chaawᴿ chingᴸ", "High", "ch-", "-", "cymbals", "High-class consonant."),
    ("ฐ", "ฐอ ฐาน", "thaawᴿ thaanᴿ", "High", "th-", "-t", "base", "High-class consonant."),
    ("ถ", "ถอ ถุง", "thaawᴿ thoongᴿ", "High", "th-", "-t", "bag", "High-class consonant."),
    ("ผ", "ผอ ผึ้ง", "phaawᴿ pheungᶠ", "High", "ph-", "-", "bee", "High-class consonant."),
    ("ฝ", "ฝอ ฝา", "faawᴿ faaᴿ", "High", "f-", "-", "lid", "High-class consonant."),
    ("ศ", "ศอ ศาลา", "saawᴿ saaᴿ laaᴹ", "High", "s-", "-t", "pavilion", "High-class consonant."),
    ("ษ", "ษอ ฤาษี", "saawᴿ reuuᴹ seeᴿ", "High", "s-", "-t", "hermit", "High-class consonant."),
    ("ส", "สอ เสือ", "saawᴿ seuuaᴿ", "High", "s-", "-t", "tiger", "High-class consonant."),
    ("ห", "หอ หีบ", "haawᴿ heepᴸ", "High", "h-", "-", "box", "High-class consonant.")
]

def create_tsv_deck():
    """Create a TSV file for Anki import (no header row, mobile-friendly em padding)"""
    with open('thai_consonants.tsv', 'w', newline='', encoding='utf-8') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t', quoting=csv.QUOTE_NONE, escapechar='\\')
        # No header row
        for consonant, name, pronunciation, consonant_class, initial, final, meaning, notes in THAI_CONSONANTS:
            back_content = (
                f"<table style='margin: auto; border-collapse: collapse; text-align: center;'>"
                f"<tr><td colspan='2' style='text-align: center; padding: 0.7em;'>{name}</td></tr>"
                f"<tr><td colspan='2' style='text-align: center; padding: 0.7em;'>{pronunciation}</td></tr>"
                f"<tr>"
                f"<td style='text-align: right; padding: 0.7em; width: 50%;'>Class:</td>"
                f"<td style='text-align: left; padding: 0.7em; width: 50%;'><b>{consonant_class}</b></td>"
                f"</tr>"
                f"<tr>"
                f"<td style='text-align: right; padding: 0.7em;'>Initial Sound:</td>"
                f"<td style='text-align: left; padding: 0.7em;'><b>{initial}</b></td>"
                f"</tr>"
                f"<tr>"
                f"<td style='text-align: right; padding: 0.7em;'>Final Sound:</td>"
                f"<td style='text-align: left; padding: 0.7em;'><b>{final}</b></td>"
                f"</tr>"
                f"<tr>"
                f"<td style='text-align: right; padding: 0.7em;'>Meaning:</td>"
                f"<td style='text-align: left; padding: 0.7em;'><b>{meaning}</b></td>"
                f"</tr>"
                f"<tr><td colspan='2' style='text-align: center; padding: 0.7em;'>[sound:cheat_sheet_consonant_{consonant}.mp3]</td></tr>"
                f"<tr><td colspan='2' style='text-align: center; padding: 0.7em;'>{notes}</td></tr>"
                f"</table>"
            )
            writer.writerow([consonant, back_content])
    print(f"Created TSV file with {len(THAI_CONSONANTS)} Thai consonant cards (no header row, mobile-friendly em padding)")

def generate_audio_files():
    """Generate audio files for all Thai consonants using gTTS"""
    # Create sounds directory if it doesn't exist
    sounds_dir = "sounds"
    if not os.path.exists(sounds_dir):
        os.makedirs(sounds_dir)
        print(f"Created sounds directory: {sounds_dir}")
    
    print("Generating audio files for Thai consonants...")
    print("This may take a few minutes due to API rate limits...")
    
    for i, (consonant, name, pronunciation, consonant_class, initial, final, meaning, notes) in enumerate(THAI_CONSONANTS):
        try:
            # Create filename
            filename = f"{sounds_dir}/cheat_sheet_consonant_{consonant}.mp3"
            
            # Skip if file already exists
            if os.path.exists(filename):
                print(f"✓ {consonant} - Audio file already exists")
                continue
            
            # Generate text to speak (consonant name in Thai)
            text_to_speak = name
            
            # Create gTTS object with Thai language
            tts = gTTS(text=text_to_speak, lang='th', slow=False)
            
            # Save the audio file
            tts.save(filename)
            
            print(f"✓ {consonant} - Generated {filename}")
            
            # Add a small delay to avoid hitting rate limits
            time.sleep(0.5)
            
        except Exception as e:
            print(f"✗ {consonant} - Error generating audio: {e}")
    
    print(f"\nAudio generation complete! Files saved in '{sounds_dir}/' directory")
    print("Copy these files to your Anki media folder to use them in your deck.")

def create_anki_package():
    """Create a proper Anki package structure"""
    # This would require the genanki library for a full implementation
    print("To create a proper .apkg file, install genanki: pip install genanki")
    print("Then use the genanki library to create the deck")

def main():
    """Main function to run the deck generation"""
    print("Thai Consonants Anki Deck Generator")
    print("=" * 40)
    
    # Create TSV deck
    create_tsv_deck()
    
    # Ask user if they want to generate audio files
    print("\n" + "=" * 40)
    response = input("Do you want to generate audio files using gTTS? (y/n): ").lower().strip()
    
    if response in ['y', 'yes']:
        try:
            # Check if gTTS is installed
            import gtts
            generate_audio_files()
        except ImportError:
            print("\nError: gTTS is not installed.")
            print("To install gTTS, run: pip install gTTS")
            print("Then run this script again.")
    else:
        print("Skipping audio generation.")
    
    print("\n" + "=" * 40)
    print("To import into Anki:")
    print("1. Open Anki")
    print("2. File -> Import")
    print("3. Select thai_consonants.tsv")
    print("4. Choose 'Basic' as the note type")
    print("5. Map Front and Back fields")
    print("6. Import")
    
    if response in ['y', 'yes']:
        print("\nFor audio files:")
        print("1. Copy files from 'sounds/' directory to your Anki media folder")
        print("2. Restart Anki to load the audio files")

if __name__ == "__main__":
    main() 