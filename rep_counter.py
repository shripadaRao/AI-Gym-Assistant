import mediapipe as mp
import cv2
import numpy as np
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

# Curl counter variables
counter_left = -1
counter_right = -1
#stage = None
up_left = False
up_right = False 

cap = cv2.VideoCapture(0)

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
        
        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            
            # Get coordinates
            shoulder_left = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow_left = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist_left = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            shoulder_right = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            elbow_right = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            wrist_right = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            

            # Calculate angle
            angle_left = calculate_angle(shoulder_left, elbow_left, wrist_left)
            angle_right = calculate_angle(shoulder_right, elbow_right, wrist_right)
            
            # Visualize angle for left hand
            cv2.putText(image, str(angle_left), 
                           tuple(np.multiply(elbow_left, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )

            # Visualize angle for right hand
            cv2.putText(image, str(angle_right), 
                           tuple(np.multiply(elbow_right, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )

            
            # Curl counter logic           
            if not up_left and angle_left > 160:
                up_left = True
                counter_left +=1
            elif angle_left <30 :
                up_left =False

            if not up_right and angle_right > 160:
                up_right = True
                counter_right +=1
            elif angle_right <30 :
                up_right =False
            
                       
        except:
            pass
        

        # Rep data
        cv2.putText(image, 'Left Reps', (12,16), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter_right), 
                    (10,70), 
                    cv2.FONT_HERSHEY_DUPLEX, 2, (255,255,255), 2, cv2.LINE_AA)

        cv2.putText(image, 'Right Reps', (500,16), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter_left), 
                    (500,70), 
                    cv2.FONT_HERSHEY_DUPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        

        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
        
        cv2.imshow('REP COUNTER', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

text = "Congrats!. you have done {} left reps and {} right reps. Total Number of reps is {}.".format(counter_left, counter_right, counter_right+counter_left)
print(text)
print("Please do check the app dir for the auto generated result :)")

total_reps = counter_left + counter_right
path = "pics/pic2"
im = cv2.imread(path + ".png", 1)
font = cv2.FONT_HERSHEY_TRIPLEX

from time import gmtime, strftime
dt_time = strftime("%a, %d %b %Y %H:%M:%S")
cv2.putText(im, '{}'.format(dt_time), (470,800), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

cv2.putText(im, 'Your Left Reps is {}'.format(counter_left), (500,500), font, 1.1, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(im, 'Your Right Reps is {}'.format(counter_right), (500,575), font, 1.1, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(im, 'Your Total Reps is {}'.format(total_reps), (450,700), font, 1.3, (0, 0, 0), 2, cv2.LINE_AA)
cv2.imwrite(path + '_1.jpg', im)