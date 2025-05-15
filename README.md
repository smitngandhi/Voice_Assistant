# Luna - AI Voice Assistant

Luna is your AI-based voice assistant built in Python. It can assist with tasks like opening applications, providing weather updates, reading the latest news, retrieving facts, and performing web-based searches using Google, YouTube, and Wikipedia.

## Features

- Voice-based command recognition
- Application launcher and closer (e.g., Chrome, CMD, VSCode, etc.)
- Get latest news headlines and descriptions using NewsAPI
- Retrieve interesting random facts
- Weather/temperature info by city
- Web search via Google, YouTube, Wikipedia
- ChatGPT and Selenium integration for enriched responses

## Tech Stack

- Python 3.8+
- `speech_recognition`
- `pyttsx3`
- `pyautogui`
- `webbrowser`
- `requests`
- `selenium`
- `randfacts`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/luna-assistant.git
   cd luna-assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file to store your NewsAPI key:
   ```env
   NEWS_API_KEY=your_newsapi_key_here
   ```

4. Replace the API key in `news.py` and `selenium_web.py` if not using `.env`

## Usage

Run the assistant:
```bash
python main.py
```

Start with the magical phrase:
```
Hey Luna
```

Then ask her to:
- Open apps like "open chrome"
- Ask for temperature in a city
- Play a video on YouTube
- Search Wikipedia or Google
- Read the news
- Share a fun fact

## File Structure

```
.
├── driver/
│   ├── apps.py
│   ├── news.py
│   └── selenium_web.py
├── main.py
├── README.md
└── requirements.txt
```