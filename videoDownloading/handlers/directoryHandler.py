import os
import shutil

import videoDownloading.downloadFormating.downloader as downloader


# Returns true if the yotuuve video is already in videos/<playlistName>

def is_in_videos(link, playlistName=None):
    if (playlistName is not None):
        playlistName = "{}/".format(playlistName)
    else:
        playlistName = ""
    dw = downloader.downloader()
    videoTitle = dw.get_title(link).replace(
        "(", "").replace(
        ")", "").replace(
            " ", "") + ".mp4"
    title = "./videoDownloading/videos/{}{}".format(playlistName, videoTitle)
    if (os.path.isfile(title)):
        return True
    else:
        print("Downloading: {}".format(title), flush=True)
        return False


# Returns a dictionary of all the playlists and the the songs inside of them

def get_file_names():
    directories = []
    for path in os.walk('./videoDownloading/videos'):
        directories.append(path)
    dictionary = {}
    dictionary["singularVideos"] = directories[0][2]
    directories.pop(0)
    for playListNames in directories:
        dictionary[(playListNames[0]).replace(
            "./videoDownloading/videos/", "")] = []
        for fullFileNames in playListNames:
            for fileNames in fullFileNames:
                if (fileNames[0] != "[" and len(fileNames) != 1):
                    dictionary[(playListNames[0]).replace(
                        "./videoDownloading/videos/", "")].append(fileNames)

    return dictionary


# deletes the file

def delete_file(file):
    try:
        os.remove("./videoDownloading/videos/{}".format(file))
    except OSError as error:
        try:
            shutil.rmtree("./videoDownloading/videos/{}".format(file))
        except BaseException:
            for song in os.listdir("./videoDownloading/videos"):
                if song.endswith(".mp4"):
                    os.remove(os.path.join("./videoDownloading/videos", song))


# Returns an array of all the .mp4 files inside the

def get_songs(path):
    mylist = os.listdir(path)
    for element in mylist:
        if (".mp4" not in element):
            mylist.remove(element)
    return mylist

def delete_not_in_playlist(url, playlistName):
    songsInDirectory = []
    for t in os.walk("./videoDownloading/videos/{}/".format(playlistName)):
        songsInDirectory = t[2]
    
    dw = downloader.downloader()
    songsInPlaylist = dw.get_playlist_songs(url)
    print(songsInDirectory)
    print(songsInPlaylist)
    for song in songsInDirectory:
        if(song not in songsInPlaylist):
            os.remove("./videoDownloading/videos/{}/{}".format(playlistName, song))