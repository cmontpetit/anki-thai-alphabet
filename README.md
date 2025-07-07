# Thai Consonants & Vowels Anki Decks

A comprehensive set of Anki decks for learning all Thai consonants and vowels, with detailed information including pronunciation, tone class, and example words.

## Features

- **Thai consonants and vowels** with complete information
- **Paiboon romanization** with superscript tone markers (ᴹ, ᴿ, ᴸ, ᴴ, ᶠ)
- **Tone class** (High, Mid, Low) for consonants
- **Initial and final sounds** for consonants
- **Example words** and meanings
- **Educational notes** for each consonant
- **HTML table layout** for clean, mobile-friendly display
- **Optional audio generation** using Google Text-to-Speech (gTTS) for both decks

## Card Format

### Consonant Deck
**Front:** Thai consonant character

**Back:**
- Consonant name in Thai script
- Paiboon pronunciation with tone markers
- Tone class (High/Mid/Low)
- Initial sound
- Final sound
- Meaning of the example word
- Audio file reference
- Educational notes

### Vowel Deck
**Front:** Thai vowel syllable (with ก as base consonant)

**Back:**
- HTML table showing the vowel row from the reference chart
- Paiboon pronunciation with tone marker (if available)
- Audio file reference

## Tone Markers

The decks use superscript tone markers in Paiboon romanization:
- **ᴹ** = Mid tone
- **ᴿ** = Rising tone
- **ᴸ** = Low tone
- **ᴴ** = High tone
- **ᶠ** = Falling tone

## Quick Start

### 1. Generate Decks

**Consonants:**
```bash
python generate_thai_consonant_deck.py
```
**Vowels:**
```bash
python generate_thai_vowel_deck.py
```
Both scripts will prompt you to optionally generate audio files after creating the TSV.

### 2. Import into Anki
1. Open Anki
2. File → Import
3. Select the appropriate TSV file (`thai_consonants.tsv` or `thai_vowels.tsv`)
4. Choose "Basic" as the note type
5. Map Front and Back fields
6. Import

### 3. Add Audio Files (Optional)
If you chose to generate audio, copy files from the `sounds/` directory to your Anki media folder and restart Anki.

## Files

- `thai_consonants.tsv` - TSV file for consonant deck (no header row)
- `thai_vowels.tsv` - TSV file for vowel deck (no header row)
- `generate_thai_consonant_deck.py` - Script to generate consonant deck and audio
- `generate_thai_vowel_deck.py` - Script to generate vowel deck and audio
- `requirements.txt` - Python dependencies
- `sounds/` - Directory containing generated audio files

## Audio Generation

Both scripts use Google Text-to-Speech (gTTS) to generate pronunciation audio files:
- **Language:** Thai (th)
- **Format:** MP3
- **Content:** Consonant or vowel syllable in Thai script
- **Naming:**
  - Consonants: `cheat_sheet_consonant_{consonant}.mp3`
  - Vowels: `cheat_sheet_vowel_{syllable}.mp3`

After TSV generation, you will be prompted to generate audio files. If you accept, the script will create all necessary audio files in the `sounds/` directory.

## Learning Tips

1. **Start with Mid Class** consonants as they have the most straightforward tone rules
2. **Learn by class** - group consonants by their tone class
3. **Practice writing** each consonant and vowel while reviewing
4. **Use the example words** to build vocabulary
5. **Focus on initial sounds** first, then learn final sound variations
6. **Listen to the audio** to improve pronunciation
7. **Pay attention to tone markers** in the romanization

## Customization

You can modify the scripts to:
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

Feel free to improve these decks by:
- Adding more example words
- Improving pronunciation guides
- Adding more detailed notes
- Creating additional card types
- Enhancing audio generation

## License

This project is open source and available under the MIT License.
