from code_evaluator_BForce import code_evaluator
from agno.agent import Agent
from pydantic import BaseModel, Field
from agno.models.groq import Groq
from agno.tools.python import PythonTools
from agno.models.google import Gemini
import os
from dotenv import load_dotenv
load_dotenv()


class SubOptimalApproach(BaseModel):
    problem_statement: str =Field(description="the problem statement")
    basic_approach: str =Field(description="the approach to solve the problem")
    basic_algorithm: str =Field(description="the algorithm to solve the problem")
    basic_time_complexity: str = Field(description="the time complexity of the algorithm or code")
    basic_space_complexity: str = Field(description="the space complexity of the algorithm or code")
    basic_code: str = Field(description="the code to solve the problem")
    suboptimal_approach: str =Field(description="the approach to solve the problem")
    suboptimal_algorithm: str =Field(description="the algorithm to solve the problem")
    suboptimal_time_complexity: str = Field(description="the time complexity of the algorithm or code")
    suboptimal_space_complexity: str = Field(description="the space complexity of the algorithm or code")

suboptimal_agent=Agent(
    name="suboptimal Approach Agent",
    model=Groq(id='llama-3.3-70b-versatile', api_key=os.getenv("GROQ_API_KEY")),
    description = "You are an AI agent specialized in improving brute force algorithms into sub-optimal approaches.",
    instructions = [
        "You will receive the following information from the user:",
        "1. A problem statement.",
        "2. A brute force/basic approach to solve it.",
        "3. The brute force code implementation.",
        "4. The time and space complexity of the brute force approach.",
        "Your task:",
        "- Analyze the brute force solution.",
        "- Propose a **sub-optimal approach** that improves on the brute force solution, but is not yet the most optimal.",
        "- Focus on making it more efficient in terms of time or space, while keeping it simpler than the optimal solution.",
        "- Return only the improved approach/algorithm in a clear and structured way.",
        "⚠️ Do NOT provide the fully optimal solution — only the sub-optimal one."
    ],
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    add_context="You have to sub-optimize the brute force approach not give the fully optimized approach.",
    response_model=SubOptimalApproach
    ,use_json_mode=True
)


class SuboptimalCode(BaseModel):
  sub_optimal_algorithm:str
  sub_optimal_approach:str
  problem_statement:str
  basic_approach_code:str
  sub_optimal_code:str
  time_space_complexity:str = Field(description="the time and space complexity of the sub-optimized code")


sub_agent=Agent(
    name="suboptimal Approach Code Agent",
    model=Gemini(id="gemini-2.0-flash",api_key=os.getenv("GOOGLE_API_KEY")),
    tools=[PythonTools(run_code=True)],
description="You are an expert competitive programming and algorithms agent specializing in writing optimal solutions.",
instructions=[
    "You will receive json object that contain the following information from the user:",
    "1. Problem statement",
    "2. Basic (possibly brute-force) approach",
    "3. Corresponding code for the basic approach",
    "4. A known suboptimal algorithm (with time and space complexity)",

    "Your tasks are:",
    "- Carefully analyze the problem statement and the provided approaches.(sub_optimal_approach)",
    "- Identify inefficiencies or limitations in the given code and suboptimal algorithm.",
    "- Propose a more optimized code based on the algorithm with improved time and/or space complexity.",
    "- Explain why your optimized solution is better.",
    "- Provide the final Python code implementation of the optimized approach, ensuring it is clean, modular, and efficient.",
    "- Clearly state the optimized solution’s time and space complexity."
    "- The basic approach code and the sub optimal code should be different."
],
show_tool_calls=True,
    response_model=SuboptimalCode
)




# resp=suboptimal_agent.run(querry_1).content
# print(resp)
# print(resp.sunoptimal_approach)
# print(resp.sunoptimal_algorithm)
# querry={"role":"user",
#  "content":f"sub_optimal_algorithm:{resp.sunoptimal_algorithm},sub_optimal_approach:{resp.sunoptimal_approach},problem_statement:{resp.problem_statement},basic_approach:{resp.basic_code}"}

# resp=sub_agent.run(querry).content
# print(resp)


# suboptimal_team=Team(
#     name="Suboptimal Approach Team",
#     members=[suboptimal_agent,code_evaluator],
#     mode="collaborate",
#     model=Groq(id='llama-3.3-70b-versatile', api_key=os.getenv("GROQ_API_KEY")),
#     description="This team is designed to answer questions about the suboptimal approach to the users question",
#     instructions=[
#         "based on the input run the `suboptimal_agent` to get the suboptimal way to solve the question"
#         "then run the `code_evaluator` agent"],
#     show_tool_calls=True,
#     add_datetime_to_instructions=True,
#     response_model=SubOptimalApproach
#     ,use_json_mode=True
# )

# querry="""user_input="Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i." constraints='0 <= n <= 105' problem_statement="Count the number of 1's in the binary representation of each number from 0 to n and return them in an array." basic_approach='Iterate from 0 to n. For each number, convert it to its binary representation and count the number of 1s. Store the count in the corresponding index of the result array.' basic_algorithm='1. Initialize an array `ans` of size n + 1 with all elements set to 0.\n2. Iterate from i = 0 to n:\n   a. Convert the integer `i` to its binary representation.\n   b. Count the number of 1s in the binary string.\n   c. Assign the count to `ans[i]`.\n3. Return the array `ans`.' basic_time_complexity='O(n * log(n)) -  Iterating from 0 to n takes O(n). Converting each number i to binary takes O(log i) which is approximately O(log n). Counting 1s in the binary string is O(log n). Therefore the total time complexity would be O(n*log(n)).' basic_space_complexity='O(n) -  The array `ans` takes O(n) space. Converting to binary takes O(log n) space but is dominated by the O(n) space of ans' basic_code="python\ndef countBits(n):\n    ans = [0] * (n + 1)\n    for i in range(n + 1):\n        binary = bin(i)[2:]\n        count = binary.count('1')\n        ans[i] = count\n    return ans\n"""

# querry_1="""
# user_input="You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.\n\nIncrement the large integer by one and return the resulting array of digits.\nExample 1:\nInput: digits = [1,2,3]\nOutput: [1,2,4]\nExplanation: The array represents the integer 123.\nIncrementing by one gives 123 + 1 = 124.\nThus, the result should be [1,2,4].\nExample 2:\nInput: digits = [4,3,2,1]\nOutput: [4,3,2,2]\nExplanation: The array represents the integer 4321.\nIncrementing by one gives 4321 + 1 = 4322.\nThus, the result should be [4,3,2,2].\nExample 3:\nInput: digits = [9]\nOutput: [1,0]\nExplanation: The array represents the integer 9.\nIncrementing by one gives 9 + 1 = 10.\nThus, the result should be [1,0].\nConstraints:\n    1 <= digits.length <= 100\n    0 <= digits[i] <= 9\n    digits does not contain any leading 0's." constraints="1 <= digits.length <= 100\n0 <= digits[i] <= 9\ndigits does not contain any leading 0's." examples=['Input: digits = [1,2,3]\nOutput: [1,2,4]\nExplanation: The array represents the integer 123.\nIncrementing by one gives 123 + 1 = 124.\nThus, the result should be [1,2,4].', 'Input: digits = [4,3,2,1]\nOutput: [4,3,2,2]\nExplanation: The array represents the integer 4321.\nIncrementing by one gives 4321 + 1 = 4322.\nThus, the result should be [4,3,2,2].', 'Input: digits = [9]\nOutput: [1,0]\nExplanation: The array represents the integer 9.\nIncrementing by one gives 9 + 1 = 10.\nThus, the result should be [1,0].'] problem_statement='Given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer, increment the large integer by one and return the resulting array of digits.' basic_approach="Start from the least significant digit (rightmost) and add one. If there's a carry, propagate it to the next digit until there's no carry or we reach the most significant digit. If there's a carry after processing the most significant digit, add a new digit '1' at the beginning of the array." basic_algorithm='1. Initialize carry to 1.\n2. Iterate through the digits array from right to left.\n3. Add the carry to the current digit.\n4. If the sum is 10, set the current digit to 0 and carry to 1. Otherwise, set the current digit to the sum and carry to 0. Break the loop.\n5. After the loop, if carry is still 1, insert 1 at the beginning of the digits array.\n6. Return the modified digits array.' basic_time_complexity='O(n), where n is the number of digits in the input array.' basic_space_complexity='O(1) in the average case, O(n) in the worst case (when a new digit is added at the beginning).' basic_code='python\ndef plusOne(digits):\n    n = len(digits)\n    carry = 1\n    for i in range(n - 1, -1, -1):\n        digits[i] += carry\n        if digits[i] == 10:\n            digits[i] = 0\n            carry = 1\n        else:\n            carry = 0\n            break\n    if carry == 1:\n        digits.insert(0, 1)\n    return digits\n'
# """