# -*- coding: utf-8 -*-
"""
Parameter Varying for Difference Images
---------------------------------------

Author: Ruby Kuhr
        University of Manchester 3rd Year Physics Student
-----------------

Date: 03/03/2026
----------------

This code extracts the mean brightness and scatter of each difference image
from all text files with the name format {VARIABLE_TEXT_NAME}_0{VARIABLE[i]}. A figure
showing how the mean brightness and scatter vary as the parameter varies is
produced. This figure is displayed to the user and saved to the directory if
save == True. This figure contains data for 10 test images.

"""

# Imports
import numpy as np
import matplotlib.pyplot as plt

# Varying Parameters
VARIABLE = (1,2,3,4)
VARIABLE_NAME = "Number of Gaussian Fits" # Title of the Image
VARIABLE_TEXT_NAME = "ngauss" # Must appear as it does in text files

# Set to True to save the figure
SAVE = False

#------------------------------------------------------------------------------

# Other Variables
NUMBER_VARIATIONS = len(VARIABLE)
NUMBER_OF_IMAGES = 10
IMAGES = ('20060914_101', '20061022_107', '20061117_137', '20061202_039',
          '20061203_105', '20070826_171', '20071006_072', '20071009_061',
          '20071105_065', '20090102_013')

# Main Body of Code
# Opening the first file
firstfile = np.genfromtxt(f'{VARIABLE_TEXT_NAME}_0{VARIABLE[0]}.txt', delimiter = ' ')
mean = firstfile[:,1]
scatter = firstfile[:,3]

# Continuing to stack onto the mean and scatter variables
for i in range(1, NUMBER_VARIATIONS):
    data = np.genfromtxt(f'{VARIABLE_TEXT_NAME}_0{i}.txt', delimiter = ' ')
    mean = np.vstack((mean, data[:,1]))
    scatter = np.vstack((scatter, data[:,3]))

# Creating the figure
fig, ax = plt.subplots(nrows=2, ncols=5, figsize=(25,10))
for i in range(0, NUMBER_OF_IMAGES):
    if i <= 4:
        j = 0
        k = i
    else:
        j = 1
        k = i - 5
    image_mean = mean[:,i]
    image_scatter = scatter[:,i]
    ax[j, k].errorbar(VARIABLE, image_mean, image_scatter, fmt='k.',
                      ecolor='r')
    ax[j, k].set_title(f'LT_i_{IMAGES[i]}_stack.fits')
    ax[j, k].set_xlabel(f'{VARIABLE_NAME}')
    ax[j, k].set_ylabel('Mean brightness of difference image')
plt.suptitle(f'{VARIABLE_NAME}')
plt.tight_layout()
if SAVE is True:
    plt.savefig(f'{VARIABLE_TEXT_NAME}.png')
plt.show()

