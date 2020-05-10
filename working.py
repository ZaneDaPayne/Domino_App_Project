# -*- coding: utf-8 -*-
"""
Created on Sat May  9 23:03:30 2020

@author: Zane
"""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

class MainWindow(FloatLayout):
    # def capture(self):
    #     camera=self.ids.camera
    #     # camera.play="False"
    #     camera.export_to_png("IMG_domino.png")
    
    # def cyclecam(self):
    #     index = self.ids.camera.index
    #     try:
    #         index = index + 1
    #         self.ids.camera.index = index
    #     except:
    #         self.ids.camera.index = 0
    pass
    

class WorkingApp(App):
    def build(self):
        return MainWindow()
    
       
if __name__=="__main__":
    WorkingApp().run()

