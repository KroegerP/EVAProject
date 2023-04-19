from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING

from reports.generateReport import generateReport
import utils.interfaceHelpers as UI
from constants.window import *
from constants.colors import *
from database.queries.query import getPercentConfirmsPerTimePeriod

if TYPE_CHECKING:
    from UIController import UIController


def individualReport(UIController: UIController, medName: str) -> None:
    UIController.clearUI("Report")

    stats = getPercentConfirmsPerTimePeriod(UIController.conn, medName)

    if stats < 0:
        stats_text = f"No Confirmations\nreported in the\npast week"
    else:
        # stats_text = (
        #     f"{stats:.4g}% of confirmations\nreported as taken\nin the past week"
        # )
        stats_text = f"{stats:.4g}% reported as taken."

    report_image_path = generateReport(UIController.conn, medName)

    report_image = tk.PhotoImage(file=report_image_path)
    report_label = tk.Label(image=report_image)
    report_label.image = report_image
    report_label.config(borderwidth=0)

    reports_label = tk.Label(
        UIController.canvas,
        text=f"Report for {medName}",
        bg=PRIMARY_COLOR,
        font=(TEXT_FONT, 48, "normal"),
    )
    stats_label = tk.Label(
        UIController.canvas,
        text=stats_text,
        bg=PRIMARY_COLOR,
        font=(TEXT_FONT, 24, "normal"),
    )
    # cog_report_btn = UI.NewExitBtn(master=UIController.canvas, text='Cognitive Report', command=UIController.goToHome)
    go_back_btn = UI.NewExitBtn(
        master=UIController.canvas, text="Go Back", command=UIController.goToReport
    )

    UIController.canvasIds["Report"].append(
        UIController.canvas.create_window(
            WINDOW_PADDING - 20, WINDOW_PADDING - 20, window=reports_label, anchor=tk.NW
        )
    )
    # UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT_PADDING, window=cog_report_btn, anchor=tk.SE))
    UIController.canvasIds["Report"].append(
        UIController.canvas.create_window(
            WINDOW_PADDING - 10,
            WINDOW_HEIGHT_PADDING + 10,
            window=go_back_btn,
            anchor=tk.SW,
        )
    )
    UIController.canvasIds["Report"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, window=report_label, anchor=tk.CENTER
        )
    )
    UIController.canvasIds["Report"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH_PADDING + 20,
            WINDOW_PADDING - 20,
            window=stats_label,
            anchor=tk.NE,
        )
    )
