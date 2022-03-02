import math
from bluePipeline import bluePipeline
from redPipeline import redPipeline
import cv2
#bottom of camera 15 'incehs' above ground, and angle of aroung 70 to 85 degrees
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_EXPOSURE,-4)
blue = bluePipeline()
red = redPipeline()

#select pipeline
pipeline = red

def findDist(area):
    dis = 9.32 + -0.846*math.log(area)
    meters = round((100*dis), 3)
    return meters
def offset(cx,width):
    return (width/2)-(cx/2)
while True:
    # printing distance from pipeline code
    ret, frame = cap.read()
    pipeline.process(frame)
    cv2.imshow('frame', pipeline.cv_dilate_output)
    #img = frame.copy()
    #cv2.imshow('frame1', img)
    contours = pipeline.filter_contours_output
    maxArea = 0
    maxIndex = 0
    width = 620
    if contours:
        for i in range(len(contours)):
            if cv2.contourArea(contours[i])> maxArea:
                maxArea = cv2.contourArea(contours[i])
                maxIndex = i
        contour = contours[maxIndex]
        (cx, cy), radius = cv2.minEnclosingCircle(contour)
        off = offset(cx, width)
        dist = findDist(cv2.contourArea(contour))
        print(f"The ball is {dist} meters away \n with an offset of {off} pixels \n on a frame {width} pixels wide!\n")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
