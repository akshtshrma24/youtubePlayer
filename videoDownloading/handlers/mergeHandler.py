import threading
import time

import pytube

import videoDownloading.handlers.downloadPegHandler as downloadPegHandler
from videoDownloading.handlers.directoryHandler import *
import videoDownloading.handlers.vlcHandler as vlcHandler
from videoDownloading.handlers.directoryHandler import *


# downloads the files and merges the 2 files together

def download_merge(link):
    if ("playlist" not in link):
        if (not is_in_videos(link)):
            vlc = vlcHandler.VlcHandler()
            tph = downloadPegHandler.TubePegHandler()
            audio = tph.download_audio_convert(link)
            name = tph.download_video_merge(link)
            threading.Thread(target=vlc.play_song, args=(name, )).start()
            time.sleep(2)
            delete_file(name)
    else:
        p = pytube.Playlist(link)
        playlistName = p.title
        delete_not_in_playlist(link, playlistName)
        for url in p.video_urls:
            if (not is_in_videos(url, playlistName)):
                tph = downloadPegHandler.TubePegHandler()
                audio = tph.download_audio_convert(url)
                tph.download_video_merge(url, playlistName)
