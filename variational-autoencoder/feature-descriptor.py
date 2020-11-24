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

a = np.arange(1027,1357)
top = md.load("../prot.pdb", atom_indices=a)

# swap this for whatever you have. The code for now supports contacts, dihedral, and angles. 
feat = DihedralFeaturizer(types=['chi1', 'chi2'])
dump(feat, "featurizer.pkl")

# this basically maps every feature to atom indices. 
df1 = pd.DataFrame(feat.describe_features(top))
dump(df1, "feature_descriptor.pkl")
