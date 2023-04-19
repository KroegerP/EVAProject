from datetime import datetime
from typing import Union


class WeeklyReminder:
    """
    Class corresponding to the `weeklyreminders` table in the EVA database

    Inputs:
        `sql_tuple`:          SQL tuple returned from a query to initialize data

    Attributes:
        `id`:               ID of the medication. Unique to the medication as the user uploads a
                            medication via the workflow.
        `medication_id`:    Medication Id
        `monday`:           Monday.
        `tuesday`:          Date the medication was filled, from the bottle scan.
        `wednesday`:        Amount of refills left for the bottle, from the bottle scan.
        `friday`:           # of times per day the user should be notified to take medication, this
                            is currently stored in the db as a number and converted to a list of
                            strings for use with the confirmation system.
        `saturday`:         # of times per week the user should be notified to take medication.
        `sunday`:           Folder path to the image generated from the bottle scan (to be deprecated).
    """

    def __init__(self, sql_tuple: tuple) -> None:
        self.id = sql_tuple[0]
        self.medication_id = sql_tuple[1]
        self.monday = sql_tuple[2]
        self.tuesday = sql_tuple[3]
        self.wednesday = sql_tuple[4]
        self.thursday = sql_tuple[5]
        self.friday = sql_tuple[6]
        self.saturday = sql_tuple[7]
        self.sunday = sql_tuple[8]

    def days_list(self) -> list:
        my_list = []
        if self.monday:
            my_list.append("Monday")
        if self.tuesday:
            my_list.append("Tuesday")
        if self.wednesday:
            my_list.append("Wednesday")
        if self.thursday:
            my_list.append("Thursday")
        if self.friday:
            my_list.append("Friday")
        if self.saturday:
            my_list.append("Saturday")
        if self.sunday:
            my_list.append("Sunday")

        return my_list

    id: int
    medication_id: int
    monday: bool
    tuesday: bool
    wednesday: bool
    thursday: bool
    friday: bool
    saturday: bool
    sunday: bool
