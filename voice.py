import pyaudio
import wikipedia

voice= pyaudio.init()
In = input("searching wikipedia/google:")
result= wikipedia.summary(In, sentence=3)
print(result)
voice.say(result)
voice.runAndwait()