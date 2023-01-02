import os


class ffmpeg:

    # Converts the given file to mp3, given file must be in mp4 format
    def convert_mp4_to_mp3(self, audio):
        os.system(
            "ffmpeg -i {} -vn -ab 128k -ar 44100 -y audio.mp3 >/dev/null 2>&1".format(
                audio.replace(
                    "(", "").replace(
                    ")", "")))
        os.system("rm -rf audio.webm")
        return "audio.mp3"

    # stitches the video and audio together if it is in playlist        
    def stitch_together(self, title, playlistName=None):
        if(playlistName != None): playlistName = "{}/".format(playlistName)
        else: playlistName = ""

        os.system(
            "ffmpeg -i audio.mp3 -itsoffset 0 -i video.mp4 -acodec copy -vcodec copy -copyts ./videos/pray.mp4 >/dev/null 2>&1")
        os.system("rm -rf audio.mp3 video.mp4")
        try:
            os.mkdir("./videos/" + playlistName)
        except OSError as error:
            print("Already Directory")
        os.rename(
            "./videos/pray.mp4",
            "./videos/" + playlistName + 
            title.replace(
                "(",
                "").replace(
                ")",
                "").replace(
                " ",
                "") +
            ".mp4")
