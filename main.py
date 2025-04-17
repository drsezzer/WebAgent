from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import os
os.environ["ANONYMIZED_TELEMETRY"] = "false"

import asyncio
llm = ChatOpenAI(model='gpt-4o')

STARTING_TASK = """Research the life details (from a family history point of view) of 
the first duke of marlborough, and write a short biography of him.  
Ask questions if you need to know more about him."""

async def main():
    agent = Agent(
        task = STARTING_TASK,
        llm = llm,
    )
    result = await agent.run()
    print(result)
    result.save_to_file("output.json")

asyncio.run(main())
