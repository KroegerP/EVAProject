from __future__ import annotations
import json
import tkinter as tk
from typing import TYPE_CHECKING

from drugInfo.readSite import get_image, readSite
import utils.interfaceHelpers as UI

from constants.window import *
from constants.colors import *

if TYPE_CHECKING:
    from UIController import UIController


def individualDrug(UIController: UIController, medName: str) -> None:
    UIController.clearUI("DrugInfo")

    image_path = None
    site_info = readSite(medName)

    med_label = tk.Label(
        UIController.canvas,
        text=f"{medName}",
        bg=PRIMARY_COLOR,
        font=(TEXT_FONT, 40, "normal"),
    )
    desc_text = tk.Label(
        UIController.canvas,
        text=f'{site_info["siteText"]}',
        bg=PRIMARY_COLOR,
        font=(TEXT_FONT, 20, "normal"),
        wraplength=750,
        justify="left",
    )
    dosage_text = tk.Label(
        UIController.canvas,
        text=f'{site_info["dosage_text"]}',
        bg=PRIMARY_COLOR,
        font=(TEXT_FONT, 20, "normal"),
        wraplength=750,
        justify="left",
    )
    meta_label = tk.Label(
        UIController.canvas,
        text="Sourced from Drugs.com",
        bg=PRIMARY_COLOR,
        font=(TEXT_FONT, 15, "normal"),
    )

    go_back_btn = UI.NewExitBtn(
        master=UIController.canvas, text="Go Back", command=UIController.goToDrugInfo
    )

    if "image_url" in site_info:
        image_path = get_image(site_info["image_url"])
    elif "image_path" in site_info:
        image_path = site_info["image_path"]

    if image_path:
        print(image_path)
        report_image = tk.PhotoImage(file=image_path)
        report_label = tk.Label(image=report_image)
        report_label.image = report_image

        image_text = tk.Label(
            UIController.canvas,
            text=f"Pill of {medName}",
            bg=PRIMARY_COLOR,
            font=(TEXT_FONT, 20, "normal"),
        )

        UIController.canvasIds["DrugInfo"].append(
            UIController.canvas.create_window(
                WINDOW_WIDTH - (WINDOW_PADDING * 2),
                WINDOW_HEIGHT / 1.5,
                window=image_text,
                anchor=tk.E,
            )
        )
        UIController.canvasIds["DrugInfo"].append(
            UIController.canvas.create_window(
                WINDOW_WIDTH_PADDING,
                WINDOW_HEIGHT / 2.25,
                window=report_label,
                anchor=tk.E,
            )
        )

    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20, window=med_label, anchor=tk.N
        )
    )
    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(
            WINDOW_PADDING, WINDOW_HEIGHT / 2.75, window=desc_text, anchor=tk.W
        )
    )
    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(
            WINDOW_PADDING, WINDOW_HEIGHT / 1.5, window=dosage_text, anchor=tk.W
        )
    )
    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(
            0, WINDOW_HEIGHT, window=go_back_btn, anchor=tk.SW
        )
    )
    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH, WINDOW_HEIGHT, window=meta_label, anchor=tk.SE
        )
    )
