import sys
import pandas as pd
import numpy as np
from sklearn import preprocessing
import sklearn
import tkinter
import matplotlib.pyplot as plt


chur=pd.read_csv("/home/sureshb/ECS/R/cherry1.csv")
# print(chur)
# print(chur.head(5))
num_rows=chur.shape[0]
count_nan = chur.isnull().sum()

print(count_nan)
counterwithoutnan = count_nan[count_nan == 0]

chur = chur[counterwithoutnan.keys()]

from sklearn.preprocessing import StandardScaler
# create a feature vector
x=chur.ix[:,:-1].values
print(x)
standard_scale=StandardScaler()
x_std=standard_scale.fit_transform(x)

from sklearn.manifold import TSNE
# creating tsne visualization
tsne= TSNE(n_components=2,random_state=0)
x_test_2d=tsne.fit_transform(x_std,chur)
#
# X=chur.ix[:,:-1].values
# scaler = preprocessing.StandardScaler().fit(X)
#
# from sklearn.manifold import TSNE
# # creating tsne visualization
# tsne= TSNE(n_components=2,random_state=0)
# x_test_2d=tsne.fit_transform(x_std,chur)