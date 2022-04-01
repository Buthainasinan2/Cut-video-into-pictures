
import cv2 
import os
import shutil
from datetime import datetime
filename = 'C:\\Users\online\\cut_video.mp4'
if os.path.exists('output'):
   shutil.rmtree('output')
os.makedirs('output')
cap = cv2.VideoCapture(filename)
count = 0
while cap.isOpened():
    ret, frame =cap.read()
    if ret ==True:
        cv2.imshow('window-name', frame)
        t=datetime.now()
        ts=t.strftime('%H%M%S')
        cv2.imwrite(".\\output\\frame%s.jpg"% int(ts), frame)
        count = count+1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyALLWindows()
