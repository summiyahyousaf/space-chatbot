import json
import random
from datetime import datetime


from api_handler import (
    get_nasa_apod,
    get_iss_location,
    get_people_in_space,
    get_latest_spacex_launch
)

# LOAD JSON FILES
with open("../data/history.json","r")as file:
    history=json.load(file)

with open("../data/planets.json", "r") as file:
    planets = json.load(file)

with open("../data/astronauts.json", "r") as file:
    astronauts = json.load(file)

with open("../data/missions.json", "r") as file:
    missions = json.load(file)

with open("../data/facts.json", "r") as file:
    facts = json.load(file)


PLANET_ALIASES = {
    "mercury": ["mercury"],

    "venus": [
        "venus",
        "morning star",
        "evening star"
    ],

    "earth": [
        "earth",
        "blue planet",
        "our planet",
        "home planet"
    ],

    "mars": [
        "mars",
        "red planet"
    ],

    "jupiter": [
        "jupiter",
        "largest planet",
        "biggest planet",
        "gas giant"
    ],

    "saturn": [
        "saturn",
        "planet with rings",
        "ringed planet"
    ],

    "uranus": [
        "uranus",
        "ice giant"
    ],

    "neptune": [
        "neptune",
        "farthest planet",
        "windy planet"
    ]
}


# MAIN CHATBOT FUNCTION


def save_history(query):

    with open("../data/history.json", "r") as file:
        history = json.load(file)

    history.append({
        "query": query,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    with open("../data/history.json", "w") as file:
        json.dump(history, file, indent=4)


def get_response(user_input):

    user_input = user_input.lower().strip()
    save_history(user_input)
    user_words = user_input.split()

    # GREETING

    if (
        "hi" in user_words
        or "hello" in user_words
        or "hey" in user_words
        or "salam" in user_words
    ):
        return "Hello! Let's explore space together."

    # SPACEX

    elif (
        "spacex" in user_input
        or ("launch" in user_input and "latest" in user_input)
    ):
        return get_latest_spacex_launch()

    # ISS

    elif (
        "iss" in user_words
        or "space station" in user_input
        or "international space station" in user_input
    ):
        return get_iss_location()

    # PEOPLE IN SPACE

    elif (
        "astronauts in space" in user_input
        or "people in space" in user_input
        or "currently in space" in user_input
        or "who is in space" in user_input
    ):
        return get_people_in_space()

    # NASA APOD

    elif (
        "nasa image" in user_input
        or "picture of the day" in user_input
        or "apod" in user_input
    ):
        return get_nasa_apod()

    # GENERAL MISSIONS

    elif (
        "mission" in user_input
        or "missions" in user_input
    ):

        mission_names = "\n".join(
            [f"• {mission.title()}" for mission in missions.keys()]
        )

        return (
            "Space Missions:\n\n"
            f"{mission_names}\n\n"
            "Ask me about any one of them for details."
        )

    # SPECIAL QUESTIONS

    elif (
        ("first astronaut" in user_input or "first person" in user_input)
        and "moon" in user_input
    ):
        return (
            "Neil Armstrong was the first human "
            "to walk on the Moon during Apollo 11 in 1969."
        )

    elif "first human in space" in user_input:
        return "Yuri Gagarin was the first human in space in 1961."

    elif (
        "first woman in space" in user_input
        or "first female astronaut" in user_input
    ):
        return (
            "Valentina Tereshkova was the first woman "
            "in space in 1963."
        )

    elif (
        "first woman" in user_input
        and "moon" in user_input
    ):
        return (
            "No woman has walked on the Moon yet. "
            "NASA's Artemis program aims to land "
            "the first woman on the Moon."
        )

    # PLANETS

    detected_planet = None

    for planet, aliases in PLANET_ALIASES.items():
        for alias in aliases:
            if alias in user_input:
                detected_planet = planet
                break

        if detected_planet:
            break

    if detected_planet:

        data = planets[detected_planet]

        if "moon" in user_input:
            return (
                f"{detected_planet.capitalize()} has "
                f"{data['moons']} moon(s)."
            )

        elif "distance" in user_input:
            return (
                f"{detected_planet.capitalize()} is "
                f"{data['distance_from_sun']} "
                f"away from the Sun."
            )

        elif "nickname" in user_input or "called" in user_input:
            return (
                f"{detected_planet.capitalize()} is known as "
                f"{data['nickname']}."
            )

        elif "fact" in user_input:
            return data["fact"]

        else:
            return (
                f"\nPlanet: {detected_planet.capitalize()}\n"
                f"\nNickname: {data['nickname']}\n"
                f"\nMoons: {data['moons']}\n"
                f"\nDistance from Sun: {data['distance_from_sun']}\n"
                f"\nFact: {data['fact']}"
            )

    # SPECIFIC ASTRONAUTS

    for astronaut in astronauts:

        if astronaut in user_input:

            data = astronauts[astronaut]

            return (
                f"\nAstronaut: {astronaut.title()}\n"
                f"Country: {data['country']}\n"
                f"Achievement: {data['achievement']}\n"
                f"Mission: {data['mission']}"
            )

    # GENERAL ASTRONAUT QUESTIONS

    if (
        "astronaut" in user_input
        or "astronauts" in user_input
    ):
        return (
            "Here are several famous astronauts:\n\n"
            "• Neil Armstrong\n"
            "• Buzz Aldrin\n"
            "• Yuri Gagarin\n"
            "• Valentina Tereshkova\n"
            "• Chris Hadfield\n"
            "• Sunita Williams\n\n"
            "Ask me about any astronaut by name!"
        )

    # SPECIFIC MISSIONS

    for mission in missions:

        if mission.lower() in user_input:

            data = missions[mission]

            return (
                f"\nMission: {mission.title()}\n"
                f"Year: {data['year']}\n"
                f"Description: {data['description']}"
            )

  

    # RANDOM FACT

    if "fact" in user_input:
        return random.choice(list(facts.values()))

    # SEARCH HISTORY

    if (
        user_input == "history"
        or "search history" in user_input
        or "recent searches" in user_input
    ):

        with open("../data/history.json", "r") as file:
            history = json.load(file)

        if not history:
            return "No search history found."

        recent = history[-10:]

        response = "📜 Your Recent Searches:\n\n"

        for item in reversed(recent):
            response += (
                f"• {item['query']} "
                f"({item['time']})\n"
            )

        return response

    # DEFAULT

    return "Sorry, I don't know about that yet."