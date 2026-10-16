from pathlib import Path
from datasets import load_dataset


for lang in ["afr", "deu", "ron"]:
    ds = load_dataset("brighter-dataset/BRIGHTER-emotion-categories", lang)
    out = Path("data/raw") / lang
    out.mkdir(parents=True, exist_ok=True)
    for split, data in ds.items():
        data.to_csv(out/ f"{split}.csv")