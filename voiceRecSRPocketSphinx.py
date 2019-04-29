#Python 3.6 or lower

import speech_recognition as sr
import sys
import time
from csvInteractor import csvInteractor

recognizedWords = ""
attendanceDict = {}
nameList = []
csvOutputBuilder = []

def nameRecognition(mic):
    recognizedString = ""
    with mic as source:
        print("Say Something!")
        audio = r.listen(source, timeout = 5, phrase_time_limit=5)
    
    print("Audio Clip acquired!")

    try:
        print("entered try block")
        recognizedString += r.recognize_sphinx(audio, keyword_entries=nameList)      #You can add your own command here
        print("Recognized word was:" + recognizedString)
    except sr.UnknownValueError:
        print("say again")
    except sr.RequestError as e:
        print("Errored out.")
        print(e)
        pass
    
    return recognizedString

# obtain audio from the microphone
r = sr.Recognizer()
mic = sr.Microphone()

if not len(sys.argv) == 2:
	print("Correct syntax is: \"py(thon3) voiceRecSRPocketSphinx.py nameOfCSV.csv\"")
	print("Terminating...")
	sys.exit()

csvName = sys.argv[1]
csv = csvInteractor()
csv.pull(csvName)
#print(csv.attendance_list) #debugging
for tuplet in csv.attendance_list:
    name = (tuplet[0].lower(), 1.0)
    print(name)
    nameList.append(name)

for tuplet in nameList:
    attendanceDict[tuplet[0]] = "Absent"

print(nameList)
print(attendanceDict)

for iterator in nameList:
    recognizedWords += nameRecognition(mic)

hereList = recognizedWords.split(" ")

for item in hereList:
    if item in attendanceDict:
        print(item)
        print(attendanceDict[item])
        attendanceDict[item] = "Present"

for key,value in attendanceDict.items():
    temp = (key,value)
    csvOutputBuilder.append(temp)

print(attendanceDict)
print(csvOutputBuilder)
print("finished")



