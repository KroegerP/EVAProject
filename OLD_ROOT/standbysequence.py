import initalSetup
from reminder import *
from voiceRec import *
from drugsCom import *
#import Rams31

def drugsInfo():
    speech.speak("Sure. Can you say the name of the medicine you want information on?")
    display.putText("Sure. Can you say the name of the medicine you want information on?")
    theMedName = command()
    soupy = specificDruginfo(theMedName)

    # tempStr = 'Select an option to learn more information about ' + theMedName
    # Responce.speechandsay(tempStr)
    # Responce.speechandsay('Warnings\nHow should I take\nSide Effects\n or None')
    # specificCommand = command()
    # userSelection(soupy, specificCommand)
    # print("madeit")


def try1():
    print("You've reached the regular sppech sequence. Now you can scan bottles, ask quesitons, or wait for a reminder.")
    count = 1
    while True:
        myCom = command()
        if "about my" in myCom or "information" in myCom or "info" in myCom:
            drugsInfo()
        elif "scan" in myCom:
            drugsInfo()
        #print("inpu")
        #tempinpu = input()
        #if tempinpu == "scan":
        #    Rams31.captureImages()
        print(count)
        count += 1

try1()


