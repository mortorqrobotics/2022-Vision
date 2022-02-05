import cv2
from bluePipeline import bluePipeline
from redPipeline import redPipeline

cap = cv2.VideoCapture(1)
blue = bluePipeline()
red = redPipeline()
while True:
    ret, frame = cap.read()

    red.process(frame)
    cv2.imshow('frame', red.cv_dilate_output)

    img = frame.copy()
    # if len(red.find_blobs_output) > 0:
    #     for i in range(0, len(red.find_blobs_output)):
    #         print(red.find_blobs_output[i].pt)
    #     center = (int(red.find_blobs_output[0].pt[0]), int(red.find_blobs_output[0].pt[1]))
    #     img = cv2.circle(frame, center, int(red.find_blobs_output[0].size/2), (0, 0, 255), 8)

    cv2.drawContours(image=img, contours=red.filter_contours_output, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.imshow('frame2', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
while True:
    ret, frame = cap.read()

    blue.process(frame)
    cv2.imshow('frame', blue.cv_dilate_output)

    img = frame.copy()
    cv2.drawContours(image=img, contours=blue.filter_contours_output, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.imshow('frame2', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
cap.release()
cv2.destroyAllWindows()