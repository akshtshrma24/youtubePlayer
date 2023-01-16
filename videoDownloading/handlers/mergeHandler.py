import pytube

import videoDownloading.handlers.tubePegHandler as tubePegHandler
from videoDownloading.handlers.directoryHandler import *


# downloads the files and merges the 2 files together

def download_merge(link):
    if ("playlist" not in link):
        if (not is_in_videos(link)):
            tph = tubePegHandler.TubePegHandler()
            audio = tph.download_audio_convert(link)
            tph.download_video_merge(link)
    else:
        p = pytube.Playlist(link)
        print("here")
        for url in p.video_urls:
            name = p.title
            if (not is_in_videos(url, name)):
                tph = tubePegHandler.TubePegHandler()
                audio = tph.download_audio_convert(url)
                tph.download_video_merge(url, name)
