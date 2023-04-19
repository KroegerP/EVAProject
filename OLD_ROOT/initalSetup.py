import speech
import display
import connectWifi
import requests
import time
import Responce

def firstPowerOn():
    welcomeString = "Hi there. My name's Eva. Let's start with setting up the wifi."
    Responce.speechandsay(welcomeString)

    wifiNameString = "Please enter the name of your wifi network using the onscreen keyboard"
    Responce.speechandsay(wifiNameString)
    print("wifiNameInput: ")
    #wifiName = input()
    wifiName = "Alex's iPhone"

    #wifiName = myOutput()
    #print(myVar)
    #wifiName = setwifiparam()

    wifiPassString = "Please enter the password of your wifi network using the onscreen keyboard"
    Responce.speechandsay(wifiPassString)
    print("wifiPassInput: ")
    #wifiPass = input()
    wifiPass = "Aspenthecat1!"


    wifiConnectingMessage = "Connecting to wifi"
    Responce.speechandsay(wifiConnectingMessage)

    connectWifi.createNewConnection(wifiName, wifiName, wifiPass)

    time.sleep(5)

    url = "http://www.kite.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        success = "You connected to the internet successfully!"
        Responce.speechandsay(success)
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection.")

    namePrompt = "My name is Eva. What's your name?"
    Responce.speechandsay(namePrompt)

    #userName = input()
    userName = "Alex"

    namePrompt = "Hi " + userName + ". You're all set up. I'll let you know when it's time to take your medicine."
    Responce.speechandsay(namePrompt)

    askQuestions = "Feel free to ask me any questions in the meantime."
    Responce.speechandsay(askQuestions)

#firstPowerOn()

