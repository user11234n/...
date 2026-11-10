import requests
url = "https://eonet.gsfc.nasa.gov/api/v2.1/events"
response = requests.get(url)
data = response.json()

# print(data)


print("This is an everchanging database of events across the world, collected and explained by NASA.")

def check_events():
    user_input = input("Would you like to check somewhere (Yes or no)? ").strip().lower()
    if user_input == "yes":
        while True:
            where_to_look = input("What state or country would you like to check? ").strip()
            what_city = input(f"Which city in {where_to_look} would you like to check? ").strip()
            counter = 1

            for event in data["events"]:
                title = event["title"]
                if where_to_look.lower() in title.lower() and what_city.lower() in title.lower():
                    print(f"{counter}-{event['title']}")
                    counter += 1
                    information_events(event)

            if counter == 1:
                print("It doesn't look like there are any notable natural events here right now, would you like to retype your entry? ")
                retype_entry = input("").strip().lower()

                if retype_entry == "yes":
                    print("Okay, one moment.")

                if retype_entry == "no":
                    return
                continue

            again = input("Would you like to check another place? ").strip().lower()
            if again == "yes":
                print("Okay, one moment...")
            if again == "no":
                print("Okay. ")
                print("Exiting...")
                return
    elif user_input == "no":
        print("Alright")
        print("Exiting...")
        return

    else:
        print("Please use valid input")

def information_events(event):
    more_info = input(f"Would you like more information about {event['title']}? ").strip().lower()
    if more_info == "yes":
        description = event.get("description")
        if description:
            print(f"Description: {description}")
        else:
            print("No description is available.")

        link = event.get("link")
        if link:
            print(f"More information: {link}")

        for source in event.get("sources", []):
            source_url = source.get("url")
            if source_url:
                print(f"Source ({source.get('id', 'unknown')}): {source_url}")
    elif more_info == "no":
        print("Okay")
        return None
    else:
        print("Please try to use a valid answer")


            
check_events()


            
                   


