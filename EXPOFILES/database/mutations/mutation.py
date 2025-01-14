import os
import psycopg2
import psycopg2.extensions
import psycopg2.errors

from utils.fileHandler import delete_images, move_images
from utils.firebase.firebase import FirebaseApp
from database.classes.medications import Medication
from database.queries.query import getMedByName, getReminderById, getReminderByMedId
from datetime import datetime

from database.dbUtils import executeQuery


def createConfirm(
    conn: psycopg2.extensions.connection, medName: str, taken: bool = False
):
    med = getMedByName(conn, medName)

    string = f"INSERT INTO public.confirmations (medname,taken,medicationid,created_at) \
	                VALUES ('{medName}',{taken},'{med.id}',NOW());"
    data = executeQuery(conn, string)

    print(f"RESULTING DATA: {data}")

    return


# TODO: Update so that the ID for a weeklyreminders row is created and added
def createMedicine(
    conn: psycopg2.extensions.connection,
    medName: str,
    dateFilled: datetime,
    refills: int,
    refillDate: datetime,
    timesPerDay: int,
    timesPerWeek: int,
    folderPath: str,
):
    dateFilledStr: str = dateFilled.strftime("%\d/%m/%Y")
    refillDateStr: str = refillDate.strftime("%\d/%m/%Y")

    sql = f"INSERT INTO public.medications \
            (medname, datefilled, refillsleft, refilldate, \
            timesperday, timesperweek, folderpath, created_at) \
            VALUES ('{medName}', TO_DATE('{dateFilledStr}', YYYYMMDD),\
            {refills}, TO_DATE('{refillDateStr}', YYYYMMDD), {timesPerDay}, {timesPerWeek}, '{folderPath}', NOW());"

    data = executeQuery(conn, sql)

    print(f"RESULTING DATA: {data}")

    return


def createMedFromDict(
    conn: psycopg2.extensions.connection, newMedDict: dict, firebase: FirebaseApp
):
    medName = newMedDict["medName"] if "medName" in newMedDict else None
    dateFilled = (
        newMedDict["dateFilled"]
        if "dateFilled" in newMedDict
        else datetime.now().strftime("%Y-%M-%D")
    )
    refillsLeft = newMedDict["refillsLeft"] if "refillsLeft" in newMedDict else None
    refillDateStr = newMedDict["refillDate"] if "refillDate" in newMedDict else None
    timesPerDay = newMedDict["timesPerDay"] if "timesPerDay" in newMedDict else None
    # folderPath = newMedDict["medName"] if "medName" in newMedDict else None
    folderPath = f"EXPOFILES/database/meds/{medName}"

    print(medName)
    print(dateFilled)
    print(refillsLeft)
    print(refillDateStr)
    print(timesPerDay)
    print(folderPath)

    if os.getenv("DB_LOCATION", None) == "firestore" and firebase is not None:
        firebase.add_medication_by_user_id(
            {
                "medname": medName,
                "priority": 1,
                "refill_date": refillDateStr,
                "initial_pill_count": 0,
                "amount_per_use": 2,
                "times_per_day": timesPerDay,
                "times_per_week": ["Monday", "Wednesday", "Friday"],
                "date_added": dateFilled,
            }
        )

    sql = f"INSERT INTO public.medications \
            (medname, datefilled, refillsleft, refilldate, \
            timesperday, timesperweek_id, folderpath, created_at) \
            VALUES ('{medName}', '{dateFilled}',\
            {refillsLeft}, '{refillDateStr}', '{timesPerDay}', '1','{folderPath}', NOW());"

    data = executeQuery(conn, sql)

    med: Medication = getMedByName(conn, medName)

    if med is None:
        print("ERROR: Unable to query for new med, returning.")
        return

    create_reminders = (
        f"INSERT INTO public.weeklyreminders (medications_id) VALUES ({med.id});"
    )

    data = executeQuery(conn, create_reminders)

    reminder = getReminderByMedId(conn, med.id)

    alterMedicine(conn, med, "timesperweek_id", str(reminder.id))
    alterMedicine(conn, med, "folderpath", f"{folderPath}/{med.id}/")

    move_images(
        "EXPOFILES/database/new/",
        med.id,
        med.medName,
    )
    delete_images("EXPOFILES/database/new")

    print("New medication added!")


def updateDaysPerWeek(
    conn: psycopg2.extensions.connection, reminder_id: str, newVal: str
):
    try:
        sql = f"UPDATE weeklyreminders \
                SET monday = '{newVal[0]}', \
                tuesday = '{newVal[1]}', \
                wednesday = '{newVal[2]}', \
                thursday = '{newVal[3]}', \
                friday = '{newVal[4]}', \
                saturday = '{newVal[5]}', \
                sunday = '{newVal[6]}' \
                WHERE id = '{reminder_id}'"

    except IndexError:
        print(f"ERROR: newVal length is incorrect for date setting: {newVal}")
        return {"errors": "Unable to update medication"}

    data = executeQuery(conn, sql)

    if data is None:
        return {"errors": "Unable to update medication"}

    return {"Days Per Week": "new days"}


def alterMedicine(
    conn: psycopg2.extensions.connection,
    med: Medication,
    fieldToEdit: str,
    newVal: str,
) -> dict:
    attr_list = [a for a in dir(med) if not a.startswith("__")]
    for attr in attr_list:
        if fieldToEdit == attr:
            if fieldToEdit in ["refillDate", "dateFilled"]:
                continue
            else:
                setattr(med, attr, newVal)

    print(f"TIMES PER WEEK ID {med.timesPerWeekId}")

    dateFilledStr: str = med.dateFilled.strftime("%Y-%m-%d")
    refillDateStr: str = med.refillDate.strftime("%Y-%m-%d")

    # If its timesPerWeek, we update a different table
    if fieldToEdit == "timesPerWeek":
        weekly_reminder = getReminderById(conn, med.timesPerWeekId)
        if weekly_reminder:
            sql = f"UPDATE weeklyreminders \
                    SET monday = '{newVal[0]}', \
                    tuesday = '{newVal[1]}', \
                    wednesday = '{newVal[2]}', \
                    thursday = '{newVal[3]}', \
                    friday = '{newVal[4]}', \
                    saturday = '{newVal[5]}', \
                    sunday = '{newVal[6]}', \
                    WHERE id = '{med.timesPerWeekId}'"
        else:
            print("ERROR GETTING REMINDERS DATA TO SET")
    elif fieldToEdit == "timesperweek_id":
        sql = f"UPDATE medications \
                SET \
                timesperweek_id = '{newVal}' \
                WHERE id = '{med.id}';"
    elif fieldToEdit == "folderpath":
        sql = f"UPDATE medications \
                SET \
                folderpath = '{newVal}' \
                WHERE id = '{med.id}';"
    else:
        sql = f"UPDATE medications \
                SET medname = '{med.medName}', \
                datefilled = '{newVal if fieldToEdit == 'dateFilled' else dateFilledStr}', \
                refillsleft = '{med.refillsLeft}', \
                refilldate = '{newVal if fieldToEdit == 'refillDate' else refillDateStr}', \
                timesperday = '{med.timesPerDay}' \
                WHERE id = '{med.id}'"

    data = executeQuery(conn, sql)

    if data == "0" or data is None:
        return {"errors": "Unable to update medication"}

    print(f"Updated {fieldToEdit} with {newVal}")

    return {fieldToEdit: newVal}


def archiveMedication(conn: psycopg2.extensions.connection, medId: int):
    sql = f"UPDATE public.medications \
                SET archived=true \
                WHERE id={medId};"

    data = executeQuery(conn, sql)

    print(data)

    return
