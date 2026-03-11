# tämä koodi on tehty copilot tekoälyllä
# ohjeena tehtävänanto itsistä

from collections import defaultdict
from typing import Dict, List, Tuple

# ------------------------------
# Lähtötiedot: taulukon sisältö
# Aktiviteetti -> (Edeltäjät, Kesto tunnissa)
# Riippuvuudet tulkitaan: edeltäjä -> aktiviteetti
# ------------------------------
activities: Dict[str, Tuple[List[str], int]] = {
    "A": (["C"], 10),
    "B": (["G"], 10),
    "C": ([], 5),
    "D": (["A"], 20),
    "E": ([], 15),
    "F": (["D", "H", "E", "B"], 10),
    "G": ([], 5),
    "H": (["A"], 10),
}

# Rakenna suunnattu verkko: edeltäjä -> seuraaja
succ = defaultdict(list)  # seuraajalistat
pred_count = defaultdict(int)  # sisääntulevien kaarien määrä (ei välttämätön tässä, mutta hyödyllinen)

for task, (preds, _dur) in activities.items():
    pred_count[task] += 0  # varmista avain
    for p in preds:
        succ[p].append(task)
        pred_count[task] += 1
        pred_count[p] += 0

# Lähteet (ei edeltäjiä) ja nielut (ei seuraajia)
sources = sorted([t for t, (preds, _d) in activities.items() if not preds])
sinks = sorted([t for t in activities.keys() if not succ[t]])

# DFS: kaikki polut lähteistä nieluihin
def all_paths_from_sources_to(targets: List[str] | None = None) -> List[List[str]]:
    """
    Palauttaa kaikki polut kaikista lähteistä annettuihin nieluihin.
    Jos targets on None, käytetään kaikkia nieluja.
    """
    target_set = set(targets) if targets else set(sinks)
    paths: List[List[str]] = []

    def dfs(node: str, path: List[str]):
        path.append(node)
        if node in target_set and node in sinks:
            paths.append(path.copy())
        for nxt in succ[node]:
            dfs(nxt, path)
        path.pop()

    for s in sources:
        dfs(s, [])
    return paths

def path_duration(path: List[str]) -> int:
    """Polun kokonaiskesto (aktiviteettien kestojen summa)."""
    return sum(activities[t][1] for t in path)

# Laske ja tulosta tulokset
all_paths = all_paths_from_sources_to()
paths_to_F = [p for p in all_paths if p and p[-1] == "F"]
sorted_paths = sorted(all_paths, key=path_duration, reverse=True)
critical = sorted_paths[0] if sorted_paths else []

print("Lähteet (ilman edeltäjiä):", sources)
print("Nielut (ilman seuraajia):", sinks)
print()
print("Kaikki polut lähteistä nieluihin (solmujen järjestys):")
for p in all_paths:
    print(" -> ".join(p), f"  (kesto: {path_duration(p)} h)")

print()
print("Polut, jotka päättyvät F:ään:")
for p in paths_to_F:
    print(" -> ".join(p), f"  (kesto: {path_duration(p)} h)")

print()
if critical:
    print("Kriittisin polku (pisin kesto):", " -> ".join(critical), f"  (kesto: {path_duration(critical)} h)")
else:
    print("Polkuja ei löytynyt.")