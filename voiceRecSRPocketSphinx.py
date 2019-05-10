#Python 3.6 or lower

import speech_recognition as sr
import sys
import time
from csvInteractor import csvInteractor

class voice:
    def __init__(self):
        self.recognizedWords = ""
        self.attendanceDict = {}
        self.nameList = []
        self.csvOutputBuilder = []

    def nameRecognition(self, r, mic):
        recognizedString = ""
        with mic as source:
            print("Say Something!")
            audio = r.listen(source, timeout = 5, phrase_time_limit=5)
        
        print("Audio Clip acquired!")

        try:
            print("entered try block")
            recognizedString += r.recognize_sphinx(audio, keyword_entries=self.nameList)      #You can add your own command here
            print("Recognized word was:" + recognizedString)
        except sr.UnknownValueError:
            print("say again")
        except sr.RequestError as e:
            print("Errored out.")
            print(e)
            pass
        
        return recognizedString
    def main(self, filename):
        # obtain audio from the microphone
        r = sr.Recognizer()
        mic = sr.Microphone()

        csvName = filename
        csv = csvInteractor()
        csv.pull(csvName)
        #print(csv.attendance_list) #debugging
        for tuplet in csv.attendance_list:
            name = (tuplet[0].lower(), 1.0)
            #print(name)
            self.nameList.append(name)

        for tuplet in self.nameList:
            self.attendanceDict[tuplet[0]] = "Absent"

        #print(nameList)
        #print(attendanceDict)

        for iterator in self.nameList:
            self.recognizedWords += self.nameRecognition(r, mic)

        hereList = self.recognizedWords.split(" ")

        for item in hereList:
            if item in self.attendanceDict:
                #print(item)
                #print(attendanceDict[item])
                self.attendanceDict[item] = "Present"

        for key,value in self.attendanceDict.items():
            temp = (key,value)
            self.csvOutputBuilder.append(temp)

        #print(attendanceDict) #debugging
        print(self.csvOutputBuilder)
        output = csvInteractor()
        output.attendance_list = self.csvOutputBuilder
        output.push("output.csv")
        print("finished")



