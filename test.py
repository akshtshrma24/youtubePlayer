import vlc
import time

vlc_instance = vlc.Instance()
     
# creating a media player
player = vlc_instance.media_player_new()
    
# creating a media
media = vlc_instance.media_new("./videos/cuttingHair")
    
# setting media to the player
player.set_media(media)
    
# play the video
player.play()
    
# wait time
time.sleep(5)
    
player.pause()

# getting the duration of the video
duration = player.get_length()
    