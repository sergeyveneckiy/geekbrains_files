import cv2
import numpy as np

# get stream from webcam
video = cv2.VideoCapture(0)

# create first picture with object that we need to detect
_, first_frame = video.read()

x=300
y=305
width =100
height=115


# cut specific area from first frame and make some manipulatino with color
myarea = first_frame[y:y+height, x:x+width]
hsv_myarea = cv2.cvtColor(myarea, cv2.COLOR_BGR2HSV)
myarea_hist = cv2.calcHist([hsv_myarea], [0], None, [180], [0,180])
myarea_hist = cv2.normalize(myarea_hist, myarea_hist, 0, 255, cv2.NORM_MINMAX)

# settings to meanShift algorithm
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)


# get every frame from webcam in loop
while True:
   _, frame = video.read()


   cv2.imshow("1", first_frame )
   cv2.imshow("2", myarea )
   #cv2.imshow("3", hsv_myarea)

   # color manipulation
   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   mask = cv2.calcBackProject([hsv], [0], myarea_hist, [0,180], 1)

   # launch meanshift algorithm
   _, track_area = cv2.meanShift(mask, (x, y, width, height), term_criteria)

   # draw green rectangle on our area
   x, y, w, h = track_area
   cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)


   #cv2.imshow("Frame_hsv", hsv)
   #cv2.imshow("Frame_mask", mask)
   cv2.imshow("My stream from WebCam", frame)

   # wait key ESC to quit from program
   key = cv2.waitKey(60)
   if key == 27:
      break

# close webcam stream
video.release()
cv2.destroyAllWindows()

