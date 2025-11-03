#11111

print ("🍽️Hi! Welcome to the Lunch Recommender!")


while True:
    print ("\nAny clues for today's lunch?\n(1.✅Yes, got some preferences/ 2.❌No ideas at all, choose it for me!)")
    user_feeling = input(">>").strip()
    if user_feeling == "1":
        break
    elif user_feeling == "2":
        break
    else:
        if user_feeling == "":
            print("❗️Invalid input❗\nYou didn't enter anything! Please enter 1 or 2")
        else:
            print("❗️Invalid input❗\nPlease enter 1 or 2")

#a list in a dictionaries to store all available lunch options
Food_list = [{"name": "Tom yum soup", "flavour": ["sour", "salty", "spicy"], "country": "Thai", "weather": ["cold"]},
                 {"name": "sushi", "flavour": ["salty"], "country": "Japanese", "weather": ["neutral"]},
                 {"name": "Butter chicken", "flavour": ["salty", "spicy"], "country": "Indian", "weather": ["cold"]},
                 {"name": "mango chicken curry", "flavour": ["salty", "spicy","sweet"], "country": "Indian", "weather": ["hot"]},
                 {"name": "Masala dosa", "flavour": ["salty"], "country": "Indian", "weather": ["hot"]},
                 {"name": "Panner Tikka Masala", "flavour": ["salty"], "country": "Indian", "weather": ["cold","neutral"]},
                 {"name": "hot pot", "flavour": ["spicy", "salty"], "country": "Chinese", "weather": ["cold"]},
                 {"name": "soba noodle", "flavour": ["salty"], "country": "Japanese", "weather": ["hot"]},
                 {"name": "spicy abura soba", "flavour": ["salty","spicy"], "country": "Japanese", "weather": ["hot"]},
                 {"name": "pad see ew", "flavour": ["sweet"], "country": "Thai", "weather": ["neutral"]},
                 {"name": "salmon salad", "flavour": ["salty"], "country": "Western", "weather": ["hot","neutral"]},
                 {"name": "kebab wrap", "flavour": ["salty"], "country": "Middle-Eastern", "weather": ["neutral"]},
                 {"name": "falafel salad bowl", "flavour": ["salty"], "country": "Middle-Eastern", "weather": ["hot"]},
                 {"name": "lamb tagine", "flavour": ["salty"], "country": "Middle-Eastern", "weather": ["cold"]},
                 {"name": "shawarma plate", "flavour": ["salty"], "country": "Middle-Eastern", "weather": ["hot"]},
                 {"name": "Moroccan honey chicken", "flavour": ["sweet","salty"], "country": "Middle-Eastern", "weather": ["cold"]},
                 {"name": "Tonkotsu ramen", "flavour": ["salty"], "country": "Japanese", "weather": ["cold"]},
                 {"name": "Spicy Tonkotsu ramen", "flavour": ["salty","spicy"], "country": "Japanese", "weather": ["cold","neutral"]},
                 {"name": "Kimbap", "flavour": ["salty"], "country": "Korean", "weather": ["neutral"]},
                 {"name": "Hainan chicken rice", "flavour": ["salty"], "country": "Chinese", "weather": ["neutral"]},
                 {"name": "fish and chips", "flavour": ["salty"], "country": "Western", "weather": ["neutral"]},
                 {"name": "beef burger", "flavour": ["salty"], "country": "Western", "weather": ["neutral"]},
                 {"name": "pork katsu curry don", "flavour": ["salty"], "country": "Japanese", "weather": ["neutral"]},
                 {"name": "tamagoyaki", "flavour": ["sweet"], "country": "Japanese", "weather": ["neutral"]},
                 {"name": "sashimi don", "flavour": ["salty"], "country": "Japanese", "weather": ["hot"]},
                 {"name": "seafood spaghetti", "flavour": ["salty"], "country": "Italian", "weather": ["neutral"]},
                 {"name": "Arrabbiata Pasta", "flavour": ["salty","spicy"], "country": "Italian", "weather": ["cold"]},
                 {"name": "lasagne", "flavour": ["salty"], "country": "Italian", "weather": ["cold"]},
                 {"name": "pasta salad", "flavour": ["salty"], "country": "Italian", "weather": ["hot"]},
                 {"name": "seafood risotto", "flavour": ["salty"], "country": "Italian", "weather": ["hot"]},
                 {"name": "mushroom risotto", "flavour": ["salty"], "country": "Italian", "weather": ["cold"]},
                 {"name": "pizza", "flavour": ["salty"], "country": "Western", "weather": ["neutral"]},
                 {"name": "egg fired rice", "flavour": ["salty"], "country": "Chinese", "weather": ["neutral"]},
                 {"name": "green curry rice", "flavour": ["salty", "spicy"], "country": "Thai","weather": ["neutral"]},
                 {"name": "soup dumplings", "flavour": ["salty"], "country": "Chinese", "weather": ["cold"]},
                 {"name": "boat noodle", "flavour": ["salty"], "country": "Thai", "weather": ["cold"]},
                 {"name": "pad ka pao moo sub", "flavour": ["salty", "spicy"], "country": "Thai", "weather": ["neutral"]},
                 {"name": "kimchi fried rice", "flavour": ["salty", "spicy"], "country": "Korean", "weather": ["neutral","cold"]},
                 {"name": "Korean fired chicken", "flavour": ["salty", "spicy"], "country": "Korean", "weather": ["neutral"]},
                 {"name": "pad thai", "flavour": ["sweet", "spicy"], "country": "Thai", "weather": ["neutral"]},
                 {"name": "kung pao chicken", "flavour": ["sweet"], "country": "Chinese", "weather": ["neutral"]},
                 {"name": "Chinese spicy cold noodles", "flavour": ["salty"], "country": "Chinese", "weather": ["hot"]},
                 {"name": "Korean cold noodles", "flavour": ["sweet"], "country": "Korean", "weather": ["hot"]},
                 {"name": "Korean army stew", "flavour": ["salty","spicy"], "country": "Korean", "weather": ["hot"]},
                 {"name": "Korean Doenjang Jjigae", "flavour": ["salty","spicy"], "country": "Korean", "weather": ["cold"]},
                 {"name": "spicy baked potato", "flavour": ["salty","spicy"], "country": "western", "weather": ["neutral"]},
                 {"name": "spicy buffalo chicken sandwich", "flavour": ["salty","spicy"], "country": "western", "weather": ["neutral"]},
                 {"name": "spicy meat pie", "flavour": ["salty","spicy"], "country": "western", "weather": ["cold","neutral"]},
                 {"name": "BBQ ribs", "flavour": ["salty","spicy","sweet"], "country": "western", "weather": ["cold","neutral"]},
                 {"name": "honey mustard chicken", "flavour": ["sweet","salty"], "country": "western", "weather": ["cold","neutral"]},
                 {"name": "Hawaiian pizza", "flavour": ["sweet"], "country": "western", "weather": ["cold","neutral","hot"]},
                 {"name": "beef pho", "flavour": ["salty"], "country": "Vietnamese", "weather": ["cold"]},
                 {"name": "Banh Mi with pork", "flavour": ["salty"], "country": "Vietnamese", "weather": ["neutral"]},
                 {"name": "Vietnamese fresh spring rolls", "flavour": ["salty"], "country": "Vietnamese", "weather": ["hot"]},
                 {"name": "Vietnamese chicken salad", "flavour": ["salty"], "country": "Vietnamese", "weather": ["hot"]},
                 ]

if user_feeling == "1":
    print("Got it! Let's go through a quiz to find out your Lunch of the day!")

#Start the quiz
#Option1: if user want to answer questions to get lunch recommendations
#flavour choice
    #use a while loop to keep asking user until we get a valid input
    while True:
        print("\n" + "-" * 110)
        print("FLAVOUR SELECTION")
        print("\nWhat flavour are you in the mood for today?\n(1.🌶️spicy/ 2.🧂salty/ 3.🍬sweet)")
        user_flavour = input(">>").strip()
        if user_flavour == "1":
            user_flavour = "spicy"
            break
        elif user_flavour == "2":
            user_flavour = "salty"
            break
        elif user_flavour == "3":
            user_flavour = "sweet"
            break
        else:
            if user_flavour == "":
                print("❗️Invalid input❗\nYou didn't enter anything! Please enter an integer between 1 to 3")
            else:
                print("❗️Invalid input❗️\nPlease entre an integer between 1 to 3")


#ask for a cuisine's country choice
    while True:
        print("\n" + "-" * 110)
        print("CUISINE SELECTION")
        print("\n🌍Which country's cuisine are you craving today?\n(1. Chinese/ 2.Japanese/ 3.Korean/ 4.Western/ 5.Italian/ 6.Indian/ 7.Thai/ 8.Middle-Eastern/ 9.Vietnamese)")
        user_country = input(">>").strip()

        #convert number to country name to improve user typing efficiency
        if user_country == "1":
            user_country = "Chinese"
            break
        elif user_country == "2":
            user_country = "Japanese"
            break
        elif user_country == "3":
            user_country = "Korean"
            break
        elif user_country == "4":
            user_country = "Western"
            break
        elif user_country == "5":
            user_country = "Italian"
            break
        elif user_country == "6":
            user_country = "Indian"
            break
        elif user_country == "7":
            user_country = "Thai"
            break
        elif user_country== "8":
            user_country = "Middle-Eastern"
            break
        elif user_country== "9":
            user_country = "Vietnamese"
            break
        else:
            if user_country == "":
                print("❗️Invalid input❗\nYou didn't enter anything! Please enter an integer between 1 to 9")
            else:
                print("❗️Invalid input❗️\n!!Please entre an integer between 1 to 9!!")


#ask if user want to consider weather for their recommendation
#Reference: access weather api：Automate the boring stuff with Python : practical programming for total beginners (Sweigart, 2024)
    import requests

    city_name = "Sydney"
    state_code = "NSW"
    country_code = "AU"
    api_key = "241057b29d24cf0b09e308b88121a651"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
#first api call, get the coordinates of sydney
    response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_key}')
    import json
    response_data = json.loads(response.text)
#use this latitude and longitude information to find out the current temperature of Sydney
    lat = json.loads(response.text)[0]['lat']
    lon = json.loads(response.text)[0]['lon']

#second api call,
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
    response_data =json.loads(response.text)


    description = response_data["weather"][0]["description"]  #"Holds a string description, such as 'Clear', 'Rain', or 'Snow'" (Sweigart, 2024)
    temp_k = response_data["main"]["temp"]     #Holds the current temperature in Kelvin (Sweigart, 2024)
    feels_like_kelvin = response_data["main"]["feels_like"] #Holds the human perception of the temperature in Kelvin (Sweigart, 2024)

#OpenWeather returns the temperature data in Kelvin, so need to covert Kelvin to Celsius
    feels_like_c = round(feels_like_kelvin - 273.15, 1)
    temp_c = round(temp_k - 273.15, 1)

    #print out the temperature and shows it to user
    print("\n" + "-" * 110)
    print("🌡️TEMPERATURE OF THE DAY")
    print(f"\nToday's weather in {city_name}:{description}")
    print(f"Actual Temperature:{temp_c}degrees Celsius")
    print(f"Feels like:{feels_like_c}degrees Celsius")

    #give user a chance to choose if they want to consider current temperature
    while True:
        print(f"\nWould you like me to consider today's weather for your recommendation? \n (1.Yes/ 2.No)")
        weather_choice = input(">>").strip()
        if weather_choice in ["1","2"]:
            break
        else:
            print("❗️Invalid input❗\nPlease enter 1 or 2")

#set weather condition as none so that if user don't want to consider weather, we can filter this score
    weather_condition = None

    if weather_choice == "1":
        while True:
            print("\nWhich temperature would you like me to use?")
            print("(1.Actual temperature/ 2.Feels like temperature)")
            temp_choice = input(">>").strip()

            if temp_choice in ["1","2"]:
                break
            else:
                if temp_choice == "":
                    print("❗️Invalid input❗\nYou didn't enter anything! Please enter 1 or 2")
                else:
                    print("❗️Invalid input❗\n Please enter 1 or 2")

        if temp_choice == "2":
            temp_to_use = feels_like_c
            print(f"Using feels like temperature:{temp_to_use}degrees Celsius")
        else:
            temp_to_use = temp_c
            print(f"Using actual temperature:{temp_to_use}degrees Celsius")

    #categorise the weather condition in 3 types
        if temp_to_use >18 and temp_to_use <= 26:
            weather_condition ="neutral"
            print("Great temperature for all kinds of food!")
        elif temp_to_use >26:
            weather_condition ="hot"
            print("Omg! Today is so hotttt! \nDon't worry! I'll recommend some refreshing food for you:)")
        else:
            weather_condition ="cold"
            print("\nFreezing cold, right? \nLet me recommend something to warm you up!")

    else:
        print("Okay, I'll focus on your flavour and cuisine preferences!")


    #scoring system to calculate scores for each food
    scores = {} #create an empty dictionary to store food names and their scores
    for food in Food_list:
        score =0 #start with 0 point for each food

     #skip this food if user chose weather condition but the weather condition doesn't match
        if weather_condition != None:
            if weather_condition not in food["weather"]:
                continue

        #scores for flavour
        #add 1 point if flavour match
        if user_flavour in food["flavour"]:
            score +=1

        #scores for country
        #add 1 point if country match
        if food["country"]== user_country:
            score +=1

        #scores for temperature
        #add 1 point if weather if considered
        if weather_condition != None:
            score += 1

        #store the score for this food
        scores[food["name"]]=score

    #use max() to find the food with highest score and use the .get method to look up each food's score
    best_choice =max(scores, key=scores.get)
    print("\n" + "-" * 110)
    print("✨RECOMMENDATION")
    print(f"\nBased on your preferences, we recommend:{best_choice}")
    print("🎉\nHope you like our recommendation!")
    print("\n" + "-" * 110)









#Option 2: user want to have random recommendation
#if user choose to have random recommendation in the beginning of the quiz
elif user_feeling == "2":
    print("\n" + "-" * 110)
    print("✨RANDOM RECOMMENDATION MODE")
    print("\nNo worries! Let me choose it for you randomly!")

    import random

    #user can get random recommendations for maximum 10 times, after 10 times, ask user if they want to answer some questions
    attempt_count = 0
    max_attempts = 10

    #keep generating random suggestions until user is satisfied or reaches 10 attempts
    while attempt_count < max_attempts:
        #pick a randon food from the food list
        suggestion = random.choice(Food_list)["name"]
        print("\n" + "-" * 110)
        print("✨YOUR RECOMMENDATION")
        print(f"\nHow about having: {suggestion}?")
        print("\n" + "-" * 110)

        #ask if the user is happy with this random result
        while True:
            print("Are you satisfied with this recommendation?")
            print("1.Yes, sounds good to me!/ 2.Not really, give me another one")
            satisfaction = input(">>").strip()

            #ends here if the user is happy with the random result
            if satisfaction == "1":
                print(f"😊Perfect! Enjoy your {suggestion} and have a nice day!🎉")
                break
            elif satisfaction == "2":
                attempt_count += 1   #increase attempt counter
                if attempt_count < max_attempts:
                    print("\n😊No problem! Let me pick another dish for you !")
                break
        #debug, avoid user to entre numbers other than 1 or 2
            else:
                if satisfaction == "":
                    print("❗️Invalid input❗\nYou didn't enter anything! Please enter 1 or 2")
                else:
                    print("❗️Invalid input❗️\nPlease enter 1 or 2")

        if satisfaction == "1":
            break

    #after giving user 10 recommendations and they are still unsatisfied, offer the quiz option
    #ask if user want to do the quiz
    if attempt_count == max_attempts:
          print("\nHmm, seems like the random choices aren't working for you today...")
          print("How about answering a few questions so I can give you a better recommendation?")
          print("1.Alright then/ 2.No, I want to stick to the random choices")
          retry = input(">>").strip()

          if retry == "1":
              print("\nGreat! Let's strat the quiz")

              #if user says yes, go back to the initial quiz in option 1 and ask some questions to give recommendation
              #repeat the same codes in option 1
              #ask flavour again
              while True:
                print("\n" + "-" * 110)
                print("FLAVOUR SELECTION")
                print("\nWhat flavour are you in the mood for today?\n(1.🌶️spicy/ 2.🧂salty/ 3.🍬sweet)")
                user_flavour = input(">>").strip()
                if user_flavour == "1":
                    user_flavour = "spicy"
                    break
                elif user_flavour == "2":
                    user_flavour = "salty"
                    break
                elif user_flavour == "3":
                    user_flavour = "sweet"
                    break
                else:
                    if user_flavour == "":
                        print("❗️Invalid input❗\nYou didn't enter anything! Please enter an integer between 1 to 3")
                    else:
                        print("❗️Invalid input❗\nPlease entre integer between 1 to 3")


              #select country
              while True:
                   print("\n" + "-" * 110)
                   print("CUISINE SELECTION")
                   print("\n🌍Which country's cuisine are you craving today?\n(1. Chinese/ 2.Japanese/ 3.Korean/ 4.Western/ 5.Italian/ 6.Indian/ 7.Thai/ 8.Middle-Eastern/ 9.Vietnamese)")
                   user_country = input(">>").strip()
                   if user_country == "1":
                        user_country = "Chinese"
                        break
                   elif user_country == "2":
                        user_country = "Japanese"
                        break
                   elif user_country == "3":
                        user_country = "Korean"
                        break
                   elif user_country == "4":
                        user_country = "Western"
                        break
                   elif user_country == "5":
                        user_country = "Italian"
                        break
                   elif user_country == "6":
                        user_country = "Indian"
                        break
                   elif user_country == "7":
                        user_country = "Thai"
                        break
                   elif user_country== "8":
                        user_country = "Middle-Eastern"
                        break
                   elif user_country== "9":
                        user_country = "Vietnamese"
                        break
                   else:
                       if user_country == "":
                           print("❗️Invalid input❗\nYou didn't enter anything! Please enter an integer between 1 to 9")
                       else:
                           print("❗️Invalid input❗\nPlease enter an integer between 1 to 9")



              # ask if user wants to consider current temperature
              import requests

              city_name = "Sydney"
              state_code = "NSW"
              country_code = "AU"
              api_key = "241057b29d24cf0b09e308b88121a651"
              url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

              response = requests.get(
                  f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_key}')
              import json
              response_data = json.loads(response.text)
              # use this latitude and longitude information to find out the current temperature of Sydney

              lat = json.loads(response.text)[0]['lat']
              lon = json.loads(response.text)[0]['lon']

              response = requests.get(
                  f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
              response_data = json.loads(response.text)


              description = response_data["weather"][0]["description"]
              temp_k = response_data["main"]["temp"]
              feels_like_k = response_data["main"]["feels_like"]

              #convert kelvin to celsius
              feels_like_c = round(feels_like_k - 273.15, 1)
              temp_c = round(temp_k - 273.15, 1)

              # print out the temperature and shows it to user
              print("\n" + "-" * 110)
              print("🌡️TEMPERATURE OF THE DAY")
              print(f"\nToday's weather in {city_name}:{description}")
              print(f"Actual Temperature:{temp_c}degrees Celsius")
              print(f"Feels like:{feels_like_c}degrees Celsius")

              # give user a chance to choose if they want to consider current temperature
              while True:
                  print()
                  print(f"\nWould you like me to consider today's weather for your recommendation? \n (1.Yes/ 2.No)")
                  weather_choice = input(">>").strip()

                  if weather_choice in ["1","2"]:
                      break
                  else:
                      if weather_choice == "":
                          print("❗️Invalid input❗\nYou didn't enter anything! Please enter 1 or 2")
                      else:
                          print("❗️Invalid input❗\nPlease enter 1 or 2")


              weather_condition = None

              if weather_choice == "1":
                  while True:
                    print("\nWhich temperature would you like me to use?")
                    print("(1.Actual temperature/ 2.Feels like temperature)")
                    temp_choice = input(">>").strip()

                    if temp_choice in ["1","2"]:
                        break
                    else:
                        if temp_choice == "":
                            print("❗️Invalid input❗\nYou didn't enter anything! Please enter 1 or 2")
                        else:
                            print("❗️Invalid input❗\nPlease enter 1 or 2")

                  if temp_choice == "2":
                      temp_to_use = feels_like_c
                      print(f"Using feels like temperature:{temp_to_use}degrees Celsius")
                  else:
                      temp_to_use = temp_c
                      print(f"Using actual temperature:{temp_to_use}degrees Celsius")

                  # define weather condition in 3 types
                  if temp_to_use >18 and temp_to_use <= 26:
                      weather_condition ="neutral"
                      print("Great temperature for all kinds of food!")
                  elif temp_to_use >26:
                      weather_condition ="hot"
                      print("Omg! Today is so hotttt! \nDon't worry! I'll recommend some refreshing food for you:)")
                  else:
                      weather_condition ="cold"
                      print("\nFreezing cold, right? \nLet me recommend something to warm you up!")

              else:
                  print("Okay, I'll focus on your flavour and cuisine preferences!")


              #scoring system
              scores = {}
              for food in Food_list:
                  score =0

                  if weather_condition != None:
                      if weather_condition not in food["weather"]:
                          continue

                  #scores for flavour
                  if user_flavour in food["flavour"]:
                      score +=1

                  #scores for country
                  if food["country"]== user_country:
                      score +=1

                  #scores for temperature
                  if weather_condition != None:
                      score += 1

                  scores[food["name"]]=score

              best_choice = max(scores, key=scores.get)
              print("\n" + "-" * 110)
              print("✨RECOMMENDATION")
              print(f"\nBased on your preferences, we recommend:{best_choice}")
              print("🎉Hope you like our recommendation!")
              print("\n" + "-" * 110)

          else:
              #if user still wants random choice, give them the last suggestion and end the program
              print(f"Alright, then my final recommendation is: {suggestion}")
              print("Hope you enjoy your meal!")







