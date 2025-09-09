from pydantic import BaseModel
from agno.agent import Agent
from agno.models.google import Gemini
import os
from dotenv import load_dotenv
load_dotenv()

class QuestionFinderInput(BaseModel):
    user_input:str
    problem_statement:str
    difficulty:str
    examples:list[str]
    explanations:list[str]
    constraints:list[str]


# Agent without tools for structured output
question_finder=Agent(
    name='Question Finder',
    model=Gemini(id='gemini-2.0-flash',api_key=os.getenv("GOOGLE_API_KEY")),
    description = "Formats given content into structured format",
    instructions = [
        "Format the given content into the required structure with problem statement, difficulty, examples,constraints, and explanations."
        ],
    response_model=QuestionFinderInput
)