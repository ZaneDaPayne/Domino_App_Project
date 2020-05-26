# -*- coding: utf-8 -*-
"""
Created on Mon May  4 00:32:17 2020

Might get camera to work on android using AndroidCamera class.

@author: Zane
"""


from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
#from kivy.uix.image import Image
import os
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.properties import DictProperty
from kivy.utils import platform
from xcamera import XCamera

class MyCamera(XCamera):
    pass

class Screenmanager(ScreenManager):
    pass

class StartScreen(Screen):
    pass
    
class MainWindow(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self._request_android_permissions()
    @staticmethod
    def is_android():
        return platform == 'android'
    def _request_android_permissions(self):
        """
        Requests CAMERA permission on Android.
        """
        if not self.is_android():
            return
        from android.permissions import request_permission, Permission
        request_permission(Permission.CAMERA)
        
    # def capture(self):
    #     camera=self.ids.camera
    #     # camera.play="False"
    #     camera.export_to_png("IMG_domino.png")
        
        
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
        self.update_score()
    def add_dot(self):
        self.add_dots_val = self.add_dots_val + 1
        if self.add_dots_val>=0:
            self.ids.dot_count.text = f"DOTS +{self.add_dots_val}"  
        else:
            self.ids.dot_count.text = f"DOTS {self.add_dots_val}"
        self.update_score()
    def minus_blank(self):
        self.add_blanks_val = self.add_blanks_val - 1
        if self.add_blanks_val>=0:
            self.ids.blank_count.text = f"BLANKS +{self.add_blanks_val}"  
        else:
            self.ids.blank_count.text = f"BLANKS {self.add_blanks_val}"
        self.update_score()
    def minus_dot(self):
        self.add_dots_val = self.add_dots_val - 1
        if self.add_dots_val>=0:
            self.ids.dot_count.text = f"DOTS +{self.add_dots_val}"  
        else:
            self.ids.dot_count.text = f"DOTS {self.add_dots_val}"
        self.update_score()
    
    def update_score(self):
        print("update_score\nself.num_dots:",self.num_dots)
        self.score = (self.num_dots+self.add_dots_val)+(self.num_blanks+self.add_blanks_val)*25
        self.ids.score_label.text = f"Score: {self.score}"
        print(self.ids.score_label.text)
        
    def reset(self):
        print("reset")
        try:
            os.remove("IMG_domino.jpg")
        except:
            pass    
        try:
            app = MDApp.get_running_app()
            self.ids.checkwindow.remove_widget(app.dynamic_ids.plot) # remove the plot
        except:
            pass
        self.num_dots, self.num_blanks, self.add_dots_val, self.add_blanks_val = 0,0,0,0
        self.update_score()
        self.ids.blank_count.text = f"BLANKS +0"
        self.ids.dot_count.text = f"DOTS +0"
        
    def createimg(self):
        print("createimg")
        self.im = plt.imread("IMG_domino.jpg")
        self.dot_template = plt.imread("dot_template.jpg")
        figsize = self.ids.checkwindow.size # this breaks 
        fig = plt.figure(figsize=(20,20))
        ax = fig.add_axes((0,0,1,1))
        ax.axis("off")
        
        from skimage.feature import match_template
        from skimage.transform import resize
        from matplotlib.patches import Rectangle
        from skimage.color import rgb2gray
        from scipy.ndimage import label,find_objects
        from numpy import copy
        
        im_c = self.im
        im = rgb2gray(self.im)
        dot = rgb2gray(self.dot_template)
        
        temp_match = match_template(im,dot,pad_input=True) # use template matching to create image with peaks where matches are found       
        thresh=0.6
        labeled_array, num_features = label(temp_match>thresh)
        slices = find_objects(labeled_array)
        self.num_dots = len(slices)
        self.update_score()
        ax.imshow(im_c) # show color image           
        # draw rectangles around dots
        for sl in slices :  
            dy,dx  = sl
            xy     = (dx.start, dy.start)
            width  = (dx.stop - dx.start +10)
            height = (dy.stop - dy.start +10)
            rect = Rectangle(xy,width,height,fc='none',ec='red',lw=2.5)
            ax.add_patch(rect,)

        self.drawimg()
        
    def drawimg(self):
        print("drawimg")
        app = MDApp.get_running_app()
        plot = FigureCanvasKivyAgg(plt.gcf(),pos_hint={"top":1})
        self.ids.checkwindow.add_widget(plot) # add plot to the check window          
        app.dynamic_ids['plot'] = plot
        plt.close() #closes figures for the next run        
    

class Sandbox(MDApp):
    dynamic_ids = DictProperty({}) # my own dictionary for dynamic widget ids  
    def build(self):
        pass #the kv file does the building
    
       
if __name__=="__main__":
    Sandbox().run()







