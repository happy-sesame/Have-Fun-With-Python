from gtts import gTTS
from gtts.lang import tts_langs
from datetime import datetime
import os

GREETINGS_MP3 = "greetings.mp3"
START_GREETINGS = "start " + GREETINGS_MP3

# get current time
now = datetime.now()

# set grettings based on current time
if (now.hour < 12):
    greetings = "Good morning"
    greetings_cn = "早上好"
elif (now.hour<18):
    greetings = "Good afternoon"
    greetings_cn = "下午好"
elif (now.hour < 20):
    greetings = "Good everning"
    greetings_cn = "傍晚好"
else:
    greetings = "Good night"
    greetings_cn = "晚上好"

# create the speech
tts = gTTS(greetings)
tts_cn = gTTS(greetings_cn, lang='zh-cn')

# write the speech to the mp3 file
with open(GREETINGS_MP3,'wb') as f:
    tts.write_to_fp(f)
    tts_cn.write_to_fp(f)

# play the mp3 file
os.system(START_GREETINGS)

# find out what languages are supported by gtts
all_supports_langs = tts_langs('com')
for abr in all_supports_langs.keys():
    print(abr, all_supports_langs.get(abr), sep='\t')















# from playsound import playsound
# HELLO_MP3 = 'hello.mp3'
# HELLP_FR_MP3 = 'hello_bonjour.mp3'
#
# tts = gTTS('hello')
# tts_en = gTTS('hello', lang='en')
# tts_fr = gTTS('bonjour', lang='fr')
#
# tts.save('hello.mp3')
# playsound('hello.mp3')
#
# with open('hello_bonjour.mp3', 'wb') as f:
#     tts_en.write_to_fp(f)
#     tts_fr.write_to_fp(f)
# playsound('hello_bonjour.mp3')
#
# # mp3 = tts.get_urls()
# # ['https://translate.google.com/translate_tts?ie=UTF-8&q=hello&tl=en&ttsspeed=1&total=1&idx=0&client=tw-ob&textlen=5&tk=316070.156329']
# # print (mp3)
