import os
import moviepy
import moviepy.editor

os.chdir(str(input("Enter the directory of the videos: ")))

os.system("ls") # list the files in the directory

video_list = []
for file in os.listdir():
    if file.endswith(".mp4"):
        video_list.append(file)

for i in range(len(os.listdir())):

    video_name2 = video_list[i]
    video_name = "'" + video_list[i] + "'"

    print('\n')
    print("Video Selected: " + video_name2)
    seconds = int(input("Enter the number of seconds you want to trim from the start: "))
    retrieve_duration = moviepy.editor.VideoFileClip(video_name2)

    duration = retrieve_duration.duration

    duration_end = duration - 10

    os.system("ffmpeg -i " + video_name + " -ss " + str(seconds) + " -to " + str(duration_end) + " -c copy " + video_name.replace(".mp4", "_trimmed.mp4"))
    print(video_name2 + " has been trimmed.")
    print("\n")
    print("\n")
