def fft_template_match(image, template, sigma=50, threshold=0.9):
    
    '''
    This function takes in an image and a template, applies a high-pass filter to both,
    then returns a template match of the filtered images
    '''
    
    #Input Errors
    if sigma < 0:
        print('Error: sigma must be greater than zero.')
    if threshold > 1:
        print('Error: threshold must be between -1 and 1')
    elif threshold < -1:
        print('Error: threshold must be between -1 and 1')
    
    try:
        from skimage.feature import match_template
        from skimage import data, color, img_as_float, filters
        import numpy as np
    except:
        print("Error: could not import modules")
    
    #converts image to grayscale
    image = color.rgb2gray(image)
    template = color.rgb2gray(template)

    #converts image to float
    image = img_as_float(image)    
    template = img_as_float(template)
    
    #applies fourier transformation
    image_tf = np.fft.fft2(image, norm='ortho')
    template_tf = np.fft.fft2(template, norm='ortho')
    
    #move 4 corners to center
    image_tf = np.fft.fftshift(image_tf)
    template_tf = np.fft.fftshift(template_tf)
    
    #create a meshgrid in the x-y plane with the same dimensions as the image
    im_y_shape, im_x_shape = np.shape(image)
    tp_y_shape, tp_x_shape = np.shape(template)
    
    im_xi = np.linspace(0, im_x_shape-1, im_x_shape)
    tp_xi = np.linspace(0, tp_x_shape-1, tp_x_shape)
    
    im_yi = np.linspace(0, im_y_shape-1, im_y_shape)
    tp_yi = np.linspace(0, tp_y_shape-1, tp_y_shape)
    
    im_x, im_y = np.meshgrid(im_xi, im_yi)
    tp_x, tp_y = np.meshgrid(tp_xi, tp_yi)
    
    #get an approximation for the center
    im_center_x, im_center_y = np.round(im_x_shape/2), np.round(im_y_shape/2)
    tp_center_x, tp_center_y = np.round(tp_x_shape/2), np.round(tp_y_shape/2)
    
    #create equation for high-pass filter
    im_filt = 1 - np.exp(-((im_x - im_center_x)**2 + (im_y - im_center_y)**2)/(2*sigma**2))
    tp_filt = 1 - np.exp(-((tp_x - tp_center_x)**2 + (tp_y - tp_center_y)**2)/(2*sigma**2))
  
    #multiply the image by the filter
    image_tf = np.multiply(image_tf, im_filt)
    template_tf = np.multiply(template_tf, tp_filt)
       
    #un-center the image
    image_tf = np.fft.ifftshift(image_tf)
    template_tf = np.fft.ifftshift(template_tf)
    
    #perform and inverse fourier-transform
    image = np.real(np.fft.ifft2(image_tf))
    template = np.real(np.fft.ifft2(template_tf))

    '''
    Now that we've applied a high-pass filter, we need to run it through template matching
    '''
    
    #template matching using skimage function
    result = match_template(image, template)
    
    #Scale the result to consist of values between 0 and 1
    v = result[:, 1]   # result[:, -1] for the last column
    result[:, 1] = (v - v.min()) / (v.max() - v.min())
    
    #convert result into an array of booleans, True if above matching threshold, otherwise False
    bool_result = result > 0.5
    
    #convert the bool result into binary
    bool_result = bool_result*1
    
    return bool_result, image, template, result
    