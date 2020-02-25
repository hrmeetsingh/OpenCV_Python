## OpenCV_Python
Python program for detecting colored object using OpenCV library

### What it does
Uses OpenCV library for Python to capture video from the camera and highlights an area of interest with object of the desired color. Lets the user adjust the HSV(Hue,Saturation,Value) values and get the optimal value for the color of the object. Can be used to get HSV values quickly.

### Setup for Mac (Linux wip)
* Ensure Python 3 installed - `python3 --version`
* install virtualenv if doesnot exist already - `pip3 install virtualenv`
* Create virtual environment - `virtualenv venv`
* Activate virtual environment - `source venv/bin/activate`
* Install dependencies inside virtual environment - `pip3 install -r requirements_mac.txt`
* Run program - `python3 DetectObjectColor.py`

### Use
Run program from the command. It shows two windows - Image preview and the other one with trackbars labelled "Hue_Low", "Saturation_Low", "Value_Low" and three other for High values. There is one trackbar for Calibrating the HSV value. With "Calibration" on, the image preview shows "Threshold Image", the one OpenCV uses internally to find and define contours. The trackbar values can be adjusted by approximation to get exact HSV range for the object color.
