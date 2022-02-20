from bluePipeline import bluePipeline
from redPipeline import redPipeline
import cv2

cap = cv2.VideoCapture(1)
# 39000, 34000
#3600, 3200
#900, 700
#cap.set(cv2.CAP_PROP_EXPOSURE,-5)
blue = bluePipeline()
red = redPipeline()
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
    cv2.imshow('frame1', red.resize_image_output)
    # if red.filter_contours_output:
    #     print("ball")
    # else:
    #     print("no ball")
    contours = red.filter_contours_output
    maxArea = 0
    maxIndex = 0
    if contours:
        for i in range(len(contours)):
            if cv2.contourArea(contours[i])> maxArea:
                maxArea = cv2.contourArea(contours[i])
                maxIndex = i
        contour = contours[maxIndex]
        #sending distance and offset to network tables
        print(findDist(cv2.contourArea(contour)*4))
        (cx, cy), radius = cv2.minEnclosingCircle(contour)
        width = 320
        #print(offset(cx, width))
    cv2.drawContours(image=img, contours=red.filter_contours_output, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()