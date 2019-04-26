#Python 3.6 or lower

import speech_recognition as sr
import sys
import time
from csvReader import csvReader

global v_command
# obtain audio from the microphone
r = sr.Recognizer()
mic = sr.Microphone()

if not len(sys.argv) == 2:
	print("Correct syntax is: \"py(thon3) voiceRecSRPocketSphinx.py nameOfCSV.csv\"")
	print("Terminating...")
	sys.exit()

csvName = sys.argv[1]
csv = csvReader()
csv.pull(csvName)
#print(csv.attendance_list) #debugging
nameList = []
for tuplet in csv.attendance_list:
    name = (tuplet[0].lower(), 1.0)
    print(name)
    nameList.append(name)

print(nameList)

with mic as source:
    print("Say Something!")
    audio = r.listen(source)
    
print("Audio Clip acquired!")

try:
    print("entered try block")
    v_command = r.recognize_sphinx(audio, keyword_entries=nameList)      #You can add your own command here
    print("Recognized word was:" + v_command)
except sr.UnknownValueError:
    print("say again")
except sr.RequestError as e:
    print("Errored out.")
    print(e)
    pass


print("finished")



