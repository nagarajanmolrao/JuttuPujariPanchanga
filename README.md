# JuttuPujariPanchanga
A simple python script which scrapes a particular day's Pachanga from "https://www.drikpanchang.com/" ,stores it in a JSON file and sends a formatted message from the JSON file to a telegram group.

###### The project name "JuttuPujariPanchanga" is simply a funny name that I came with and means no disrespect to any individual or any profession.

### DESCRIPTION
This main idea for the development of this program was to have a minimalist way of reading the panchanga of the day. This program uses an amazing module, called the "BeautifulSoup", which plays the major role in getting the data from the website to a normal form.
Basically , for a lay man, all it does is, it parses the HTML source code and offer a handful functions to find and retrieve what is required in an easy way.

_More on it can be found here :_ [https://realpython.com/beautiful-soup-web-scraper-python/]

The URL of the DrikPanchang site itself contains many query parameters:
-	_date_ : This parameter can be used to generate panchanga of a particular date.(formats as **dd/mm/yyyy**)(The date for which the panchanga is generated is derived from the system on which it runs on.)
-	_time-format_ : This parameter can be used to specify the time format in which the values in the panchanga are to be in. (the values can only be "12hour", "24hour" and "24plushour")(more details on "24plushour" time format [https://www.drikpanchang.com/tutorials/basics/time-after-midnight.html])
-	_geoname-id_ : This parameter is used to specify the location for which the panchanga is to be generated. (to know the _geoname-id_ of a place, head over to [https://www.drikpanchang.com/location/panchang-location-details.html], type in to search your location and select your preferred location. The page should refresh and your new URL would look something like [https://www.drikpanchang.com/location/panchang-location-details.html?geoname-id=1277333] ,which clearly has the _geoname-id_ in it)

So with the help of these parameters one can generate panchanga for any location and for any date you want.

Moreover the program overwrites the JSON file ,_"panchangam.json"_ every time the program runs.

#### INSTALLATION

-	Clone the GitHub repository and change into the directory

	`git clone https://github.com/nagarajanmolrao/JuttuPujariPanchanga`
-	Copy the _"telegram_details_template.json"_ to _"telegram_details.json"_
-	Put in the actual Bot token and the Telegram Group Chat ID in _"telegram_details.json"_ file
-	Install the python dependencies

	`pip install -r requirements.txt`
-	Just run the _"main.py"_ file

	`python main.py`
-	See the panchanga appear on your telegram group.

##### DOCKER INSTRUCTIONS

-	Clone the GitHub repository and change into the directory

	`git clone https://github.com/nagarajanmolrao/JuttuPujariPanchanga`
-	Copy the _"telegram_details_template.json"_ to _"telegram_details.json"_
-	Put in the actual Bot token and the Telegram Group Chat ID in _"telegram_details.json"_ file
-	To set at what time the message must be sent, change the time after the word _"tomorrow"_ in the sleep command in _"BotCronScript.sh"_ to any required time in 24HOUR format.
-	Build the docker image

	`docker build . -t juttu_pujari_panchanga`
-	Run the docker image

	`docker run -d juttu_pujari_panchanga`


