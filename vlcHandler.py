import vlc

vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()

# plays the one song
def play_song(file):
    player.stop()
    if(player != None):
        player.stop()
    media = vlc_instance.media_new("./videos/{}".format(file))
    player.set_media(media)
    player.play()
    
