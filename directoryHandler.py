import os

import downloader


#Returns true if the yotuuve video is already in videos/<playlistName>

def is_in_videos(link, playlistName=None):
    if(playlistName != None): playlistName = "{}/".format(playlistName)
    else: playlistName = ""
    dw = downloader.downloader()
    title = "./videos/" + playlistName + dw.get_title(link).replace("(","").replace(")","").replace(" ", "") + ".mp4"
    return os.path.isfile(title)

#Returns the titles of the playlists

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
                if(fileNames[0] != "[" and len(fileNames) != 1): dictionary[(playListNames[0]).replace("./videos/", "")].append(fileNames)
    
    return dictionary

def delete_file(file):
    try:
        os.remove("./videos/{}".format(file))
    except OSError as error:
        print(error)


