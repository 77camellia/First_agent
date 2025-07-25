#my_agent/agent.py
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


model = LiteLlm(model="deepseek/deepseek-chat")

root_agent = Agent(
    name="simple_assistant",
    model=model,
    instruction="A helpful assistan.",
)