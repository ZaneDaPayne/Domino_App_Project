# App GUI development
This branch is for the development of the app GUI and packaging for use on android. See "Setup" if you want to run this on windows, or "Compile" if you want to compile this app yourself on Linux.
 
# Setup
This is fairly straight forward to run on Windows or Linux. Simply install all the dependencies and run the camera.py file. 

*NOTE: If using Spyder you may encouter a problem where your kernel will crash on successive runs. You will need to setup Spyder to execute code in an external console. At the top of the window: Tools->Preferences->Run then under "Console" select "Execute in an external system terminal".*

To run the app on desktop:
1. Install [Kivy](https://kivy.org/doc/stable/installation/installation-windows.html) and other depdencies:
    - [numpy](https://pypi.org/project/numpy/)
    - [KivyMD](https://github.com/HeaTTheatR/KivyMD)
    - [scikit-image](https://scikit-image.org/docs/stable/install.html)
    - [opencv](https://pypi.org/project/opencv-python/)
    - [matplotlib](https://matplotlib.org/3.2.1/users/installing.html)
    - garden.matplotlib
        - With kivy installed, open a terminal and type ```garden install matplotlib```
2. Clone or download the app_gui branch and run the camera.py file

# Compile
Currently you cannot compile the app on Windows because python4android is not supported. You will need to use Linux or MacOS. I have successfully compiled the app on Ubuntu 16.04 and this is the newest version supported by kivy. It may work on newer versions.

We will use Buildozer to compile the app. On the first run (or if you delete the .buildozer file) it will take ~15 min with a download speed of 100 Mb/s since it will clone the current master branch of python4android and install/compile other dependencies.

Open a terminal by pressing Ctrl+Alt+T or by pressing the Windows key and typing "terminal" and pressing Enter. You will need to reinstall all of the above packages. <br/>
*Tip: You can copy and past to and from the console using Ctrl+Shit+C and Ctrl+Shift+V.*
1. Install python 3.6 and pip3
    - To install python 3.6 type ```sudo apt update``` then ```sudo apt install python3.6```. Check that it has installed properly by typing ```python3```. You should see the python 3.6.x and some other stuff then ```>>>``` indicating that you are running python. Type ```exit()``` to exit python.
    - To install pip3 type ```sudo apt install python3-pip```
2. Reinstall the above packages using ```pip3```
3. Install Buildozer
    - Install git with ```pip3 install git```
    - Navigate to where your python packages are installed with ```cd /usr/local/lib/python3.6/dist-packages```
    - Run ```git clone https://github.com/kivy/buildozer.git``` then ```cd buildozer``` and ```sudo python3 setup.py install```
    - Install buildozer dependencies by following [these](https://buildozer.readthedocs.io/en/latest/installation.html#targeting-android) instructions
4. Navigate back to where you downloaded the repository. ```cd ..``` will go up one directory while ```cd ~/``` will go to the home directory
5. Rename the "camera.py" file to "main.py"
6. Plug you Android device in and run ```buildozer -v android debug deploy run```. This will compile the app and install and run it on whatever Android device is detected. This makes it easy to quickly update the app to fix bugs and troublshoot. If you only want to compile the app run ```buildozer -v android debug``` and it will be saved in the "bin" directory that is created.

**Debugging:**

To debug the app while it runs (or doesn't) on Android you will need to install adb. Run ```sudo apt-get install android-tools-adb``` then ```adb logcat | grep python```. This will display only output related to python. If you want to see all the output run ```abd logcat```, although this will move at the speed of light so good luck seeing anything useful. To exit press Ctrl+C.

**Common Errors:**
To fix, open the file explorer and press Ctrl+H to show hidden folders. Delete the .buildozer folder and bin folder. Then redo step 6.

Here is an example of of how the app looks on Windows:

<img src="https://github.com/ZaneDaPayne/Domino_App_Project/blob/Images/detection.PNG" alt="The dots are detected" width="300"/>

# To Do
- [ ] Fix camera orientation
- [ ] Make start screen text resizable
- [ ] Better looking start button
- [ ] Add settings screen (maybe kivymd has something for this)
    - Color of dots
    - Value of blanks
    - Which camera to use
- [ ] Skimage recipe
- [ ] Splash screen logo
- [ ] App icon
- [ ] Make incrementing icons resizable
- [ ] Make detected dots easier to see/more noticable
