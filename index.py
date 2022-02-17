from bluePipeline import bluePipeline
from redPipeline import redPipeline
import cv2

cap = cv2.VideoCapture(0)
blue = bluePipeline(cap)
red = bluePipeline(cap)
while True:
    # printing distance from pipeline code
    ret, frame = cap.read()
    red.process(frame)
    cv2.imshow('frame', red.cv_dilate_output)
    img = frame.copy()
    cv2.drawContours(image=img, contours=red.filter_contours_output, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.imshow('frame1', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# while True:
#     ret, frame = cap.read()

#     blue.process(frame)
#     cv2.imshow('frame', blue.cv_dilate_output)

#     img = frame.copy()
#     cv2.drawContours(image=img, contours=blue.filter_contours_output, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
#     cv2.imshow('frame2', img)q
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

cap.release()
cv2.destroyAllWindows()