# -*- coding: utf-8 -*-
"""
Created on Sun May 31 23:53:06 2020

@author: Zane
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
import cv2

im = cv2.imread("Dominoes.jpg")        
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