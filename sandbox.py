# -*- coding: utf-8 -*-
"""
Created on Mon May  4 00:32:17 2020

Might get camera to work on android using AndroidCamera class.

@author: Zane
"""


from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
import os
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.properties import DictProperty
from skimage.io import imread

class Screenmanager(ScreenManager):
    pass
    
class MainWindow(Screen):
    def capture(self):
        camera=self.ids.camera
        # camera.play="False"
        camera.export_to_png("IMG_domino.png")
        
        
    def cyclecam(self):
        index = self.ids.camera.index
        try:
            index = index + 1
            self.ids.camera.index = index
        except:
            self.ids.camera.index = 0

class OverlayWindow(Screen): 
    def __init__(self, **kwargs):
        self.add_blanks_val = 0
        self.add_dots_val = 0
        #initialize the variables
        self.num_dots = 0 
        self.num_blanks = 0
        self.score = 0
        self.im = None
        self.dot_template = None
        self.blank_template = None
        super(OverlayWindow, self).__init__(**kwargs)
    
    
    def add_blank(self):
        self.add_blanks_val = self.add_blanks_val + 1
        if self.add_blanks_val>=0:
            self.ids.blank_count.text = f"BLANKS +{self.add_blanks_val}"  
        else:
            self.ids.blank_count.text = f"BLANKS {self.add_blanks_val}"
    def add_dot(self):
        self.add_dots_val = self.add_dots_val + 1
        if self.add_dots_val>=0:
            self.ids.dot_count.text = f"DOTS +{self.add_dots_val}"  
        else:
            self.ids.dot_count.text = f"DOTS {self.add_dots_val}"
    def minus_blank(self):
        self.add_blanks_val = self.add_blanks_val - 1
        if self.add_blanks_val>=0:
            self.ids.blank_count.text = f"BLANKS +{self.add_blanks_val}"  
        else:
            self.ids.blank_count.text = f"BLANKS {self.add_blanks_val}"
    def minus_dot(self):
        self.add_dots_val = self.add_dots_val - 1
        if self.add_dots_val>=0:
            self.ids.dot_count.text = f"DOTS +{self.add_dots_val}"  
        else:
            self.ids.dot_count.text = f"DOTS {self.add_dots_val}"
        
    def removeimg(self):
        try:
            os.remove("IMG_domino.png")
        except:
            pass
        
        try:
            app = MDApp.get_running_app()
            self.ids.checkwindow.remove_widget(app.dynamic_ids.plot) # remove the plot
        except:
            pass
        
    def createimg(self):
        self.im = imread("IMG_domino.png",as_gray=True)
        self.dot_template = plt.imread("dot_template.jpg")
        figsize = self.ids.checkwindow.size # this breaks 
        fig,ax = plt.subplots()
        print(type(self.im))
        self.numdots = self.detect_dots(self.im,self.dot_template)# this draws on the axes as well
        self.drawimg()
        
    def drawimg(self):
        app = MDApp.get_running_app()
        plot = FigureCanvasKivyAgg(plt.gcf())
        self.ids.checkwindow.add_widget(plot) # add plot to the check window   
        app.dynamic_ids['plot'] = plot
        plt.close() #closes figures for the next run
        
    def detect_dots(im,template,threshold=0.6,output_img=True,print_num=False,return_num=True):
        print(type(im))
        from skimage.feature import match_template
        from skimage.transform import resize
        from matplotlib.patches import Rectangle
        from skimage.color import rgb2gray
        from scipy.ndimage import label,find_objects
        from numpy import copy
        import matplotlib.pyplot as plt
        
        im_c = imread("IMG_domino.png")
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
        else:
            pass
        
        # return integer number of dots option
        if return_num == True:
            return numdots
        else:
            pass
    

class Sandbox(MDApp):
    dynamic_ids = DictProperty({}) # my own dictionary for dynamic widget ids
    
    
    def build(self):
        pass #the kv file does the building
    
       
if __name__=="__main__":
    Sandbox().run()










