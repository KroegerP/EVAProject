from utils.firebase.firebase import FirebaseApp

from UIController import UIController
from database.dbUtils import connectToEvaDB


def main():
    app_conn = connectToEvaDB()
    firebase_app = FirebaseApp()

    # Test message to EVA Mobile App
    # firebase_app.send_message({'testing': '123'})

    myUIController = UIController(app_conn)

if __name__ == '__main__':
    main()