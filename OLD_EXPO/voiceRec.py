import speech_recognition as sr
#import speech
# import drugsCom

r = sr.Recognizer()

def navigateCommand():
    curCommand = command()
    print(curCommand)
    return curCommand



    # if curCommand == "eva":
    #     speech.speak("what can i help you with")

    # if "about my" in curCommand or "information" in curCommand or "info" in curCommand:
    #     drugsCom.getMedName()
    #     theMedName = command()
    #     drugsCom.specificDruginfo(theMedName)




def command():
    with sr.Microphone() as source:
        listening = True
        while listening:
            audio = r.listen(source, phrase_time_limit=5) # phase limit will effect things. toggle it accordingly
            if audio:
                try:
                    result = r.recognize_google(audio)
                    result = result.lower()
                    print(result)

                    return result

                    # if result == "eva":
                    #     speech.speak("what can i help you with")
                    #     result = ''
                    # else:
                    #     result = result.replace('eva ', '')
                    #     print(result)

                    # if "about my" in result or "information" in result or "info" in result:
                    #     drugsCom.getMedName()
                    # break
                except sr.UnknownValueError:
                    print()
                except sr.speech_recognition.RequestError:
                    print()




            # try:
            #     result = r.recognize_google(audio)
            #
            # except sr.UnknownValueError:
            #     print("Sorry i can't understand")
            #     break


# def secondCommand():
#     with sr.Microphone() as source:
#         audio = r.listen(source)
#         result = r.recognize_google(audio)
#         print(result)
#         return(result)





