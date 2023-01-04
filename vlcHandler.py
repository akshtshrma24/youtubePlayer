import vlc

from directoryHandler import * 



# Creates instance so only one instance is running at all times, to avoid multipled videos playing at once
vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()
player.audio_set_volume(90)

# Disable gc collect because seg faults occur after .stop and before media_new type methods
gc.disable()

# plays the one song
def play_vlc(file):
    if(".mp4" not in file):
        songList = get_songs("./videos/{}".format(file))
        media = vlc_instance.media_list_new(songList)
    else:
        media = vlc_instance.media_new("./videos/{}".format(file))
    player.stop()
    player.set_media(media)
    player.play()