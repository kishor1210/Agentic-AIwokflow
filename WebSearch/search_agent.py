from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq

import groq
import os
from dotenv import load_dotenv
load_dotenv()

groq.api = os.getenv("GROQ_API_KEY")


web_agent = Agent(
    name="Web Agent",
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("Tell me about Indian state?", stream=True)
