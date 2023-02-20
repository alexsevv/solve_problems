# https://www.youtube.com/watch?v=_XHV3NjU_og&list=LL&index=3
# переводим текст в голос
import gtts
from playsound import playsound

tts = gtts.gTTS('Привет всем, как жизнь молодая?', lang='ru')
tts.save('converted_text.mp3')
playsound('converted_text.mp3')
