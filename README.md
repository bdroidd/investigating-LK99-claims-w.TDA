This repository contains programs and Jupyter Notebook files that are able to implement the following workflow, which is used to evaluate the LK-99 material (Pb9Cu(PO4)6O)
for its superconductivity via topological data analysis and first-principles calculations. The input for the first program, structuralRelaxation_PBEsol.py, 
is the LK-99 CIF data, contained in LK-99.cif.

1. structural optimization: structuralRelaxation_PBEsol.py, pointCloud_converter.py
2. electronic structure calculation: electronicstructure_SCAN.py, Hubbard+UCorrection.py
3. density functional theory: SCF_highPrecision.py, analyzingAnharmonicPhonons.py, smearing_MP.py
4. phonon calculations: phononCalculations_DFPT.py, phonon-mediatedSuperconductivity_EPW_SCAN.py
5. electron-phonon coupling analysis: plottingEliashberg.py
6. topological data analysis: LK99_persistent_entropy.ipynb, LK99_mapper_keplermapper.ipynb
7. Z2 invariant computation: topologicalInvariantComputation_Z2Pack.py 
8. comparative analysis: LK99_superconductivityAnalysis.py

The packages needed to run this code are Quantum ESPRESSO for DFT/DFPT, giotto-tda and kepler-mapper for topological data analysis methods, and matplotlib for visualization. 
Additionally, pymatgen and numpy are required for a program that executes the SCAN self-consistent field calculation, among other operations, and EPW is important for electron-
phonon coupling analysis.
