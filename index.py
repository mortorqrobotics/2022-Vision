from bluePipeline import bluePipeline
from redPipeline import redPipeline
import cv2
#bottom of camera 15 'incehs' above ground, and angle of aroung 70 to 85 degrees
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_EXPOSURE,-4)
blue = bluePipeline()
red = redPipeline()

__resize_image_width = 320 
__resize_image_height = 240
__resize_image_interpolation = cv2.INTER_CUBIC
resize_image_output = None

#select pipeline
pipeline = red

@staticmethod
def __resize_image(input, width, height, interpolation):
    """Scales and image to an exact size.
    Args:
        input: A numpy.ndarray.
        Width: The desired width in pixels.
        Height: The desired height in pixels.
        interpolation: Opencv enum for the type fo interpolation.
    Returns:
        A numpy.ndarray of the new size.
    """
    return cv2.resize(input, ((int)(width), (int)(height)), 0, 0, interpolation)

def findDist(area):
    dis = 615000*(1/(area+2000))+12.2
    meters = round((0.0254*dis), 3)
    return meters
def offset(cx,width):
    return (width/2)-cx
while True:
    # printing distance from pipeline code
    ret, frame = cap.read()
    # Step Resize_Image0:
    resize_image_output = __resize_image(frame, __resize_image_width, __resize_image_height, __resize_image_interpolation)
    pipeline.process(resize_image_output)
   # cv2.imshow('frame', pipeline.cv_dilate_output)
    cv2.imshow('frame', resize_image_output)
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
