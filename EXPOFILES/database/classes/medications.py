from datetime import datetime
from typing import Union


class Medication:
    """
    Class corresponding to the `medications` table in the EVA database

    Inputs:
        `sql_tuple`:          SQL tuple returned from a query to initialize data

    Attributes:
        `id`:               ID of the medication. Unique to the medication as the user uploads a
                            medication via the workflow.
        `medName`:          Medication name.
        `dateFilled`:       Date the medication was filled, from the bottle scan.
        `refillsLeft`:      Amount of refills left for the bottle, from the bottle scan.
        `timesPerDay`:      # of times per day the user should be notified to take medication, this
                            is currently stored in the db as a number and converted to a list of
                            strings for use with the confirmation system.
        `timesPerWeek`:     # of times per week the user should be notified to take medication.
        `folderPath`:       Folder path to the image generated from the bottle scan (to be deprecated).
        `createdAt`:        Time in which the medication was added to the DB.
    """

    def __init__(self, sql_tuple: tuple) -> None:
        dpw_options = [
            ["Wednesday"],
            ["Wednesday"],
            ["Monday", "Thursday"],
            ["Monday", "Wednesday", "Friday"],
            ["Monday", "Wednesday", "Friday", "Sunday"],
            ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ],
        ]

        self.id = sql_tuple[0]
        self.medName = sql_tuple[1]
        self.dateFilled = sql_tuple[2]
        self.refillsLeft = sql_tuple[3]
        self.refillDate = sql_tuple[4]
        self.timesPerDay = sql_tuple[5]
        self.timesPerWeekId = sql_tuple[6]
        self.folderPath = sql_tuple[7]
        self.createdAt = sql_tuple[8]
        self.archived = sql_tuple[9]

    id: int
    medName: Union[str, None]
    dateFilled: Union[datetime, None]
    refillsLeft: Union[int, None]
    refillDate: Union[datetime, None]
    timesPerDay: Union[int, None]
    timesPerWeekId: Union[list[str], None]
    folderPath: Union[str, None]
    createdAt: Union[datetime, None]
    archived: Union[bool, None]
