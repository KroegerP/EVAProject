from __future__ import annotations
import functools
import os
import tkinter as tk
from typing import TYPE_CHECKING, Union
from scanBottle.postScanDisplay.refillDate import selectRefillDate
from scanBottle.counter import Counter

from database.mutations.mutation import createMedFromDict
from database.classes.medications import Medication
from scanBottle.postScanDisplay.utility import goToEdit

from constants.colors import *
import utils.interfaceHelpers as UI
from constants.window import *

if TYPE_CHECKING:
    from UIController import UIController


def nextStep(UIController: UIController, textList: list[str], newMed: dict):
    UIController.clearUI("ScanBottle")
    # Next step here, probably dateFilled
    selectRefillDate(UIController, textList, newMed)


def selectOption(
    UIController: UIController, textList: list[str], newMed: dict, newVal: int
):
    print(f"Selected text for med name: {newVal}")
    newMed["timesPerDay"] = newVal

    nextStep(UIController, textList, newMed)
    return


def selectTimesPerDay(
    UIController: UIController,
    textList: list[str],
    newMed: Union[dict, None],
):
    if newMed is None:
        newMed = {}

    title_text = tk.Label(
        UIController.canvas,
        text="How many times per day should you take this?",
        font=(TEXT_FONT, 32, "bold"),
        background=PRIMARY_COLOR,
    )

    my_counter = Counter(UIController.canvas, curVal=1)

    label_frame = tk.Frame(UIController.canvas, background=os.getenv("PRIMARY_COLOR"))
    label_frame.grid(row=0, column=0, sticky="w")

    finish_btn = UI.NewExitBtn(
        master=UIController.canvas,
        text="Finish",
        command=lambda: goToEdit(UIController, newMed),
    )

    next_btn = UI.NewExitBtn(
        master=UIController.canvas,
        text="Next",
        command=functools.partial(
            selectOption, UIController, textList, newMed, my_counter.get_value()
        ),
    )

    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=finish_btn, anchor=tk.SW
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH_PADDING, WINDOW_HEIGHT_PADDING, window=next_btn, anchor=tk.SE
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 2, WINDOW_PADDING, window=title_text, anchor=tk.N
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 2,
            WINDOW_HEIGHT / 2,
            window=my_counter.frame,
            anchor=tk.CENTER,
        )
    )
    return
