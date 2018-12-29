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
emotions = ['Anger', 'Contempt', 'Disgust', 'Fear', 'Joy', 'Neutral', 'Sad', 'Surprise']
X = df[emotions]
X_reduced = pca.fit_transform(X)
df2 = pd.DataFrame(X_reduced)

# Create empty data frame
output = pd.DataFrame()

# Loop through files
for x in fls[:10]:
    if x == 'T034-005.xlsx':
        tmp = pd.read_excel(path_in + x, header=7, usecols='A:J', sort=False, index_col='Frame#')
        tmp = tmp[emotions]
        tmp_reduced = pd.DataFrame(pca.fit_transform(tmp))
        tmp_reduced['ID'] = x
        output = output.append(tmp_reduced)
    elif x == 'T009-006.xlsx':
        tmp = pd.read_excel(path_in + x, header=9, usecols='A:J', sort=False, index_col='Frame#')
        tmp = tmp[emotions]
        tmp_reduced = pd.DataFrame(pca.fit_transform(tmp))
        tmp_reduced['ID'] = x
        output = output.append(tmp_reduced)
    else:
        tmp = pd.read_excel(path_in + x, header=8, usecols='A:J', sort=False, index_col='Frame#')
        tmp = tmp[emotions]
        tmp_reduced = pd.DataFrame(pca.fit_transform(tmp))
        tmp_reduced['ID'] = x
        output = output.append(tmp_reduced)

# Create ID column
output['ID'] = output['ID'].str[:8]

# Export data
output.to_csv(path_out + 'data-faces.csv', index=False)
