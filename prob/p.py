import pandas as pd

# I like black cats
p = pd.DataFrame(
    [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
    ],
    columns=[".", "i", "like", "black", "cats"],
    index=[".", "i", "like", "black", "cats"],
)

idx = p.loc["."].idxmax()
while not idx == ".":
    print(idx)
    idx = p.loc[idx].idxmax()
