from datetime import datetime
import os
import signal
from time import strftime
import tkinter as tk
from tkinter import messagebox
import psycopg2.extensions
from scanBottle.camera.cameraControls import Camera

from scanBottle.individualEdit import individualEdit
from homeGui import homeGui
from confirmationGUI import confirmGui
from drugInfoGui import loadingDrugGui
from reportsGui import reportGui
from scanBottle.scanBottleGui import scanBottleGui
from scanBottle.scannerInstructions import bottleScannerGui
from scanBottle.editBottleGui import editBottleGui

from database.queries.query import timesList
import utils.interfaceHelpers as UI
from utils.firebase.firebase import FirebaseApp
from firebase_admin import firestore

from constants.colors import *
from constants.window import *


class UIController:
    """
    Class to handle UI for each screen and will contain core properties used
    throughout the code. This will perform asset cleanup and content management,
    as well as provide a DB connection at any point of the App
    Inputs:
        conn:       Postgresql connection object

    Arributes:


    """

    root: tk.Tk
    canvas: tk.Canvas
    conn: psycopg2.extensions.connection
    confirmDict: dict
    canvasIds: dict
    geometry: str

    def __init__(self, conn: psycopg2.extensions.connection) -> None:
        self.root = tk.Tk()
        self.conn = conn
        self.firebase = FirebaseApp()
        self.confirmDict = timesList(self.conn)
        # If these Id keys are changed, they must be updated on respective files
        self.canvasIds = {
            "Home": [],
            "Confirm": [],
            "Report": [],
            "DrugInfo": [],
            "ScanBottle": [],
        }

        # Root properties - these will remain consistent
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.title("Everyone's Virtual Assistant")
        # self.root.attributes('-fullscreen', True) # -- Look into using this instead

        # Canvas where all UI elements will be added to / removed from
        self.canvas = tk.Canvas(
            self.root,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            background=os.getenv("PRIMARY_COLOR"),
        )
        self.canvas.pack(fill="both", expand=True)

        self.clock_text = UI.clockText(root=self.root)

        # Load Home UI
        self.currentLocation = "Home"
        self.closeAndNavigateTo("Initialize", self.currentLocation)

        # Intitialize time based functionality
        self.clock()

        # self.firebase.read_users_collection()

        self.root.mainloop()

    def homeScreen(self):
        print("Loading Home Screen")
        homeGui(self)

    def scanSelect(self):
        print("Going to Bottle Scanning")
        # loadingRamGui()
        # displayFunct()
        scanBottleGui(self)

    def openBottleScanner(self):
        print("Loading Bottle Scanner")
        self.clearUI("ScanBottle")
        bottleScannerGui(self)

    def editBottleInfo(self):
        print("Info editor list")
        self.clearUI("ScanBottle")
        editBottleGui(self)

    def individualInfoEdit(self, medName, updateVal=None):
        print("Going to individual info edit...")
        self.clearUI("ScanBottle")
        individualEdit(self, medName, update_val=updateVal)

    def confirmSelect(self):
        print("Going to Medicine Confirmation")
        confirmGui(self)

    def reportSelect(self):
        print("Going to Reports")
        reportGui(self)

    def drugInfoSelect(self):
        print("Going to Drug Info")
        loadingDrugGui(self)

    def goToHome(self):
        self.closeAndNavigateTo(self.currentLocation, "Home")

    def goToDrugInfo(self):
        self.closeAndNavigateTo(self.currentLocation, "DrugInfo")

    def goToScanBottle(self):
        self.closeAndNavigateTo(self.currentLocation, "ScanBottle")

    def goToReport(self):
        self.closeAndNavigateTo(self.currentLocation, "Report")

    def goToConfirm(self, hour: str, minute: str):
        self.clearUI(self.currentLocation)
        self.currentLocation = "Confirm"
        confirmGui(self, hour, minute)

    def closeAndNavigateTo(self, curLocation: str, nextDesination: str) -> None:
        """
        Important for setting keys correctly
        """
        print(f"Going to {nextDesination} from {curLocation}")
        self.clearUI(curLocation)
        self.loadUI(nextDesination)

    def clearUI(self, canvasKey: str) -> None:
        if canvasKey == "Initialize":
            return
        try:
            [self.canvas.delete(itemId) for itemId in self.canvasIds[canvasKey]]
        except KeyError:
            print(
                f"ERROR: Cannot find canvas key {canvasKey} in dict keys {self.canvasIds.keys()}"
            )
        return

    def loadUI(self, nextDestination) -> None:
        if nextDestination == "Home":
            self.currentLocation = "Home"
            self.homeScreen()
        elif nextDestination == "Report":
            self.currentLocation = "Report"
            self.reportSelect()
        elif nextDestination == "DrugInfo":
            self.currentLocation = "DrugInfo"
            self.drugInfoSelect()
        elif nextDestination == "Confirm":
            self.currentLocation = "Confirm"
            self.confirmSelect()
        elif nextDestination == "ScanBottle":
            self.currentLocation = "ScanBottle"
            self.scanSelect()

    def closeEVA(self):
        # root.withdraw()
        if messagebox.askyesno(
            title="Exit EVA?", message="Are you sure you want to exit?"
        ):
            self.root.destroy()
        else:
            print("Canceled exit request")
            # root.deiconify()

    # Maybe split up code, need to see if it will affect the event loop
    def clock(self):
        time_string = strftime("%I:%M %p \n %A, %B %d, %Y")
        date = datetime.now()

        # TODO: Create field for checking if the confirm has already been performed
        for key in self.confirmDict:
            confirm = key
            hour_minute = confirm.split(":")
            print(f'TIME: {date.strftime("%H:%M")}')

            try:
                hour = hour_minute[0]
                minute = hour_minute[1]
            except IndexError:
                print(
                    f"Error getting hour minute split from entry {hour_minute} in list {UIController.confirmDict}, time must be in a HH:MM format!"
                )
                hour = -1
                minute = -1

            if date.strftime("%H") == hour and date.strftime("%M") == minute:
                self.goToConfirm(hour, minute)

        self.clock_text.config(text=time_string)
        self.clock_text.after(10000, self.clock)

    def start_camera(self) -> Camera:
        my_camera = Camera(self.canvas)
        return my_camera

    def run_camera(self, camera: Camera) -> None:
        camera.update_feed(camera.stream)
        self.canvas.after(10, self.run_camera, camera)

    def stop_camera(self, camera: Camera) -> None:
        try:
            pgid = os.getpgid(camera.p.pid)
            os.killpg(pgid, signal.SIGINT)
        except:
            print("ERROR KILLING CAMERA")
