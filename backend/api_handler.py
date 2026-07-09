import requests
import webbrowser
from config import NASA_API_KEY


#NASA APOD

def get_nasa_apod():

    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            webbrowser.open(data["url"])

            return (
                f"\n NASA Picture of the Day \n"
                f"Title: {data['title']}\n"
                f"Date: {data['date']}\n"
                f"\nOpening image in your browser..."
            )

        return f"NASA API returned status code {response.status_code}"

    except Exception as e:
        return f"NASA API Error: {e}"


#ISS LOCATION

def get_iss_location():

    url = "http://api.open-notify.org/iss-now.json"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            latitude = data["iss_position"]["latitude"]
            longitude = data["iss_position"]["longitude"]

            return (
                f"\n Current ISS Location\n"
                f"Latitude: {latitude}\n"
                f"Longitude: {longitude}"
            )

        return f"ISS API returned status code {response.status_code}"

    except Exception as e:
        return (
            "ISS API is currently unavailable.\n"
            f"Technical details: {e}"
        )


#CURRENT PEOPLE IN SPACE

def get_people_in_space():

    url = "http://api.open-notify.org/astros.json"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            number = data["number"]
            people = data["people"]

            astronaut_names = " "

            for person in people:
                astronaut_names += (
                    f" {person['name']} "
                    f"({person['craft']})\n"
                )

            return (
                f"\n There are currently "
                f"{number} astronauts in space.\n\n"
                f"{astronaut_names}"
            )

        return f"Astronaut API returned status code {response.status_code}"

    except Exception as e:
        return (
            "Astronaut API is currently unavailable.\n"
            f"Technical details: {e}"
        )


# SPACEX LATEST LAUNCH

def get_latest_spacex_launch():

    url = "https://api.spacexdata.com/v5/launches/latest"

    try:
        response = requests.get(url, timeout=10)

        print("SpaceX Status Code:", response.status_code)

        if response.status_code == 200:

            data = response.json()

            mission_name = data.get("name", "Unknown Mission")
            launch_date = data.get("date_utc", "Unknown Date")

            success_value = data.get("success")

            if success_value is True:
                success = "Yes"
            elif success_value is False:
                success = "No"
            else:
                success = "Unknown"

            details = data.get(
                "details",
                "No additional details available."
            )

            return (
                f"\n Latest SpaceX Launch \n\n"
                f"Mission: {mission_name}\n"
                f"Launch Date: {launch_date}\n"
                f"Mission Successful: {success}\n\n"
                f"Details:\n{details}"
            )

        return (
            f"SpaceX API returned status code "
            f"{response.status_code}"
        )

    except Exception as e:
        return f"SpaceX API Error: {e}"