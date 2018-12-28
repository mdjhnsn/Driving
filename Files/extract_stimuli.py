import os
import pandas as pd

# Set local variables
lst = sorted(os.listdir("/Users/mj/Repos/Driving/Files/Stimuli Files"))
path_in = "/Users/mj/Repos/Driving/Files/Stimuli Files/"
path_out = "/Users/mj/Repos/Driving/Files/"

# Fix problem with Mac OS X
try:
    lst.remove('.DS_Store')
except Exception:
    pass

# Create empty data frame
output = pd.DataFrame()

# Loop through files
for x in lst[:3]:
    tmp = pd.read_excel(path_in + x, header=8, parse_cols="A,B,E,F,G")
    tmp["ID"] = x
    output = output.append(tmp)

# Create some ID columns
output["ID"] = output["ID"].str[:8]

# Export data
output.to_csv(path_out + "data-stimuli.csv", index=False)
