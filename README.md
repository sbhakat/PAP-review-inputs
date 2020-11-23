# PAP-review-inputs

This repository corresponds to the review article entititled Beyond benzamide-trypsin & alanine dipeptide: pepsin-like aspartic proteases (PAPs) as model systems for combining biomolecular simulation with biophysical experiments
It contains orer parameters as a part of Plumed files and other inputs necessary to perform further computational  study.

Informations on the folder:

1. WT-TIP3P: contains plumed.dat file and PCA eigenvector (ev1.dat) necessary to peform 1D PCA well-tempered metadynamics with Plumed 1.3. 
2. 2D-PCA: contains inputs to perform 2D PCA metadynamics with Plumed 2.5 or higher.
3. Metadynamics-torsion: metadynamics with torsion CVs (chi1 and chi2 angles of Tyr)
4. Metadynamics unbining: metadynamics simulation which using centre of mass CV to facilitate ligand unbining from plasmepsin-II.
5. Metadynamics-COM: 2D metadynamics simulation using COM CVs described here https://www.biorxiv.org/content/10.1101/2020.04.27.062539v1 
6. Plumed-PasAg: plumed input which uses passive-agressive classifier
7. Plumed-TICs: plumed input for TICA using dihedral angles.
8. Plumed-reweight: reweighting script
9. TICA-generation: scripts to perform TICA analyses on plasmepsin-II.

Softwares required:
1. Plumed 1.3, 2.5 
2. Python 3.6 or higher
3. MDtraj
4. Gromacs patched with plumed
5. SciPy for machine learning
6. Gnuplot (plotting)
7. Jupyter Notebook
8. MSMBuilder

Please contact bhakatsoumendranath@gmail.com if you need more information.
