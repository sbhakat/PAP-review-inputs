#msmbuilder imports 
from msmbuilder.dataset import dataset
from msmbuilder.featurizer import ContactFeaturizer
from msmbuilder.featurizer import DihedralFeaturizer
from msmbuilder.decomposition import tICA
from msmbuilder.cluster import MiniBatchKMeans
from msmbuilder.msm import ContinuousTimeMSM
from msmbuilder.utils import verbosedump,verboseload
from msmbuilder.cluster import KCenters
from msmbuilder.utils import load,dump

#other imports
import os,glob,shutil
import numpy as np
import mdtraj as md
import pandas as pd 
import pickle
#prettier plots

#Loading the trajectory
a = np.arange(1027,1357)
ds = dataset("../trajfit.xtc", topology="../prot.pdb", atom_indices=a)


#Featurization
featurizer = DihedralFeaturizer(types=['chi1', 'chi2'])
#dump(featurizer,"raw_featurizer.pkl")

#from msmbuilder.utils import load,dump
f=DihedralFeaturizer(types=['chi1', 'chi2'], sincos=False)
dump(f,"raw_featurizer.pkl")

#featurizer = DihedralFeaturizer(types=['chi1', 'chi2'], resids= 73,74,75,76,77,78,79,80,81,82,83)
diheds = featurizer.fit_transform(ds)
dump(diheds, "features.pkl")
                                 
#print(ds[0].shape)
print(diheds[0].shape)

# this basically maps every feature to atom indices. 
#df1 = pd.DataFrame(featurizer.describe_features(ds))
#dump(df1, "feature_descriptor.pkl")

#Robust scaling
from msmbuilder.preprocessing import RobustScaler
scaler = RobustScaler()
scaled_diheds = scaler.fit_transform(diheds)

print(diheds[0].shape)
print(scaled_diheds[0].shape)

#Reducing dimension
tica_model = tICA(lag_time=10, n_components=5)
# fit and transform can be done in seperate steps:
tica_model.fit(diheds)
tica_trajs = tica_model.transform(diheds)

print(diheds[0].shape)
print(tica_trajs[0].shape)

#lets dump the tica mdl for future use
verbosedump(tica_model,"tica_mdl_flapchi1angle.pkl")
verbosedump(tica_trajs,"tica_data.pkl")
