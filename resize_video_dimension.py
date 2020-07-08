import os
import cv2
import numpy as np
import moviepy.editor as mp
Input_dir = 'test/'
Out_dir = 'test/'
if not os.path.exists(Out_dir):
    os.makedirs(Out_dir)
videos = os.listdir(Input_dir)
for video in videos:
    clip = mp.VideoFileClip(Input_dir+video)
    clip_resized = clip.resize((320, 240))
    clip_resized.write_videofile(Out_dir+video[:-4]+'out.mp4')