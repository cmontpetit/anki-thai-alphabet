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
    # High class
    ("ข", "ขอ ไข่", "khaawᴿ khàiᴸ", "High", "kh-", "-k", "egg", "High-class consonant. The 'kh' sound is aspirated, like in 'kite'."),
    ("ฉ", "ฉอ ฉิ่ง", "chaawᴿ chîngᴸ", "High", "ch-", "-", "cymbal", "High-class consonant. Aspirated 'ch' sound."),
    ("ถ", "ถอ ถุง", "thaawᴿ thǔngᴿ", "High", "th-", "-t", "bag", "High-class consonant. Aspirated 't' sound."),
    ("ผ", "ผอ ผึ้ง", "phaawᴿ phûengᴸ", "High", "ph-", "-", "bee", "High-class consonant. Aspirated 'p' sound."),
    ("ฝ", "ฝอ ฝา", "faawᴿ fáaᴹ", "High", "f-", "-", "lid", "High-class consonant. The 'f' sound as in 'fan'."),
    ("ศ", "ศอ ศาลา", "saawᴿ sǎaᴹ-laaᴹ", "High", "s-", "-t", "pavilion", "High-class consonant. Same sound as ส. Used in Sanskrit/Pali loanwords."),
    ("ษ", "ษอ ฤาษี", "saawᴿ rʉʉᴹ-sǐiᴿ", "High", "s-", "-t", "hermit", "High-class consonant. Same sound as ส. Used in Sanskrit/Pali loanwords."),
    ("ส", "สอ เสือ", "saawᴿ sǔeaᴿ", "High", "s-", "-t", "tiger", "High-class consonant. The 's' sound as in 'see'."),
    ("ห", "หอ หีบ", "haawᴿ hìipᴸ", "High", "h-", "-", "box", "High-class consonant. The 'h' sound as in 'hat'."),

    # Mid class
    ("ก", "กอ ไก่", "gaawᴹ gaiᴸ", "Mid", "g-", "-k", "chicken", "This is the first consonant in the Thai alphabet. It represents the 'g' sound as in 'go'."),
    ("จ", "จอ จาน", "jaawᴹ jaanᴹ", "Mid", "j-", "-t", "plate", "The 'j' sound as in 'jam'."),
    ("ฎ", "ฎอ ชฎา", "daawᴹ cháᴴ-daaᴹ", "Mid", "d-", "-t", "headdress", "Same sound as ด. Used in Sanskrit/Pali loanwords."),
    ("ฏ", "ฏอ ปฏัก", "dtaawᴹ bpaᴹ-dtàkᴸ", "Mid", "dt-", "-t", "goad", "Same sound as ต. Used in Sanskrit/Pali loanwords."),
    ("ด", "ดอ เด็ก", "daawᴹ dèkᴸ", "Mid", "d-", "-t", "child", "The 'd' sound as in 'dog'."),
    ("ต", "ตอ เต่า", "dtaawᴹ dtàoᴸ", "Mid", "dt-", "-t", "turtle", "The 'dt' sound as in 'stop'."),
    ("บ", "บอ ใบไม้", "baawᴹ baiᴹ-máaiᴸ", "Mid", "b-", "-p", "leaf", "The 'b' sound as in 'boy'."),
    ("ป", "ปอ ปลา", "bpaawᴹ bplaaᴹ", "Mid", "bp-", "-p", "fish", "The 'bp' sound as in 'spin'."),
    ("อ", "ออ อ่าง", "aawᴹ àangᴸ", "Mid", "ʔ-", "-", "basin", "The glottal stop sound. Also used as a vowel carrier."),

    # Low class
    ("ค", "คอ ควาย", "khaawᴹ khwaaiᴹ", "Low", "kh-", "-k", "buffalo", "Low-class consonant. Same sound as ข but different tone rules."),
    ("ฆ", "ฆอ ระฆัง", "khaawᴹ ráᴴ-khangᴹ", "Low", "kh-", "-k", "bell", "Low-class consonant. Same sound as ค."),
    ("ง", "งอ งู", "ngaawᴹ nguuᴹ", "Low", "ng-", "-ng", "snake", "The 'ng' sound as in 'sing'. Only appears at the end of syllables in Thai."),
    ("ช", "ชอ ช้าง", "chaawᴹ cháaᴴng", "Low", "ch-", "-t", "elephant", "Low-class consonant. Same sound as ฉ but different tone rules."),
    ("ซ", "ซอ โซ่", "saawᴹ sôᴰh", "Low", "s-", "-t", "chain", "The 's' sound as in 'see'."),
    ("ฌ", "ฌอ เฌอ", "chaawᴹ chəəᴹ", "Low", "ch-", "-", "tree", "Low-class consonant. Same sound as ช."),
    ("ญ", "ญอ หญิง", "yaawᴹ yĭngᴿ", "Low", "y-", "-n", "woman", "The 'y' sound as in 'yes'. Also used for final 'n' sound."),
    ("ฑ", "ฑอ มณโฑ", "thaawᴹ monᴹ-thooᴹ", "Low", "th-", "-t", "Mandodari", "Low-class consonant. Same sound as ท. Used in Sanskrit/Pali loanwords."),
    ("ฒ", "ฒอ ผู้เฒ่า", "thaawᴹ phûuᴸ-thâoᴰ", "Low", "th-", "-t", "elder", "Low-class consonant. Same sound as ท. Used in Sanskrit/Pali loanwords."),
    ("ณ", "ณอ เณร", "naawᴹ naynᴹ", "Low", "n-", "-n", "novice monk", "Same sound as น. Used in Sanskrit/Pali loanwords."),
    ("ท", "ทอ ทหาร", "thaawᴹ tháᴴ-hǎanᴿ", "Low", "th-", "-t", "soldier", "Low-class consonant. Same sound as ถ but different tone rules."),
    ("ธ", "ธอ ธง", "thaawᴹ thongᴹ", "Low", "th-", "-t", "flag", "Low-class consonant. Same sound as ท."),
    ("น", "นอ หนู", "naawᴹ nǔuᴿ", "Low", "n-", "-n", "mouse", "The 'n' sound as in 'no'."),
    ("พ", "พอ พาน", "phaawᴹ phaanᴹ", "Low", "ph-", "-p", "tray", "Low-class consonant. Same sound as ผ but different tone rules."),
    ("ฟ", "ฟอ ฟัน", "faawᴹ fanᴹ", "Low", "f-", "-p", "teeth", "Low-class consonant. Same sound as ฝ but different tone rules."),
    ("ภ", "ภอ สำเภา", "phaawᴹ sǎmᴹ-phaoᴹ", "Low", "ph-", "-p", "junk", "Low-class consonant. Same sound as พ."),
    ("ม", "มอ แมว", "maawᴹ maewᴹ", "Low", "m-", "-m", "cat", "The 'm' sound as in 'man'."),
    ("ย", "ยอ ยักษ์", "yaawᴹ yákᴴ", "Low", "y-", "-", "giant", "The 'y' sound as in 'yes'."),
    ("ร", "รอ เรือ", "raawᴹ rʉaᴹ", "Low", "r-", "-n", "boat", "The 'r' sound as in 'run'."),
    ("ล", "ลอ ลิง", "laawᴹ lingᴹ", "Low", "l-", "-n", "monkey", "The 'l' sound as in 'let'."),
    ("ว", "วอ แหวน", "waawᴹ wǎenᴿ", "Low", "w-", "-", "ring", "The 'w' sound as in 'wet'."),
    ("ฬ", "ฬอ จุฬา", "laawᴹ jùᴸ-laaᴹ", "Low", "l-", "-n", "kite", "Same sound as ล. Used in Sanskrit/Pali loanwords."),
    ("ฮ", "ฮอ นกฮูก", "haawᴹ nókᴰ-hûukᴸ", "Low", "h-", "-", "owl", "Low-class consonant. Same sound as ห but different tone rules.")
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