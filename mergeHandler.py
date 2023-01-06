import pytube

import tubePegHandler
from directoryHandler import *


def download_merge(link):
    if ("playlist" not in link):
        if (not is_in_videos(link)):
            tph = tubePegHandler.tubePegHandler()
            audio = tph.download_audio_convert(link)
            tph.download_video_merge(link)
    else:
        p = pytube.Playlist(link)
        for url in p.video_urls:
            name = p.title
            if (not is_in_videos(url, name)):
                tph = tubePegHandler.tubePegHandler()
                audio = tph.download_audio_convert(url)
                tph.download_video_merge(url, name)
