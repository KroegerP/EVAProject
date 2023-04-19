# PACKAGES
import tkinter as tk
import psycopg2.extensions
from tkinter import messagebox
from time import strftime
from typing import TypedDict
from datetime import datetime

# MODULES
from voiceRec import *
import confirmationGUI as confirmUI
import utils.interfaceHelpers as UI
from evaGUI import *
from postScanDisplay import *
from reportsGui import *
from drugInfoGui import *
from constants.window import *
from database.dbUtils import connectToEvaDB
from database.queries.query import timesList

class EVAGUI:
    """
    Class to handle UI for each screen and will contain core properties used
    throughout the code. This will perform asset cleanup and content management,
    as well as provide a DB connection at any point of the App
    
    Inputs:
        `root`:       Tkinter root object for creating UI
        `conn`:       Postgres connection object
    """
    def __init__(self, UIController):

        self.UIController = UIController
        self.root = UIController.root
        # self.conn = UIController.conn
        # Data Setup
        # This will be used to manage the UI elements on the canvas
        # self.canvasIds: TypedDict = {}
        # List of confirms to ask for the current day
        # TODO: Set up query that can populate this on startup
        # self.confirmList: TypedDict = timesList(self.conn)
        # Geometry for the application window size
        # geometry = f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}'
        # self.root.attributes('-fullscreen', True) # -- Look into using this instead

        # Root properties - these will remain consistent
        # self.root.geometry(geometry)
        # self.conn = connectToEvaDB()
        # self.root.title("Elderly Virtual Assistant")

        
        # Main control for UI Elements
        # If using fullscreen, you may need to edit this line
        # UIController.canvas = tk.Canvas(self.root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        # UIController.canvas.pack(fill="both", expand=True)

        # Initializing assets
        self.background_image = tk.PhotoImage(file='EXPOFILES/assets/view.png')
        self.eva_face = tk.PhotoImage(file="EXPOFILES/assets/evaFace4Home.png")

        # TODO: Maybe just rewrite this string depending on where we are rather than making new text to manage?
        self.eva_text = "Hi I'm Eva.\nHow can I help you?"
        self.clock_text = tk.Label(self.root, text="", font=("Roboto", 32), fg="black")

        # Program Navigation Buttons
        scan_btn = UI.NewHomeBtn(master=self.UIController.canvas, text='Scan Bottle', command=self.UIController.scanSelect)
        drug_info_btn = UI.NewHomeBtn(master=self.UIController.canvas, text='Drug Info', command=self.UIController.drugInfoSelect)
        confirm_btn = UI.NewHomeBtn(master=self.UIController.canvas, text='Daily Confirmation', command=self.UIController.confirmSelect)
        report_btn = UI.NewHomeBtn(master=self.UIController.canvas, text='Reports', command=self.UIController.reportSelect)
        exit_btn = UI.NewHomeBtn(master=self.UIController.canvas, text='Exit', command=self.closeEVA)

        # Adding assets to the canvas and the canvasIds list
        # These can be used to control the visibility of items
        self.UIController.canvasIds["Home"].append(self.UIController.canvas.create_image(
            0, 0, image=self.background_image, anchor="nw"
        ))
        self.UIController.canvasIds["Home"].append(self.UIController.canvas.create_image(
            0, 0, image=self.eva_face, anchor="nw"
            ))
        self.UIController.canvasIds["Home"].append(self.UIController.canvas.create_window(
            70, 530, anchor='nw', window=self.clock_text
        ))
        self.canvasIds["Home"].append(UIController.canvas.create_text(
            300, 250, text=self.eva_text, font=("Roboto", 40), fill="black"
        ))
        self.canvasIds["Home"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING,200,window=scan_btn, anchor=tk.E))
        self.canvasIds["Home"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING,300,window=drug_info_btn, anchor=tk.E))
        self.canvasIds["Home"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING,400,window=confirm_btn, anchor=tk.E))
        self.canvasIds["Home"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING,500,window=report_btn, anchor=tk.E))
        self.canvasIds["Home"].append(UIController.canvas.create_window(0 ,800,window=exit_btn, anchor=tk.SW))

        self.clock()
        # self.root.mainloop()

    def closeEVA(self):
        # self.root.withdraw()
        if messagebox.askyesno(
            title="Exit EVA?", 
            message="Are you sure you want to exit?"
            ):
            self.root.destroy()
        else:
            print("Canceled exit request")
            # self.root.deiconify()

    # Maybe split up code, need to see if it will affect the event loop
    def clock(self):
        time_string = strftime('%I:%M %p \n %A \n %B %d, %Y')
        date = datetime.now()

        # TODO: Create field for checking if the confirm has already been performed
        for key in self.confirmList:
            confirm = key
            hour_minute = confirm.split(':')
            print(f'HOUR: {date.strftime("%H")} MINUTE: {date.strftime("%M")} DATE: {hour_minute}')

            try:
                hour = hour_minute[0]
                minute = hour_minute[1]                
            except IndexError:
                print(f'Error getting hour minute split from entry {hour_minute} in list {self.confirmList}, time must be in a HH:MM format!')
                hour = -1
                minute = -1   

            if date.strftime("%H") == hour and date.strftime("%M") == minute:
                confirmUI.confirmGui(self, self.UIController.canvas)


        self.clock_text.config(text= time_string)
        self.clock_text.after(10000,self.clock)
    