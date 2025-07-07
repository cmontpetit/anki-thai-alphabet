from gtts import gTTS
import os
import importlib.util

spec = importlib.util.spec_from_file_location("vowel_deck", "generate_thai_vowel_deck.py")
if spec is None or spec.loader is None:
    raise ImportError("Could not load generate_thai_vowel_deck.py for vowel extraction.")
vowel_deck = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vowel_deck)
vowel_rows = vowel_deck.vowel_rows

unique_syllables = set()
for row in vowel_rows:
    for i, cell in enumerate(row):
        if i == 2 or not cell:
            continue
        unique_syllables.add(cell)

os.makedirs("sounds", exist_ok=True)
for syllable in unique_syllables:
    tts = gTTS(text=syllable, lang='th')
    filename = f"sounds/cheat_sheet_vowel_{syllable}.mp3"
    tts.save(filename)
    print(f"Generated {filename} for {syllable}") 