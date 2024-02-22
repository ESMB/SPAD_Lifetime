#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 12:22:57 2021

@author: Mathew
"""

from os.path import dirname, join as pjoin
import scipy.io as sio
import numpy as np
from skimage.io import imread
from skimage import filters,measure
import matplotlib.pyplot as plt
import tifffile




# Read the files 

mat_fname=r"/Users/Mathew/Documents/Current analysis/Flow/Lifetime.mat"
mat_contents = sio.loadmat(mat_fname,squeeze_me=True)
lifetimes=mat_contents['A']
lifetimes= np.transpose(lifetimes, (2, 0, 1))
lifetimes=lifetimes[1:,:,:]

mat_fname1="/Users/Mathew/Documents/Current analysis/Flow/Intensity.mat"
mat_contents2 = sio.loadmat(mat_fname1,squeeze_me=True)
intensities=mat_contents2['B']
intensities= np.transpose(intensities, (2, 0, 1))
intensities=intensities[1:,:,:]
# Remove rogue pixels

to_remove=np.percentile(intensities, 99)
intensities_thresh=intensities<to_remove
intensities=intensities*intensities_thresh

tifffile.imwrite(mat_fname+'_lifetetime.tiff', lifetimes, photometric='minisblack')

tifffile.imwrite(mat_fname1+'_intensity.tiff', intensities, photometric='minisblack')


alpha_mask = intensities.astype(float) / 255



plt.imshow(lifetimes[5],cmap='rainbow', vmin=0, vmax=100)
plt.colorbar()  # Add color bar
plt.imshow(alpha_mask[5], alpha=0.5)

plt.xticks([])
plt.yticks([])
plt.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False)
plt.show()


plt.imshow(intensities[5])
