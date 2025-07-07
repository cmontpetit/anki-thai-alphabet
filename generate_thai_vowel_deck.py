import csv
import re
import os
from gtts import gTTS
import time

# Vowel transcription mapping with tone markers (using same system as consonants)
# Format: syllable -> transcription_with_tone
# Only include transcriptions for actual Thai syllables, not roman vowel sounds
# Tone mapping: ᴹ=Mid, ᴿ=Rising, ᴸ=Low, ᴴ=High, ᶠ=Falling
vowel_transcriptions = {
    "ก็-": "gàᶠ",
    "กะ": "gàᶠ",
    "แก็-": "gàeᶠ",
    "แกะ": "gàeᶠ",
    "ก็อ-": "gàwᶠ",
    "เกาะ": "gàwᶠ",
    "เก็-": "gèᶠ",
    "เกะ": "gèᶠ",
    "เกิ-": "gə̀ᶠ",
    "เกอะ": "gə̀ᶠ",
    "โกะ": "gòᶠ",
    "โก-": "gōᴹ",
    "โก": "gōᴹ",
    "กิ-": "gìᶠ",
    "กิ": "gìᶠ",
    "กึ-": "gʉ̀ᶠ",
    "กึ": "gʉ̀ᶠ",
    "กื": "gʉ̄ᴹ",
    "กึอ": "gʉ̄ᴹ",
    "กุ-": "gùᶠ",
    "กุ": "gùᶠ",
    "กู-": "gūᴹ",
    "กู": "gūᴹ",
    "เกียะ": "gìaᶠ",
    "เกีย-": "gīaᴹ",
    "เกีย": "gīaᴹ",
    "เกือะ": "gʉ̀aᶠ",
    "เกือ-": "gʉ̄aᴹ",
    "เกือ": "gʉ̄aᴹ",
    "กัวะ": "gùaᶠ",
    "กว-": "gūaᴹ",
    "กัว": "gūaᴹ",
    "ไก": "gaiᴹ",
    "ไก-": "gaiᴹ",
    "ใก": "gaiᴹ",
    "กาย": "gaaiᴹ",
    "กัย": "gaiᴹ",
    "ไกย": "gaiᴹ",
    "ก็อย": "gàwyᶠ",
    "กอย": "gàwyᶠ",
    "เกย": "gə̀yᶠ",
    "โกย": "gòyᶠ",
    "กุ": "gùyᶠ",
    "เกือย": "gʉ̀ayᶠ",
    "กวย": "guayᴹ",
    "กวาย": "guayᴹ",
    "เกา": "gaoᴹ",
    "กาว": "gaoᴹ",
    "แก็ว": "gàewᶠ",
    "แกว": "gàewᶠ",
    "เกอว": "gə̀awᶠ",
    "เก็ว": "gèwᶠ",
    "เกว": "gèwᶠ",
    "กิว": "giwᴹ",
    "เกียว": "gìawᶠ",
    "กํา": "gamᴹ",
    "ฤ-": "rʉ́ᴿ",
    "ฤ": "rʉ́ᴿ",
    "ฤ-": "ríᴿ",
    "กา-": "gaaᴹ",
    "กา": "gaaᴹ",
    "แก-": "gaaeᴹ",
    "แก": "gaaeᴹ",
    "กอ-": "gaawᴹ",
    "กอ": "gaawᴹ",
    "เก-": "geeᴹ",
    "เก": "geeᴹ",
    "เกิ-": "gəəᴹ",
    "เกิ-": "gəəᴹ",
    "เก": "gəəᴹ",
    "เกีย-": "giaaᴹ",
    "เกือ-": "gʉaaᴹ"
}

# Vowel data as per the PNG (first few rows for sample, add more as needed)
vowel_rows = [
    ["กั-", "กะ", "aa/ah", "กา-", "กา"],
    ["แก็-", "แกะ", "ae", "แก-", "แก"],
    ["ก็อ-", "เกาะ", "aaw", "กอ-", "กอ"],
    ["เก็-", "เกะ", "eh/ey", "เก-", "เก"],
    ["เกิ-", "เกอะ", "erh/uuhr", "เกิ-", "เกิ-", "เก"],
    ["", "โกะ", "oh", "โก-", "โก"],
    ["กิ-", "กิ", "ee", "กี-", "กี"],
    ["กึ-", "กึ", "eu", "กื", "กึอ"],
    ["กุ-", "กุ", "oo", "กู-", "กู"],
    ["", "เกียะ", "ia", "เกีย-", "เกีย"],
    ["", "เกือะ", "eua", "เกือ-", "เกือ"],
    ["", "กัวะ", "ua", "กว-", "กัว"],
    ["ไก", "", "ai", "ไก-", ""],
    ["ใก", "", "ai", "กาย", ""],
    ["กัย", "", "ai", "", ""],
    ["ไกย", "", "ai", "", ""],
    ["ก็อย", "", "aawy", "กอย", ""],
    ["", "", "eeuy", "เกย", ""],
    ["", "", "oy/ohy", "โกย", ""],
    ["กุ", "", "uy/ui", "", ""],
    ["", "", "euuay", "เกือย", ""],
    ["กวย", "", "uay", "กวาย", ""],
    ["เกา", "", "ao", "กาว", ""],
    ["แก็ว", "", "aeo", "แกว", ""],
    ["", "", "uaaw", "เกอว", ""],
    ["เก็ว", "", "ayo", "เกว", ""],
    ["กิว", "", "iu", "", ""],
    ["", "", "iaao", "เกียว", ""],
    ["กํา", "", "ahm", "กํา", ""],
    ["ฤ-", "ฤ", "rue", "", ""],
    ["ฤ-", "", "ri/reer", "ฤ-", ""]
]

# Table headers as in the PNG
headers = ["SHORT", "LONG"]
subheaders = ["Closed", "Open", "Sound", "Closed", "Open"]

# Helper to make bold in Anki (using <b> tags)
def bold(text):
    return f"<b>{text}</b>" if text else ""

def extract_vowel_symbol(cell):
    # Remove HTML tags and return the first Thai vowel mark
    # Remove <span ...>ก</span> if present
    cell = re.sub(r'<span[^>]*>ก</span>', '', cell)
    # Remove leading ก if present
    if cell and cell[0] == 'ก':
        cell = cell[1:]
    # Remove leading dashes or whitespace
    cell = cell.lstrip('-').strip()
    # Return the first Thai character (vowel mark)
    for ch in cell:
        if '\u0E00' <= ch <= '\u0E7F' and ch not in 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ':
            return ch
    # Fallback: return first non-empty char
    return cell[0] if cell else ''

def make_table(row, bold_idx):
    cells = [
        bold(row[0]) if bold_idx == 0 else row[0],
        bold(row[1]) if bold_idx == 1 else row[1],
        row[2],
        bold(row[3]) if bold_idx == 3 else row[3],
        bold(row[4]) if bold_idx == 4 else row[4],
    ]
    table = f"""
<div style='text-align:center'>
<table border='1' cellpadding='3' style='border-collapse:collapse; margin:auto;'>
  <tr><th colspan='2'>SHORT</th><th></th><th colspan='2'>LONG</th></tr>
  <tr><th>Closed</th><th>Open</th><th>Sound</th><th>Closed</th><th>Open</th></tr>
  <tr><td>{cells[0]}</td><td>{cells[1]}</td><td>{cells[2]}</td><td>{cells[3]}</td><td>{cells[4]}</td></tr>
</table>
</div>
"""
    return table

def generate_audio_files():
    """Generate audio files for all Thai vowels using gTTS"""
    sounds_dir = "sounds"
    if not os.path.exists(sounds_dir):
        os.makedirs(sounds_dir)
        print(f"Created sounds directory: {sounds_dir}")
    print("Generating audio files for Thai vowels...")
    print("This may take a few minutes due to API rate limits...")
    # Collect all unique vowel syllables used as card fronts
    unique_vowels = set()
    for row in vowel_rows:
        for idx in [0, 1, 3, 4]:
            if idx < len(row):
                vowel = row[idx]
                if vowel and vowel != "-":
                    unique_vowels.add(vowel)
    for vowel in unique_vowels:
        filename = f"{sounds_dir}/cheat_sheet_vowel_{vowel}.mp3"
        if os.path.exists(filename):
            print(f"✓ {vowel} - Audio file already exists")
            continue
        try:
            tts = gTTS(text=vowel, lang='th', slow=False)
            tts.save(filename)
            print(f"✓ {vowel} - Generated {filename}")
            time.sleep(0.5)
        except Exception as e:
            print(f"✗ {vowel} - Error generating audio: {e}")
    print(f"\nAudio generation complete! Files saved in '{sounds_dir}/' directory")
    print("Copy these files to your Anki media folder to use them in your deck.")

def main():
    with open("thai_vowels.tsv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        for row in vowel_rows:
            for idx, cell in enumerate([0, 1, 3, 4]):
                vowel = row[cell]
                if not vowel or vowel == "-":
                    continue
                front = vowel
                back = make_table(row, cell)
                vowel_symbol = extract_vowel_symbol(vowel)
                if vowel_symbol:
                    sound_file = f"[sound:sounds/cheat_sheet_vowel_{vowel}.mp3]"
                    transcription = vowel_transcriptions.get(vowel, "")
                    if transcription:
                        back += f"<div style='text-align:center; margin-top:6px;'><b>{transcription}</b></div>"
                    back += f"<div style='text-align:center; margin-top:6px;'>{sound_file}</div>"
                writer.writerow([front, back])
    print(f"Created TSV file with Thai vowel cards (no header row, mobile-friendly em padding)")
    print("\n" + "=" * 40)
    response = input("Do you want to generate audio files using gTTS? (y/n): ").lower().strip()
    if response in ['y', 'yes']:
        try:
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
    print("3. Select thai_vowels.tsv")
    print("4. Choose 'Basic' as the note type")
    print("5. Map Front and Back fields")
    print("6. Import")
    if response in ['y', 'yes']:
        print("\nFor audio files:")
        print("1. Copy files from 'sounds/' directory to your Anki media folder")
        print("2. Restart Anki to load the audio files")

if __name__ == "__main__":
    main() 