from pathlib import Path
import pandas as pd

PROCESSED_DIR = Path(__file__).resolve().parents[1] / "data" / "processed"

def load_processed(lang, split):
    return pd.read_csv(PROCESSED_DIR / f"{lang}_{split}.csv")