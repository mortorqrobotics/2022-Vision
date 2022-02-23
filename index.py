from bluePipeline import bluePipeline
from redPipeline import redPipeline
import cv2
#bottom of camera 15 incehs above ground, and angle of aroung 70 to 85 degrees
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_EXPOSURE,-4)
blue = bluePipeline()
red = bluePipeline()
def findDist(area):
    dis = 615000*(1/(area+2000))+12.2
    meters = round((0.0254*dis), 3)
    return meters
def offset(cx,width):
    return width/2-cx
while True:
    # printing distance from pipeline code
    ret, frame = cap.read()
    red.process(frame)
    cv2.imshow('frame', red.cv_dilate_output)
    img = frame.copy()
    cv2.imshow('frame1', img)
    contours = red.filter_contours_output
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
        #print(offset(cx, width))
        print(findDist(cv2.contourArea(contour)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()