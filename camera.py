# -*- coding: utf-8 -*-
"""
Created on Mon May  4 00:32:17 2020

@author: Zane
"""


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen

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
    pass
    

class CameraApp(App):
    def build(self):
        pass
    
       
if __name__=="__main__":
    CameraApp().run()

