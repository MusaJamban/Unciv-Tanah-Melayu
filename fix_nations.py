import json
import re
from pathlib import Path

path = Path("jsons") / "Nations.json"
if not path.exists():
    print("ERROR: Tak jumpa jsons/Nations.json.")
    print("Letak fail ini dalam folder utama repository Unciv-Tanah-Melayu, kemudian jalankan semula.")
    input("Tekan Enter untuk keluar...")
    raise SystemExit(1)

with path.open("r", encoding="utf-8") as f:
    nations = json.load(f)

percent_stats = {"Gold", "Culture", "Science", "Production", "Food", "Happiness", "Faith"}
changed = []

for nation in nations:
    for i, unique in enumerate(nation.get("uniques", [])):
        # Modern Unciv global percentage-stat syntax
        m = re.fullmatch(r"\[([+-]?\d+)\]% (Gold|Culture|Science|Production|Food|Happiness|Faith)", unique)
        if m:
            new = f"[{m.group(1)}]% [{m.group(2)}] [in all cities]"
            changed.append((nation.get("name", "?"), unique, new))
            nation["uniques"][i] = new
            continue

        # Modern Unciv flat stat-bundle syntax. Preserve capital-only scope.
        m = re.fullmatch(r"\[([+-]?\d+)\] (Gold|Culture|Science|Production|Food|Happiness|Faith)( <in capital>)?", unique)
        if m:
            new = f"[{m.group(1)} {m.group(2)}]" + (m.group(3) or "")
            changed.append((nation.get("name", "?"), unique, new))
            nation["uniques"][i] = new

# Validate output before replacing original file.
encoded = json.dumps(nations, ensure_ascii=False, indent=2) + "\n"
json.loads(encoded)
backup = path.with_suffix(".json.backup")
backup.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
path.write_text(encoded, encoding="utf-8")

print(f"Selesai. {len(changed)} unique ditukar.")
print(f"Backup asal disimpan sebagai: {backup}")
for civ, old, new in changed:
    print(f"- {civ}: {old}  ->  {new}")
print("\nSekarang buka GitHub Desktop, semak jsons/Nations.json, kemudian Commit dan Push.")
input("Tekan Enter untuk keluar...")
