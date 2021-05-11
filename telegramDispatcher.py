import json
import requests

telegram_creds = ""


# noinspection PyBroadException
def read_telegram_bot():
    global telegram_creds
    try:
        with open("telegram_details.json", "r") as teleJson:
            telegram_creds = json.load(teleJson)
    except:
        print("Error while reading Telegram Bot and Chat Details\n")
        exit(-1)


# noinspection PyBroadException
def send_msg():
    global telegram_creds
    msg = ""
    if telegram_creds == "":
        read_telegram_bot()
    try:
        with open("panchangam.json", "r") as jsonData:
            panchangamJson = json.load(jsonData)
    except:
        print("Error reading \"panchangam.json\" file\n")
        exit(-1)
    else:
        for i in panchangamJson:
            msg = msg + "<b>" + i + "</b>" + ": " + panchangamJson[i] + "\n"
        post_url = "https://api.telegram.org/bot" + telegram_creds["token"] + "/sendMessage?chat_id=" + telegram_creds["chat_id"] + "&parse_mode=html" + "&text=" + msg
        status = requests.post(post_url)
        return status
