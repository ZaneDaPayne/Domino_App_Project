# Domino_App_Project

The goal of this project is to design an android app that uses computer vision to tabulate the score for a game of dominos. 

# Motivation

Totaling scores after a game of dominos can be annoying and the game would be more enjoyable if there was an app to do that. Skimage offers tools and utilities that engage methods for object recognition and detection. This project motivates the use of these packages in order to facilitate a GUI application.

# Build Status

**Phase I: Domino dot recognition (SciKit-Image, OpenCV, and PIL)**

The goal of this phase is to write a program that can detect and count dots and blank spaces for various domino arrangement. During the coding process, it is important that the program includes salient features to account for noisy backgrounds, blurry images, cropped out dominos, colored dominos and dots, shadows, and other anomalies that may be captured by a phone camera.

**Methods** (Codes Available in [Image-Processing-Codes](https://github.com/ZaneDaPayne/Domino_App_Project/tree/Image-Processing-Codes) branch):
1. Defining and drawing contours
2. ImageProps
3. Edge Detection
4. Filtering (High Pass filtering followed by one of the above methods)
5. Convolutions
6. Blob Detection

**Phase II: App Design (Kivy)**

We are currently in the process of developing an Android app to integrate our domino detection code using Kivy. The goal is to create a UI that is appealing and user-friendly, while still being feature rich.

Currently there is no python4android recipe for scikit-image. This means we cannot compile our fully featured app that uses tools from scikit-image to do the detection. The current working version uses tools from OpenCV instead. Checkout the [app_gui](https://github.com/ZaneDaPayne/Domino_App_Project/tree/app_gui) branch to see the current progress on this and more.

# Features
**Detection:**

Detects and counts regions of contrast that are taken to be dots.

**App:**

The app allows users to correct for over/under counting of either dots or blank spaces with buttons to increment both. This allows the app to be useable even when the detection misses something or detects false positives.

*In the future* we would like to add settings so the user can change the value of blank spaces if they wish to play using different rules, and choose the type of dominoes (white dots, black dots, colored dots) and the type of environment (light, dark) to increase the accuracy of detection.

# Documentation
See the documentation to learn more about  [Kivy](https://buildmedia.readthedocs.org/media/pdf/kivy/latest/kivy.pdf) and [KivyMD](https://kivymd.readthedocs.io/en/latest/) .
To learn more about image processing tools, see the [SciKit-Image Documentation](https://scikit-image.org/docs/stable/) and [OpenCV Documentation](https://docs.opencv.org/master/index.html).
# Installation
We finally have a functioning app available for download. This is still full of bugs and lacking in features, but it functions with careful use.

**NOTE:** You *must* hold the shutter button until you hear the shutter sound (about 1 sec) or the app will crash. It will take about 2 seconds to then change screens and show the score.

To install the apk:
1. Download the apk file to your android phone
2. Locate and try to open the file
3. Select allow install from unkown sources
4. Select open or locate and open the installed app
5. Accept the storage and camera permissions

The app is now ready to use.

# Useage
When first opening the app you should see prompts to allow permissions, tap accept for both.

.
<img src="https://github.com/ZaneDaPayne/Domino_App_Project/blob/Images/Step%201.jpg" alt="Allow camera access" width="300"/>
<img src="https://github.com/ZaneDaPayne/Domino_App_Project/blob/Images/Step%202.jpg" alt="Allow storage access" width="300"/>
.

Press the start button and wait for the camera to initialize (~1 sec).

<img src="https://github.com/ZaneDaPayne/Domino_App_Project/blob/Images/Step%203.jpg" alt="Start" width="300"/>

Hold the shutter button until you hear the shutter sound, or about 1 second, then release to take the picture.

<img src="https://github.com/ZaneDaPayne/Domino_App_Project/blob/Images/Step%204.jpg" alt="Take the picture" width="300"/>

After another 1-2 seconds you will be taken to the scoring screen where you can see the detected dots and the calculated score. Use the buttons labeled DOTS and BLANKS to adjust for over/under counting.

<img src="https://github.com/ZaneDaPayne/Domino_App_Project/blob/Images/Step%205.jpg" alt="The score is displayed" width="300"/>
