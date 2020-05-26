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
from kivy.utils import platform

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
        
    def capture(self):
        camera=self.ids.camera
        camera.export_to_png("IMG_domino.png")
            
    def detect_domino(self,im):
        im = plt.imread("IMG_domino.png")
        #some processing with im
            
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
        self.score = self.num_dots + self.num_blanks*25
        self.ids.score_label.text = f"Score: {self.score}"
      
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
        self.num_dots, self.num_blanks = 0,0
        self.update_score()
        
    def createimg(self):
        im = plt.imread("IMG_domino.png")
        fig,ax = plt.subplots()
        ax.imshow(im)
        ax.axis("off")
        self.drawimg()
        
    def drawimg(self):
        app = MDApp.get_running_app()
        plot = FigureCanvasKivyAgg(plt.gcf(),pos_hint={"top":1})
        self.ids.checkwindow.add_widget(plot) # add plot to the check window
        
        
        app.dynamic_ids['plot'] = plot
        plt.close() #closes figures for the next run
    

class CameraApp(MDApp):
    dynamic_ids = DictProperty({}) # my own dictionary for dynamic widget ids
    def build(self):
        pass #the kv file does the building
    
       
if __name__=="__main__":
    CameraApp().run()

