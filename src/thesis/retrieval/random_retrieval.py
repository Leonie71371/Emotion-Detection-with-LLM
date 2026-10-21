import pandas as pd
import numpy as np

class RandomRetriever:
    def __init__(self, pool: pd.DataFrame, seed: int = 42) -> None:
        self.pool = pool
        self.rng = np.random.default_rng(seed)

    def random_retrieval(self, query, k: int = 5) -> list[dict]:
        examples = self.pool.sample(n = k, random_state = self.rng)
        return examples.to_dict("records")

        


