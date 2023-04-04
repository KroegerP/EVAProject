from __future__ import annotations

from datetime import datetime
import speech_recognition as sr
from pocketsphinx import LiveSpeech
from typing import TYPE_CHECKING
import functools
from drugInfo import individualDrug
from confirmations import individualConfirm
from reports import individualReport
from scanBottle import individualEdit

if TYPE_CHECKING:
    from UIController import UIController

# Initialize the speech recognition
r = sr.Recognizer()


# Create a function that will be called when the command is given
def record_speech(UIController: UIController, medications):
    # Record the command from the microphone
    myText = UIController.canvas.nametowidget(name="evaText")
    myText.configure(
        text="I'm listening, please say\n the page you wish\n to navigate to."
    )
    UIController.root.update()
    for phrase in LiveSpeech():
        print(phrase)
        if "add" in phrase:
            UIController.goToScanBottle()
            UIController.openBottleScanner()
        elif "edit" in phrase:
            UIController.goToScanBottle()
            UIController.editBottleInfo()
        elif "scan" in phrase:
            UIController.goToScanBottle()
        elif "drug" in phrase:
            UIController.goToDrugInfo()
    # with sr.Microphone() as source:
    #    print("Listening...")
    #    r.pause_threshold = 1
    #    audio = r.listen(source)

    # try:
    # Use the Google Speech Recognition API
    #    command = r.recognize_google(audio).title()
    #    navigateMenu(UIController, command, medications)
    #    print("You said: " + command + "\n")

    # Error handling
    # except sr.UnknownValueError:
    #    myText.configure(
    #        text="I'm sorry, I couldn't understand\n you. Please press the button\nto try again."
    #    )
    #    UIController.root.update()
    #    print("I couldn't understand you. Please try again.")

    return


def navigateMenu(UIController, voiceStr, medications=None):
    date = datetime.now().strftime("%H %M")
    date = date.split(" ")
    if UIController.currentLocation == "Report":
        if medications != None:
            for index, med in enumerate(medications):
                if f"{med.medName}" in voiceStr:
                    individualReport.individualReport(UIController, med.medName)
    elif UIController.currentLocation == "Confirm":
        if medications != None:
            for index, med in enumerate(medications):
                if f"{med.medName}" in voiceStr:
                    individualConfirm.individualConfirm(UIController, med.medName, med)
    elif UIController.currentLocation == "DrugInfo":
        if medications != None:
            for index, med in enumerate(medications):
                if f"{med.medName}" in voiceStr:
                    individualDrug.individualDrug(UIController, med.medName)
    elif UIController.currentLocation == "ScanBottle":
        if medications != None:
            for index, med in enumerate(medications):
                if f"{med.medName}" in voiceStr:
                    individualEdit.individualEdit(UIController, med.medName, None)
    if "Add" in voiceStr:
        UIController.goToScanBottle()
        UIController.openBottleScanner()
    elif "Edit" in voiceStr:
        UIController.goToScanBottle()
        UIController.editBottleInfo()
    elif "Scan" in voiceStr:
        UIController.goToScanBottle()
    elif "Drug" in voiceStr:
        UIController.goToDrugInfo()
    elif "Confirmation" in voiceStr:
        UIController.goToConfirm(hour=date[0], minute=date[1])
    elif "Report" in voiceStr:
        UIController.goToReport()
    else:
        print("try again")
