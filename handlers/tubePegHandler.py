import os

import downloadFormating.downloader as downloader
import downloadFormating.ffmpeg as ffmpeg

dw = downloader.downloader()
fg = ffmpeg.ffmpeg()


class tubePegHandler:

    # Downloads and converts the mp4 audio to mp3 audio, returns the file name

    def download_audio_convert(self, link):
        raw_audio = dw.download_audio(link)
        return fg.convert_mp4_to_mp3(raw_audio)

    # Downloads the video and stitches to mp3, saves in correct folder

    def download_video_merge(self, link, playlistName=None):
        dw.download_video(link)
        title = dw.get_title(link).replace("(", "").replace(")", "")
        return fg.stitch_together(title, playlistName)
