import pandas as pd
from sklearn.preprocessing import normalize

s = [
    "I like black cats",
    "I like red cats",
    "I like blue cats",
    "I like pink dogs",
    "I like orange dogs",
]
words = set()

for line in s:
    for w in line.split(" "):
        words.add(w)

words = list(words)
words.insert(0, ".")

p = pd.DataFrame(
    0,
    columns=words,
    index=words,
)
for line in s:
    arr = line.split(" ")
    arr.append(".")
    arr.insert(0, ".")
    for i in range(len(arr)):
        if i == len(arr) - 1:
            continue
        c = arr[i]
        n = arr[i + 1]
        p.loc[c][n] += 1

p = p.div(p.sum(axis=1), axis=0)
# print(p)

idx = p.loc["."].idxmax()
while not idx == ".":
    print(idx)
    idx = p.loc[idx].idxmax()
