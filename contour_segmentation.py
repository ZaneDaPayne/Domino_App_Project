#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:30:45 2020

@author: harini
"""


from skimage.color import rgb2gray
from skimage import measure
from skimage import io
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
im = io.imread('domino2.jpg',as_gray=True); #upload image and convert to grayscale
image = rgb2gray(im)
#Getting threshold value
thresh = threshold_otsu(image)
#Applying threshold
thresholded_image = image > thresh
#Find contours at a constant value
contours = measure.find_contours(thresholded_image, 0.8)

#We can use the next two lines in # to determine the number of dots and calculate the total score, silence if necessary!
for contour in contours:
    print(contour.shape)
fig, ax = plt.subplots()
ax.imshow(image, cmap=plt.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()   