import pandas as pan
import numpy as num

db = pan.read_csv("./war.csv")
new = db.sort_values("tiempo", ascending=False)
pip = db.sort_values("crimenes", ascending=True)
print(new)
print("---------------------------------------------")
print(pip)