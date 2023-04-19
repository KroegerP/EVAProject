from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from UIController import UIController

APP_LOCATIONS = ['Home', 'Drug Info', 'Report', 'Confirm']

# Function to delete all the UI from the canvas given a specific location
# Returns False if the given app location is not in the list above
def resetWindow(canvas: tk.Canvas, canvasIds: dict,appLocation: str) -> bool:
    """
    Method to cleanup objects on the current canvas
    Inputs:
        canvas:         Tkinter canvas object
        canvasIds:      Id's object containing the ID's on the canvas
        appLocation:    The location in which the app is LEAVING, meaning that the
                        method will cleanup objects that have been added to the
                        `appLocation` key of the canvasIds dictionary
    """
    if appLocation not in APP_LOCATIONS:
        print(f"ERROR: App location {appLocation} not present in {APP_LOCATIONS}!")
        return False
    else:
        [canvas.itemconfig(itemId,state='hidden') for itemId in canvasIds[appLocation]]
        return True

def clearLocalUI(canvas: tk.Canvas, ids: list[int]) -> None:
    for id in ids:
        print(id)
        canvas.delete(id)

def findNearestConfirmTime(UIController: UIController, hour: str, min: str) -> bool:

    for time in UIController.confirmDict.keys():
        print(f'HOUR MIN: {hour}:{min}, to {UIController.confirmDict[time]}')

        hour = int(hour)
        minute = int(minute)

        closest_hour = min(UIController.confirmDict[time], key=lambda x:abs(x-int(hour)))
        closest_minute = min(UIController.confirmDict[time], key=lambda x:abs(x-int(minute)))


        # TODO: Remove closest confirm time for med when 
        # if hour_min in UIController.confirmDict[time]:
        #     UIController.confirmDict.pop(hour_min)
        #     return True

    return False