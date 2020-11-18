#Execute like python importing_plumed.py >tic{TICnumber}.dat
from tica_metadynamics.plumed_writer import render_tica_plumed_file
from msmbuilder.featurizer import DihedralFeaturizer
import pandas as pd 
import mdtraj as md 
from msmbuilder.utils import load
#python imports
import os,glob
import numpy as np
import pickle

tica_model = load("./tica_mdl_flapchi1angle.pkl")

a = np.arange(1119,1277)
top = md.load("../prot.pdb", atom_indices=a)

# swap this for whatever you have. The code for now supports contacts, dihedral, and angles. 
feat = DihedralFeaturizer(types=['chi1', 'chi2'])

# this basically maps every feature to atom indices. 
df1 = pd.DataFrame(feat.describe_features(top))
#print(df1)

output  = render_tica_plumed_file(tica_mdl= tica_model, df= df1, n_tics= 10, multiple_tics=None)
#Printing TIC1
#print(output[0])
#Printing TIC2
print(output[4])
