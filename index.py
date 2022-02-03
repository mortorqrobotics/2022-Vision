import cv2
from bluePipeline import BluePipeline
from grip import GripPipeline

cap = cv2.VideoCapture(0)
blue = BluePipeline()
red = GripPipeline()

# while True:
#     ret, frame = cap.read()
#     blew.process(frame)
#     cv2.imshow('frame', blew.hsv_threshold_output)
#     img = frame
#     if len(red.find_blobs_output) > 0:
#         # print(red.find_blobs_output[0].pt)
#         center = (int(red.find_blobs_output[0].pt[0]), int(red.find_blobs_output[0].pt[1]))
#         img = cv2.circle(frame, center, int(red.find_blobs_output[0].size/2), (0, 0, 255), 8)
#     cv2.imshow('frame2', img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

while True:
    ret, frame = cap.read()

    red.process(frame)
    cv2.imshow('frame', red.hsv_threshold_output)

    img = frame
    if len(red.find_blobs_output) > 0:
        # print(red.find_blobs_output[0].pt)
        center = (int(red.find_blobs_output[0].pt[0]), int(red.find_blobs_output[0].pt[1]))
        img = cv2.circle(frame, center, int(red.find_blobs_output[0].size/2), (0, 0, 255), 8)
    cv2.imshow('frame2', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()