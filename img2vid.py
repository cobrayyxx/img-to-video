import cv2
import numpy as np
import os

# choose codec according to format needed
cap = cv2.imread('./save/4_00001.jpeg')
width = cap.shape[1] 
height = cap.shape[0]
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video = cv2.VideoWriter('video2.mp4', fourcc, 30
                        , (width, height))
basepath = "./save"
# Get the list of frames in the input folder
frames = [f for f in os.listdir(basepath) if f.endswith('.jpeg') or f.endswith('.png')]
frames.sort()  # Ensure frames are in the correct order
for entry in frames:
    img = cv2.imread(os.path.join(basepath, entry))
    video.write(img)

video.release()
cv2.destroyAllWindows()
