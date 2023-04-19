from __future__ import annotations
import os
import tkinter as tk
from tkinter import messagebox
from typing import TYPE_CHECKING, Union
from database.mutations.mutation import archiveMedication
from utils.data_manip import list_to_string
from database.queries.query import getMedByName, getReminderById
from scanBottle.editInfo import editInfo
from database.classes.medications import Medication


from constants.colors import *
import utils.interfaceHelpers as UI
from constants.window import *

if TYPE_CHECKING:
    from UIController import UIController


def camel_case_split(my_str: str):
    words = [[my_str[0]]]

    for c in my_str[1:]:
        if words[-1][-1].islower() and c.isupper():
            words.append(list(c))
        else:
            words[-1].append(c)

    string_arr = ["".join(word) for word in words]
    title_str = ""
    for str in string_arr:
        title_str = title_str + f"{str.capitalize()} "

    return title_str


def goToCorrectionPage(
    UIController: UIController, med: Medication, fieldToEdit: str, curVal: str
):
    print("Going to corrections page!")
    UIController.clearUI("ScanBottle")
    editInfo(UIController, med, fieldToEdit, curVal)
    return


def goBack(UIController: UIController):
    UIController.clearUI("ScanBottle")
    UIController.editBottleInfo()
    return


def confirmDelete(UIController: UIController, medName: str, medId: int):
    if messagebox.askyesno(
        title=f"Archive {medName}?",
        message=f"Are you sure you want to archive {medName}?",
    ):
        archiveMedication(UIController.conn, medId)
        goBack(UIController)
    else:
        print("Canceled archive request")


def individualEdit(
    UIController: UIController, medName: str, update_val: Union[dict, None]
):
    UIController.clearUI("ScanBottle")
    med = getMedByName(UIController.conn, medName)
    weekly_reminder = getReminderById(UIController.conn, med.timesPerWeekId)

    title_text = tk.Label(
        UIController.canvas,
        text="Click on a button to edit the value",
        font=(TEXT_FONT, 32, "bold"),
        background=PRIMARY_COLOR,
    )

    if update_val:
        for item in update_val:
            title_string = camel_case_split(item)

            print(title_string)
            edited_text = tk.Label(
                UIController.canvas,
                text=f"{title_string}\nupdated to\n{update_val[item]}",
                font=(TEXT_FONT, 24, "bold"),
                background=os.getenv("LIGHT_GREEN")
                if title_string.lower() != "errors"
                else os.getenv("LIGHT_RED"),
            )
            # UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(WINDOW_PADDING, WINDOW_WIDTH_PADDING, window=edited_text, anchor=tk.SW))
            UIController.canvasIds["ScanBottle"].append(
                UIController.canvas.create_window(
                    WINDOW_PADDING + 250,
                    WINDOW_HEIGHT / 2,
                    window=edited_text,
                    anchor=tk.E,
                )
            )

    label_frame = tk.Frame(UIController.canvas, background=os.getenv("PRIMARY_COLOR"))
    label_frame.grid(row=0, column=0, sticky="w")

    button_frame = tk.Frame(UIController.canvas, background=os.getenv("PRIMARY_COLOR"))
    button_frame.grid(row=0, column=0, sticky="w", rowspan=5)

    go_back_btn = UI.NewExitBtn(
        master=UIController.canvas, text="Go Back", command=lambda: goBack(UIController)
    )

    archive_btn = UI.NewExitBtn(
        master=UIController.canvas,
        text="Archive",
        command=lambda: confirmDelete(UIController, med.medName, med.id),
    )

    name_label = UI.newFrameLabel(button_frame, "Med Name")
    refills_label = UI.newFrameLabel(button_frame, "Refills Remaining")
    per_week_label = UI.newFrameLabel(button_frame, "Days Notified")
    per_day_label = UI.newFrameLabel(button_frame, "Times Notified")
    refill_date_label = UI.newFrameLabel(button_frame, "Refill Date")
    date_filled_label = UI.newFrameLabel(button_frame, "Date Filled")

    name_label.grid(row=0, column=0, pady=GRID_PADDING)
    refills_label.grid(row=1, column=0, pady=GRID_PADDING)
    per_week_label.grid(row=2, column=0, pady=GRID_PADDING)
    per_day_label.grid(row=3, column=0, pady=GRID_PADDING)
    refill_date_label.grid(row=4, column=0, pady=GRID_PADDING)
    date_filled_label.grid(row=5, column=0, pady=GRID_PADDING)
    # date_added_label.grid(row=6, column=0, pady=GRID_PADDING)

    days_string = list_to_string(weekly_reminder.days_list())

    UI.newFrameButton(
        button_frame,
        med.medName,
        command=lambda: goToCorrectionPage(UIController, med, "medName", med.medName),
    ).grid(row=0, column=1, pady=GRID_PADDING)
    UI.newFrameButton(
        button_frame,
        str(med.refillsLeft),
        command=lambda: goToCorrectionPage(
            UIController, med, "refillsLeft", str(med.refillsLeft)
        ),
    ).grid(row=1, column=1, pady=GRID_PADDING)
    UI.newFrameButton(
        button_frame,
        days_string,
        command=lambda: goToCorrectionPage(
            UIController, med, "timesPerWeek", days_string
        ),
    ).grid(row=2, column=1, pady=GRID_PADDING)
    UI.newFrameButton(
        button_frame,
        str(med.timesPerDay),
        command=lambda: goToCorrectionPage(
            UIController, med, "timesPerDay", str(med.timesPerDay)
        ),
    ).grid(row=3, column=1, pady=GRID_PADDING)
    UI.newFrameButton(
        button_frame,
        med.refillDate.strftime("%A, %B %d, %Y"),
        command=lambda: goToCorrectionPage(
            UIController, med, "refillDate", med.refillDate.strftime("%m/%d/%Y")
        ),
    ).grid(row=4, column=1, pady=GRID_PADDING)
    UI.newFrameButton(
        button_frame,
        med.dateFilled.strftime("%A, %B %d, %Y"),
        command=lambda: goToCorrectionPage(
            UIController, med, "dateFilled", med.dateFilled.strftime("%m/%d/%Y")
        ),
    ).grid(row=5, column=1, pady=GRID_PADDING)

    # if update_val:

    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            0, WINDOW_HEIGHT, window=go_back_btn, anchor=tk.SW
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH_PADDING + 15,
            WINDOW_HEIGHT_PADDING + 15,
            window=archive_btn,
            anchor=tk.SE,
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 1.9, WINDOW_HEIGHT / 2, window=button_frame, anchor=tk.CENTER
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 2, WINDOW_PADDING, window=title_text, anchor=tk.N
        )
    )
    return
