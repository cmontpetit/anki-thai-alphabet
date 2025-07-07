from gtts import gTTS
import os
import re

# Manually map vowel symbols to Thai vowel names (add more as needed)
vowel_name_map = {
    'ai': 'สระ ไอ',
    'กว-': 'สระ อัว',
    'กวย': 'สระ อวย',
    'กวาย': 'สระ อวาย',
    'กอ': 'สระ ออ',
    'กอ-': 'สระ ออ',
    'กอย': 'สระ ออย',
    'กัย': 'สระ ไัย',
    'กัว': 'สระ อัว',
    'กัวะ': 'สระ อัวะ',
    'กาย': 'สระ อาย',
    'กาว': 'สระ อาว',
    'กิ': 'สระ อิ',
    'กิ-': 'สระ อิ',
    'กิว': 'สระ อิว',
    'กี': 'สระ อี',
    'กี-': 'สระ อี',
    'กึ': 'สระ อึ',
    'กึ-': 'สระ อึ',
    'กึอ': 'สระ อึอ',
    'กื': 'สระ อือ',
    'กุ': 'สระ อุ',
    'กุ-': 'สระ อุ',
    'กู': 'สระ อู',
    'กู-': 'สระ อู',
    'ก็อ-': 'สระ ออ',
    'ก็อย': 'สระ ออย',
    'กํา': 'สระ อำ',
    'ฤ': 'สระ ฤ',
    'ฤ-': 'สระ ฤ',
    'เก': 'สระ เอ',
    'เก-': 'สระ เอ',
    'เกย': 'สระ เออย',
    'เกว': 'สระ เอว',
    'เกอว': 'สระ เออว',
    'เกอะ': 'สระ เออะ',
    'เกะ': 'สระ เอะ',
    'เกา': 'สระ เอา',
    'เกาะ': 'สระ ออ',
    'เกิ-': 'สระ เออ',
    'เกีย': 'สระ เอีย',
    'เกีย-': 'สระ เอีย',
    'เกียว': 'สระ เอียว',
    'เกียะ': 'สระ เอียะ',
    'เกือ': 'สระ เอือ',
    'เกือ-': 'สระ เอือ',
    'เกือย': 'สระ เอือย',
    'เกือะ': 'สระ เอือะ',
    'เก็-': 'สระ เอะ',
    'เก็ว': 'สระ เอ็ว',
    'แก': 'สระ แอ',
    'แก-': 'สระ แอ',
    'แกว': 'สระ แอว',
    'แกะ': 'สระ แอะ',
    'แก็-': 'สระ แอะ',
    'แก็ว': 'สระ แอ็ว',
    'โก': 'สระ โอ',
    'โก-': 'สระ โอ',
    'โกย': 'สระ โอย',
    'โกะ': 'สระ โอะ',
    'ใก': 'สระ ใอ',
    'ไก': 'สระ ไอ',
    'ไก-': 'สระ ไอ',
    'ไกย': 'สระ ไอย',
}

def extract_vowel_symbols_from_row(row):
    # Ignore the sound column (index 2)
    symbols = []
    for i, cell in enumerate(row):
        if i == 2 or not cell:
            continue
        # Remove consonants and dashes, keep only Thai vowel marks
        # Remove <span ...>ก</span> if present
        cell = re.sub(r'<span[^>]*>ก</span>', '', cell)
        # Remove leading ก if present
        if cell and cell[0] == 'ก':
            cell = cell[1:]
        # Remove trailing/leading dashes
        cell = cell.strip('-').strip()
        # Add all Thai characters except ก
        for ch in cell:
            if '\u0E00' <= ch <= '\u0E7F' and ch not in 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ':
                symbols.append(ch)
    return symbols

def main():
    # Import vowel_rows from generate_thai_vowel_deck.py
    import importlib.util
    spec = importlib.util.spec_from_file_location("vowel_deck", "generate_thai_vowel_deck.py")
    if spec is None or spec.loader is None:
        raise ImportError("Could not load generate_thai_vowel_deck.py for vowel extraction.")
    vowel_deck = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(vowel_deck)
    vowel_rows = vowel_deck.vowel_rows

    # Collect all unique vowel symbols
    all_symbols = set()
    for row in vowel_rows:
        all_symbols.update(extract_vowel_symbols_from_row(row))
    all_symbols = {s for s in all_symbols if s}

    os.makedirs("sounds", exist_ok=True)
    for symbol in all_symbols:
        name = vowel_name_map.get(symbol)
        if not name:
            print(f"No Thai name for symbol: {symbol}")
            continue
        tts = gTTS(text=name, lang='th')
        filename = f"sounds/cheat_sheet_vowel_{symbol}.mp3"
        tts.save(filename)
        print(f"Generated {filename} for {name}")

if __name__ == "__main__":
    main() 