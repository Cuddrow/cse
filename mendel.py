import pandas as pd

crossbred_flower = ["B", "b"]
table = pd.DataFrame(index=crossbred_flower, columns=crossbred_flower)
table.iloc[0,0] = "BB"
table.iloc[0,1] = "Bb"
table.iloc[1,0] = "bB"
table.iloc[1,1] = "bb"

print(table)
