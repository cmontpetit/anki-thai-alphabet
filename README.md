# Thai Consonants Anki Deck

A comprehensive Anki deck for learning all 41 Thai consonants with detailed information including pronunciation, tone class, and example words.

**Note:** This deck includes 41 consonants, excluding 3 obsolete consonants (ฅ, ฃ, ฦ) that are rarely used in modern Thai.

## Features

- **41 Thai consonants** with complete information
- **Paiboon romanization** with superscript tone markers (ᴴ, ᴸ, ᴿ, ᴰ, ᴹ)
- **Tone class** (High, Mid, Low) for proper tone rules
- **Initial and final sounds** for understanding consonant behavior
- **Example words** with meanings
- **Educational notes** for each consonant
- **HTML table layout** for clean, mobile-friendly display
- **Optional audio generation** using Google Text-to-Speech (gTTS)

## Card Format

Each card follows this structure:

### Front
- Thai consonant character

### Back
- HTML table with:
  - Consonant name in Thai script
  - Paiboon pronunciation with tone markers
  - Tone class (High/Mid/Low)
  - Initial sound
  - Final sound  
  - Meaning of the example word
  - Audio file reference
  - Educational notes

## Example Card

**Front:** ก

**Back:**
```
กอ ไก่
gaawᴹ gaiᴸ
Class: Mid
Initial Sound: g-
Final Sound: -k
Meaning: chicken
[sound:cheat_sheet_consonant_ก.mp3]
Notes: This is the first consonant in the Thai alphabet. It represents the 'g' sound as in 'go'.
```

## Tone Markers

The deck uses superscript tone markers in Paiboon romanization:
- **ᴴ** = High tone
- **ᴸ** = Low tone  
- **ᴿ** = Rising tone
- **ᴰ** = Falling tone
- **ᴹ** = Mid tone

## Quick Start

### 1. Import the Deck
1. Open Anki
2. File → Import
3. Select `thai_consonants.tsv`
4. Choose "Basic" as the note type
5. Map Front and Back fields
6. Import

### 2. Optional: Add Audio Files
If you want pronunciation audio:

1. **Install gTTS:**
   ```bash
   pip install gTTS
   ```

2. **Generate audio files:**
   ```bash
   python generate_thai_deck.py
   ```

3. **Add to Anki:**
   - Copy files from `sounds/` directory to your Anki media folder
   - Restart Anki to load the audio files

## Files

- `thai_consonants.tsv` - TSV file ready for Anki import (no header row)
- `generate_thai_deck.py` - Python script to generate the deck and audio files
- `requirements.txt` - Python dependencies
- `sounds/` - Directory containing generated audio files

## Thai Consonant Classes

### High Class (อักษรสูง)
- Used with high tone marks
- Consonant names have rising tone (ᴿ)
- Includes: ข, ฉ, ถ, ผ, ฝ, ศ, ษ, ส, ห

### Mid Class (อักษรกลาง)  
- Used with mid tone marks
- Consonant names have mid tone (ᴹ)
- Includes: ก, จ, ฎ, ฏ, ด, ต, บ, ป, อ

### Low Class (อักษรต่ำ)
- Used with low tone marks
- Consonant names have mid tone (ᴹ)
- Includes: ค, ช, ซ, ท, น, พ, ฟ, ม, ย, ร, ล, ว, ฮ, and others

## Excluded Consonants

This deck excludes 3 obsolete consonants that are rarely used in modern Thai:

- **ฅ** (ฅอ คน) - Low class, kh- sound, -k final, meaning "person"
- **ฃ** (ฃอ ขวด) - High class, kh- sound, -k final, meaning "bottle"  
- **ฦ** (ฦอ ฦๅ) - Low class, l- sound, -n final, meaning "lue"

These consonants were removed from the Thai alphabet in 1942 and are not included in most modern Thai learning materials.

## Audio Generation

The script uses Google Text-to-Speech (gTTS) to generate pronunciation audio files:

- **Language:** Thai (th)
- **Format:** MP3
- **Content:** Consonant names in Thai script
- **Naming:** `cheat_sheet_consonant_{consonant}.mp3` (e.g., `cheat_sheet_consonant_ก.mp3`)

### Troubleshooting Audio Generation

**Xcode License Issues (macOS):**
```bash
sudo xcodebuild -license accept
```

**Alternative Installation:**
```bash
# Using Homebrew
brew install python3
pip3 install gTTS

# Using conda
conda install -c conda-forge gtts
```

**Network Issues:**
- Check your internet connection
- Try using a VPN
- The deck works perfectly without audio files

## Learning Tips

1. **Start with Mid Class** consonants as they have the most straightforward tone rules
2. **Learn by class** - group consonants by their tone class
3. **Practice writing** each consonant while reviewing
4. **Use the example words** to build vocabulary
5. **Focus on initial sounds** first, then learn final sound variations
6. **Listen to the audio** to improve pronunciation
7. **Pay attention to tone markers** in the romanization

## Customization

You can modify the `generate_thai_deck.py` script to:
- Add more example words
- Include additional pronunciation guides
- Modify the HTML table format
- Add more educational notes
- Change audio generation settings

## Resources

- [Thai Language Wikipedia](https://en.wikipedia.org/wiki/Thai_language)
- [Thai Alphabet](https://en.wikipedia.org/wiki/Thai_alphabet)
- [Thai Tone Rules](https://en.wikipedia.org/wiki/Thai_language#Tones)
- [gTTS Documentation](https://gtts.readthedocs.io/)

## Contributing

Feel free to improve this deck by:
- Adding more example words
- Improving pronunciation guides
- Adding more detailed notes
- Creating additional card types
- Enhancing audio generation

## License

This project is open source and available under the MIT License.
