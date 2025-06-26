# filtrar_genomas_redundantes.py

import pandas as pd

ANI_THRESHOLD = 99.9
INPUT = "fastani_output.tsv"
REDUNDANT_FILE = "redundant_genomes.txt"

df = pd.read_csv(INPUT, sep="\t", header=None,
                 names=["query", "reference", "ani", "fragments", "total"])

redundant_pairs = df[df["ani"] > ANI_THRESHOLD]

to_remove = set()
for _, row in redundant_pairs.iterrows():
    q = row["query"]
    r = row["reference"]
    if q not in to_remove:
        to_remove.add(r)

with open(REDUNDANT_FILE, "w") as out:
    for genome in sorted(to_remove):
        out.write(f"{genome}\n")

print(f"🧹 Genomas redundantes detectados: {len(to_remove)}")
