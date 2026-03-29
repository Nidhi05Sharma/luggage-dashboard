import pandas as pd

data = {
    "brand": ["Safari", "VIP"],
    "price": [2000, 3500]
}

df = pd.DataFrame(data)

print("Setup working")
print(df)