from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(tools=[DuckDuckGoTools()], show_tool_calls=True)
agent.print_response("Quante cliniche dentali ha il network di Caredent Primo Group in Italia?", markdown=True)