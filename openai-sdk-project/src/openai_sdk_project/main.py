import os
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel
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
async def test_installation():
    agent=Agent(
        name="Test Agent",
        instructions="You are a helpful assistant that provides concise reponses",
        model=model

        )

    result = await  Runner.run(agent,"Hello Are you working correctly ?")
    print(result.final_output)



def async_test_installation():
    return asyncio.run(test_installation())



    