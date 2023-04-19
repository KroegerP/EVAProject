from __future__ import annotations
from datetime import datetime
import functools
import os
import tkinter as tk
from typing import TYPE_CHECKING
from utils.wrappers import on_rpi

from database.mutations.mutation import createConfirm

from constants.colors import *
from constants.window import *
import utils.interfaceHelpers as UI
from utils.itemHelpers import clearLocalUI

# this is the function called when the button is clicked

if TYPE_CHECKING:
    from UIController import UIController


def confirmMedTake(UIController: UIController, medName: str, taken: bool):
    createConfirm(UIController.conn, medName, taken)

    if taken:
        ttl = f"Patient has taken their {medName}."
    else:
        ttl = f"Patient has not taken their {medName}!"

    # if on_rpi() and os.getenv("APP_ENV") == "production":
    UIController.firebase.send_notification(
        title=ttl,
        body="Open the app to see more info.",
        data={"drug": medName, "taken": f"{taken}"},
    )
    print("Completed Confirm!")
    UIController.clearUI("Confirm")
    hour_min = datetime.now().strftime("%H:%M").split(":")

    UIController.goToConfirm(hour=hour_min[0], minute=hour_min[1])
    return


def individualConfirm(
    UIController: UIController, medName: str, medId: str, filePath: str
):
    # Creating a photoimage object to use image
    UIController.clearUI("Confirm")
    photo = tk.PhotoImage(file=r"%s" % filePath)
    photo_label = tk.Label(
        image=photo, width=WINDOW_WIDTH / 2, height=WINDOW_HEIGHT / 2
    )
    photo_label.image = photo
    photo_label.pack()
    confirm_label = tk.Label(
        text=f"Have you taken your {medName}?",
        font=(TEXT_FONT, 55, "normal"),
        background=os.getenv("PRIMARY_COLOR"),
    )

    no_btn = UI.ConfirmationButtons(
        master=UIController.canvas,
        text="No",
        color="#FF4040",
        command=functools.partial(confirmMedTake, UIController, medName, False),
    )
    yes_btn = UI.ConfirmationButtons(
        master=UIController.canvas,
        text="Yes",
        color="#76EE00",
        command=functools.partial(confirmMedTake, UIController, medName, True),
    )
    idk_btn = UI.ConfirmationButtons(
        master=UIController.canvas,
        text="IDK",
        color="#FFB90F",
        command=UIController.goToHome,
    )

    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(
            WINDOW_PADDING, WINDOW_HEIGHT / 2, window=photo_label, anchor=tk.W
        )
    )
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20, window=confirm_label, anchor=tk.N
        )
    )
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 1.5, window=idk_btn, anchor=tk.E
        )
    )
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 2, window=no_btn, anchor=tk.E
        )
    )
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 3, window=yes_btn, anchor=tk.E
        )
    )
