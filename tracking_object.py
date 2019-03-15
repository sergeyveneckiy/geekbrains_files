import cv2
import numpy as np

video = cv2.VideoCapture(0)

_, first_frame = video.read()

x=300
y=305
width =100
height=115

myarea = first_frame[y:y+height, x:x+width]
hsv_myarea = cv2.cvtColor(myarea, cv2.COLOR_BGR2HSV)
myarea_hist = cv2.calcHist([hsv_myarea], [0], None, [180], [0,180])
myarea_hist = cv2.normalize(myarea_hist, myarea_hist, 0, 255, cv2.NORM_MINMAX)


term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
   _, frame = video.read()

   cv2.imshow("1", first_frame )
   cv2.imshow("2", myarea )
   #cv2.imshow("3", hsv_myarea)

   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   mask = cv2.calcBackProject([hsv], [0], myarea_hist, [0,180], 1)

   _, track_area = cv2.meanShift(mask, (x, y, width, height), term_criteria)

   x, y, w, h = track_area
   cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)


   #cv2.imshow("Frame_hsv", hsv)
   #cv2.imshow("Frame_mask", mask)
   cv2.imshow("My stream from WebCam", frame)

   key = cv2.waitKey(60)
   if key == 27:
      break

video.release()
cv2.destroyAllWindows()

