# Load packages
import os
import pandas as pd

# Set local variables
cwd = os.getcwd()
lst = sorted(os.listdir(cwd + "/FACS Files"))
lst.remove('.DS_Store')  # Fixes problem with Mac OS X
path_in = cwd + "/FACS Files/"
path_out = cwd + "/"

# Create empty data frame
output = pd.DataFrame()

# Loop through files
for x in lst[:5]:
    if x == 'T034-005.xlsx':
        tmp = pd.read_excel(path_in + x, header=7, usecols="A:J", sort=False)
        tmp["ID"] = x
        output = output.append(tmp)
    elif x == 'T009-006.xlsx':
        tmp = pd.read_excel(path_in + x, header=9, usecols="A:J", sort=False)
        tmp["ID"] = x
        output = output.append(tmp)
    else:
        tmp = pd.read_excel(path_in + x, header=8, usecols="A:J", sort=False)
        tmp["ID"] = x
        output = output.append(tmp)

# Create ID column
output["ID"] = output["ID"].str[:8]

# Export data
output.to_csv(path_out + "data-faces.csv", index=False)
