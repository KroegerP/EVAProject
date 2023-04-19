import os
import tkinter as tk

import dotenv

from constants.colors import PRIMARY_COLOR


class Keyboard:
    def __init__(self, root: tk.Canvas, text_input: str):
        self.root = root
        self.shift_pressed = False

        self.text_widget = tk.Text(
            root, height=3, width=50, font=(os.getenv("TEXT_FONT"), 32, "normal")
        )
        for letter in text_input:
            self.text_widget.insert(
                "end", letter.upper() if self.shift_pressed else letter
            )
        self.text_widget.grid(row=0, column=0)
        self.create_keyboard()

    def create_keyboard(self):
        # Create frame to hold keyboard buttons
        self.keyboard_frame = tk.Frame(
            self.root, name="!keyboard_frame", background=os.getenv("PRIMARY_COLOR")
        )
        self.keyboard_frame.grid(row=1, column=0)

        # Create letter buttons
        letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in letters:
            button = tk.Button(
                self.keyboard_frame,
                name=f"!button{letter}",
                text=letter.upper() if self.shift_pressed else letter,
                width=10,
                height=3,
                command=lambda l=letter: self.press_letter(l),
                font=(os.getenv("TEXT_FONT"), 18, "normal"),
            )
            button.grid(row=(ord(letter) - 97) // 7, column=(ord(letter) - 97) % 7)
            # print(button.winfo_name())
            # button_name = f'!keyboard_frame.!button{letter}'
            # button_name = f'!frame.!button{letter}'
            # button.winfo_toplevel().nametowidget(button_name)

        # Create shift button
        shift_button = tk.Button(
            self.keyboard_frame,
            text="Shift",
            width=22,
            height=3,
            font=(os.getenv("TEXT_FONT"), 18, "normal"),
            background=os.getenv("LIGHT_BLUE"),
            command=self.toggle_shift,
        )
        shift_button.grid(row=4, column=5, columnspan=2)

        # Create backspace button
        backspace_button = tk.Button(
            self.keyboard_frame,
            text="Backspace",
            width=22,
            height=3,
            font=(os.getenv("TEXT_FONT"), 18, "normal"),
            background=os.getenv("LIGHT_RED"),
            command=self.press_backspace,
        )
        backspace_button.grid(row=3, column=5, columnspan=2)

        # Create space button
        space_button = tk.Button(
            self.keyboard_frame,
            text="Space",
            width=36,
            height=3,
            font=(os.getenv("TEXT_FONT"), 18, "normal"),
            command=lambda: self.press_letter(" "),
        )
        space_button.grid(row=4, column=1, columnspan=4, rowspan=2)

        # Create enter button
        # enter_button = tk.Button(self.keyboard_frame, text='Enter', width=22, height=4, background=os.getenv('GREEN_COLOR'), command=lambda: self.press_letter('\n'))
        # enter_button.grid(row=4, column=5, columnspan=2, padx=5)

    def press_letter(self, letter):
        # Add letter to text widget
        self.text_widget.insert("end", letter.upper() if self.shift_pressed else letter)

        # Reset shift after key press
        self.shift_pressed = False

    def press_backspace(self):
        last_char_index = self.text_widget.index("end-1c")

        line = last_char_index.split(".")[0]
        char = int(last_char_index.split(".")[1])
        char -= 1
        lower_range = f"{line}.{char}"

        # Check if text widget is empty
        if self.text_widget.index("end-1c") == "1.0":
            return

        # Remove last character from text widget
        self.text_widget.delete(lower_range, tk.END)

    def toggle_shift(self):
        # Toggle shift button state
        self.shift_pressed = not self.shift_pressed

        # Update letter button labels with shifted/unshifted characters
        for letter in "abcdefghijklmnopqrstuvwxyz":
            button_text = letter.upper() if self.shift_pressed else letter
            button = self.root.nametowidget(f"!keyboard_frame.!button{letter}")
            button.config(text=button_text)

    def getValue(self):
        return str(self.text_widget.get("1.0", tk.END))


# Create main window
if __name__ == "__main__":
    dotenv.load_dotenv()

    root = tk.Tk()

    # Create text widget to display keyboard input

    input_value = "Testing"

    # Create keyboard
    keyboard = Keyboard(root, input_value)

    # Start the main loop
    root.mainloop()
