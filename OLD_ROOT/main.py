import evaGUI
import initalSetup
import datetime

import textExtraction
from reminder import *
from voiceRec import *
from drugsCom import *
from evaGUI import *
from postScanDisplay import *
from homeScreenGui import *
#import Rams31

def drugsInfo():
    speech.speak("Sure. Can you say the name of the medicine you want information on?")
    display.putText("Sure. Can you say the name of the medicine you want information on?")
    theMedName = command()
    soupy = specificDruginfo(theMedName)

    url = 'https://www.drugs.com/' + theMedName + '.html'

    tempStr = 'Select an option to learn more information about ' + theMedName
    Responce.speechandsay(tempStr)
    Responce.speechandsay('Warnings\nHow should I take\nSide Effects\n or None')
    specificCommand = command()

    userSelection(specificCommand, url)

    # userSelection(soupy, specificCommand)
    # print("madeit")


def regSequence():
    print("You've reached the regular speech sequence. Now you can scan bottles, ask quesitons, or wait for a reminder.")
    count = 1
    #displayHomeScreen()
    while True:
        now = datetime.now()

        print(now.minute)

        if now.minute % 15 == 0:
            checkRunThrough()

        myCom = command()
        if "about my" in myCom or "information" in myCom or "info" in myCom:
            drugsInfo()

        #need to add touch command to that


        elif "scan" in myCom or "bottle" in myCom:
            loadingRamGui()
            displayFunct()

        print("madeit")
        print(count)
        count += 1

regSequence()

