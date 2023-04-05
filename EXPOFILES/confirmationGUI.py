from __future__ import annotations
import functools
import os
import tkinter as tk
from typing import TYPE_CHECKING
import voiceCommand

from confirmations.individualConfirm import individualConfirm
from constants.window import *
import utils.interfaceHelpers as UI
from utils.itemHelpers import clearLocalUI
from database.queries.query import medicationsQuery
from constants.colors import *
from database.classes.medications import Medication

# this is the function called when the button is clicked

if TYPE_CHECKING:
    from UIController import UIController

# img = None

medIndexStart = 0
medIndexEnd = 4

def goToCommand(UIController, medName, medId, filePath):
    UIController.clearUI("Confirm")
    print("Click")
    individualConfirm(UIController, medName=medName, medId=medId, filePath=filePath)
    pass


def goBack(UIController: UIController):
    # clearLocalUI(UIController.canvas, ui_ids)
    UIController.goToHome()

def updateGrid(UIController: UIController, displayedMedications: list[Medication]):
    myButtons = UIController.canvas.nametowidget(name="buttonFrame")
    for index in range(0,4):
        widget = myButtons.grid_slaves(row=index, column=0)[0]
        med = displayedMedications[index]
        widget.configure(text=med.medName)
        widget.configure(
            text=med.medName,
            command=functools.partial(
                goToCommand,
                UIController,
                med.medName,
                med.id,
                (med.folderPath + med.medName + ".png") if med.medName in ['Ciprofloxacin', 'metroNIDAZOLE', 'Rosuvastatin', 'Ibuprofen',  'Tamsulosin'] else 'EXPOFILES/database/meds/Ibuprofen/3/Ibuprofen.png',
            ))

    UIController.root.update()

def iterateForward(UIController: UIController, medications : list[Medication]):
    #iterate list forward 4
    global medIndexStart
    global medIndexEnd
    if (medIndexEnd + 1) <= len(medications):
        medIndexStart += 1
        medIndexEnd += 1
    dispalyedMedications = medications[medIndexStart:medIndexEnd]
    updateGrid(UIController, dispalyedMedications)

def iterateBackwards(UIController: UIController, medications: list[Medication]):
    global medIndexStart
    global medIndexEnd
    if medIndexStart > 0:
        medIndexStart -= 1
        medIndexEnd -= 1
    dispalyedMedications = medications[medIndexStart:medIndexEnd]
    updateGrid(UIController, dispalyedMedications)


def confirmGui(UIController: UIController, hour: str = "00", minute: str = "00"):
    confirm_key = f"{hour}:{minute}"

    if confirm_key in UIController.confirmDict.keys():
        num_meds = len(UIController.confirmDict[confirm_key])
        confirm_label = tk.Label(
            text=f"You have {num_meds} medications", font=("arial", 55, "normal")
        )

        medications = UIController.confirmDict[confirm_key]

        button_frame = tk.Frame(
            UIController.canvas, background=os.getenv("PRIMARY_COLOR"), border=1, name="buttonFrame"
        )
        button_frame.grid(row=0, column=0, sticky="e", rowspan=len(medications))

        for index, med in enumerate(UIController.confirmDict[confirm_key]):
            UI.NewMedBtn(
                master=UIController.canvas,
                text=f"{med}",
                command=functools.partial(goToCommand, UIController, med),
            ).grid(row=index, column=0, pady=GRID_PADDING)

        medications = UIController.confirmDict[confirm_key]

    else:
        print("Returning all medications!")

        medications = medicationsQuery(UIController.conn)

        if(len(medications) < 4):
            displayedMedications = medications
        else:
            displayedMedications = medications[medIndexStart:medIndexEnd]

        button_frame = tk.Frame(
            UIController.canvas, background=os.getenv("PRIMARY_COLOR"), border=1, name="buttonFrame"
        )
        button_frame.grid(row=0, column=0, sticky="e", rowspan=4)

        for index, med in enumerate(displayedMedications):
            UI.NewMedBtn(
                master=button_frame,
                text=f"{med.medName}",
                command=functools.partial(
                    goToCommand,
                    UIController,
                    med.medName,
                    med.id,
                    (med.folderPath + med.medName + ".png") if med.medName in ['Ciprofloxacin', 'metroNIDAZOLE', 'Rosuvastatin', 'Ibuprofen',  'Tamsulosin'] else 'EXPOFILES/database/meds/Ibuprofen/3/Ibuprofen.png',
                ),
            ).grid(row=index, column=0, pady=GRID_PADDING)

    eva_face = UI.evaFace(file="EXPOFILES/assets/evaFaceRedLarge.png")
    microphone = tk.PhotoImage(file="EXPOFILES/assets/microphone.png")

    eva_text = UI.evaText(
        name="evaText",
        canvas=UIController.canvas,
        text=f"Select the \nmedicine to confirm \nfor {hour}:{minute}",
    )
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(275, WINDOW_HEIGHT / 5, window=eva_text)
    )
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(275, WINDOW_HEIGHT / 2, window=eva_face)
    )
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 2, window=button_frame, anchor=tk.E
        )
    )

    iterateFowardButton = tk.Button(
        master=UIController.canvas,
        text="->",
        command=functools.partial(iterateForward, UIController, medications),
        bg="#F44336",
        font=(TEXT_FONT, 48, "normal"),
        fg="#ffffff"
    )

    iterateBackwardsButton = tk.Button(
        master=UIController.canvas,
        text="<-",
        command=functools.partial(iterateBackwards, UIController, medications),
        bg="#F44336",
        font=(TEXT_FONT, 48, "normal"),
        fg="#ffffff"
    )

    go_back_btn = UI.NewExitBtn(
        master=UIController.canvas,
        text="Go Back",
        command=functools.partial(goBack, UIController),
    )

    VC_btn = tk.Button(
        master=UIController.canvas,
        image=microphone,
        command=functools.partial(
            voiceCommand.record_speech, UIController, medications
        ),
        bg="#F44336",
    )
    VC_btn.image = microphone
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(
            0, WINDOW_HEIGHT, window=go_back_btn, anchor=tk.SW
        )
    )
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(
            375, WINDOW_HEIGHT, window=VC_btn, anchor=tk.SW
        )
    )
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(
            1130, WINDOW_HEIGHT / 1.05, window=iterateFowardButton, anchor=tk.SW
        )
    )
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(
            585, WINDOW_HEIGHT / 1.05, window=iterateBackwardsButton, anchor=tk.SW
        )
    )
