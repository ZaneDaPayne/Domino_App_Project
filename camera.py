# -*- coding: utf-8 -*-
"""
Created on Mon May  4 00:32:17 2020

@author: Zane
"""


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

class MainWindow(FloatLayout):
    pass
    

class CameraApp(App):
    def build(self):
        return MainWindow()
    
       
if __name__=="__main__":
    CameraApp().run()

