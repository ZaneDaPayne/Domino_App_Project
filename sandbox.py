# -*- coding: utf-8 -*-
"""
Created on Mon May  4 00:32:17 2020

Might get camera to work on android using AndroidCamera class.

@author: Zane
"""


from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.uix.label import Label
import os
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.properties import DictProperty, StringProperty
from kivy.utils import platform
from xcamera import XCamera
import cv2
import PIL
import numpy as np

class ScaleLabel(Image):
    text = StringProperty('')

    def on_text(self, *_):
        # Just get large texture:
        l = Label(text=self.text)
        l.font_size = '2000dp'  # something that'll give texture bigger than phone's screen size
        l.texture_update()
        # Set it to image, it'll be scaled to image size automatically:
        self.texture = l.texture

class MyCamera(XCamera):
    pass

class Screenmanager(ScreenManager):
    pass

class StartScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self._request_android_permissions()
    @staticmethod
    def is_android():
        return platform == 'android'
    def _request_android_permissions(self):
        """
        Requests CAMERA, and read/write permission on Android.
        """
        if not self.is_android():
            return
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.CAMERA,Permission.WRITE_EXTERNAL_STORAGE,
                            Permission.READ_EXTERNAL_STORAGE])   
    
class MainWindow(Screen):
    def capture(self):
        app = MDApp.get_running_app()
        cam = app.dynamic_ids.cam
        x,y = cam.x,cam.y
        width,height = cam.resolution[0],cam.resolution[1]
        data = cam.texture.get_region(x,y,width,height).pixels #this is a byte string of type ubyte
        im = PIL.Image.frombytes(mode='RGBA',size=(width,height),data=data)
        im_arr = np.array(im)
        #print(im_arr)
        # im_arr = np.frombuffer(data, np.uint8).reshape((height,width,4)) #because rgba
        # print(im_arr.shape)
        app.dynamic_ids['im'] = im_arr
        # im = cv2.imdecode(im_arr,cv2.IMREAD_COLOR) #this is a vector
        # print(im)
        
    def create_cam(self):
        app = MDApp.get_running_app()
        if 'cam' in app.dynamic_ids:
            return
        cam = XCamera(index=0,play=True)
        print(cam.resolution)
        print("Camera Created")
        self.ids.camwindow.add_widget(cam)
        app.dynamic_ids['cam'] = cam
        
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
        self.imgdirectory = './'
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
            os.remove(os.path.join(self.imgdirectory,"IMG_domino.jpg"))
        except:
            print("image not removed!")    
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
        app = MDApp.get_running_app()
        
        # if platform=='android':
        #     from android import storage
        #     self.imgdirectory = storage.primary_external_storage_path()
        # self.im = cv2.imread(os.path.join(self.imgdirectory,"IMG_domino.jpg"))
        fig = plt.figure(figsize=(20,20))
        ax = fig.add_axes((0,0,1,1))
        ax.axis("off")
        
        from matplotlib.patches import Rectangle,Circle
        
        im = app.dynamic_ids.im
        r,g,b,a = cv2.split(im)#convert to rgb
        im_c = cv2.merge([r,g,b])
        ax.imshow(im_c) # show color image
        im = cv2.cvtColor(im,cv2.COLOR_RGBA2GRAY)
        print(im.shape)
        print(im_c.shape)
        
        min_size = min(im.shape)*0.01
        max_size = min(im.shape)*0.1
        
        th, thresh = cv2.threshold(im,100,225,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
        contours = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]
        
        dots = []
        for cnt in contours: 
            xy,radius = cv2.minEnclosingCircle(cnt)
            x = cnt[:,0,0]
            y = cnt[:,0,1]
            width,height = max(x)-min(x),max(y)-min(y)
            if (min_size<radius<max_size)&(min(width,height)*1.5>max(width,height)):
                dots.append([xy,radius])
        
        for dot in dots:
            xy, radius = dot
            circ = Circle(xy,radius,fc='none',ec='yellow',lw=2)
            ax.add_patch(circ,)
            
        self.num_dots = len(dots)
        self.update_score()
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







