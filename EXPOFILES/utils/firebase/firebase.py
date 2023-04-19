import os
from typing import Any
import firebase_admin
import firebase_admin.messaging
from firebase_admin import credentials, firestore
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request
from utils.wrappers import env_wrapper

from constants.auth import *


class FirebaseApp:
    def __init__(self):
        creds = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", None)
        if creds is None:
            raise ValueError(
                "Credentials path is not defined in .env, or the dotenv package did not load the file correctly."
            )
        self.cred = credentials.Certificate(creds)
        self.default_app = firebase_admin.initialize_app()
        self.messaging = firebase_admin.messaging
        self.scopes = ["https://www.googleapis.com/auth/firebase.messaging"]
        self.firestore: firestore = firestore.client(self.default_app)

        # TOKEN IS A PER DEVICE REGISTRATION
        # When you load the mobile app, the home screen will display your appllication ID (or if I get time it will be in the settings),
        # this will soon be changed so that you input this into the EVA, and then your device is registered to the EVA device
        self.token = os.getenv("DEVICE_REG_TOKEN")
        self.headers = {
            "Authorization": "Bearer " + self._get_access_token(),
            "Content-Type": "application/json; UTF-8",
        }

        return

    def _get_access_token(self):
        """Retrieve a valid access token that can be used to authorize requests.

        :return: Access token.
        """
        service_data_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", None)

        credentials: Credentials = Credentials.from_service_account_file(
            filename=service_data_path, scopes=self.scopes
        )
        request = Request()
        credentials.refresh(request)
        return credentials.token

    # @env_wrapper
    def send_notification(self, title: str, body: str, data: dict) -> None:
        """
        Accepts title and body strings, and will push it to a device,
        with an optional data field to send a payload
        """

        android_config = self.messaging.AndroidConfig(priority="high")

        if data:
            notif = self.messaging.Notification(title=title, body=body)
            msg = self.messaging.Message(
                token=self.token, notification=notif, data=data, android=android_config
            )
        else:
            notif = self.messaging.Notification(title=title, body=body)
            msg = self.messaging.Message(
                token=self.token, notification=notif, android=android_config
            )

        response = self.messaging.send(msg)

        # Response should be a message ID string
        print("Notificaation: ", response)

        return

    @env_wrapper
    def send_message(self, data) -> None:
        """
        Accepts a dictionary of strings, and will send it to a device
        """
        new_message = self.messaging.Message(token=self.token, data=data)

        response = self.messaging.send(new_message)

        # Response should be a message ID string
        print("Message: ", response)

        return

    def add_user(self, data: dict[str, str]):
        ref = self.firestore.collection("users").document()
        ref.set(
            {
                "firstname": data["firstname"],
                "email": data["email"],
                "emergency_contact_phone": data["emergency_contact_phone"],
                "lastname": data["lastname"],
                "emergency_contact_name": data["emergency_contact_name"],
            }
        )

    def add_medication_by_user_id(self, data: dict[str, Any]):
        ref = (
            self.firestore.collection("users")
            .document("BMzcY66MlmwygVrdDgvh")
            .collection("medications")
            .document()
        )
        ref.set(
            {
                "medname": data["medname"],
                "priority": data["priority"],
                "initial_pill_count": data["initial_pill_count"],
                "amount_per_use": data["amount_per_use"],
                "times_per_week": data["times_per_week"],
                "date_added": data["date_added"],
                "refill_date": data["refill_date"],
                "times_per_day": data["times_per_day"],
            }
        )

    def read_users_collection(self):
        users_ref = self.firestore.collection("users")
        docs = users_ref.stream()

        for doc in docs:
            print(f"{doc.id} => {doc.to_dict()}")
