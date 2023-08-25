import os
import sys
import moviepy.editor
from time import sleep

def trimmer():
    # ask for the directory to trim and change dir to it
    directory = input("What directory would you like to trim? ")
    os.chdir(directory)
    # get the name of all the files in the directory
    files = os.listdir(directory)
    # ask for the amount of seconds to trim off the end of each video
    trim_end = int(input("How many seconds would you like to trim off the end of each video? "))

    # go thru each file in the directory
    for file_name in files:
        duration = moviepy.editor.VideoFileClip(file_name).duration
        duration_end = duration - trim_end
        
        # if the file is a video
        if file_name.endswith(".mp4") or file_name.endswith(".mkv") or file_name.endswith(".avi"):
            # ask user how many seconds to trim
            duration_start = int(input(f"How many seconds to trim off '{file_name}'? "))
            # trim the video using ffmpeg
            os.system(f"ffmpeg -i {file_name} -ss {duration_start} -to {duration_end} -c copy {file_name.replace('.','_trimmed.', 1)}")
            # rename the trimmed video to remove '_trimmed' from the filename
            os.rename(file_name.replace('.','_trimmed.', 1), file_name.replace('.','_trimmed.', 1).replace("_trimmed", ""))
            # move the file into the trimmed_videos folder
            if not os.path.exists("trimmed_videos"):
                os.makedirs("trimmed_videos")
            os.system(f"mv {file_name.replace('.','_trimmed.', 1).replace('_trimmed','')} trimmed_videos")

    print("Done trimming videos!")
    sleep(5)

    # ask the user if they want to trim another video
    while True:
        answer = input("Do you want to trim another video? (y/n) ")
        if answer == 'n':
            break
        elif answer == 'y':
            trimmer()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

   
    print("Thank you for using my program! Goodbye!")
    sleep(3)
    sys.exit()

trimmer()
