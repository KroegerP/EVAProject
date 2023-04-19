import json
import os
from PIL import Image
from typing import Union

from bs4 import BeautifulSoup
import requests

whatis = "What is"
warningString = "Warning"
seString = "side effects"
iTakeString = "take"


def find_image(soup) -> Union[str, None]:
    image_url = None
    image_div = soup.find("div", {"class": "drugImageHolder"})

    children = image_div.findChildren()
    for child in children:
        # Image element has a src attribute that we're looking for
        if "src" in child.attrs.keys():
            image_url = child.attrs["src"]

    print(f"IMAGE URL {image_url}")

    return image_url


def get_dosage(soup: BeautifulSoup) -> str:
    dosage_text = ""

    dosage_div = soup.find("h2", {"id": "dosage"})

    siblings = dosage_div.find_next_siblings("p")
    for index in range(2):
        dosage_text = dosage_text + siblings[index].text

    return dosage_text


def readSite(drugName: str) -> dict:
    url = f"https://www.drugs.com/{drugName}.html"
    site_info = {"siteText": "", "dosage_text": ""}
    infoCount = 0

    try:
        resp = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Unable to connect to the internet!")
        json_file = open("EXPOFILES/assets/IbuprofenInfo.json")
        site_info = json.load(json_file)
        return site_info

    print(resp.status_code)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "lxml")
        # print(soup.prettify()) # For debugging

        site_info["image_url"] = find_image(soup)
        site_info["dosage_text"] = get_dosage(soup)

        for data in soup.find_all("h2"):
            if whatis in data.text:
                for dat in data.find_all_next(["p", "h2"]):
                    if infoCount > 0:
                        break
                    if dat.name == "h2":
                        break
                    site_info["siteText"] = dat.text
                    return site_info
                    infoCount = infoCount + 1
                site_info["siteText"] = "Could not find the medicine on Drugs.com"
                return site_info
    else:
        site_info["siteText"] = "Could not open Drugs.com to get medicine information"
        return site_info


def jpg_to_png(file_path: str) -> str:
    im = Image.open(file_path)
    new_path = file_path.replace(".jpg", ".png")
    print(f"Converting file to png: {new_path}")
    im.save(new_path)
    return new_path


def get_image(url: str) -> Union[str, None]:
    file_name = url.split("/")[-1].lower()
    file_directory = f"EXPOFILES/assets/drugInfoImages/{file_name}"
    check_dir = file_directory

    print(file_directory)

    if file_name.split(".")[-1] == "jpg":
        check_dir = file_directory.replace(".jpg", ".png")

    print(os.path.exists(check_dir))

    # File is already downloaded, no need to perform requests
    if os.path.exists(check_dir):
        return check_dir

    r = requests.get(url)

    if r.status_code == 200:
        with open(file_directory, "wb") as f:
            f.write(r.content)
    else:
        print("ERROR GETTING IMAGE")
        return None

    if file_name.split(".")[-1] == "jpg":
        file_directory = jpg_to_png(file_directory)

    print(file_directory)

    return file_directory
