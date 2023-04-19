import tkinter as tk
from time import strftime
from voiceRec import *
from confirmationGUI import *

from evaGUI import *
from postScanDisplay import *
from reportsGui import *
from drugInfoGui import *

def options():
    print("options")

def my_time():
    time_string = strftime('%I:%M %p \n %A \n %B %d, %Y')
    my_text.config(text=time_string)
    my_text.after(1000, my_time)  # time delay of 1000 milliseconds

def scanSelect():
    loadingRamGui()
    displayFunct()

def confirmSelect():
    loadingGui("EXPOFILES/assets/image1.png")

def reportSelect():
    loadingReportGui()

def drugInfoSelect():
    loadingDrugGui()

# def openNewWindow():
#     # Toplevel object which will
#     # be treated as a new window
#     newWindow = Toplevel(root)

#     # sets the title of the
#     # Toplevel widget
#     newWindow.title("New Window")

#     # sets the geometry of toplevel
#     newWindow.geometry("1280x800")

#     # A Label widget to show in toplevel
#     Label(newWindow,
#           text="This is a new window").pack()

def showHomeScreen():

    root = Tk()
    root.geometry("1280x800")
    root.title("Elderly Virtual Assistant")

    background_image = tk.PhotoImage(file='EXPOFILES/assets/view.png')
    evaFace = tk.PhotoImage(file="EXPOFILES/assets/evaFace4Home.png")

    my_canvas = tk.Canvas(root, width=1280, height=800)
    my_canvas.pack(fill="both", expand=True)

    my_canvas.create_image(
        0, 0, image=background_image, anchor="nw"
    )
    my_canvas.create_image(
        0, 0, image=evaFace, anchor="nw"
        )
    global my_text
    my_text = tk.Label(
        root, text="", font=("Roboto", 50), fg="black"
    )

    myText_window = my_canvas.create_window(
        70, 530, anchor='nw', window=my_text
    )


    evaText = "Hi I'm Eva.\nHow can I help you?"
    my_canvas.create_text(
        410, 80, text=evaText, font=("Roboto", 40), fill="white"
    )

    button_frame = tk.Frame(my_canvas)
    button_frame.rowconfigure(0, weight=1)
    button_frame.rowconfigure(1, weight=1)
    button_frame.rowconfigure(2, weight=1)
    button_frame.rowconfigure(3, weight=1)

    btn1 = tk.Button(
        button_frame, 
        text='Scan Bottle', 
        bg='#E1912A', 
        font=('arial', 50, 'normal'), 
        command=scanSelect
    )

    btn2 = tk.Button(
        button_frame, 
        text='Drug Info', 
        bg='#A1E12A', 
        font=('arial', 50, 'normal'), 
        command=drugInfoSelect
    )
    
    btn3 = tk.Button(
        button_frame, 
        text='Confirmation Demo', 
        bg='#1AA8AC', 
        font=('arial', 50, 'normal'), 
        command=confirmSelect
    )
    
    btn4 = tk.Button(
        button_frame, 
        text='Reports', 
        bg='#6F31CF', 
        font=('arial', 55, 'normal'), 
        command=reportSelect)

    btn1.grid(row=0, column=0, sticky=tk.E)
    btn2.grid(row=1, column=0, sticky=tk.E)
    btn3.grid(row=2, column=0, sticky=tk.E)
    btn4.grid(row=3, column=0, sticky=tk.E)

    button_frame.pack(fill='x')

    print("expoFunct")
    # while True:
    #     my_time()
    #     root.update_idletasks()
    #     root.update()
    root.mainloop()

if __name__ == '__main__':
    showHomeScreen()

#home screen may need to be image absed then guia based. I just need to find a good way to update and close the image.

# showHomeScreen()