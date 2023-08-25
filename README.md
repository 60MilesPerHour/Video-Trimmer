## Video Trimmer README

---

### Introduction

The Video Trimmer script provides a simple utility to trim videos based on user input. It allows users to specify how many seconds to trim from the start and the end of each video. All trimmed videos are then moved to a `trimmed_videos` directory for easy identification and access.

---

### Dependencies

1. `os`: Provides a portable way to use operating system-dependent functionality.
2. `sys`: Provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
3. `moviepy.editor`: Offers tools for video editing.
4. `time`: Provides various time-related functions.
5. `ffmpeg`: A multimedia framework, used by `moviepy` for video processing.

---

### Setup and Installation

1. Ensure you have Python installed on your system. If not, download and install Python from [here](https://www.python.org/downloads/).

2. Install `moviepy` which will automatically handle the `ffmpeg` installation for you:
    ```bash
    pip install moviepy
    ```

3. If, for some reason, `ffmpeg` isn't installed with `moviepy`, you can manually download and install `ffmpeg` from [here](https://ffmpeg.org/download.html).

---

### How to Use

1. Run the script using:
    ```bash
    python video_trimmer.py
    ```

2. Follow the on-screen prompts:
    - Input the directory containing the videos you wish to trim.
    - Specify how many seconds to trim from the end of each video.
    - For each video, specify how many seconds to trim from the start.
    - The script will process each video and move the trimmed videos to a `trimmed_videos` directory.

3. Once done, you have the option to trim another video or exit the program.

---

### Notes

- Only `.mp4`, `.mkv`, and `.avi` video formats are supported.
- Ensure you have enough disk space as the script will generate new trimmed video files.
- The script uses `ffmpeg` (which comes with `moviepy`) to handle video processing. Ensure you have `ffmpeg` available on your system or in your PATH.

---

Thank you for using the Video Trimmer! If you encounter any issues or need further assistance, please refer to the official documentation of the dependencies or reach out for support.
