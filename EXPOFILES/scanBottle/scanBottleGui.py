from __future__ import annotations
import functools
import tkinter as tk
from typing import TYPE_CHECKING

import voiceCommand
from constants.colors import *
from constants.window import *
import utils.interfaceHelpers as UI

# this is the function called when the button is clicked

if TYPE_CHECKING:
    from UIController import UIController

def scanBottleGui(UIController: UIController):

	eva_face = UI.evaFace(file="EXPOFILES/assets/evaFaceRedLarge.png")

	eva_text = UI.evaText(
		name="evaText",
        canvas=UIController.canvas, 
        text="What would you\nlike to do?"
    )
	UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(
        275, WINDOW_HEIGHT / 5, window=eva_text
    ))
	UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(
        275, WINDOW_HEIGHT / 2, window=eva_face
    ))

	add_btn = UI.NewHomeBtn(master=UIController.canvas, text='Add New Bottle', command=UIController.openBottleScanner)
	edit_btn = UI.NewHomeBtn(master=UIController.canvas, text='Edit Bottle Info', command=UIController.editBottleInfo)
	go_back_btn = UI.NewExitBtn(master=UIController.canvas, text='Go Back', command=UIController.goToHome)
	
	UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 1.5, window=edit_btn, anchor=tk.E))
	UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 3, window=add_btn, anchor=tk.E))
	UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(0, WINDOW_HEIGHT, window=go_back_btn, anchor=tk.SW))
