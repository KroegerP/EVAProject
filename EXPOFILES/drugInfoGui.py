from __future__ import annotations
import os
import tkinter as tk
from typing import TYPE_CHECKING

from drugInfo.individualDrug import individualDrug
import functools
import voiceCommand

from database.queries.query import medicationsQuery

from constants.window import *
import utils.interfaceHelpers as UI
from database.classes.medications import Medication

if TYPE_CHECKING:
    from UIController import UIController

medIndexStart = 0
medIndexEnd = 4

def goToCommand(UIController, medName):
    print("Click")
    individualDrug(UIController, medName=medName)
    return

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

def loadingDrugGui(UIController: UIController):
    # This is the section of code which creates the a label
    d_info_label = tk.Label(
        UIController.canvas,
        text="Drug Info",
        bg=os.getenv("PRIMARY_COLOR"),
        font=(os.getenv("TEXT_FONT"), 40, "normal"),
    )

    go_back_btn = UI.NewExitBtn(
        master=UIController.canvas, text="Go Back", command=UIController.goToHome
    )

    UIController.canvasIds["DrugInfo"] = []

    medications = medicationsQuery(UIController.conn)

    if(len(medications) < 4):
            displayedMedications = medications
    else:
        displayedMedications = medications[medIndexStart:medIndexEnd]

    button_frame = tk.Frame(
        UIController.canvas, background=os.getenv("PRIMARY_COLOR"), border=1, name="buttonFrame"
    )
    button_frame.grid(row=0, column=0, sticky="e", rowspan=len(medications))

    for index, med in enumerate(displayedMedications):
        UI.NewMedBtn(
            master=button_frame,
            text=f"{med.medName}",
            command=functools.partial(goToCommand, UIController, med.medName),
        ).grid(row=index, column=0, pady=GRID_PADDING)

    eva_face = UI.evaFace(file="EXPOFILES/assets/evaFaceRedLarge.png")
    microphone = tk.PhotoImage(file="EXPOFILES/assets/microphone.png")
    eva_text = UI.evaText(
        name="evaText",
        canvas=UIController.canvas,
        text="Select a \nmed for information",
    )
    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(275, WINDOW_HEIGHT / 5, window=eva_text)
    )
    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(275, WINDOW_HEIGHT / 2, window=eva_face)
    )
    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 2, window=button_frame, anchor=tk.E
        )
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

    iterateFowardButton = tk.Button(
        master=UIController.canvas,
        text="->",
        command=functools.partial(iterateForward, UIController, medications),
        bg="#F44336",
        font=("Inter", 48, "normal"),
        fg="#ffffff"
    )

    iterateBackwardsButton = tk.Button(
        master=UIController.canvas,
        text="<-",
        command=functools.partial(iterateBackwards, UIController, medications),
        bg="#F44336",
        font=("Inter", 48, "normal"),
        fg="#ffffff"
    )

    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(
            0, WINDOW_HEIGHT, window=go_back_btn, anchor=tk.SW
        )
    )
    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(
            375, WINDOW_HEIGHT, window=VC_btn, anchor=tk.SW
        )
    )

    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20, window=d_info_label, anchor=tk.N
        )
    )

    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(
            1130, WINDOW_HEIGHT / 1.05, window=iterateFowardButton, anchor=tk.SW
        )
    )
    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(
            585, WINDOW_HEIGHT / 1.05, window=iterateBackwardsButton, anchor=tk.SW
        )
    )
