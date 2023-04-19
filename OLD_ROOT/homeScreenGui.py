from tkinter import *
from tkinter import messagebox
from time import strftime


root = Tk()
root.geometry("1280x800")


def options():
    print("options")

def my_time():
    time_string = strftime('%I:%M %p \n %A \n %B %d %Y')
    return time_string
    my_text.config(text=time_string)
    my_text.after(1000, my_time)  # time delay of 1000 milliseconds

def displayHomeScreen():
    bg = PhotoImage(file="EXPOFILES/assets/view.png")

    my_canvas = Canvas(root, width=1280, height=800)
    my_canvas.pack(fill="both", expand=True)

    my_canvas.create_image(0, 0, image=bg, anchor="nw")
    myTexty = my_time()
    my_canvas.create_text(280, 650, text=myTexty, font=("Roboto", 50), fill="white")

    evaText = "Hi I'm Eva.\nHow can I help you?"
    my_canvas.create_text(360, 80, text=evaText, font=("Roboto", 40), fill="white")

    optionButtonImage = PhotoImage(file="output-onlinepngtools.png")

    option_Button = Button(root, image=optionButtonImage, borderwidth=0, command=options)

    optionButton_window = my_canvas.create_window(1150, 40, anchor='nw', window=option_Button)

    my_time()
    root.mainloop()
