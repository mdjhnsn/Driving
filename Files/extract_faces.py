#!/usr/bin/env python
'''
Python program to extract faces data and append to a single large csv file (>600MB)

File Issues: manually fix these so that the header row is 9
  - T034-005.xlsx: header starts on row 8
  - T009-006.xlsx: header starts on row 10
'''


import os
import pandas as pd

# Get list of files in directory
lst = sorted(os.listdir("Files/FACS Files"))
lst.remove('.DS_Store')

# Path to Files
path = "Files/FACS Files/"

# Variable Start/Stop
x1 = 0

# First File
output = pd.read_excel(path + lst[x1], header=8, usecols="A:J")

# Create ID
output["ID"] = lst[x1]

# Loop for all of the files in
for x in lst[x1 + 1:]:
    if x['T034-005.xlsx']:
        tmp = pd.read_excel(path + x, header=7, usecols="A:J", sort=False)
        tmp["ID"] = x
        output = output.append(tmp)
    elif x['T009-006.xlsx']:
        tmp = pd.read_excel(path + x, header=9, usecols="A:J", sort=False)
        tmp["ID"] = x
        output = output.append(tmp)
    else:
        tmp = pd.read_excel(path + x, header=8, usecols="A:J", sort=False)
        tmp["ID"] = x
        output = output.append(tmp)

# Create some ID columns
output["ID"] = output["ID"].str[:8]

# Export data
output.to_csv("data-faces.csv", index=False)
