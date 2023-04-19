from tkinter import *
from tkinter import messagebox
from time import strftime



root = Tk()
root.geometry("1280x800")

def options():
    print("options")

def my_time():
    time_string = strftime('%I:%M %p \n %A \n %B %d %Y')
    #return time_string
    my_text.config(text=time_string)
    my_text.after(1000, my_time)  # time delay of 1000 milliseconds


bg = PhotoImage(file = "EXPOFILES/assets/view.png")

my_canvas = Canvas(root,width = 1280, height = 800 )
my_canvas.pack(fill="both", expand=True)


# my_text = Label(root, text = "hi", font=("Helvetica", 50), fg = "black")
# my_text.place(x=100, y=500)
#my_text.pack()

my_canvas.create_image(0,0,image=bg, anchor="nw")

my_text = Label(root, text = "", font=("Helvetica", 50), fg = "black")

myText_window = my_canvas.create_window(70,530, anchor = 'nw', window = my_text)

#my_canvas.create_text(300,600,text="", font=("Roboto", 50), fill="white")

optionButtonImage = PhotoImage(file = "output-onlinepngtools.png")

option_Button = Button(root, image = optionButtonImage, borderwidth=0, command=options)

optionButton_window = my_canvas.create_window(1150,40, anchor='nw', window=option_Button)







# my_label = Label(root)
# my_label.place(x=0, y=0, relwidth=1, relheight=1)
#

#
my_time()
root.mainloop()

#
# C = Canvas(top, bg="blue", height=250, width=300)
# filename = PhotoImage(file = r"C:\Users\Alex Davison\Desktop\raspberry-pi.png")
# background_label = Label(top, image=filename)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
#
# C.pack()
# top.mainloop