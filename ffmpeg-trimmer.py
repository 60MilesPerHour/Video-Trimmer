import os
import moviepy
import moviepy.editor

os.chdir('/home/miles/Desktop/Season3/') # change to the directory you want to trim videos from

os.system("ls") # list the files in the directory

num_videos = len(os.listdir())

video_list = []
for file in os.listdir():
    if file.endswith(".mp4"):
        video_list.append(file)

for i in range(num_videos):
    video_name2 = video_list[i]
    video_name = "'" + video_list[i] + "'"
    retrieve_duration = moviepy.editor.VideoFileClip(video_name2)
    duration = retrieve_duration.duration
    # subtract 5 seconds from the duration's end time
    duration_end = duration - 10
    # trim the video
    os.system("ffmpeg -i " + video_name + " -ss 00:00:05 -to " + str(duration_end) + " -c copy " + video_name.replace(".mp4", "_trimmed.mp4"))
    # os.system("ffmpeg -i " + video_name + " -ss 00:00:05 -c copy " + video_name.replace(".mp4", "_trimmed.mp4"))
    print("Video " + str(i+1) + " has been trimmed.")
    print("\n")