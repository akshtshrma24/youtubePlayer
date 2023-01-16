import threading
import time

import pytube

import videoDownloading.handlers.tubePegHandler as tubePegHandler
from videoDownloading.handlers.directoryHandler import *
import videoDownloading.handlers.vlcHandler as vlcHandler
from videoDownloading.handlers.directoryHandler import *

# downloads the files and merges the 2 files together

def download_merge(link):
    if ("playlist" not in link):
        if (not is_in_videos(link)):
            vlc = vlcHandler.VlcHandler()
            tph = tubePegHandler.TubePegHandler()
            audio = tph.download_audio_convert(link)
            name = tph.download_video_merge(link)
            # This should be moved out of this function, Will do make issue so dont forget
            threading.Thread(target=vlc.play_song, args=(name, )).start()
            time.sleep(2)
            delete_file(name)
    else:
        p = pytube.Playlist(link)
        print("here")
        for url in p.video_urls:
            name = p.title
            if (not is_in_videos(url, name)):
                tph = tubePegHandler.TubePegHandler()
                audio = tph.download_audio_convert(url)
                tph.download_video_merge(url, name)
            else:
                print("alredy a thing", flush=True)
