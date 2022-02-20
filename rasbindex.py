from bluePipeline import bluePipeline
from redPipeline import redPipeline
from networktables import NetworkTables
import cv2

#bottom of camera 15 inches above ground, and angle of aroung 70 to 85 degrees

NetworkTables.initialize(server='10.15.15.2')
table = NetworkTables.getTable('FRCMap')

cap = cv2.VideoCapture(0)

blue = bluePipeline()
red = redPipeline()

#extract distance from visdible area of ball 
def findDist(area):
    dis = 615000*(1/(area+2000))+12.2
    meters = round((0.0254*dis), 3)
    return meters

# extract offset angle from ball position and 
def offset(cx,width):
    return width/2-cx

def sendToTables(pipeline):
    # processing image
    ret, frame = cap.read()
    pipeline.process(frame)
    contours = pipeline.filter_contours_output
    # finding ball countour
    maxArea = 0
    maxIndex = 0
    for i in range(contours):
        if cv2.contourArea(contours[i])> maxArea:
            maxArea = cv2.contourArea(contours[i])
            maxIndex = i
    contour = contours[maxIndex]
    #sending distance and offset to network tables
    distance = findDist(cv2.contourArea(contour))
    (cx, cy), radius = cv2.minEnclosingCircle(contour)
    off = offset(cx, 480)
    table.putNumber("Offset: ", off)
    table.putNumber("Distance: ", distance)

while True:
    if table.getNumber("Alliance: ", 0) == 1:
        sendToTables(red)
    elif table.getBoolean("Alliance: ", 0) == 2:
        sendToTables(blue)