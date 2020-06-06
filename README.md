# Domino_App_Project

The goal of this project is to design an android app that uses computer vision to tabulate the score for a game of dominos. 

# Motivation

Totaling scores after a game of dominos can be annoying and the game would be more enjoyable if there was an app to do that. Skimage offers tools and utilities that engage methods for object recognition and detection. This project motivates the use of these packages in order to facilitate a GUI application.

# Build Status

**Phase I: Domino dot recognition (SciKit Image and PIL)**

The goal of this phase is to write a program that can detect and count dots and blank spaces for various domino arrangement. During the coding process, it is important that the program includes salient features to account for noisy backgrounds, blurry images, cropped out dominos, colored dominos and dots, shadows, and other anomalies that may be captured by a phone camera.

**Methods (Codes Available in Repo):
1. Defining and drawing contours
2. ImageProps
3. Edge Detection
4. Filtering (High Pass filtering followed by one of the above methods)
5. Convolutions
6. Blob Detection

**Phase II: App Design (Kivy)**
We are currently in the process of developing an app to integrate our domino detection code using Kivy. The goal is to create a UI that is appealing and user-friendly on Android devices using Python code.

Currently there is no python4android recipe for scikit-image. This means we cannot compile our fully featured app that uses tools from scikit-image to do the detection. Checkout the [app_gui](https://github.com/ZaneDaPayne/Domino_App_Project/tree/app_gui) branch to see the current progress on this and more.

# Features
Some features of the code.

The app allows users to correct for over/under counting of either dots or blank spaces with buttons to increment both. This allows the app to be useable even when the detection misses something or picks something up in the background.


In the future we would like to add setting so the user can change the value of blank spaces if they wish to play different rules.

We also would like to allow the user to change some parameters for the detection code, to improve it's accuracy under specific conditions.

# Documentation
See the documentation to learn more about  [Kivy](https://buildmedia.readthedocs.org/media/pdf/kivy/latest/kivy.pdf) and [KivyMD](https://kivymd.readthedocs.io/en/latest/) .
To learn more about image processing tools, see the [SciKit-Image Documentation](https://scikit-image.org/docs/stable/).
# Installation
When the app is fully functioning on android, an apk will be added to the main branch. 

To install the apk:
1. Download the apk file to your android phone
2. Locate and try to open the file
3. Select allow install from unkown sources
The app should now install and be ready to use.


# Setup
Until the app is fully functional on android you can run the app on your desktop to see the proof of concept.

To run the app on desktop:
1. Install Kivy and other depdencies
    - KivyMD
    - scikit-image
    - opencv
    - matplotlib
    - garden.matplotlib
        - With kivy installed, open a terminal and type ```garden install matplotlib```
2. Clone or download the app_gui branch and run the camera.py file


Here is an example of the detection on a Windows Application

![Image of Detection](https://github.com/ZaneDaPayne/Domino_App_Project/blob/Images/detection.PNG)
