from google.adk.agents import LlmAgent
from google.adk.tools import google_search


MODEL = "gemini-2.0-flash-001"

idea_agent = LlmAgent(
    model = MODEL,
    name = "idea_agent",
    description="Brainstorm creative and exciting project and business ideas on user's request",
    instruction="You are a creative and innovative agent. Use the tool to Brainstorm and respond to the user with 3 exciting project ideas based on the user's request",
    tools=[google_search],
    disallow_transfer_to_peers=True,
)

refiner_agent = LlmAgent(
    model = MODEL,
    name = "refiner_agent",
    description="Reviews provided project ideas and selects only those that are being implemented by less people",
    instruction="Use your tools to review the provided project ideas, respond only with the ideas that are REALLY good",
    tools=[google_search],
    disallow_transfer_to_peers=True
)

root_agent = LlmAgent(
    model=MODEL,
    name = "root_agent",
    instruction= f""" You are a project planner, coordinating specialist agents.
    Your goal is to provide a really good project idea to the user, follow the below instructions:
    1. First, use {idea_agent} to brainstorm ideas based on user's request.
    2. Then, use {refiner_agent} to take those ideas to filter them for the provided requirements.
    3. Present the final, refined list to the user along with the requirements and pre-requisites for the project.
    """,
    sub_agents=[idea_agent,refiner_agent],
    
)