import time
from .qution_finder import question_finder
from .brute_force import basic_approach_team
from agno.team import Team
from pydantic import BaseModel,Field
from agno.models.google import Gemini
import os
from dotenv import load_dotenv
load_dotenv()
class LeetCode(BaseModel):
    user_input:str
    constraints:str
    examples:list[str]
    problem_statement: str =Field(description="the problem statement")
    basic_approach: str =Field(description="the approach to solve the problem")
    basic_algorithm: str =Field(description="the algorithm to solve the problem")
    basic_time_complexity: str = Field(description="the time complexity of the algorithm or code")
    basic_space_complexity: str = Field(description="the space complexity of the algorithm or code")
    basic_code: str = Field(description="the code to solve the problem")
    


leetcode_team=Team(
    name="Leetcode Team",
    mode='collaborate',
    members=[question_finder,basic_approach_team],
    model=Gemini(id='gemini-2.0-flash',api_key=os.getenv('GOOGLE_API_KEY')),
    description="You are an expert DSA problem analysis team that transforms raw problem statements into structured, comprehensive problem breakdowns with brute-force solutions.",
    instructions=[
        "PROBLEM ANALYSIS WORKFLOW:",
        "1. EXTRACTION PHASE:",
        "   - Run the `question_finder` agent to parse and extract key problem components",
        "   - Identify problem statement, constraints, examples, and edge cases",
        "   - Standardize the problem format for consistent processing",
        
        "2. SOLUTION GENERATION PHASE:",
        "   - Run the `basic_approach_team` to develop the fundamental brute-force solution",
        "   - Focus on correctness over efficiency for the initial approach",
        "   - Ensure the solution handles all given constraints and examples",
        
        "3. QUALITY ASSURANCE:",
        "   - Verify that all required fields are populated with meaningful content",
        "   - Ensure the basic algorithm is step-by-step and implementable",
        "   - Validate that time/space complexity analysis is accurate",
        "   - Confirm the code solution is syntactically correct and runnable",
        
        "OUTPUT REQUIREMENTS:",
        "- Provide a complete, structured problem analysis",
        "- Include working brute-force code that solves all test cases",
        "- Deliver clear algorithmic steps that can be easily understood",
        "- Ensure complexity analysis is precise and well-justified"
    ],
    response_model=LeetCode,
    use_json_mode=True,

)