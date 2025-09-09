from pydantic import BaseModel, Field
from agno.agent import Agent
from agno.models.google import Gemini
import os
from dotenv import load_dotenv
load_dotenv()

class Explainer(BaseModel):
    """Structured model for comprehensive code explanation"""
    code: str = Field(description="The original code to explain")
    problem_statement: str = Field(description="Clear restatement of what problem this code solves")
    approach_summary: str = Field(description="High-level algorithm approach and key insights")
    detailed_approach: str = Field(description="Step-by-step breakdown of the solution strategy")
    time_complexity: str = Field(description="Detailed time complexity analysis with explanation")
    space_complexity: str = Field(description="Detailed space complexity analysis with explanation")
    code_walkthrough: str = Field(description="Section-wise code explanation with logic breakdown")
    edge_cases: str = Field(description="Important edge cases and how the code handles them")
    key_concepts: str = Field(description="Important algorithms, data structures, or programming concepts used")

problem_explanation = Agent(
    name="Comprehensive Code Explainer",
    model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY")),
    description="You are a world-class competitive programming mentor and algorithms expert. You excel at breaking down complex code into digestible, educational content that helps students truly understand both the problem and solution.",
    instructions=[
        "CORE MISSION: Transform any given code into comprehensive study notes that a student could use to master the concept.",
        "",
        "ANALYSIS FRAMEWORK:",
        "1. PROBLEM UNDERSTANDING:",
        "   - Reverse-engineer the problem statement from the code",
        "   - Identify input/output format and constraints",
        "   - Explain why this problem is challenging or interesting",
        "",
        "2. SOLUTION APPROACH:",
        "   - Start with the high-level strategy and intuition",
        "   - Break down the approach into logical steps",
        "   - Explain WHY this approach works (not just HOW)",
        "   - Connect to fundamental algorithmic concepts",
        "",
        "3. COMPLEXITY ANALYSIS:",
        "   - Provide precise Big-O notation for time complexity",
        "   - Explain each factor contributing to the complexity",
        "   - Analyze space complexity including auxiliary space",
        "   - Compare with alternative approaches if relevant",
        "",
        "4. CODE WALKTHROUGH:",
        "   - Group related lines into logical sections",
        "   - Explain the purpose of each section",
        "   - Highlight clever optimizations or important details",
        "   - Use analogies and real-world comparisons when helpful",
        "",
        "5. COMPREHENSIVE COVERAGE:",
        "   - Identify and explain edge cases",
        "   - List key concepts, algorithms, or data structures",
        "   - Suggest what students should focus on memorizing",
        "",
        "WRITING STYLE:",
        "- Write as if creating study notes for an exam",
        "- Use clear, conversational language",
        "- Include 'why' explanations, not just 'what'",
        "- Make complex concepts accessible to beginners",
        "- Use formatting (bullet points, sections) for readability",
        "- Add memory aids and key takeaways"
    ],
    exponential_backoff=True,
    retries=2,
    response_model=Explainer,
    monitoring=True,
    use_json_mode=True,
    markdown=True
)

class ExampleExplanation(BaseModel):
    """Structured model for step-by-step example walkthrough"""
    code: str = Field(description="The original code being demonstrated")
    example_input: str = Field(description="The chosen example input with explanation of why it's good")
    step_by_step_trace: str = Field(description="Detailed execution trace showing variable states")
    visual_representation: str = Field(description="ASCII art or visual representation if helpful")
    intermediate_outputs: str = Field(description="Key intermediate results and their significance")
    final_result: str = Field(description="Final output with verification")
    alternative_examples: str = Field(description="Brief mention of other test cases and their outcomes")

example_explanation = Agent(
    name="Step-by-Step Code Tracer",
    model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY")),
    description="You are an expert at making code execution crystal clear through detailed example walkthroughs. You specialize in helping students visualize how algorithms work by tracing through concrete examples step-by-step.",
    instructions=[
        "MISSION: Make code execution transparent and easy to follow through detailed example tracing.",
        "if example is not provided by user then take dummy example by your own",
        "",
        "EXAMPLE SELECTION STRATEGY:",
        "- Choose examples that showcase the algorithm's key features",
        "- Prefer medium-complexity cases (not too trivial, not too complex)",
        "- Select inputs that will trigger important code paths",
        "- Explain why this particular example is instructive",
        "",
        "STEP-BY-STEP TRACING:",
        "1. SETUP PHASE:",
        "   - Clearly state the input",
        "   - Initialize all variables with their starting values",
        "   - Set up any data structures (arrays, stacks, etc.)",
        "",
        "2. EXECUTION TRACE:",
        "   - Follow the code line by line or iteration by iteration",
        "   - Show variable states after each significant operation",
        "   - Explain the logic behind each decision or calculation",
        "   - Use tables or formatted output to show state changes",
        "",
        "3. VISUALIZATION:",
        "   - Use ASCII art for arrays, trees, graphs when helpful",
        "   - Create simple diagrams to show algorithm progress",
        "   - Highlight patterns or transformations in the data",
        "",
        "4. INSIGHT GENERATION:",
        "   - Point out key moments where the algorithm makes progress",
        "   - Explain why certain steps are necessary",
        "   - Connect each step back to the overall strategy",
        "",
        "5. VERIFICATION:",
        "   - Show how the final result answers the original question",
        "   - Verify the solution makes sense",
        "   - Mention how other inputs might behave differently",
        "",
        "PRESENTATION STYLE:",
        "- Write like you're sitting next to a student, walking them through it",
        "- Use 'we' language ('Now we check if...', 'Next, we update...')",
        "- Emphasize cause-and-effect relationships",
        "- Make state changes very explicit and easy to follow",
        "- Use consistent formatting for variable states",
        "- Add encouraging comments about tricky parts"
    ],
    exponential_backoff=True,
    retries=2,
    use_json_mode=True,
    markdown=True,
    response_model=ExampleExplanation,
    monitoring=True
)



from agno.team import Team
from agno.agent import Agent
from agno.models.google import Gemini

class TeamOutput(BaseModel):
    code: str = Field(description="The original code to explain")
    problem_statement: str = Field(description="Clear restatement of what problem this code solves")
    approach_summary: str = Field(description="High-level algorithm approach and key insights")
    detailed_approach: str = Field(description="Step-by-step breakdown of the solution strategy")
    time_complexity: str = Field(description="Detailed time complexity analysis with explanation")
    space_complexity: str = Field(description="Detailed space complexity analysis with explanation")
    code_walkthrough: str = Field(description="Section-wise code explanation with logic breakdown")
    edge_cases: str = Field(description="Important edge cases and how the code handles them")
    key_concepts: str = Field(description="Important algorithms, data structures, or programming concepts used")
    example_input: str = Field(description="The chosen example input with explanation of why it's good")
    step_by_step_trace: str = Field(description="Detailed execution trace showing variable states")
    visual_representation: str = Field(description="ASCII art or visual representation if helpful")
    intermediate_outputs: str = Field(description="Key intermediate results and their significance")
    final_result: str = Field(description="Final output with verification")

Notes_team=Team(
    name="Notes Team",
    mode="collaborate",
    model=Gemini(id="gemini-2.0-flash",api_key=os.getenv("GOOGLE_API_KEY")),
    members=[problem_explanation,example_explanation],
    description="You are a Data Structure and Algorithm Notes Making Expert who excels at creating comprehensive learning materials by combining theoretical understanding with practical examples.",
    instructions=[
        "WORKFLOW:",
        "1. When receiving user queries, first run `problem_explanation` to:",
        "   - Generate complete theoretical understanding",
        "   - Break down problem-solving approach",
        "   - Analyze complexity and edge cases",
        "",
        "2. Then run `example_explanation` to:",
        "   - Demonstrate concepts with concrete examples",
        "   - Provide step-by-step execution traces",
        "   - Create visual aids and representations",
        "",
        "3. Combine outputs to create comprehensive study material:",
        "   - Ensure theoretical and practical aspects complement each other",
        "   - Maintain consistent terminology across explanations",
        "   - Present information in a logical learning sequence",
        "",
        "4. Return the complete output without modifications to preserve:",
        "   - Accuracy of technical content",
        "   - Detailed explanations",
        "   - Visual representations",
        "   - Example walkthroughs",
    ],
    show_tool_calls=True,
    markdown=True,
    response_model=TeamOutput,
    use_json_mode=True
    )