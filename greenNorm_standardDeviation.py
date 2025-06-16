import pandas as pd

# Raw RGB data from the image (manually extracted and structured)
data = {
    "Storage Temp (°C)": ["~28°C"]*15 + ["6°C"]*15 + ["-18°C"]*15,
    "Set No.": list(range(1, 16)) * 3,
    "Red": [
        21, 21, 23, 24, 38, 23, 26, 22, 20, 18, 18, 15, 16, 20, 20,
        32, 9, 25, 32, 24, 26, 21, 25, 21, 21, 25, 25, 29, 32, 32,
        28, 29, 28, 28, 32, 22, 30, 15, 26, 30, 26, 20, 32, 20, 35
    ],
    "Green": [
        22, 22, 22, 25, 38, 26, 26, 23, 18, 19, 18, 15, 16, 19, 21,
        41, 35, 29, 43, 27, 32, 26, 33, 26, 26, 31, 32, 36, 41, 42,
        38, 44, 40, 37, 44, 44, 38, 37, 36, 42, 33, 43, 44, 38, 54
    ],
    "Blue": [
        14, 14, 11, 16, 32, 9, 17, 17, 9, 12, 9, 12, 12, 13, 14,
        14, 28, 14, 8, 11, 13, 12, 11, 11, 10, 10, 9, 10, 6, 5,
        17, 14, 17, 17, 13, 36, 18, 27, 13, 13, 15, 30, 17, 29, 12
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Compute Normalised Green Value
df["GreenNorm"] = df["Green"] / (df["Red"] + df["Green"] + df["Blue"])

# Group by storage temperature and calculate average GreenNorm
grouped = df.groupby("Storage Temp (°C)")["GreenNorm"].agg(["mean", "std"])

df.head(), grouped
#|////////////////////////////////////////////////////////////////////|
#|------------------------RESULTS OBTAINED----------------------------|
#|////////////////////////////////////////////////////////////////////|
'''
(  Storage Temp (°C)  Set No.  Red  Green  Blue  GreenNorm
 0             ~28°C        1   21     22    14   0.385965
 1             ~28°C        2   21     22    14   0.385965
 2             ~28°C        3   23     22    11   0.392857
 3             ~28°C        4   24     25    16   0.384615
 4             ~28°C        5   38     38    32   0.351852,
                        mean       std
 Storage Temp (°C)                    
 -18°C              0.469889  0.028375
 6°C                0.473109  0.031621
 ~28°C              0.382402  0.022667)
'''
