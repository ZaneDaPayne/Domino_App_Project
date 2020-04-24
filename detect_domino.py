# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:03:04 2020

@author: Zane
"""

def detect_dots(im,template,threshold=0.6,output_img=True,print_num=False,return_num=True):
    """Detects dots in supplied image using supplied template of a dot.
    
    Parameters
    ----------
    im : ndarray
        Can be rgba, rgb or grayscale. Dots will be detected in this image
        using the template.
    template : ndarray
        Can be rgba, rgb or grayscale. Template of a dot. This should contain
        the whole dot and some of the background for the best results.
    threshold : float, optional
        Should be between -1 and 1. Used to adjust the minimum confidence of 
        detected dots. Higher will detect more dots. Decrease if background 
        objects are being detected.
    output_img : boolean, optional
        Displays an image with rectangles plotted over detected dots for 
        verification.
    print_num : boolean, optional
        Prints the number of dots detected.
    return_num : boolean, optional
        retruns the number of dots detected as an integer.
        
    Returns
    -------
    int 
        Number of detected dots as integer. Optional, see return_num.
        
    Notes
    -----
    The default threshold was set for light colored dominoes on a dark mostly 
    uniform background.
    The rectangles on the output image are slightly offcenter from the
    detected dots in the 4:30 direction.
    
    Examples
    --------
    >>>import matplotlib.pyplot as plt
    >>>im = plt.imread("path/to/image.jpg")
    >>>template = plt.imread("path/to/template.jpg")
    >>>detect_dots(im,template,thresh=0.74,return_num=False)
    """
        
    from skimage.feature import match_template
    from skimage.transform import resize
    from matplotlib.patches import Rectangle
    from skimage.color import rgb2gray
    from scipy.ndimage import label,find_objects
    from numpy import copy
    import matplotlib.pyplot as plt
    
    im_c = copy(im)
    im = rgb2gray(im_c)
    dot = rgb2gray(template)
    
    temp_match = match_template(im,dot,pad_input=True) # use template matching to create image with peaks where matches are found
    
    thresh=0.6
    labeled_array, num_features = label(temp_match>thresh)
    slices = find_objects(labeled_array)
    numdots = len(slices)
    
    # print number of dots option
    if print_num == True:
        print(f"There are {numdots} dots.")
    else:
        pass
    
    # show output image option
    if output_img == True:
        fig,ax = plt.subplots(figsize=(10,10))
        ax.imshow(im_c,cmap='gray') # show color image
        
        # draw rectangles around dots
        for sl in slices :  
            dy,dx  = sl
            xy     = (dx.start, dy.start)
            width  = (dx.stop - dx.start +10)
            height = (dy.stop - dy.start +10)
            rect = Rectangle(xy,width,height,fc='none',ec='red',lw=2.5)
            ax.add_patch(rect,)
        ax.set_title("Detected dots")
        plt.show()
    else:
        pass
    
    # return integer number of dots option
    if return_num == True:
        return numdots
    else:
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    