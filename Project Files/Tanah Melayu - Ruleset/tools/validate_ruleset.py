import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]; js=root/"jsons"
files=list(js.glob("*.json")); data={p.stem:json.loads(p.read_text(encoding="utf-8")) for p in files}
tech_cols=data["Techs"]; tech={t["name"] for c in tech_cols for t in c["techs"]}; nations={n["name"] for n in data["Nations"]}; units={u["name"] for u in data["Units"]}; errors=[]
for c in tech_cols:
 if c.get("era") not in {e["name"] for e in data["Eras"]}: errors.append(f"unknown era {c.get('era')}")
 for t in c["techs"]:
  for p in t.get("prerequisites",[]):
   if p not in tech: errors.append(f"tech {t['name']}: unknown prerequisite {p}")
for u in data["Units"]:
 if u.get("requiredTech") and u["requiredTech"] not in tech: errors.append(f"unit {u['name']}: unknown tech {u['requiredTech']}")
 if u.get("uniqueTo") and u["uniqueTo"] not in nations: errors.append(f"unit {u['name']}: unknown nation {u['uniqueTo']}")
 if u.get("replaces") and u["replaces"] not in units: errors.append(f"unit {u['name']}: unknown replacement {u['replaces']}")
for b in data["Buildings"]:
 if b.get("requiredTech") and b["requiredTech"] not in tech: errors.append(f"building {b['name']}: unknown tech {b['requiredTech']}")
for r in data["TileResources"]:
 for terrain in r.get("terrainsCanBeFoundOn",[]):
  if terrain not in {t["name"] for t in data["Terrains"]}: errors.append(f"resource {r['name']}: unknown terrain {terrain}")
 if r.get("improvement") and r["improvement"] not in {i["name"] for i in data["TileImprovements"]}: errors.append(f"resource {r['name']}: unknown improvement {r['improvement']}")
if errors: print("FAIL"); print("\n".join(errors)); raise SystemExit(1)
print(f"PASS: {len(files)} JSON files; {len(tech)} technologies; {len(nations)} nation entries; {len(units)} units; {len(data['Buildings'])} buildings; no cross-reference errors")
