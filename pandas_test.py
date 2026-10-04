import pandas as pd

data = {
    "name": ["A", "B", "C", "D"],
    "age": [22, 23, 21, 24],
    "cgpa": [2.8, 3.2, 3.7, 2.5]
}

df = pd.DataFrame(data)

print(df)

print(df.head(2))
print(df.tail(2))
print(df.columns)
print(df.info())
print(df.describe())

print(df["age"])
print(df["age"].max())
print(df["age"].min())

below3 = df["cgpa"] < 3

print(below3)