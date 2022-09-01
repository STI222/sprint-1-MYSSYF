import pandas as pan
print(pan.__version__ +" pandas")
import numpy as num
print(num.__version__ +" numpy")
print("---------------------------------------------")
db = pan.read_csv("./war.csv")
new = db.sort_values("tiempo", ascending=False)
pip = db.sort_values("crimenes", ascending=True)
print(new)
print("---------------------------------------------")
print(pip)