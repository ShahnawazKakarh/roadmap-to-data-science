import os
from moviepy import VideoFileClip

def get_total_video_duration(folderpath):
    """Get total duration of a video file in seconds"""

    total_duration = 0
    for filename in os.listdir(folderpath):
        if filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):
            video_file_path = os.path.join(folderpath, filename)
            try:
                video = VideoFileClip(video_file_path)
                total_duration += video.duration
                video.close()
            except Exception as e:
                print("Error loading video file:: ${video_file_path}: {e}")
                continue

    hours = int(total_duration // 3600)
    minutes = int((total_duration % 3600) // 60)
    seconds = int(total_duration % 60)
    return "Total Duration: {} hours, {} minutes, {} seconds".format(hours, minutes, seconds)


folderpath = "./sample_videos"
print(get_total_video_duration(folderpath))

# command to initialize uv project
#  uv init .


# uv run main.py
# Using CPython 3.11.1 interpreter at: /Users/shahnawazkhan/.pyenv/versions/3.11.1/bin/python3.11
# Creating virtual environment at: .venv
# Hello from project1-uv!
# Creaeted by Shahnawaz Khan using UV library