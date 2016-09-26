#!/usr/bin/env python
'''
Python Program to extract and stimuli files to a single csv file
'''

import os
import pandas as pd

# Get list of files in directory
lst = sorted(os.listdir("Stimuli/"))

# Path to Files
path = "Stimuli/"

# Variable Start/Stop
x1 = 0

# First File
output = pd.read_excel(path + lst[x1], header=8, parse_cols="A,B,E,F,G")

# Create ID
output["ID"] = lst[x1]

# Loop for all of the files in
for x in lst[x1 + 1:]:
    tmp = pd.read_excel(path + x, header=8, parse_cols="A,B,E,F,G")
    tmp["ID"] = x
    output = output.append(tmp)

# Create some ID columns
output["ID"] = output["ID"].str[:8]

# Export data
output.to_csv("data-stimuli.csv", index=False)
