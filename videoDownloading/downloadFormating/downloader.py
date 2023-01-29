from pytube import YouTube, exceptions, Playlist


class downloader:

    # Gets the title of the youtube video, sometimes it fails retries until it
    # gets it

    def get_title(self, link):
        while True:
            try:
                title = YouTube(link).title
            except exceptions.PytubeError:
                continue
            break
        return title

    ## Returns the songs in the playlist in storable format

    def get_playlist_songs(self, url):
        songsInPlaylist = []
        p = Playlist(url)
        for url in p.video_urls:
            songsInPlaylist.append(self.get_title(url).replace(" ", "").replace(")", "").replace("(", "") + ".mp4")
        return songsInPlaylist

    # Downloads the audio returns audio.mp4

    def download_audio(self, link):

        YouTube(link).streams.filter(
            only_audio=True).desc().first().download(filename="audio.webm")
        return "audio.webm"

    # Downloads the first resolution Video returns the file Name

    def download_video(self, link):
        YouTube(link).streams.filter(
            progressive=True,
            file_extension='mp4').first().download(filename="video.mp4")
        return "video.mp4"
