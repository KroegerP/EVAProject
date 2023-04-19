from __future__ import annotations
from scanBottle.counter import Counter
import os
from typing import TYPE_CHECKING

from constants.window import WINDOW_HEIGHT
import tkinter as tk
from database.mutations.mutation import createMedFromDict

if TYPE_CHECKING:
    from UIController import UIController


def goToEdit(UIController: UIController, newMed: dict):
    if not "medName" in newMed:
        newMed["medName"] = "Unknown"
    print(f"Creating medication with data: {newMed.keys()}")

    createMedFromDict(UIController.conn, newMed, UIController.firebase)

    UIController.clearUI("ScanBottle")
    UIController.individualInfoEdit(newMed["medName"])


def buildDateField(UIController: UIController, curVal: str = "01/01/2023"):
    date_ids = []
    for index in range(0, len(curVal)):
        if curVal[index] == "/":
            forward_slash = tk.Label(
                master=UIController.canvas,
                text=curVal[index],
                background=os.getenv("PRIMARY_COLOR"),
                font=(os.getenv("TEXT_FONT"), 40),
            )
            UIController.canvasIds["ScanBottle"].append(
                UIController.canvas.create_window(
                    ((index) * 125) + 75,
                    WINDOW_HEIGHT / 2,
                    window=forward_slash,
                    anchor=tk.CENTER,
                )
            )
        else:
            if index == 0 or index == 3:
                counter_frame = Counter(
                    UIController.canvas,
                    curVal[index],
                    upperLimit=1,
                    index=index,
                )
            elif index == 6:
                counter_frame = Counter(
                    UIController.canvas,
                    curVal[index],
                    lowerLimit=1,
                    upperLimit=2,
                    index=index,
                )
            else:
                counter_frame = Counter(UIController.canvas, curVal[index], index=index)
            date_ids.append(counter_frame)
            UIController.canvasIds["ScanBottle"].append(
                UIController.canvas.create_window(
                    ((index) * 125) + 75,
                    WINDOW_HEIGHT / 2,
                    window=counter_frame.frame,
                    anchor=tk.CENTER,
                )
            )
    return date_ids
