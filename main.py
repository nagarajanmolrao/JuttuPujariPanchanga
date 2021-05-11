import requests
import json
from bs4 import BeautifulSoup
import datetime
import telegramDispatcher as telegramSend

today = datetime.datetime.now().strftime("%d/%m/%Y")


# noinspection PyBroadException
def generate_url():
    global today
    return "https://www.drikpanchang.com/panchang/day-panchang.html?date=" + today + "&time-format=24hour&geoname-id=1277333"
# geoname-id=1265863 for Krishnagiri
# geoname-id=1277333 for Bengaluru


# noinspection PyBroadException
def scrape_panchangam(url):
    global today
    # Make a request
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Create all_h1_tags as empty list
    all_key = []
    all_value = []
    panchangam = {}

    contentTable = soup.find('div', {'class': 'dpTableCardWrapper'})
    # print(contentTable)
    cards = contentTable.find_all('div', {'class': 'dpTableCard'})
    # print(cards)
    for card in cards:
        rows = card.find_all('div', {'class': 'dpTableRow'})
        for i in rows:
            keys = i.find_all('div', {'class': 'dpTableCell dpTableKey'})
            values = i.find_all('div', {'class': 'dpTableCell dpTableValue'})
            for j in keys:
                all_key.append(j.get_text())
            for j in values:
                all_value.append(j.get_text())
            try:
                panchangam = {str(all_key[i]): str(all_value[i]) for i in range(len(all_key))}
            except:
                pass
            # print(panchangam)

    # Normalize Udaya Lagna Muhurta for the day
    ULMD = panchangam[""]
    list_of_names = ["Mesha", "Vrishabha", "Mithuna", "Karka", "Simha", "Kanya", "Tula", "Vrishchika", "Dhanu",
                     "Makara", "Kumbha", "Meena"]
    normal_ULMD = ""
    for i in range(0, len(list_of_names)):
        if i != 11:
            start_pos = ULMD.find(list_of_names[i]) + len(list_of_names[i]) + 3
            end_pos = ULMD.find(list_of_names[i + 1])
            normal_ULMD = normal_ULMD + list_of_names[i] + ": " + ULMD[start_pos:end_pos] + "\n"
        else:
            start_pos = ULMD.find(list_of_names[i]) + len(list_of_names[i]) + 3
            end_pos = len(ULMD)
            normal_ULMD = normal_ULMD + list_of_names[i] + ": " + ULMD[start_pos:end_pos] + "\n"
    panchangam[ULMD[:31]] = panchangam[""]
    del panchangam[""]
    panchangam[ULMD[:31]] = normal_ULMD

    # Remove unnecessary keys from the dictionary
    panchangam.pop("\u00a0")

    # Join the Chandramasa rows
    panchangam["Chandramasa"] = panchangam["Chandramasa"] + "\n" + panchangam[" "]
    panchangam.pop(" ")

    # Normalize by removing Unicode Characters in values
    for i in panchangam:
        panchangam[i] = panchangam[i].encode('ascii', 'ignore').decode()

    todayDict = {"Today's Date": today}
    todayDict.update(panchangam)
    panchangam = todayDict
    with open("panchangam.json", "w") as file:
        json.dump(panchangam, file, indent=4)


if __name__ == '__main__':
    scrape_panchangam(generate_url())
    telegramSend.send_msg()
