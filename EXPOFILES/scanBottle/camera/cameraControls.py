import os
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import pytesseract
import io

import cv2


class Camera:  # Originally a tk object, some stuff may reflect that
    """
    Class for the Camera, place the label in the scene to get the feed on screen
    """

    def __init__(self, root):
        # Set up the camera feed
        cmd = ["raspistill", "-t", "0", "-w", "640", "-h", "480", "-o", "-"]
        self.p = subprocess.Popen(cmd, stdout=subprocess.PIPE, preexec_fn=os.setsid)
        self.stream = io.BytesIO(self.p.stdout.read())

        # self.test_image = tk.Label(root)
        # photo = ImageTk.PhotoImage("EXPOFILES/assets/image1.png")
        # self.test_image.config(image=photo)
        # self.test_image.image = photo

        # Create a label to display the camera feed
        self.label = tk.Label(root)
        self.label.pack()

        # Continuously update the camera feed on the label
        self.photo = None
        self.update_feed(self.stream)

    def update_feed(self, stream):
        # Read the next image from the stream
        stream.seek(0)
        image = Image.open(stream)

        # Resize the image to fit the label
        image = image.resize((640, 480))

        # Convert the image to a Tkinter-compatible format
        photo = ImageTk.PhotoImage(image)

        # Update the label to show the new image
        self.label.config(image=photo)
        self.label.image = photo

        # Schedule the next update
        # self.after(10, self.update_feed, stream)


class CV2Camera:  # Originally a tk object, some stuff may reflect that
    """
    Class for the Camera, place the label in the scene to get the feed on screen
    """

    def __init__(self, root):
        # Set up the camera feed
        self.cap = cv2.VideoCapture(0)

        # set camera resolution to 320x240
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

        # Create a label to display the camera feed
        self.label = tk.Label(root, name="!labelCamera")
        self.label.pack()

        # Continuously update the camera feed on the label
        self.update_label(root)

    def update_label(self, root):
        ret, frame = self.cap.read()
        if ret:
            # convert the OpenCV frame to a PIL image
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            # update the Tkinter label with the PIL image
            self.label.image = ImageTk.PhotoImage(img)
            self.image_ref = ImageTk.PhotoImage(img)
            self.label.config(image=self.label.image)
        # schedule the update_label function to be called again in 10 milliseconds
        root.after(10, self.update_label, root)

    def stop_camera(self):
        return self.cap.release()

    def get_image(self):
        return ImageTk.getimage(self.image_ref)

    def save_image(self, temp_name: str, cur_img: Image) -> str:
        file_name = f"{temp_name}.png"
        file_directory = f"EXPOFILES/database/new/"

        if cur_img is not None:
            if not os.path.exists(file_directory):
                os.mkdir(file_directory)

            full_path = os.path.join(file_directory, file_name)

            if os.path.exists(full_path):
                os.remove(full_path)

            rgb_img = cur_img.convert("RGB")
            rgb_img.save(full_path, "PNG")
            cur_img.close()
            rgb_img.close()
            return full_path

        else:
            print("ERROR: Unable to retrieve image from camera!")
            return None

    def parse_image(self, imagePath: str) -> list[str]:
        """
        Returns a dictionary of strings parsed from the image
        """
        return_dict = {}

        if not os.path.isfile(imagePath):
            print("ERROR: Path does not exist")
            return

        # Load the image
        image = cv2.imread(imagePath)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to preprocess the image
        thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[
            1
        ]

        # Apply dilation to make the text bolder
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        dilated = cv2.dilate(thresholded, kernel, iterations=3)

        file_directory = f"EXPOFILES/database/new"

        # Working on optimizing this using eroding and dialating text, but for now
        # thresholding it gives us the best results
        cv2.imwrite(f"{file_directory}/thresh-img.png", thresholded)

        # file_path = self.save_image("dilated-img", dilated)

        # Apply OCR to recognize the text
        text: str = pytesseract.image_to_string(thresholded)

        text_lines = text.split("\n")

        return text_lines


if __name__ == "__main__":
    import pandas as pd

    url = "https://en.wikipedia.org/wiki/List_of_common_resolutions"
    table = pd.read_html(url)[0]
    table.columns = table.columns.droplevel()
    cap = cv2.VideoCapture(0)
    resolutions = {}
    for index, row in table[["W", "H"]].iterrows():
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, row["W"])
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, row["H"])
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        resolutions[str(width) + "x" + str(height)] = "OK"
    print(resolutions)
