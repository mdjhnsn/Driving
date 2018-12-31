import os
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
path_in = os.getcwd() + '/Files/FACS Files/'
path_out = os.getcwd() + '/Files/'
file_list = sorted(os.listdir(path_in))
try:
    file_list.remove('.DS_Store')
except Exception:
    pass


def load_file(file_name):
    if file_name == 'T034-005.xlsx':
        header_col = 7
    elif file_name == 'T009-006.xlsx':
        header_col = 9
    else:
        header_col = 8
    df = pd.read_excel(path_in + file_name, header=header_col, usecols='A:J', sort=False, index_col='Frame#')
    emotions = ['Anger', 'Contempt', 'Disgust', 'Fear', 'Joy', 'Neutral', 'Sad', 'Surprise']
    df = df[emotions]
    df['ID'] = file_name
    return df


df = load_file(file_list[1])
df.describe()
pca = PCA(2)
df_reduced = pd.DataFrame(pca.fit_transform(df))
