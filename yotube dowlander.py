!pip install pytube

from pytube import YouTube

video_url = input("Enter the URL of the YouTube video: ")

yt = YouTube(video_url)
video = yt.streams.first()

video.download('/path/to/download/location')
