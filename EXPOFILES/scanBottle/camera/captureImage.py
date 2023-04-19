import os
import cv2
import pytesseract


def parse_image(imagePath: str) -> dict:
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
    thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Apply dilation to make the text bolder
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilated = cv2.dilate(thresholded, kernel, iterations=3)

    file_directory = f"EXPOFILES/database/new"

    cv2.imwrite(f"{file_directory}/thresh-img.png", thresholded)
    # cv2.imwrite(f"{file_directory}/dilated-img.png", dilated)
    # cv2.imwrite(f"{file_directory}/gra-img.png", gray)
    # cv2.imwrite(f"{file_directory}/kernel-img.png", kernel)

    # Apply OCR to recognize the text
    text: str = pytesseract.image_to_string(thresholded)

    text_lines = text.split("\n")

    return text


if __name__ == "__main__":
    file_directory = f"EXPOFILES/database/new/1.png"
    if not os.path.isfile(file_directory):
        image_path = "EXPOFILES/assets/ibuprofen.jpg"
    else:
        image_path = file_directory

    text = parse_image(imagePath=image_path)

    print(type(text))
    print(text)
