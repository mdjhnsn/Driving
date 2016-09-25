#!/bin/python
#
# Python program for extracting data out of all of the excel files associated with this project
#
# This Program assumes its being exectuted from the parent directory and at that all of the excel
# appear in the /Files directory.
#
# It will write a single csv file the parent directory (~750MB)

import os
import pandas as pd

# Get list of files in directory
lst = sorted(os.listdir("./Files", ))

# Path to Files
path = "./Files/"

# Variable Start/Stop
x1 = 0

# First File
output = pd.read_excel(path + lst[x1], header=8, parse_cols="A:J")

# Create ID
output["ID"] = lst[x1]

# Loop for all of the files in
for x in lst[x1+1:]:
    tmp = pd.read_excel(path + x, header=8, parse_cols="A:J")
    tmp["ID"] = x
    output = output.append(tmp)

# Create some ID columns
output["ID"] = output["ID"].str[:8]

# Export data
output.to_csv("data.csv", index=False)
