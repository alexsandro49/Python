#Toca uma musica (arquivo na pasta).

from pygame import mixer
mixer.init()
mixer.music.load('love_music.mp3')
mixer.music.play(-1)
a = input('Tocar... ')
