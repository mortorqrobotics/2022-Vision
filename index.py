import math
from bluePipeline import bluePipeline
from redPipeline import redPipeline
import cv2
# bottom of camera 15 'incehs' above ground, and angle of around 70 to 85 degrees
# initial camera res is 1080 x 720 reset to 620 x 480
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_EXPOSURE,-4)
blue = bluePipeline()
red = redPipeline()

width = 640
height = 480
camera_angle = 75 # idk if this is right
height_off_ground = 0.5 # 0.5 meters and idk if this is right

diagonal = math.pow((width**2 + height**2), 0.5)
diagonal_FOV = 68.5
px_to_deg = diagonal_FOV/diagonal

#select pipeline
pipeline = red

def findDistBestFit(area):
    dis = 9.32 + -0.846*math.log(area)
    meters = round((100*dis), 3)
    return meters
def findDistTrig(y_off):
    angle = camera_angle + y_off*px_to_deg
    return math.tan(angle)*height_off_ground
def xOffset(cx,width):
    return (width/2)-(cx/2)
def yOffset(cy, height):
    return (height/2)-(cy/2)
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
    if contours:
        for i in range(len(contours)):
            if cv2.contourArea(contours[i])> maxArea:
                maxArea = cv2.contourArea(contours[i])
                maxIndex = i
        contour = contours[maxIndex]
        (cx, cy), radius = cv2.minEnclosingCircle(contour)
        x_off = xOffset(cx, width)
        y_off = yOffset(cy, height)
        dist = findDist(cv2.contourArea(contour))
        print(f"The ball is {dist} meters away \n with an offset of {off} pixels \n on a frame {width} pixels wide!\n")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
