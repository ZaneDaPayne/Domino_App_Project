# iOS Version Development

This branch is the development of the app using Xcode/Swift. The readme + build package will be constantly updated with progress. 

# Setup
The installation for Xcode/Swift is fairly straightforward. It can be run on any Unix/Linux os. If you are a macOS user, Xcode is an application that can be installed directly from the app store. Swift Toolchains and compilers can be installed as provided below. 

1. Download the latest [Swift](https://swift.org/download/#releases) package release.

2. Run the package installer, which will install an Xcode toolchain into /Library/Developer/Toolchains/.

3. An Xcode toolchain (.xctoolchain) includes a copy of the compiler, lldb, and other related tools needed to provide a cohesive development experience for working in a specific version of Swift.

4. Open Xcode’s Preferences, navigate to Components > Toolchains, and select the installed Swift toolchain.

5. Xcode uses the selected toolchain for building Swift code, debugging, and even code completion and syntax coloring. You’ll see a new toolchain indicator in Xcode’s toolbar when Xcode is using a Swift toolchain. Select the Xcode toolchain to go back to Xcode’s built-in tools.

6. Selecting a Swift toolchain affects the Xcode IDE only. To use the Swift toolchain with command-line tools, use xcrun --toolchain swift and xcodebuild -toolchain swift, or add the Swift toolchain to your path as follows:

7. $ export PATH=/Library/Developer/Toolchains/swift-latest.xctoolchain/usr/bin:"${PATH}

Additional Dependencies:
    - [python](https://www.python.org/downloads/)
    - [numpy](https://pypi.org/project/numpy/)
    - [scikit-image](https://scikit-image.org/docs/stable/install.html)
    - [opencv](https://pypi.org/project/opencv-python/)
    - [matplotlib](https://matplotlib.org/3.2.1/users/installing.html)
*Note: Xcode is its language of its own. Part of the code requrires execution/merges of Python script. In order for the app to function correctly, make sure Python is installed. In order to check if it is installed in your working os, run ```where python``` in your bash terminal.


# Compile

The code can be compiled by cloning the repository. Otherwise, downloading and opening the "Domino App" folder on this branch will work as well. Compilation step will be updated with progress.


# Feature Modifications
Features/buttons can be modified in the SceneDelegate.swift file. UISceneSessions and UIWindowSessions have to be linked and modified within each function and later connected in the main storyboard page. To test/run and one of the screens, navigate to the Main.storyboard page and click on the "View Controller" tab at top. Press 'run' using the simulator.


# Build Status

The app build is still in progress. Some buttons currently lack functionalities or are connecting to incorrect functionalities and front camera switching currently does not work. This section will be updated with progress.

Here is an example of the layout so far:


<img src="https://github.com/ZaneDaPayne/Domino_App_Project/blob/Images/ios.png" alt="The dots are detected" width="500"/>

# Things to be Fixed or Added
- [ ] Fix camera switching
- [x ] Back button on View Controller 3 does not connect back to View Controller 1. Similarily, switching between dark and white mode does not change View Controller 1
- [x ] UIIImageView in View Controller 3 needs to read image from captured image on View Controller 2.
- [ ] Backgrounds for Screen 2 and 3???
- [ ] Possibly score setting options
- [ ] Scoring options need to connect with increase and decrease in scores
- [x ] Determine app icon
- [ ] Test run on all devices and make ImageViewer is dynamic
- [x ] Captured image should fit onto ImageViewer. Aspect fit image.
- [ ] Modifications to increase accuracy with detection code.

# Documentation
See the documentation to learn more about [Xcode](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/DevelopiOSAppsSwift/)
See the documentation to learn more about  [Swift](https://swift.org/documentation/)
To learn more about image processing tools, see the [SciKit-Image Documentation](https://scikit-image.org/docs/stable/) and [OpenCV Documentation](https://docs.opencv.org/master/index.html).

