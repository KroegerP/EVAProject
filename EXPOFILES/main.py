import os
from dotenv import load_dotenv

from UIController import UIController
from database.dbUtils import connectToEvaDB

load_dotenv()

print(os.getenv("EVA_VERSION"))


def main():
    app_conn = connectToEvaDB()

    my_controller = UIController(app_conn)


if __name__ == "__main__":
    main()
