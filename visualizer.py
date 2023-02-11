import io
import os
import cv2
import glob
import gc
import pandas as pd
from os.path import basename

files = glob.glob('vis/*.mp4')
df = pd.read_csv('plotty.csv',sep=',',error_bad_lines=False)

j = 0
for file in files:
    print(str(file))
    cap = cv2.VideoCapture(file)
    out = cv2.VideoWriter(os.path.join('plotted',basename(file)),0x7634706d,25, (320,240))
    while(True): 
        for i in range (0,len(df)):
            # Capture frames in the video 
            ret, frame = cap.read() 
            # describe the type of font 
            # to be used. 
            font = cv2.FONT_HERSHEY_SIMPLEX 
        
            # Use putText() method for 
            # inserting text on video 
            cv2.putText(frame,  
                        'Predicted Label: '+str(df.iloc[j,1]), (20, 20),  
                        font, 0.5,  
                        (255, 0, 0),  
                        1,  
                        cv2.LINE_4)

            cv2.putText(frame,  
                        'Truth Label: '+str(df.iloc[j,2]), (20, 40),  
                        font, 0.5,  
                        (255, 0, 0),  
                        1,  
                        cv2.LINE_4)
            out.write(frame)
            print('printed for frame: '+str(i))
            gc.collect()

        break
        exit()
        gc.collect()
    # release the cap object 
    cap.release()
    out.release()
    cv2.destroyAllWindows() 
    gc.collect()
    j = j+1