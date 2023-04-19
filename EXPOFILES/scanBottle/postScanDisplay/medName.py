from __future__ import annotations
import functools
import os
import tkinter as tk
from typing import TYPE_CHECKING, Union

from scanBottle.postScanDisplay.dateFilled import selectDateFilled
from scanBottle.postScanDisplay.utility import goToEdit

from constants.colors import *
import utils.interfaceHelpers as UI
from constants.window import *

if TYPE_CHECKING:
    from UIController import UIController


def nextStep(UIController: UIController, textList: list[str], newMed: dict):
    UIController.clearUI("ScanBottle")
    # Next step here, probably dateFilled
    selectDateFilled(UIController, textList, newMed)


def selectOption(
    UIController: UIController, textList: list[str], newMed: dict, index: int = -1
):
    if index < 0:
        print("No option selected, continuing workflow.")
    else:
        print(f"Selected text for med name: {textList[index]}")
        newMed["medName"] = textList[index].strip().title()

    nextStep(UIController, textList, newMed)
    return


def selectMedName(
    UIController: UIController,
    textList: list[str],
    newMed: Union[dict, None] = None,
):
    if newMed is None:
        newMed = {}

    title_text = tk.Label(
        UIController.canvas,
        text="Which line from the bottle is\nthe Medication Name?\nClick Continue if none match.",
        font=(TEXT_FONT, 32, "bold"),
        background=PRIMARY_COLOR,
    )

    label_frame = tk.Frame(UIController.canvas, background=os.getenv("PRIMARY_COLOR"))
    label_frame.grid(row=0, column=0, sticky="w")

    button_frame = tk.Frame(UIController.canvas, background=os.getenv("PRIMARY_COLOR"))
    button_frame.grid(row=0, column=0, sticky="w", rowspan=len(textList))

    finish_btn = UI.NewExitBtn(
        master=UIController.canvas,
        text="Finish",
        command=lambda: goToEdit(UIController, newMed),
    )

    next_btn = UI.NewExitBtn(
        master=UIController.canvas,
        text="Next",
        command=functools.partial(selectOption, UIController, textList, newMed),
    )

    for index, textLine in enumerate(textList):
        UI.newFrameLabel(label_frame, f"{index + 1}:").grid(
            row=index, column=0, pady=GRID_PADDING
        )
        UI.newFrameButton(
            button_frame,
            name=textLine,
            command=functools.partial(
                selectOption, UIController, textList, newMed, index
            ),
        ).grid(row=index, column=1, pady=GRID_PADDING)

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
            WINDOW_WIDTH / 2,
            WINDOW_HEIGHT / 1.75,
            window=button_frame,
            anchor=tk.CENTER,
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 2.5, WINDOW_HEIGHT / 2, window=label_frame, anchor=tk.CENTER
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 2, WINDOW_PADDING, window=title_text, anchor=tk.N
        )
    )
    return
