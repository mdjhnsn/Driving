import os
import pandas as pd

# Get list of files in directory
lst = os.listdir("./Files")

# Path to Files
path = "./Files/"

# First File
output = pd.read_excel(path + lst[0], skiprows=8)

# Create ID
output["ID"] = lst[0]

# Loop for all of the files in
for x in lst[1:]:
    tmp = pd.read_excel(path + x, header=1, skiprows=7)
    tmp["ID"] = x
    output = output.append(tmp, ignore_index=True)

# Create some ID columns
output["ID"] = output["ID"].str[:8]
output["Subject"] = output["ID"].str[:4]
output["Simulation"] = output["ID"].str[-3:]

# Export data
output.to_csv("data.csv", index=False)
