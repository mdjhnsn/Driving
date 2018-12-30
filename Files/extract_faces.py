# Load packages
import os
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

# Set local variables
fls = sorted(os.listdir('/Users/mj/Repos/Driving/Files/FACS Files'))
path_in = '/Users/mj/Repos/Driving/Files/FACS Files/'
path_out = '/Users/mj/Repos/Driving/Files/'

# Fixes problem with Mac OS X
try:
    fls.remove('.DS_Store')
except Exception:
    pass

# Extract principal components
pca = PCA(2)

emotions = ['Anger', 'Contempt', 'DisguEt', 'Fear', 'Joy', 'Neutral', 'Sad', 'Surprise']

# Create empty data frame
output = pd.DataFrame()

def get_header_col(file_name):
    if file_name == 'T034-005.xlsx':
        header_col = 7
    elif file_name == 'T009-006.xlsx':
        header_col = 9
    else:
        header_col = 8
    return header_col

def load_file(path_in, header_col):
    tmp = pd.read_excel(path_in, header=header_col, usecols='A:J', sort=False, index_col='Frame#')
    tmp = tmp[emotions]
    tmp_reduced = pd.DataFrame(pca.fit_transform(tmp))
    tmp_reduced['ID'].str[:8] = path_in
    output.append(tmp_reduced)
    return output


# Create ID column
output['ID'] = output['ID'].str[:8]

# Export data
output.to_csv(path_out + 'data-faces.csv', index=False)
