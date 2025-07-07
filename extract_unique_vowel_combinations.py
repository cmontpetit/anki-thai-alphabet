import importlib.util

spec = importlib.util.spec_from_file_location("vowel_deck", "generate_thai_vowel_deck.py")
if spec is None or spec.loader is None:
    raise ImportError("Could not load generate_thai_vowel_deck.py for vowel extraction.")
vowel_deck = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vowel_deck)
vowel_rows = vowel_deck.vowel_rows

unique_vowels = set()
for row in vowel_rows:
    for i, cell in enumerate(row):
        if i == 2 or not cell:
            continue
        unique_vowels.add(cell)

for v in sorted(unique_vowels):
    print(v) 