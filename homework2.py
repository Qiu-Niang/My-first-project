#%matplotlib notebook
# Import the libraries needed in order to run the code

import sys
sys.path.append('.resources')

#if IN_COLAB:
  # In colab we need to add the dependencies to the search path
#  sys.path.append('/content/Take_home_assignment_series_2')

from mesh import *
import numpy as np
from scipy.sparse import lil_matrix as sparse_matrix
from scipy.sparse.linalg import spsolve as solve

# Create the mesh
diskMesh = Mesh('circle',None,refinement=2)

# Get the elements: returns an array with the coordinate index of the vertices
element_list = diskMesh.topology_elements

# Returns the list of vertices
p = diskMesh.points.T

# Compute the number of vertices
n = len(p)

# Plot the mesh
ax = diskMesh.draw()