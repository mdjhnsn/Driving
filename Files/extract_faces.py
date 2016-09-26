#!/usr/bin/env python
'''
Python program to extract faces data and append to a single large csv file (>600MB)

File Issues: manually fix these so that the header row is 8
  - T000-000: header starts on row 9
  - T000-000: header starts on row 7
'''


import os
import pandas as pd

# Get list of files in directory
lst = sorted(os.listdir("./Files/Faces"))

# Path to Files
path = "./Files/Faces/"

# Variable Start/Stop
x1 = 0

# First File
output = pd.read_excel(path + lst[x1], header=8, parse_cols="A:J")

# Create ID
output["ID"] = lst[x1]

# Loop for all of the files in
for x in lst[x1 + 1:]:
    tmp = pd.read_excel(path + x, header=8, parse_cols="A:J")
    tmp["ID"] = x
    output = output.append(tmp)

# Create some ID columns
output["ID"] = output["ID"].str[:8]

# Export data
output.to_csv("data.csv", index=False)
