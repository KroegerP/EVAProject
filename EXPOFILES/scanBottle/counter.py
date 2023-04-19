import os
import tkinter as tk
import dotenv


class Counter:
    def __init__(self, root, curVal=0, lowerLimit=0, upperLimit=9, index=-1):
        self.frame = tk.Frame(
            master=root,
            name=f'!frame{index if index >= 0 else ""}',
            background=os.getenv("PRIMARY_COLOR"),
        )
        self.lowerLimit = lowerLimit
        self.upperLimit = upperLimit

        # Create the increment and decrement buttons
        self.increment_button = tk.Button(
            self.frame,
            background=os.getenv("LIGHT_GREEN"),
            text="+",
            width=4,
            height=2,
            command=self.increment_counter,
            font=(os.getenv("TEXT_FONT"), 24),
        )
        self.increment_button.grid(row=0, column=0, pady=30)

        self.decrement_button = tk.Button(
            self.frame,
            text="-",
            width=4,
            height=2,
            font=(os.getenv("TEXT_FONT"), 24),
            background=os.getenv("LIGHT_RED"),
            command=self.decrement_counter,
        )
        self.decrement_button.grid(row=2, column=0, pady=30)

        # Create the text widget
        self.counter_text = tk.StringVar()
        self.counter_text.set(f"{curVal}")
        self.counter_label = tk.Label(
            self.frame,
            textvariable=self.counter_text,
            background=os.getenv("PRIMARY_COLOR"),
            font=(os.getenv("TEXT_FONT"), 40),
        )
        self.counter_label.grid(row=1, column=0, pady=30)

    def increment_counter(self):
        current_value = int(self.counter_text.get())
        if current_value >= self.upperLimit:
            self.counter_text.set(str(self.lowerLimit))
        else:
            self.counter_text.set(str(current_value + 1))

    def decrement_counter(self):
        current_value = int(self.counter_text.get())
        if current_value <= self.lowerLimit:
            self.counter_text.set(str(self.upperLimit))
        else:
            self.counter_text.set(str(current_value - 1))

    def get_value(self):
        return int(self.counter_text.get())


if __name__ == "__main__":
    dotenv.load_dotenv()

    root = tk.Tk()
    my_canvas = tk.Canvas(
        master=root, width=1280, height=800, background=os.getenv("PRIMARY_COLOR")
    )
    my_canvas.pack(fill="both", expand=True)
    my_counter_app = Counter(my_canvas)
    my_canvas.create_window(
        1280 / 2, 800 / 2, window=my_counter_app.frame, anchor=tk.CENTER
    )

    root.mainloop()
