import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy.editor

# Replace the filename below.
required_video_file = "VPB_4.mp4"
Out_path = 'Videos/'

video = moviepy.editor.VideoFileClip(required_video_file)
video_duration = int(video.duration)
print(video_duration)

times_txt = open('times.txt','w')
for i in range(0,video_duration,3):
    times_txt.write(str(i)+'-'+str(i+2)+'\n')
times_txt.close()

with open("times.txt") as f:
  times = f.readlines()

times = [x.strip() for x in times] 

for time in times:
  starttime = int(time.split("-")[0])
  endtime = int(time.split("-")[1])
  ffmpeg_extract_subclip(required_video_file, starttime, endtime, targetname=Out_path+required_video_file[:-4]+'_'+str(times.index(time)+1)+".mp4")