import os
from dotenv import load_dotenv
from agents import Agent, ModelSettings,Runner,AsyncOpenAI,OpenAIChatCompletionsModel
import asyncio
from agents.run import RunConfig



load_dotenv()


api_key=os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI API KEY NOT FOUND")


external_client=AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    
)

model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


# Define detailed instructions for our weather assistant
weather_instructions = """
You are a weather information assistant who helps users understand weather patterns and phenomena.

YOUR EXPERTISE:
- Explaining weather concepts and terminology
- Describing how different weather systems work
- Answering questions about climate and seasonal patterns
- Explaining the science behind weather events

LIMITATIONS:
- You cannot provide real-time weather forecasts for specific locations
- You don't have access to current weather data
- You should not make predictions about future weather events

STYLE:
- Use clear, accessible language that non-meteorologists can understand
- Include interesting weather facts when relevant
- Be enthusiastic about meteorology and climate science
"""





async def check_weather():
    agent=Agent(
        name="Weather Agent",
        instructions=weather_instructions,
        model=model,
    model_settings=ModelSettings(
        temperature=0.7,
        max_tokens=256
    )

        )

    result = await  Runner.run(agent,"Can you tell me about the relationship between climate change and extreme weather events?")
    print(result.final_output)



def async_check_weather():
    return asyncio.run(check_weather())



    