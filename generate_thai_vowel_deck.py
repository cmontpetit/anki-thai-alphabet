import csv
import re

# Vowel data as per the PNG (first few rows for sample, add more as needed)
vowel_rows = [
    ["ก็-", "กะ", "aa/ah", "กา-", "กา"],
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
    ["", "ไก", "", "ai", "ไก-", ""],
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

def lighten_ko_kai(text):
    # If the first character is ก, wrap it in a light grey span, leave the rest as is
    if text and text[0] == 'ก':
        return f'<span style="color:#cccccc">ก</span>{text[1:]}'
    return text

# Example words for each vowel variation (first 5 rows, 4 variations per row)
vowel_examples = [
    # [short_closed, short_open, long_closed, long_open]
    ["จัก", "จะ", "มา", "นา"],
    ["แกะ", "แค", "แมว", "แพ"],
    ["เด็ก", "เตะ", "เท", "เม"],
    ["โต๊ะ", "โต", "โค", "โม"],
    ["เกาะ", "ขอ", "ขอ", "ขอ"],
]

def extract_vowel_symbol(cell):
    # Remove HTML tags and light grey ก, return the first Thai vowel mark
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
    cells = [lighten_ko_kai(c) if i != 2 else c for i, c in enumerate(cells)]
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

def main():
    with open("thai_vowels.tsv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        for row in vowel_rows:
            for idx, cell in enumerate([0, 1, 3, 4]):
                vowel = row[cell]
                if not vowel or vowel == "-":
                    continue
                front = lighten_ko_kai(vowel)
                back = make_table(row, cell)
                vowel_symbol = extract_vowel_symbol(vowel)
                if vowel_symbol:
                    sound_file = f"[sound:sounds/cheat_sheet_vowel_{vowel_symbol}.mp3]"
                    back += f"<div style='text-align:center; margin-top:6px;'>{sound_file}</div>"
                writer.writerow([front, back])

if __name__ == "__main__":
    main() 