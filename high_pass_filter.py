def high_pass(image, sigma=50):
    
    '''
    This function takes in an image and applies a high-pass filter
    
    hw3_function Documentation
    ------------
    
    **Short Summary**
    ------------
    Applies a high-pass filter and performs template matching
    
    
    **Parameters**
    ------------

    * image: array
        The input image 
    * sigma=50: int 
        Respresentive of standard deviation of high-pass filter; increased sigma causes decreased filtering </p>

    **Returns**
    ------------

     * image: array
        The original image with a high-pass filter applied      
        
    **Expanded Description**
    ------------
    **Extended Summary**

This function takes in two images, coverts them to grey-scale float images, applies fourier transform functions found in modules numpy.ftt, applies a high-pass filter, reverts the fourier transform, and returns the image.

    '''
    
    #Input Errors
    if sigma < 0:
        print('Error: sigma must be greater than zero.')
        
    try:
        from skimage.feature import match_template
        from skimage import data, color, img_as_float, filters
        import numpy as np
    except:
        print("Error: could not import modules")
    
    #converts image to grayscale
    image = color.rgb2gray(image)

    #converts image to float
    image = img_as_float(image)    
    
    #applies fourier transformation
    image_tf = np.fft.fft2(image, norm='ortho')
    
    #move 4 corners to center
    image_tf = np.fft.fftshift(image_tf)
    
    #create a meshgrid in the x-y plane with the same dimensions as the image
    im_y_shape, im_x_shape = np.shape(image)

    im_xi = np.linspace(0, im_x_shape-1, im_x_shape)
    
    im_yi = np.linspace(0, im_y_shape-1, im_y_shape)

    im_x, im_y = np.meshgrid(im_xi, im_yi)
    
    #get an approximation for the center
    im_center_x, im_center_y = np.round(im_x_shape/2), np.round(im_y_shape/2)
    
    #create equation for high-pass filter
    im_filt = 1 - np.exp(-((im_x - im_center_x)**2 + (im_y - im_center_y)**2)/(2*sigma**2))
  
    #multiply the image by the filter
    image_tf = np.multiply(image_tf, im_filt)
       
    #un-center the image
    image_tf = np.fft.ifftshift(image_tf)
    
    #perform and inverse fourier-transform
    image = np.real(np.fft.ifft2(image_tf))
    
    return image
    