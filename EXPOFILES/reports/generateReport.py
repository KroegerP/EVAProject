from __future__ import annotations
import os
import pandas as pd
import datetime as dt

import plotly.express as px

import psycopg2
import psycopg2.extensions
from database.queries.query import getConfirmationsByMedName


def generateReport(
    conn: psycopg2.extensions.connection,
    medName: str,
) -> str:
    file_path = ""

    confirm_data = {"date": [], "time": [], "taken": []}
    hours = []

    [hours.append(f"{num}:00") for num in range(24)]

    hours = pd.to_datetime(hours).time

    confirm_tuples = getConfirmationsByMedName(conn, medName)

    if len(confirm_tuples) > 0:
        file_path = f"EXPOFILES/assets/generatedImages/{medName}.png"

        for confirm in confirm_tuples:
            created_date = confirm.createdAt.strftime("%B %d")
            created_time = confirm.createdAt.strftime("%H:%M:%S")
            created_time_int = int(confirm.createdAt.strftime("%H%M"))

            print(confirm.createdAt.strftime("%X"))

            confirm_data["date"].append(confirm.createdAt)
            confirm_data["time"].append(created_time_int)
            confirm_data["taken"].append(confirm.taken)

        confirm_data["date"] = pd.to_datetime(confirm_data["date"]).date
        # confirm_data["time"] = pd.to_datetime(confirm_data["time"]).time

        # [print(f'DATE: {d}') for d in confirm_data["date"]]
        # [print(f'TIME: {d}') for d in confirm_data["time"]]
        # [print(f'HOURS: {d}') for d in hours]

        # print([confirm_data["time"].min(), confirm_data["time"].max()])

        # [print(f'TIME: {d}') for d in confirm_data["time"]]

        fig = px.scatter(
            confirm_data,
            x="date",
            y="time",
            color="taken",
            opacity=0.5,
            labels={
                "date": "Date",
                "time": "Time of Day (HH:MM)",
                "taken": "Confirm Result",
            },
            color_discrete_sequence=["green", "red"],
            width=900,
        )

        fig.update_yaxes(range=[0, 2400])

        fig.update_layout(
            yaxis=dict(
                tickmode="array",
                tickvals=[
                    0,
                    200,
                    400,
                    600,
                    800,
                    1000,
                    1200,
                    1400,
                    1600,
                    1800,
                    2000,
                    2200,
                    2400,
                ],
                ticktext=[
                    "12:00 AM",
                    "02:00 AM",
                    "04:00 AM",
                    "06:00 AM",
                    "08:00 AM",
                    "10:00 AM",
                    "12:00 PM",
                    "2:00 PM",
                    "4:00 PM",
                    "6:00 PM",
                    "8:00 PM",
                    "10:00 PM",
                    "11:59 PM",
                ],
            ),
            # paper_bgcolor=os.getenv("PRIMARY_COLOR"),
            # legend=dict(bgcolor=os.getenv("PRIMARY_COLOR")),
            paper_bgcolor="rgba(250,249,246,1)",
            # plot_bgcolor="rgba(250,249,246,1)",
            margin=dict(l=0, r=0, b=0, t=0),
        )

        fig.update_traces(
            marker=dict(size=18, line=dict(width=2, color="DarkSlateGrey")),
            selector=dict(mode="markers"),
        )

        fig.write_image(file_path)

    return file_path
