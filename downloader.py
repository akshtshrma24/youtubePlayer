import os

from pytube import YouTube


class downloader:

    # Gets the title of the youtube video
    def get_title(self, link):
        return YouTube(link).title

    # Downloads the audio returns audio.mp4
    def download_audio(self, link):
        YouTube(link).streams.filter(
            only_audio=True).desc().first().download(filename="audio.webm")
        return "audio.webm"

    # Downloads the highest resolution Video returns the file Name
    def download_video(self, link):
        YouTube(link).streams.filter(
            progressive=True,
            file_extension='mp4').desc().first().download(filename="video.mp4")
        return "video.mp4"
