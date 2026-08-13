# Chat_bot

# 🌤️ AI Weather Chatbot Agent

An AI-powered weather chatbot built with **Python,Streamlit,LangChain,Google Gemini an dOpenWeatherMap API**.

The application allows users to ask questions about weather conditions in cities around the world. When a user asks about current weather, the LangChain agent uses a weather tool to retrieve real-time weather information from the OpenWeatherMap API.

## 🚀 Features

* 🤖 AI-powered chatbot using Google Gemini
* 🌤️ Real-time weather information
* 🌡️ Temperature information
* 💧 Humidity information
* 🌡️ Feels-like temperature
* 🌍 Weather information for different cities
* 🧠 LangChain agent with a custom weather tool
* 💬 Chat history using Streamlit session state
* 🗑️ Clear chat functionality
* ⚠️ Error handling for invalid cities and API problems
* 🔐 API keys stored using environment variables

## 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* LangGraph
* Google Gemini
* OpenWeatherMap API
* Python-dotenv
* Requests

## 📁 Project Structure

```text
Chat_bot/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env                 # Local only - do not upload
```

## ⚙️ How It Works

The application follows this basic workflow:

```text
User
  ↓
Streamlit Chat Interface
  ↓
Google Gemini
  ↓
LangChain AI Agent
  ↓
Weather Question?
  ↓
get_weather() Tool
  ↓
OpenWeatherMap API
  ↓
Weather Result
  ↓
AI Response
```

If the user asks a weather-related question, the AI agent uses the `get_weather` tool.

For example:

```text
User: What is the temperature in Nellore?

AI Agent
    ↓
get_weather("Nellore")
    ↓
OpenWeatherMap API
    ↓
Temperature + Humidity + Weather
    ↓
Chatbot Response
```

For general questions, the agent can answer normally without calling the weather tool.

## 🔑 Environment Variables

Create a `.env` file in the project directory:

```text
GOOGLE_API_KEY=your_google_api_key
WEATHER_API_KEY=your_openweathermap_api_key
```

**Never upload `.env` to GitHub.**

The `.gitignore` file should contain:

```text
.env
venv/
.venv/
__pycache__/
*.pyc
.streamlit/secrets.toml
```

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/praveen-0912/Chat_bot.git
```

Go into the project directory:

```bash
cd Chat_bot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💬 Example Questions

You can ask:

```text
What is the weather in Nellore?

What is the temperature in Hyderabad?

How humid is the weather in Chennai?

What is the weather like in Bangalore?

What is the temperature in London?
```

## 🧠 AI Agent

The application uses a LangChain agent with a custom `get_weather` tool.

The agent is instructed to:

1. Use the weather tool for weather-related questions.
2. Avoid guessing weather information.
3. Answer general questions normally.
4. Explain weather results naturally.
5. Keep responses concise.

## 🔐 Security

API keys should never be committed to GitHub.

The `.env` file is excluded using `.gitignore`.

If an API key is accidentally uploaded to GitHub, revoke or rotate the key immediately and create a new one.

## 📌 Future Improvements

* Add weather forecasts
* Add weather icons
* Add temperature charts
* Add location-based weather
* Add voice interaction
* Add multiple weather APIs
* Deploy the application online
* Add more AI tools

## 👨‍💻 Author

**Praveen**

GitHub: https://github.com/praveen-0912

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

