# Re-import libraries and reload data after code state reset
import pandas as pd
from scipy.stats import f_oneway, ttest_ind

# Reconstruct raw data
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

# Create DataFrame and calculate GreenNorm
df = pd.DataFrame(data)
df["GreenNorm"] = df["Green"] / (df["Red"] + df["Green"] + df["Blue"])

# Split by group
room_temp = df[df["Storage Temp (°C)"] == "~28°C"]["GreenNorm"]
fridge = df[df["Storage Temp (°C)"] == "6°C"]["GreenNorm"]
freezer = df[df["Storage Temp (°C)"] == "-18°C"]["GreenNorm"]

# Perform one-way ANOVA
anova_f, anova_p = f_oneway(room_temp, fridge, freezer)

# Pairwise t-tests
t_fridge_vs_room = ttest_ind(fridge, room_temp)
t_freezer_vs_room = ttest_ind(freezer, room_temp)
t_fridge_vs_freezer = ttest_ind(fridge, freezer)

anova_f, anova_p, t_fridge_vs_room, t_freezer_vs_room, t_fridge_vs_freezer

#|////////////////////////////////////////////////////////////////////////////////|
#|-----------------------------------Results--------------------------------------|
#|////////////////////////////////////////////////////////////////////////////////|
'''
(51.40306259796776,
 5.148841392669309e-12,
 Ttest_indResult(statistic=9.029749745626127, pvalue=8.712383574281988e-10),
 Ttest_indResult(statistic=9.330050414473453, pvalue=4.348158964507754e-10),
 Ttest_indResult(statistic=0.2935479788648057, pvalue=0.7712681984069156))
'''
