import os
import tkinter as tk

from constants.colors import *


def NewHomeBtn(
    master: tk.Canvas, command, text="Default", color="#F44336"
) -> tk.Button:
    return tk.Button(
        master=master,
        text=text,
        bg=color,
        font=(HOME_BUTTON_FONT, 48, "normal"),
        fg="#ffffff",
        command=command,
        width=15,
        height=2,
    )


def NewExitBtn(
    master: tk.Canvas, command, text="Default", color="#F44336"
) -> tk.Button:
    return tk.Button(
        master=master,
        text=text,
        bg=color,
        font=(TEXT_FONT, 32, "normal"),
        fg="#ffffff",
        command=command,
    )


def ConfirmationButtons(
    master: tk.Canvas, command, text="Default", color="#F44336", height=1, width=15
) -> tk.Button:
    return tk.Button(
        master=master,
        text=text,
        bg=color,
        font=(TEXT_FONT, 32, "normal"),
        fg="#ffffff",
        command=command,
        height=height,
        width=width,
    )


def NewMedBtn(
    master: tk.Canvas,
    command,
    text="Default",
    color="#F44336",
    width=15,
) -> tk.Button:
    return tk.Button(
        master=master,
        text=text,
        bg=color,
        font=(TEXT_FONT, 48, "normal"),
        fg="#ffffff",
        command=command,
        height=1,
        width=width,
    )


def evaText(
    name: str,
    canvas: tk.Canvas,
    text="Default",
    background=os.getenv("PRIMARY_COLOR"),
    fg=TEXT_COLOR,
    font=TEXT_FONT,
) -> tk.Label:
    return tk.Label(
        name=name,
        master=canvas,
        text=text,
        background=background,
        fg=TEXT_COLOR,
        font=(font, 32, "normal"),
    )


def evaFace(
    file: str = "EXPOFILES/assets/evaFaceRedLarge.png", background: str = PRIMARY_COLOR
):
    eva_face = tk.PhotoImage(file=file)
    eva_label = tk.Label(
        image=eva_face,
        width=eva_face.width(),
        height=eva_face.height(),
        background=background,
    )
    eva_label.image = eva_face
    eva_label.pack()

    return eva_label


def clockText(
    root: tk.Tk, text="", font=("Roboto", 24), fg="black", bg=os.getenv("PRIMARY_COLOR")
):
    return tk.Label(root, text=text, font=font, fg=fg, bg=bg)


def newSettingsBtn(
    master: tk.Canvas, command, color="#F44336", font=TEXT_FONT
) -> tk.Button:
    return tk.Button(
        master=master,
        text="Settings",
        bg=color,
        font=(font, 55, "normal"),
        fg="#ffffff",
        command=command,
    )


def newFrameLabel(master: tk.Frame, name: str) -> tk.Label:
    return tk.Label(
        master,
        text=name,
        fg="Black",
        font=(TEXT_FONT, 16, "bold"),
        background=os.getenv("PRIMARY_COLOR"),
    )


def newFrameButton(master: tk.Frame, name: str, command) -> tk.Button:
    return tk.Button(
        master,
        text=name,
        width=30,
        height=2,
        fg="Black",
        font=(TEXT_FONT, 16, "bold"),
        command=command,
    )


def NewDayBtn(
    master: tk.Canvas, command, text="Default", color="#F44336", name="!button"
) -> tk.Button:
    return tk.Button(
        master=master,
        name=name,
        text=text,
        bg=color,
        font=(TEXT_FONT, 48, "normal"),
        fg="#ffffff",
        command=command,
        height=1,
        width=10,
    )


def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = tk.PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x * oldWidth / newWidth)
            yOld = int(y * oldHeight / newHeight)
            rgb = "#%02x%02x%02x" % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage
