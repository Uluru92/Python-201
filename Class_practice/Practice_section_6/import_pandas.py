import pandas as pd

data2 = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]

print("Print 1:")
print(" ")
print(pd.DataFrame(data2))
print(" ")
print("Print 2:")
print(" ")
print(pd.DataFrame(data2, index=["first", "second"]))
print(" ")
print("Print 3:")
print(" ")
print(pd.DataFrame(data2,index=["first", "second"], columns=["a", "b","c"],))