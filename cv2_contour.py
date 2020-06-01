# -*- coding: utf-8 -*-
"""
Created on Sun May 31 23:53:06 2020

I think convolution then contour deteciton would be good.
Can you help me with this? I don't know how to have the output_image
be saved a bgr image so cv2 can detect the contours.
The less reading and writing to storage (saving and opening images)
the better.

@author: Zane
"""


#Convolution
from PIL import ImageDraw
import PIL
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

# Load image:
input_image = PIL.Image.open("Dominoes.jpg")
input_pixels = input_image.load()
width, height = input_image.width, input_image.height

# Create output image
output_image = PIL.Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Convert to grayscale
intensity = np.zeros((width, height))
for x in range(width):
    for y in range(height):
        intensity[x, y] = sum(input_pixels[x, y]) / 3
index=0
# Compute convolution between intensity and kernels
for x in range(1, input_image.width - 1):
    for y in range(1, input_image.height - 1):
        magx = intensity[x + 1, y] - intensity[x - 1, y]
        magy = intensity[x, y + 1] - intensity[x, y - 1]

        # Draw in black and white the magnitude
        color = int(sqrt(magx**2 + magy**2))
        draw.point((x, y), (color, color, color))
    index = index + 1
         
output_image.show()
print(output_image.shape)


import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
import cv2

im = cv2.imread("edge.jpg")# this is bgr. I want this to be output_image     
b,g,r = cv2.split(im)#convert to rgb
im_c = cv2.merge([r,g,b])

im_g = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
min_size = min(im_g.shape)*0.01
max_size = min(im_g.shape)*0.1
th, thresh = cv2.threshold(im_g,100,225,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
contours = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]
dots = []
print(len(contours))
for cnt in contours: 
    xy,radius = cv2.minEnclosingCircle(cnt)
    x = cnt[:,0,0]
    y = cnt[:,0,1]
    width,height = max(x)-min(x),max(y)-min(y)
    # bottom_left = min(x),min(y)
    if (min_size<radius<max_size)&(min(width,height)*1.5>max(width,height)):
        dots.append([xy,radius])
        
print(len(dots))       
fig = plt.figure(figsize=(5,5))
ax = fig.add_axes((0,0,1,1))
ax.axis("off")
ax.imshow(im_c) # show color image
for dot in dots:
    xy, radius = dot
    circ = Circle(xy,radius,fc='none',ec='yellow',lw=2)
    ax.add_patch(circ,)
plt.show()


