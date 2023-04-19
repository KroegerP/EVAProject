from __future__ import annotations
import functools
import os
import tkinter as tk
from PIL import Image
from typing import TYPE_CHECKING, Optional
from scanBottle.postScanDisplay.medName import selectMedName

from utils.wrappers import on_rpi
from scanBottle.camera.cameraControls import CV2Camera
from constants.colors import *
from constants.window import *
import utils.interfaceHelpers as UI

# this is the function called when the button is clicked

if TYPE_CHECKING:
    from UIController import UIController

textLines = []


def increment_image_count(UIController: UIController):
    label: tk.Label = UIController.canvas.nametowidget("!labelNumPhotos")
    num_photos = int(label["text"][-1])
    num_photos += 1
    print(num_photos)
    label.config(text=f"Photos taken: {num_photos}")
    return num_photos


def save_image(temp_name: str, cur_img: Image) -> str:
    file_name = f"{temp_name}.jpg"
    file_directory = f"EXPOFILES/database/new/"
    if cur_img is not None:
        if not os.path.exists(file_directory):
            os.mkdir(file_directory)

        full_path = os.path.join(file_directory, file_name)

        if os.path.exists(full_path):
            os.remove(full_path)

        rgb_img = cur_img.convert("RGB")
        rgb_img.save(full_path, "JPEG")
        cur_img.close()
        rgb_img.close()
        return full_path
    else:
        print("ERROR: Unable to retrieve image from camera!")
        return None


def captureImage(UIController: UIController, camera: CV2Camera):
    global textLines

    num_photos = increment_image_count(UIController)

    cur_img = camera.get_image()

    file_path = camera.save_image(num_photos, cur_img)

    parsed_text = camera.parse_image(file_path)

    print(parsed_text)

    textLines.extend(parsed_text)

    print("Click!")
    return


def goToEdit(UIController: UIController, camera: Optional[CV2Camera] = None):
    global textLines
    print("Going to med info edit")
    if on_rpi() and camera is not None:
        camera.stop_camera()

    if len(textLines) == 0:
        textLines = ["No Text Scanned"]
    UIController.clearUI("ScanBottle")
    selectMedName(UIController, textList=textLines)
    return


def goBack(UIController: UIController, camera: CV2Camera):
    print("Canceled")
    if on_rpi():
        camera.stop_camera()
    UIController.clearUI("ScanBottle")
    return


def scanningFunction(UIController: UIController):
    global text_lines
    images_taken = tk.Label(
        master=UIController.canvas,
        name="!labelNumPhotos",
        text=f"Photos taken: 0",
        background=os.getenv("PRIMARY_COLOR"),
    )

    # Check if we're on the raspberry pi or not
    if on_rpi():
        camera = CV2Camera(UIController.canvas)
        UIController.canvasIds["ScanBottle"].append(
            UIController.canvas.create_window(
                WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, window=camera.label
            )
        )

        capture_img_btn = UI.NewExitBtn(
            master=UIController.canvas,
            text="Capture Image",
            command=functools.partial(captureImage, UIController, camera),
        )

        UIController.canvasIds["ScanBottle"].append(
            UIController.canvas.create_window(
                WINDOW_WIDTH_PADDING,
                WINDOW_HEIGHT_PADDING,
                window=capture_img_btn,
                anchor=tk.SE,
            )
        )
        done_btn = UI.NewExitBtn(
            master=UIController.canvas,
            text="Done",
            command=functools.partial(goToEdit, UIController, camera),
        )
    else:
        done_btn = UI.NewExitBtn(
            master=UIController.canvas,
            text="Done",
            command=functools.partial(goToEdit, UIController),
        )
    cancel_btn = UI.NewExitBtn(
        master=UIController.canvas, text="Cancel", command=UIController.goToScanBottle
    )

    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_PADDING, WINDOW_PADDING, window=images_taken, anchor=tk.NW
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 2, WINDOW_HEIGHT_PADDING, window=done_btn, anchor=tk.S
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=cancel_btn, anchor=tk.SW
        )
    )
