#!/usr/bin/env python
# coding: utf-8

# Domino Dot Recognition: A code to detect and count dots on dominos

# The first thing that we are going to do is apply a convolution to the image. The convolution takes a gradient at every pixel in the image. If the gradient>0, that indicates that there is a rate of change in color/intensity visible to the human eye. Thus, it colors it white. If the gradient is negative, it colors it black. This code utilizes tools in Skimage and PIL.

# Let's load our dependencies

# In[7]:



from PIL import Image, ImageDraw
import numpy as np
from math import sqrt
from skimage.color import rgb2gray
from skimage import measure
from skimage import io
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from skimage.filters import threshold_otsu
from skimage import data, exposure, img_as_float
from IPython.display import Image 


# Let's load our image and make sure we have the right one

# In[2]:


#Load our image 
input_image = Image.open("domset1.png")
input_pixels = input_image.load()
width, height = input_image.width, input_image.height


# Create an output image that we have to show and convert it to grayscale

# In[3]:


# Create output image
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Convert to grayscale
intensity = np.zeros((width, height))
for x in range(width):
    for y in range(height):
        intensity[x, y] = sum(input_pixels[x, y]) / 3


# Compute the convolution of the image by taking the gradient of the image in the x and y direction. If the magnitude of x>0, draw in the pixel as white, if it is less than 0, draw in the magnitude as black. Output the image or save it to the cwd.

# In[9]:


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
            #print str(index) + " : " + str(r) + ", (x,y) = " + str(x) + ', ' + str(y)
output_image.show('edge.jpg')
#pil_img = Image(output_image)
display(output_image)


# The next step in our process is to count the dots in our domino image. This can be hard to do directly because there is a line in the middle of the domino, so that might be counted as well. I tried using a blob detection mechanism with an IPython widget that can be used to optimize the threshold and the sigma values. The biggest constraint with using skimage is that each picture is so different, thus, the contrast has to be adjusted on some images before using this method. Luckily, for this image, the contrast between black and white is very clear and we won't have to be doing any tuning.

# Let's install the dependencies

# In[14]:


from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_doh
from skimage.color import rgb2gray
from ipywidgets import interact, fixed
from skimage.util import img_as_ubyte


# Let's load the image and convert it to black and white

# In[15]:


image = img_as_ubyte(plt.imread('edge.jpg'))
image_gray = rgb2gray(image)


# Define function that identifies blobs and performs blob detection. The function takes the Laplacian of the gradient and uses a drawing tool which plots circles around the detected dots. The function also annotates the patches by specifiying the number of dots counted and displays them on the image.
# 

# In[20]:


def plot_blobs(max_sigma=30, threshold=0.1, gray=True):
    """
    Plot the image and the blobs that have been found.
    """
    blobs = blob_doh(image_gray, max_sigma=max_sigma, threshold=threshold)
    
    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_title('Domino Dot Counter')
    
    if gray:
        ax.imshow(image_gray, interpolation='nearest', cmap='gray_r')
        circle_color = 'red'
    else:
        ax.imshow(image, interpolation='nearest')
        circle_color = 'yellow'
    for blob in blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color=circle_color, linewidth=2, fill=False)
        ax.add_patch(c)
        plt.annotate('Dots counted = %s' % len(blobs), xy=(120, 120), fontsize=20, color='white')


# Add interaction widget to the code to adjust the parameters to determine optimal image conditions for counting only the dots.

# In[22]:


interact(plot_blobs, max_sigma=(10, 40, 2), threshold=(0.005, 0.02, 0.001));


# The image below describes the image which accurately counts the dots. From here we can move forward in determining how to count blank spaces.

# In[27]:


image = img_as_ubyte(plt.imread('counted.png'))
plt.imshow(image)
plt.axis('off');


# In[ ]:




