import os
import threading
import time

from videoDownloading.handlers.mergeHandler import download_merge

# Automatically updates the playlist at 2AM

while True:
    if(time.strftime("%H%p", time.localtime()) == "2AM"):
        if(os.path.isfile("./playlists.txt")):
            f = open("./playlists.txt", "r")
            for line in f.readlines():
                print("Updating Playlist")
                threading.Thread(target=download_merge, args=(line[:-1], )).start()
            # Sleep for 20 hours to make sure that it does not run again for a 
            # long time, because it wont need to be ran until next time it is 
            # 2 AM
            time.sleep(72000)
    # Check every hour if it is 2 am, if it is go into the block of code
    # which updates the playlists and goes to sleep for 20 hours
    time.sleep(3600)
    
        
