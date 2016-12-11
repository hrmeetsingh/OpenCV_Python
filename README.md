## OpenCV_Python
Python program for detecting colored object using OpenCV library

### What it does
Uses OpenCV library for Python to capture video from the camera and highlights an area of interest with object of the desired color. Lets the user adjust the HSV(Hue,Saturation,Value) values and get the optimal value for the color of the object. Can be used to get HSV values quickly.

### PreRequisites
* Python 2.7.12
* OpenCV 3.1.0 (Read [Installing OpenCV on Ubuntu](http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/) for help on installing OpenCV on Ubuntu. Windows and Mac setups are similar and help available on stackoverflow and other pages)

### Use
Run program from the command. It shows two windows - Image preview and the other one with trackbars labelled "Hue_Low", "Saturation_Low", "Value_Low" and three other for High values. There is one trackbar for Calibrating the HSV value. With "Calibration" on, the image preview shows "Threshold Image", the one OpenCV uses internally to find and define contours. The trackbar values can be adjusted by approximation to get exact HSV range for the object color.
