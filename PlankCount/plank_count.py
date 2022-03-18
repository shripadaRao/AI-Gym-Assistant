# import cv2
# from datetime import datetime

# # the duration (in seconds)
# duration = 5
# cap = cv2.VideoCapture(0+cv2.CAP_DSHOW)
# qu = 0
# while True:
    
#     ret, frame = cap.read()
#     start_time = datetime.now()
#     diff = (datetime.now() - start_time).seconds # converting into seconds
#     while( diff <= duration ):
#         ret, frame = cap.read()
#         cv2.putText(frame, str(diff), (70,70), cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0), 2, cv2.LINE_AA)# adding timer text
#         cv2.imshow('frame',frame)
#         diff = (datetime.now() - start_time).seconds

#         k = cv2.waitKey(10)
#         if k & 0xFF == ord("r"): # reset the timer
#             break
#         if k & 0xFF == ord("q"): # quit all
#             qu = 1
#             break
        
#     if qu == 1:
#         break

# cap.release()
# cv2.destroyAllWindows()


import os
import mediapipe as mp #docs https://google.github.io/mediapipe/solutions/pose
import cv2
import numpy as np
from datetime import datetime
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 

cap = cv2.VideoCapture(0)
duration =5
## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.75, min_tracking_confidence=0.75) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        ret, frame = cap.read()
        start_time = datetime.now()
        diff = (datetime.now() - start_time).seconds # converting into seconds
        while( diff <= duration ):
            ret, frame = cap.read()
            cv2.putText(frame, str(diff), (70,70), cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0), 2, cv2.LINE_AA)# adding timer text
            cv2.imshow('frame',frame)
            diff = (datetime.now() - start_time).seconds

        cv2.putText(image,'Press "q" to exit', (12,450),cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1, cv2.LINE_AA)             

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

