import pymusicplayer
import time

mp = pymusicplayer.MusicPlayer()
mp.add_song('sample4.flac', 'Song')
print(mp.get_queue())
mp.play()
time.sleep(60)
