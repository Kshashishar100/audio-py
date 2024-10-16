from gtts import gTTS
from playsound import playsound
audio="speech.mp3"
language='en'
sp=gTTS(text="hi",lang=language,slow=False)
sp.save(audio)
playsound(audio)
print("=====audio is playing=====")