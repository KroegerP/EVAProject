import os
import glob
import shutil
from urllib.parse import urlparse


def move_images(source_folder, med_id, new_name):
    image_extensions = [
        "*.jpg",
        "*.jpeg",
        "*.png",
    ]
    destination_folder = f"EXPOFILES/database/meds/{new_name}/{med_id}"
    for extension in image_extensions:
        file_pattern = os.path.join(source_folder, extension)
        for file_path in glob.glob(file_pattern):
            file_name = urlparse(file_path).path.split("/")[-1]
            f_extension = file_name.split(".")[-1]

            med_name_dir = f"EXPOFILES/database/meds/{new_name}"
            if not os.path.isdir(med_name_dir):
                os.mkdir(med_name_dir)

            med_id_dir = f"{med_name_dir}/{med_id}"
            if not os.path.isdir(med_id_dir):
                os.mkdir(med_id_dir)

            print(file_name)
            print(f_extension)

            os.rename(file_path, f"{destination_folder}/{new_name}.{f_extension}")
            # shutil.move(file_path, destination_folder)
            if os.path.isfile(destination_folder):
                os.remove(file_path)


def delete_images(folder_path):
    image_extensions = [
        "*.jpg",
        "*.jpeg",
        "*.png",
    ]
    for extension in image_extensions:
        file_pattern = os.path.join(folder_path, extension)
        for file_path in glob.glob(file_pattern):
            os.remove(file_path)
