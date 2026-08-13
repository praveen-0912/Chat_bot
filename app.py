# import os
# import requests as req
# import streamlit as st

# from dotenv import load_dotenv

# from langchain.tools import tool
# from langchain_google_genai import ChatGoogleGenerativeAI

# from langchain.agents import create_agent
# from langchain_core.messages import HumanMessage, SystemMessage

# load_dotenv()

# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# WEATHER_API = os.getenv("WEATHER_API_KEY")


# # Gemini Model
# client = ChatGoogleGenerativeAI(
#     model="gemini-3.5-flash",
#     google_api_key=GOOGLE_API_KEY
# )


# @tool
# def get_weather(city: str) -> str:
#     """
#     Fetches the current weather for a given city.
#     """

#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API}&units=metric"

#     response = req.get(url)

#     if response.status_code == 200:
#         data = response.json()

#         description = data["weather"][0]["description"]
#         temp = data["main"]["temp"]
#         humidity = data["main"]["humidity"]

#         return f"""
# City: {city}

# Temperature: {temp}°C

# Humidity: {humidity}%

# Weather: {description}
# """

#     return "Could not fetch weather."


# weather_agent = create_agent(
#     model=client,
#     tools=[get_weather],
#     system_prompt=SystemMessage(
#         content="""
# You are a helpful weather assistant.

# If the user asks about weather,
# use the weather tool.

# Otherwise answer normally.
# """
#     )
# )


# st.title("🌤 Chatbot Agent")

# question = st.text_input("Ask anything...")

# if st.button("Submit"):

#     if question:

#         result = weather_agent.invoke(
#             {
#                 "messages": [
#                     HumanMessage(content=question)
#                 ]
#             }
#         )

#         st.write(result["messages"][-1].content)







import os
import requests as req
import streamlit as st

from dotenv import load_dotenv
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

load_dotenv()

GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
WEATHER_API_KEY = st.secrets["WEATHER_API_KEY"]

# --------------------------------------------------
# Check API keys
# --------------------------------------------------

if not GOOGLE_API_KEY:
    st.error("❌ GOOGLE_API_KEY is missing in Streamlit Secrets.")
    st.stop()

if not WEATHER_API_KEY:
    st.error("❌ WEATHER_API_KEY is missing in Streamlit Secrets.")
    st.stop()

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI chatbot Agent",
    page_icon="🌤️",
    layout="centered"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main {
        padding-top: 2rem;
    }

    .title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }

    .subtitle {
        text-align: center;
        color: #777;
        margin-bottom: 2rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="title">🌤️  AI  Chatbot Agent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask me about weather anywhere in the world</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# Gemini Model
# --------------------------------------------------

client = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0
)

# --------------------------------------------------
# Weather Tool
# --------------------------------------------------

@tool
def get_weather(city: str) -> str:
    """
    Get the current weather information for a city.
    """

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={WEATHER_API_KEY}"
        "&units=metric"
    )

    try:

        response = req.get(url, timeout=10)

        if response.status_code == 200:

            data = response.json()

            city_name = data["name"]
            country = data["sys"]["country"]

            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]

            description = data["weather"][0]["description"]

            return (
                f"City: {city_name}, {country}\n"
                f"Temperature: {temperature}°C\n"
                f"Feels Like: {feels_like}°C\n"
                f"Humidity: {humidity}%\n"
                f"Weather: {description}"
            )

        elif response.status_code == 404:

            return f"Sorry, I couldn't find a city named '{city}'."

        elif response.status_code == 401:

            return "Weather API key is invalid."

        else:

            return (
                f"Weather service returned an error "
                f"(status code: {response.status_code})."
            )

    except req.exceptions.Timeout:

        return "The weather service took too long to respond."

    except req.exceptions.RequestException as e:

        return f"Unable to connect to the weather service: {e}"

    except Exception as e:

        return f"Unexpected weather error: {e}"


# --------------------------------------------------
# Create Agent
# --------------------------------------------------

weather_agent = create_agent(
    model=client,
    tools=[get_weather],
    system_prompt="""
You are a helpful AI weather assistant.

Rules:

1. If the user asks about current weather, temperature,
   humidity, climate conditions, or weather of a city,
   use the get_weather tool.

2. Do not guess weather information.

3. If the user asks a normal general question,
   answer normally without using the weather tool.

4. Give answers in a clear and friendly way.

5. If weather information is returned by the tool,
   explain it naturally to the user.

6. Keep answers concise unless the user asks for details.
"""
)

# --------------------------------------------------
# Chat history
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# Display previous messages
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# --------------------------------------------------
# Clear Chat Button
# --------------------------------------------------

if st.session_state.messages:

    if st.sidebar.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()


# --------------------------------------------------
# User Input
# --------------------------------------------------

question = st.chat_input(
    "Ask me about the Anything..."
)

# --------------------------------------------------
# Process User Question
# --------------------------------------------------

if question:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display user message
    with st.chat_message("user"):

        st.markdown(question)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                result = weather_agent.invoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": question
                            }
                        ]
                    }
                )

                answer = result["messages"][-1].content

                # Handle possible list response
                if isinstance(answer, list):

                    answer = " ".join(
                        item.get("text", "")
                        for item in answer
                        if isinstance(item, dict)
                    )

                st.markdown(answer)

                # Save assistant message
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as e:

                error_message = (
                    "Sorry, something went wrong.\n\n"
                    f"Error: `{str(e)}`"
                )

                st.error(error_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message
                    }
                )
