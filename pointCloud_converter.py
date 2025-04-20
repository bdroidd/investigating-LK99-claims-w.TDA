#
#   pointCloud_converter.py
#
#   The code below converts LK-99 CIF data into point clouds. It is written in the
#   Python programming language, requires the user to enter the path to the CIF, and
#   produces a three-dimensional scatter plot of atoms, if desired. Also, the program
#   can save the points to a text file and returns an array of atomic coordinates. 
#   One might eventually use such a point cloud to find persistent homology with 
#   libraries such as GUDHI. The coordinates can be transformed into Quantum ESPRESSO
#   input files with pymatgen.io.pwscf.
#____________________________________________________________________________________

import numpy as np
from pymatgen.core import Structure
from pymatgen.io.pwscf import PWInput
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def cif_to_point_cloud(cif_path, plot=False, save_txt=False):
    
    # loads CIF using pymatgen

    struct = Structure.from_file(cif_path)
    
    # extracts atomic positions & elements

    coords = np.array([site.coords for site in struct.sites])

    elements = [site.species_string for site in struct.sites]
    
    # saves to text file (optional)

    if save_txt:

        np.savetxt(f"{cif_path[:-4]}_point_cloud.txt", coords, 
                   
                  header="X Y Z", fmt="%.6f")
    
    # 3D visualization (optional)

    if plot:

        fig = plt.figure(figsize=(10, 7))

        ax = fig.add_subplot(111, projection='3d')
        
        # colours points by element 

        unique_elements = list(set(elements))

        colors = plt.cm.jet(np.linspace(0, 1, len(unique_elements)))
        
        for elem, color in zip(unique_elements, colors):

            idx = [i for i, e in enumerate(elements) if e == elem]

            ax.scatter(coords[idx, 0], coords[idx, 1], coords[idx, 2], 
                       
                      label=elem, c=[color], s=50, alpha=0.7)
        
        ax.set_xlabel("X (Å)")

        ax.set_ylabel("Y (Å)")

        ax.set_zlabel("Z (Å)")

        ax.set_title(f"The point cloud is {cif_path}.")

        ax.legend()

        plt.show()
    
    return coords

# an example w/application to LK-99

lk99_coords = cif_to_point_cloud("LK99.cif", plot=True, save_txt=True)

print(f"Generated {len(lk99_coords)} atomic coordinates.")