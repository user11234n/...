import requests
url = "https://eonet.gsfc.nasa.gov/api/v2.1/events"
response = requests.get(url)
data = response.json()

# print(data)


# print("This is an everchanging database of events across the world, collected and explained by NASA.")

def check_events():
    user_input = input("Would you like to check somewhere (Yes or no)?")
    counter = 1
    if user_input == "Yes" or user_input == "yes":
        where_to_look = input("What state or country would you like to check?")
        what_city = input(f"Which city in {where_to_look} would you like to check?")
        for event in data["events"]:
            if where_to_look in event["title"] and what_city in event["title"]:
                print(f"{counter}-{event["title"]}")
                counter+=1

        if what_city not in event["title"]:
            print("It doesn't look like there are any notable natural events here right now, would you like to retype your entry?")
            # retype_entry = input("")
