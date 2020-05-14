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
import weakref

class Screenmanager(ScreenManager):
    pass
    


class MainWindow(Screen):
    def capture(self):
        camera=self.ids.camera
        # camera.play="False"
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
            self.remove_widget(self.plot)
        except:
            print(self.ids)
        
    def createimg(self):
        im = plt.imread("IMG_domino.png")
        plt.imshow(im)
        self.drawimg()
        
    def drawimg(self):
        plot = FigureCanvasKivyAgg(plt.gcf(),id='plot')
        self.ids.checkwindow.add_widget(plot)
        self.plot = weakref.ref(plot)
        print(self.ids)
        plt.close()
    

class Sandbox(App):
    def build(self):
        pass #the kv file does the building
    
       
if __name__=="__main__":
    Sandbox().run()

