import os


class ffmpeg:

    # Converts the given file to mp3, given file must be in mp4 format
    def convert_mp4_to_mp3(self, audio):
        os.system(
            "ffmpeg -i {} -vn -ab 128k -ar 44100 -y audio.mp3 >/dev/null 2>&1".format(
                audio.replace(
                    "(",
                    "").replace(
                    ")",
                    "")))
        os.system("rm -rf audio.webm")
        return "audio.mp3"

    # stitches the video and audio together places it in playlist if in a playlist otherwise 
    # places in videos
    def stitch_together(self, title, playlistName=None):
        if (playlistName is not None):
            playlistName = "{}/".format(playlistName)
        else:
            playlistName = ""
        os.system(
            "ffmpeg -i audio.mp3 -itsoffset 0 -i video.mp4 -acodec copy -vcodec copy -copyts ./videoDownloading/videos/pray.mp4 ")
        os.system("rm -rf audio.mp3 video.mp4")
        try:
            os.mkdir("./videoDownloading/videos/" + playlistName)
        except OSError as error:
            print("Directory Already Exists")
        os.rename(
            "./videoDownloading/videos/pray.mp4",
            "./videoDownloading/videos/" + playlistName +
            title.replace(
                "(",
                "").replace(
                ")",
                "").replace(
                " ",
                "") +
            ".mp4")
        return playlistName + title.replace("(","").replace(")","").replace(" ","") + ".mp4"