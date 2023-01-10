import os

import videoDownloading.downloadFormating.downloader as downloader


# Returns true if the yotuuve video is already in videos/<playlistName>

def is_in_videos(link, playlistName=None):
    if (playlistName is not None):
        playlistName = "{}/".format(playlistName)
    else:
        playlistName = ""
    dw = downloader.downloader()
    title = "./videos/" + playlistName + \
        dw.get_title(link).replace("(", "").replace(")", "").replace(" ", "") + ".mp4"
    return os.path.isfile(title)


# Returns a dictionary of all the playlists and the the songs inside of them

def get_file_names():
    directories = []
    for path in os.walk('./videos'):
        directories.append(path)
    directories.pop(0)
    dictionary = {}
    for playListNames in directories:
        dictionary[(playListNames[0]).replace("./videos/", "")] = []
        for fullFileNames in playListNames:
            for fileNames in fullFileNames:
                if (fileNames[0] != "[" and len(fileNames) != 1):
                    dictionary[(playListNames[0]).replace(
                        "./videos/", "")].append(fileNames)

    return dictionary


# deletes the file

def delete_file(file):
    try:
        os.remove("./videos/{}".format(file))
    except OSError as error:
        os.rmdir("./videos/{}".format(file))


# Returns an array of all the .mp4 files inside the

def get_songs(path):
    mylist = os.listdir(path)
    for element in mylist:
        if (".mp4" not in element):
            mylist.remove(element)
    return mylist
