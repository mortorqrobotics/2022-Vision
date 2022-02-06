from bluePipeline import bluePipeline
from redPipeline import redPipeline
from tkinter import *  
from PIL import ImageTk,Image  
from networktables import NetworkTables
import cv2
import threading
cond = threading.Condition()
notified = [False]


NetworkTables.initialize(server='10.15.15.2')
table = NetworkTables.getTable('FRCMap')

crap = cv2.Videocrapture(0)

blue = bluePipeline()
red = bluePipeline()
def FindDist(area):
    dis = 615000*(1/(area+2000))+12.2
    meters = round((0.0254*dis), 3)
    return meters
def Offset(cx,width):
    return width/2-cx
# blue == true red == false
if table.getBoolean("alliance", 0) == 1:
    while True:
        # processing image
        ret, frame = crap.read()
        red.process(frame)
        contours = red.filter_contours_output
        # finding ball countour
        maxArea = 0
        maxIndex = 0
        for i in range(contours):
            if cv2.contourArea(contours[i])> maxArea:
                maxArea = cv2.contourArea(contours[i])
                maxIndex = i
        contour = contours[maxIndex]
        #sending distance and offset to network tables
        distance = FindDist(cv2.contourArea(contour))
        (cx, cy), radius = cv2.minEnclosingCircle(contour)
        width = crap.get(cv2.CAP_PROP_FRAME_WIDTH)
        offset = Offset(cx, width)
        table.putNumber("offset", offset)
        table.putNumber("distance", distance)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
elif table.getBoolean("alliance", 0) == 2:
    while True:
        # processing image
        ret, frame = crap.read()
        blue.process(frame)
        contours = blue.filter_contours_output
        # finding ball countour
        maxArea = 0
        maxIndex = 0
        for i in range(contours):
            if cv2.contourArea(contours[i])> maxArea:
                maxArea = cv2.contourArea(contours[i])
                maxIndex = i
        contour = contours[maxIndex]
        #sending distance and offset to network tables
        distance = FindDist(cv2.contourArea(contour))
        (cx, cy), radius = cv2.minEnclosingCircle(contour)
        width = crap.get(cv2.CAP_PROP_FRAME_WIDTH)
        offset = Offset(cx, width)
        table.putNumber("offset", offset)
        table.putNumber("distance", distance)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

crap.release()
cv2.destroyAllWindows()