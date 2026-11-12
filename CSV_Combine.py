
#Import the libraries if you dotn have them guys

import pandas as pd
import glob as gl
import os


folder = os.path.expanduser(
    "~/.cache/kagglehub/datasets/utsavdey1410/food-nutrition-dataset/versions/1/FINAL FOOD DATASET"
)

files = gl.glob(folder + "/FOOD-DATA-GROUP*.csv")

#Combining the CSV files into one big file
frames = []

for file in files:
    df = pd.read_csv(file)
    frames.append(df)

#new file with all the csv files combines
combined = pd.concat(frames, ignore_index = True)

print("Found ", len(files) , " files")
print("Rows: ", len(combined))
print("Columns:", combined.columns.tolist())

#Save to Combined_FOOD.csv
combined.to_csv("Combined_FOOD.csv", index = False)

print("Combined_FOOD.csv created")

#Hi everyone once you have run this code in your bash use the following command to open it:

#open Combined_FOOD.csv (Of course this will change for each new csv)

#Make sure you are in the right folder i.e. Nutritrack (Name me and Adrian came up with)


