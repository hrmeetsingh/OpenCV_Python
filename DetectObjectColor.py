"""
Program to detect coloured objects using OpenCV
"""
import cv2  # pylint: disable=import-error
import numpy as np  # pylint: disable=import-error


def get_thresholded_img(hsv):
    """
    Get thresholded image
    """
    thresh_img = cv2.inRange(hsv,np.array((cv2.getTrackbarPos('Hue_Low','Trackbars'),cv2.getTrackbarPos('Saturation_Low','Trackbars'),cv2.getTrackbarPos('Value_Low','Trackbars'))),np.array((cv2.getTrackbarPos('Hue_High','Trackbars'),cv2.getTrackbarPos('Saturation_High','Trackbars'),cv2.getTrackbarPos('Value_High','Trackbars'))))
    return thresh_img

def get_track_value(value):
    """
    return trackbar value
    """
    return value


c = cv2.VideoCapture(0)
width,height = c.get(3),c.get(4)
print("frame width and height : ", width, height)

cv2.namedWindow('Output')
cv2.namedWindow('Trackbars', cv2.WINDOW_NORMAL)
cv2.createTrackbar('Hue_Low','Trackbars',0,255, get_track_value)
cv2.createTrackbar('Hue_High','Trackbars',0,255, get_track_value)

cv2.createTrackbar('Saturation_Low','Trackbars',0,255, get_track_value)
cv2.createTrackbar('Saturation_High','Trackbars',0,255, get_track_value)

cv2.createTrackbar('Value_Low','Trackbars',0,255, get_track_value)
cv2.createTrackbar('Value_High','Trackbars',0,255, get_track_value)

cv2.createTrackbar('Caliberate','Trackbars',0,1, get_track_value)

while 1:
    _,f = c.read()
    f = cv2.flip(f,1)
    blur = cv2.medianBlur(f,5)
    hsv = cv2.cvtColor(f,cv2.COLOR_BGR2HSV)
    thrImg = get_thresholded_img(hsv)
    erode = cv2.erode(thrImg,None,iterations = 3)
    dilate = cv2.dilate(erode,None,iterations = 10)

    contours,hierarchy = cv2.findContours(dilate,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cx,cy = x+w/2, y+h/2
        cv2.rectangle(f,(x,y),(x+w,y+h),[0,0,255],2)

    if cv2.getTrackbarPos('Caliberate','Trackbars') == 1:
        cv2.imshow('Output',thrImg)
    else:
        cv2.imshow('Output',f)
    #cv2.waitKey(50)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
c.release()
