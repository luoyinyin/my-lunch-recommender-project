# my-lunch-recommender-project

General information  
* This is a Python application that allows users to get lunch recommendation by answering few questions
*  The purpose of the project: To help user save time when deciding what to eat every day

Technologies Used
* Python 3.13
* Requests moudle
* JSON
* Random moudle
* OpenWeather API

Features
* use real-time temperature data from OpenWeather to personalise the recommendation
* Have random mode to decide for users who doesn't like to make decisions

Screenshots
Example of the random recommendation mode running in the terminal
<img width="1398" height="640" alt="a8486cec-85b8-473e-9f7e-9f2a8127647a" src="https://github.com/user-attachments/assets/e00cd042-1a05-44d2-84aa-9d823ae4487a" />



Setup
* Requires Python 3.13 and an IDE
* download this repository
* open a terminal
* Install requests moudle through typing: pip install requests in the terminal
* Install random moudle
* run the program
  

Usage
The program has 2 mode
* If you enter 1 in the first questions, you enter the quiz mode.
Just follow the questions to select Flavour(spicy/salty/sweet), Country(Chinese, Thai, etc.), and wether you want to consider the current temperature of Sydney

* If you enter 2 in the first questions, it leads you to the random mode. You can request up to 10 different random dishes before invited to switch to the quiz mode. If you are still not satisfied with it and refuse to switch to quiz mode, you will get a final random recommendation and the program will end.

Project status
Completed

Room for inprovement
* Expand the food database: the current food_list is still limited. Need more diverse food items in food list to make recommendation more diverse and accurate
* Make the temperature data more flexible: the current weather API is fixed to Sydney.






