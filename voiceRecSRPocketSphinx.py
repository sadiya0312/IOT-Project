import speech_recognition as sr
import sys

global v_command
# obtain audio from the microphone
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)

print("Audio Clip acquired!")

# with sr.Microphone(device_index =2,sample_rate=48000) as source:
#     r.record(source,duration=2)
#     #r.adjust_for_ambient_noise(source)
#     #led.both_off()
#     #led.yellow()
#     print("Command?")
#     audio = r.listen(source)
#     #led.both_off()
#     #led.blue()

try:
    print("entered try block")
    v_command = r.recognize_sphinx(audio, keyword_entries=[('sadiya',1.0),('rafeeq',1.0), ('adam',1.0),('andrew',1.0),('pannapat',1.0),('wakar', 1.0)])      #You can add your own command here
    print("Recognized word was:" + v_command)
except sr.UnknownValueError:
    print("say again")
except sr.RequestError as e:
    print("Errored out.")
    print(e)
    pass


print("finished")



