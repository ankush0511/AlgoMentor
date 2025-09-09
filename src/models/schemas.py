

from pydantic import BaseModel, Field
from typing import List, Optional

class LeetCodeProblem(BaseModel):
    """Model for LeetCode problem structure"""
    user_input: str
    constraints: str
    examples: List[str]
    problem_statement: str = Field(description="the problem statement")
    basic_approach: str = Field(description="the approach to solve the problem")
    basic_algorithm: str = Field(description="the algorithm to solve the problem")
    basic_time_complexity: str = Field(description="the time complexity of the algorithm or code")
    basic_space_complexity: str = Field(description="the space complexity of the algorithm or code")
    basic_code: str = Field(description="the code to solve the problem")

class BruteForceApproach(BaseModel):
    """Model for brute force approach"""
    problem_statement: str = Field(description="the problem statement")
    basic_approach: str = Field(description="the basic or bruteforce approach to solve the problem")
    basic_algorithm: str = Field(description="the basic or bruteforce algorithm to solve the problem")
    basic_time_complexity: str = Field(description="the time complexity of the algorithm or code")
    basic_space_complexity: str = Field(description="the space complexity of the algorithm or code")
    code: str = Field(description="the code to solve the problem")
    updated_code: str = Field(description="the updated and working code to solve the problem")

class SubOptimalApproach(BaseModel):
    """Model for sub-optimal approach"""
    problem_statement: str = Field(description="the problem statement")
    basic_approach: str = Field(description="the approach to solve the problem")
    basic_algorithm: str = Field(description="the algorithm to solve the problem")
    basic_time_complexity: str = Field(description="the time complexity of the algorithm or code")
    basic_space_complexity: str = Field(description="the space complexity of the algorithm or code")
    basic_code: str = Field(description="the code to solve the problem")
    suboptimal_approach: str = Field(description="the optimized approach to solve the problem")
    suboptimal_algorithm: str = Field(description="the optimized algorithm to solve the problem")
    suboptimal_time_complexity: str = Field(description="the time complexity of the optimized algorithm")
    suboptimal_space_complexity: str = Field(description="the space complexity of the optimized algorithm")

class SuboptimalCode(BaseModel):
    """Model for sub-optimal code implementation"""
    sub_optimal_algorithm: str = Field(description="the optimized algorithm description")
    sub_optimal_approach: str = Field(description="the optimized approach explanation")
    problem_statement: str = Field(description="the original problem statement")
    basic_approach_code: str = Field(description="the basic/brute-force code")
    sub_optimal_code: str = Field(description="the optimized implementation code")
    time_space_complexity: str = Field(description="the time and space complexity analysis of the optimized code")

class OptimalApproach(BaseModel):
    """Model for optimal approach"""
    optimal_approach: str = Field(description="the most optimal approach")
    optimal_algorithm: str = Field(description="the most optimal algorithm")
    optimal_time_complexity: str = Field(description="optimal time complexity")
    optimal_space_complexity: str = Field(description="optimal space complexity")

class CodeVerification(BaseModel):
    """Model for code verification results"""
    final_debuged_suboptimized_code: str = Field(description="final debugged code")
    time_complexity: str = Field(description="time complexity")
    space_complexity: str = Field(description="space complexity")
    time_space_complexity: str = Field(description="combined time and space complexity")