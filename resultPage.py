inp =input("Press 'y' to choose to get the auto-generated result.")

import cv2
from time import strftime
import sys
#sys.path.append("Rep Counter/rep_counter")
#from file import start_time, end_time, counter_left,counter_right,total_reps
from rep_counter import *

def result():
    if inp == 'y':
        path_img = "Rep Counter/pics/pic2"
        im = cv2.imread(path_img + ".png", 1)

        font = cv2.FONT_HERSHEY_TRIPLEX

        #end time and all
        dt = strftime("%a, %d %b")
        end_time = strftime("%H:%M:%S")
        cv2.putText(im, 'Start Time : {}'.format(start_time), (500,275), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(im, 'End Time : {}'.format(end_time), (500,325), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(im, '{}'.format(dt), (600,150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        cv2.putText(im, 'Your Left Reps is {}'.format(counter_left), (500,500), font, 1.1, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(im, 'Your Right Reps is {}'.format(counter_right), (500,575), font, 1.1, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(im, 'Your Total Reps is {}'.format(total_reps), (450,650), font, 1.3, (0, 0, 0), 2, cv2.LINE_AA)

        

    else:
        pass