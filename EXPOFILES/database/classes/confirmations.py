

from datetime import datetime
from typing import Union

class Confirmation:
    """
    Class corresponding to the `medications` table in the EVA database

    Inputs:
        `sql_tuple`:          SQL tuple returned from a query to initialize data

    Attributes:
        `id`:               ID of the monfirmation. Unique to the monfirmation as the user uploads a
                            monfirmation via the workflow.
        `medName`:          Confirmation name.
        `dateFilled`:       Date the monfirmation was filled, from the bottle scan.
        `refillsLeft`:      Amount of refills left for the bottle, from the bottle scan.
        `timesPerDay`:      # of times per day the user should be notified to take monfirmation, this
                            is currently stored in the db as a number and converted to a list of
                            strings for use with the confirmation system.
        `timesPerWeek`:     # of times per week the user should be notified to take monfirmation.
        `folderPath`:       Folder path to the image generated from the bottle scan (to be deprecated).
        `createdAt`:        Time in which the monfirmation was added to the DB.
    """
    def __init__(self, sql_tuple: tuple) -> None:

        self.id = sql_tuple[0]
        self.medName = sql_tuple[1]
        self.taken = sql_tuple[2]
        self.medicationId = sql_tuple[3]
        self.createdAt = sql_tuple[4]

    id: int
    medName: Union[str, None]
    taken: Union[bool, None]
    medicationId: Union[int, None]
    createdAt: Union[datetime, None]
    archived: Union[bool, None]
