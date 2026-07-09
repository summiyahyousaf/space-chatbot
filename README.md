# Space AI Chatbot

An interactive AI-powered chatbot built using Python, Flask, HTML, CSS, and JavaScript that helps users explore space-related topics including planets, astronauts, NASA missions, ISS tracking, and SpaceX launches.

This project was developed as a learning project to explore APIs, web development, backend programming, and AI chatbot development.


## Features

### Planet Information
- Planet facts
- Planet nicknames
- Number of moons
- Distance from the Sun

### Astronaut Information
- Information about famous astronauts
- Historical space achievements
- Current astronauts in space

### Space Missions
- Mission details and descriptions
- Historical missions
- SpaceX latest launch information

### Live Space Data
- Current International Space Station (ISS) location
- Number of people currently in space
- NASA Astronomy Picture of the Day (APOD)

### Interactive Features
- Voice input using browser speech recognition
- Voice output using speech synthesis
- Typing animation
- Sidebar navigation menu
- New chat functionality

---

##  Technologies Used

### Backend
- Python
- Flask

### Frontend
- HTML
- CSS
- JavaScript

### Data Storage
- JSON files

### APIs
- NASA APOD API
- Open Notify API
- SpaceX API

### Browser Features
- Web Speech API
- Fetch API

---

##  Project Structure

```text
SpaceAI/
│
├── app.py
├── chatbot.py
├── api_handler.py
├── config.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── planets.json
│   ├── astronauts.json
│   ├── missions.json
│   └── facts.json
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── screenshots/
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/summiyahyousaf/space-chatbot.git
```

### Navigate to the project directory

```bash
cd space-chatbot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 📷 Screenshots


- Main chatbot interface
  ![image alt](https://github.com/summiyahyousaf/space-chatbot/blob/main/interface.png?raw=true)
- NASA APOD response
  ![image alt]( https://github.com/summiyahyousaf/space-chatbot/blob/main/NASA_pictureoftheday.png?raw=true)
- ISS location feature
  ![image alt](https://github.com/summiyahyousaf/space-chatbot/blob/main/current_ISS.png?raw=true)
- Sidebar menu
 ![image alt](https://github.com/summiyahyousaf/space-chatbot/blob/main/menu.png?raw=true)
- space_missions
![image alt]( https://github.com/summiyahyousaf/space-chatbot/blob/main/space_missions.png?raw=true)
---

## Learning Objectives

This project was created to learn and practice:

- Python programming
- Flask web framework
- REST APIs
- JSON data handling
- Frontend and backend integration
- Asynchronous JavaScript
- Speech recognition
- Speech synthesis
- AI chatbot development principles

---

##  Future Improvements

Planned features for future versions:

- Natural Language Processing (NLP)
- Intent recognition
- Fuzzy matching for user queries
- Chat history persistence
- User authentication and accounts
- Image upload support
- Space news integration
- Additional NASA APIs
- Mars Rover image support
- Rocket launch schedules
- AI-powered question understanding
- Database integration
- Machine Learning based response generation

---

##  APIs Used

### NASA Astronomy Picture of the Day API
Provides NASA's daily astronomy image.

### Open Notify API
Provides:
- ISS location
- Current astronauts in space

### SpaceX API
Provides:
- Latest launch information
- Mission details

---

##  Author

**Summiya Yousaf**

  BSAI student passionate about:
- Artificial Intelligence
- Machine Learning
- Space Technology

---

##  Project Status

Current Version: **v1.0**

This project is continuously evolving, with ongoing enhancements in AI, NLP, and chatbot functionality to improve performance and user experience.

---

##  License

This project is intended for educational and learning purposes.
