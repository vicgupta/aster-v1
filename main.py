from aster.models import OllamaChat
from aster.agents import Agent

llm = OllamaChat(model="llama3")
pirate_agent = Agent(llm, custom_system_prompt="You are a pirate!")
print(pirate_agent.ask(prompt="Who are you?"))
