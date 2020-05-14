# -*- coding: utf-8 -*-
"""
Created on Mon May  4 00:32:17 2020

Might get camera to work on android using AndroidCamera class.

@author: Zane
"""


from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
import os
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.properties import DictProperty

class Screenmanager(ScreenManager):
    pass
    
class MainWindow(Screen):
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
        
    def removeimg(self):
        try:
            os.remove("IMG_domino.png")
        except:
            pass
        
        try:
            app = App.get_running_app()
            self.ids.checkwindow.remove_widget(app.dynamic_ids.plot) # remove the plot
        except:
            pass
        
    def createimg(self):
        im = plt.imread("IMG_domino.png")
        fig,ax = plt.subplots()
        ax.imshow(im)
        ax.axis("off")
        self.drawimg()
        
    def drawimg(self):
        app = App.get_running_app()
        plot = FigureCanvasKivyAgg(plt.gcf())
        self.ids.checkwindow.add_widget(plot) # add plot to the check window
        
        
        app.dynamic_ids['plot'] = plot
        plt.close() #closes figures for the next run
    

class CameraApp(App):
    dynamic_ids = DictProperty({}) # my own dictionary for dynamic widget ids
    def build(self):
        pass #the kv file does the building
    
       
if __name__=="__main__":
    CameraApp().run()

