import cv2
from bluePipeline import bluePipeline
from redPipeline import redPipeline

cap = cv2.VideoCapture(1)
blue = bluePipeline()
red = redPipeline()
'''
def MinMax():
    red.__hsv_threshold_hue[0] = cv2.getTrackbarPos('red_H_min','controls')
    red.__hsv_threshold_hue[1] = cv2.getTrackbarPos('red_H_max','controls')
cv2.namedWindow('controls')
cv2.createTrackbar('red_H_min',  'controls', 0, 180, min)
cv2.createTrackbar('red_H_max',  'controls', 0, 180, max)
cv2.resizeWindow('controls', 500, 1)
'''
while True:
    ret, frame = cap.read()
    blue.process(frame)
    cv2.imshow('frame', blue.cv_dilate_output)
    img = frame.copy()
    # if len(blue.find_blobs_output) > 0:
    #     for i in range(0, len(blue.find_blobs_output)):
    #         print(blue.find_blobs_output[i].pt)
    #     center = (int(blue.find_blobs_output[0].pt[0]), int(blue.find_blobs_output[0].pt[1]))
    #     img = cv2.circle(frame, center, int(blue.find_blobs_output[0].size/2), (0, 0, 255), 8)

    cv2.drawContours(image=img, contours=blue.filter_contours_output, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.imshow('frame2', img)
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