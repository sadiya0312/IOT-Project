#Python 3.6.8
#David's Google API Voice Recognition

import speech_recognition as sr 

# Implemented later:
#
# def getVoiceInput(mic):
#     with mic as source:
#         audio = r.listen(source)
#     return audio

# def googleVoiceRec(r, audio):
#     r.recognize_google(audio)

r = sr.Recognizer()
mic = sr.Microphone()

choice = input("Type 1 to use Google Voice Recognition, type 0 to exit:\n")

while choice != '0':
    with mic as source:
        audio = r.listen(source)
    print("Audio Clip acquired!")
    
    # if choice == '1':
    #     response = {
    #         "success": True,
    #         "error": None,
    #         "transcription": None
    #     }

    #     try:
    #         response["transcription"] = r.recognize_google(audio)
    #     except sr.RequestError:
    #         # API was unreachable or unresponsive
    #         response["success"] = False
    #         response["error"] = "API unavailable"
    #     except sr.UnknownValueError:
    #         # speech was unintelligible
    #         response["error"] = "Unable to recognize speech"

    #     print(response)
    
    if choice == '1':
        returnedText = r.recognize_google(audio)
        print(returnedText)
    else:
        print("\nOther APIs not implemented yet!\n")
    choice = input("Type 0 to exit, 1 to recognize more...")

print("Program Exiting...")
exit()
    