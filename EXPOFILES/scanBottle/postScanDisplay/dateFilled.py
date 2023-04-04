from __future__ import annotations
import functools
import os
import tkinter as tk
from typing import TYPE_CHECKING, Union

from database.mutations.mutation import createMedFromDict
from database.classes.medications import Medication
from scanBottle.postScanDisplay.utility import buildDateField, goToEdit

from constants.colors import *
import utils.interfaceHelpers as UI
from constants.window import *

if TYPE_CHECKING:
    from UIController import UIController


def nextStep(UIController: UIController, textList: list[str], newMed: dict):
    UIController.clearUI("ScanBottle")
    # Next step here, probably dateFilled


def selectOption(
    UIController: UIController, textList: list[str], newMed: dict, date_ids: list
):
    date_list = []
    date_string = ""

    date_list.append(date_ids[4].get_value())
    date_list.append(date_ids[5].get_value())
    date_list.append(date_ids[6].get_value())
    date_list.append(date_ids[7].get_value())
    date_list.append(date_ids[0].get_value())
    date_list.append(date_ids[1].get_value())
    date_list.append(date_ids[2].get_value())
    date_list.append(date_ids[3].get_value())

    for index in range(len(date_list)):
        if index in [4, 6]:
            date_string = date_string + "-" + str(date_list[index])
        else:
            date_string = date_string + str(date_list[index])

    print(f"Adding Date Filled: {date_string}")

    newMed["dateFilled"] = date_string

    nextStep(UIController, textList, newMed)
    return


def selectMedName(
    UIController: UIController,
    textList: list[str],
    newMed: Union[dict, None],
):
    if newMed is None:
        newMed = {}

    title_text = tk.Label(
        UIController.canvas,
        text="What day did you fill this?",
        font=(TEXT_FONT, 32, "bold"),
        background=PRIMARY_COLOR,
    )

    label_frame = tk.Frame(UIController.canvas, background=os.getenv("PRIMARY_COLOR"))
    label_frame.grid(row=0, column=0, sticky="w")

    date_ids = buildDateField()  # TODO: ADD VALUE FROM SCAN HERE

    finish_btn = UI.NewExitBtn(
        master=UIController.canvas,
        text="Finish",
        command=lambda: goToEdit(UIController),
    )

    next_btn = UI.NewExitBtn(
        master=UIController.canvas,
        text="Next",
        command=functools.partial(
            selectOption, UIController, textList, newMed, date_ids
        ),
    )

    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=finish_btn, anchor=tk.SW
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=next_btn, anchor=tk.SE
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 2, WINDOW_PADDING, window=title_text, anchor=tk.N
        )
    )
    return
