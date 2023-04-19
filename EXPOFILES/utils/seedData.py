import csv
import random
from datetime import datetime, timedelta


def generateSeedConfirmationData(medName: str = "Ibuprofen"):
    num_tuples = 50
    id_start = 19
    foreign_key_id = 3
    bool_true_probability = 0.75
    start_date = datetime.now() - timedelta(days=7)
    hours = range(7, 21)

    with open(
        f"../database/{medName}-confirmations-data.csv", "w", newline=""
    ) as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["id", "medname", "taken", "medicationid", "created_at"])

        for i in range(num_tuples):
            boolean_value = random.choices(
                [True, False],
                weights=(bool_true_probability, 1 - bool_true_probability),
            )[0]

            created_at = start_date + timedelta(
                days=random.randint(0, 6),
                hours=random.choice(hours),
                minutes=random.randint(0, 59),
                seconds=random.randint(0, 59),
            )

            writer.writerow(
                [
                    id_start + i,
                    medName,
                    boolean_value,
                    foreign_key_id,
                    created_at.strftime("%Y-%m-%d %H:%M:%S"),
                ]
            )
