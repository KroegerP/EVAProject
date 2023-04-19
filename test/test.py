from pprint import pprint
import tkinter
import os, sys

path = os.path.dirname(__file__)

print(os.path.abspath(os.getcwd()))

pprint(sys.path)

file_name = os.path.join(path,'assets')

root = tkinter.Tk()
root.title("Fenster 1")
root.geometry("500x500")
bg = tkinter.PhotoImage(name="View",file=f'{file_name}/view.png')
bg = tkinter.PhotoImage(name="View2",file='test/assets/view.png')
evaFace = tkinter.PhotoImage(file="test/assets/evaFace4Home.png")

my_canvas = tkinter.Canvas(root, width=1280, height=800)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0, 0, image=bg, anchor="nw")
root.mainloop()