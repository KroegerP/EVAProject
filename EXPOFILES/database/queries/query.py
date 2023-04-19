from datetime import datetime
from typing import Optional, Union
import psycopg2
import psycopg2.extensions
import psycopg2.errors


from database.classes.weekly_reminders import WeeklyReminder
from database.classes.confirmations import Confirmation
from database.dbUtils import executeQuery
from constants.confirmations import *
from database.classes.medications import Medication


# TODO: Move to another file
def tuplesToMedicationList(data: list[tuple]) -> list[Medication]:
    """
    Converts tuple list to a list of `Medications`.

    Inputs:
        `data`:       The list of tuples from a query
    """
    return_list = []

    if len(data) > 0:
        for tuple in data:
            return_list.append(Medication(tuple))

    return return_list


def tuplesToConfirmationsList(data: list[tuple]) -> list[Confirmation]:
    """
    Converts tuple list to a list of `Confirmation`.

    Inputs:
        `data`:       The list of tuples from a query
    """
    return_list = []

    if len(data) > 0:
        for tuple in data:
            return_list.append(Confirmation(tuple))

    return return_list


def medicationsQuery(
    conn: psycopg2.extensions.connection,
) -> Union[list[Medication], None]:
    """
    Queries the `medications` table for all medications.

    Inputs:
        `conn`:       Postgres connection object
    """
    medications_list = []

    sql_string = "SELECT \
                    * \
                    FROM \
                        medications \
                    WHERE \
                        archived is FALSE;"

    data = executeQuery(conn, sql_string)

    medications_list = tuplesToMedicationList(data)

    return medications_list


def timesList(conn: psycopg2.extensions.connection) -> dict[list[str]]:
    """
    Queries the `medications` table for active (?) medications and,
    based on their `timesPerDay` and `timesPerWeek` fields, create a list
    of HH:MM times that the EVA must perform a confirmation check

    Inputs:
        `conn`:       Postgres connection object

    Outputs:
        `times_list`: A list of times in which to open the confirmation UI
    """
    date = datetime.now()

    sql_string = "SELECT \
                    * \
                    FROM \
                        medications \
                    WHERE \
                        archived is FALSE;"

    data = executeQuery(conn, sql_string)

    meds: list[Medication] = tuplesToMedicationList(data)

    meds_to_add: list[Medication] = []

    day_of_week = date.strftime("%A")

    for med in meds:
        reminder = getReminderById(conn, med.timesPerWeekId)
        for day in reminder.days_list():
            if day_of_week == day:
                meds_to_add.append(med)

    morning_conf = f"{MORNING_CONFIRM_H}:{MORNING_CONFIRM_M}"
    midday_conf = f"{MIDDAY_CONFIRM_H}:{MIDDAY_CONFIRM_M}"
    afternoon_conf = f"{AFTERNOON_CONFIRM_H}:{AFTERNOON_CONFIRM_M}"

    confirm_tuples = {morning_conf: [], midday_conf: [], afternoon_conf: []}

    if len(meds_to_add) > 0:
        for med in meds_to_add:
            if med.timesPerDay == 3:
                confirm_tuples[morning_conf].append(med.medName)
                confirm_tuples[midday_conf].append(med.medName)
                confirm_tuples[afternoon_conf].append(med.medName)
            elif med.timesPerDay == 2:
                confirm_tuples[morning_conf].append(med.medName)
                confirm_tuples[afternoon_conf].append(med.medName)
            elif med.timesPerDay == 1:
                confirm_tuples[afternoon_conf].append(med.medName)
            else:
                print(f"Invalid number of times to check medication {med.medName}")

    return confirm_tuples


def confirmationsQuery(conn: psycopg2.extensions.connection):
    """
    Queries the `confirmations` table for all confirmations.

    Inputs:
        `conn`:       Postgres connection object
    """
    pass


def getMedByName(
    conn: psycopg2.extensions.connection, medName: str
) -> Optional[Medication]:
    """
    Queries the `medications` a medication given an medicationId and a medName.

    Inputs:
        `conn`:       Postgres connection object
        `medName`:    Name of medication to check
    """

    sql_string = f"SELECT \
                    * \
                    FROM \
                        medications \
                    WHERE \
                        archived is FALSE\
                    AND \
                        medname = '{medName}'\
                    ORDER BY \
                        created_at DESC \
                    LIMIT 1;"

    med = executeQuery(conn, sql_string, "one")

    med = Medication(med)

    return med


def getConfirmationsByMedName(
    conn: psycopg2.extensions.connection, medName: str, interval: str = "100 days"
) -> list[Confirmation]:
    """
    Queries the `confirmations` table for confirmations by a med name.

    Inputs:
        `conn`:       Postgres connection object
        `medName`:    Name of medication to check
    """
    sql_string = f"SELECT\
                    *\
                    FROM \
                        confirmations \
                    WHERE \
                        medname = '{medName}' \
                    AND \
                        created_at >= (NOW() - INTERVAL '{interval}')\
                    ORDER BY created_at ASC;"
    try:
        data = executeQuery(conn, sql_string, "all")

        confirmations: list[Confirmation] = tuplesToConfirmationsList(data)

    except:
        print(
            f"Error: Umable to get confirmations for {medName} within the past {interval}"
        )
        confirmations = []

    return confirmations


def getPercentConfirmsPerTimePeriod(
    conn: psycopg2.extensions.connection, medName: str, interval: str = "100 days"
) -> float:
    """
    Returns the percentage of confirmations in the past week that
    are marked as taken for medication `medName`

    Inputs:
        `conn`:         Postgres connection object
        `medName`:      Name of medication to check
        `interval`:     Optional parameter to set the time interval for the query, default is 7 days

    Outputs:
        `percent_val`:  Percentage over the `interval` that the user confirmed the medication as `taken`
    """
    percent_val = 0
    sql_string = f"SELECT\
                    ( \
                        100.0 * COUNT(*) / \
                        ( SELECT COUNT(*) \
                            FROM \
                                confirmations \
                            WHERE \
                                medname = '{medName}'\
                                AND \
                                    created_at >= (NOW() - INTERVAL '{interval}'))\
                        ) AS percentage \
                    FROM \
                        confirmations \
                    WHERE \
                        medname = '{medName}' \
                        AND \
                            taken = true \
                        AND \
                            created_at >= (NOW() - INTERVAL '{interval}');"

    try:
        data = executeQuery(conn, sql_string, "one")
        percent_val = data[0]
    except:
        percent_val = -1

    print(f"% from past {interval}: {percent_val:.4g}%")

    return percent_val


def getReminderById(
    conn: psycopg2.extensions.connection, id: str
) -> Union[WeeklyReminder, None]:
    """
    Queries the `weeklyreminders` table for reminder by an id.

    Inputs:
        `conn`:       Postgres connection object
        `medName`:    Name of medication to check
    """
    sql_string = f"SELECT\
                    *\
                    FROM \
                        weeklyreminders \
                    WHERE \
                        id = '{id}';"
    try:
        data = executeQuery(conn, sql_string, "one")

        reminder = WeeklyReminder(data)

    except:
        print(f"Error: Umable to get reminder for id {id}")
        reminder = None

    return reminder

def getReminderByMedId(
    conn: psycopg2.extensions.connection, id: str
) -> Union[WeeklyReminder, None]:
    """
    Queries the `weeklyreminders` table for reminder by an id.

    Inputs:
        `conn`:       Postgres connection object
        `medName`:    Name of medication to check
    """
    sql_string = f"SELECT\
                    *\
                    FROM \
                        weeklyreminders \
                    WHERE \
                        medications_id = '{id}';"
    try:
        data = executeQuery(conn, sql_string, "one")

        reminder = WeeklyReminder(data)

    except:
        print(f"Error: Umable to get reminder for id {id}")
        reminder = None

    return reminder
