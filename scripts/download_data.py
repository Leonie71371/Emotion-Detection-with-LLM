from pathlib import Path
from datasets import load_dataset # type: ignore


out = Path("data/raw")
out.mkdir(parents=True, exist_ok=True)

for lang in ["afr", "deu", "ron"]:
    ds = load_dataset("brighter-dataset/BRIGHTER-emotion-categories", lang)
    for split, data in ds.items(): # type: ignore
        data.to_csv(out/ f"{lang}_{split}.csv", index = False)