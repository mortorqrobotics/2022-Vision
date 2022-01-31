import cv2
from bluePipeline import BluePipeline
from redPipline import RedPipeline

cap = cv2.VideoCapture(0)
blew = BluePipeline()
read = RedPipeline()

while True:
    ret, frame = cap.read()

    blew.process(frame)
    cv2.imshow('frame', blew.hsv_threshold_output)
    img = frame
    if len(read.find_blobs_output) > 0:
        # print(read.find_blobs_output[0].pt)
        center = (int(read.find_blobs_output[0].pt[0]), int(read.find_blobs_output[0].pt[1]))
        img = cv2.circle(frame, center, int(read.find_blobs_output[0].size/2), (0, 0, 255), 8)
    cv2.imshow('frame2', img)

    # if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

while True:
    ret, frame = cap.read()

    read.process(frame)
    cv2.imshow('frame', read.rgb_threshold_output)

    img = frame
    if len(read.find_blobs_output) > 0:
        # print(read.find_blobs_output[0].pt)
        center = (int(read.find_blobs_output[0].pt[0]), int(read.find_blobs_output[0].pt[1]))
        img = cv2.circle(frame, center, int(read.find_blobs_output[0].size/2), (0, 0, 255), 8)
    cv2.imshow('frame2', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()