from code_editor import code_editor
from problem_analyzer import leetcode_team
import streamlit as st
import time
from qution_finder import question_finder
from brute_force import basic_approach_team
from notes_maker.sub_optimized_agent import suboptimal_agent,sub_agent
from code_verify import code_runner, code_verify_agent
from optimal_agent import optimal_code_agent,optimal_agent_enhanced
from agno.team import Team
from pydantic import BaseModel,Field
from agno.models.google import Gemini
import os
from dotenv import load_dotenv
load_dotenv()

st.title("DSA Assistant")
# your_code_string = "print('Hello, Streamlit!')"
# response_dict = code_editor(your_code_string)





st.set_page_config(layout="wide")
query=st.text_area("Enter the problem statement here")
if query:
    if st.button("Unlock Basic Approach: "):
        basic_approach=leetcode_team.run(query).content
        st.write("Problem Statement:")
        st.write(basic_approach.problem_statement)
        st.write("Basic Approach:")
        st.write(basic_approach.basic_approach)
        st.write("Basic Algorithm:")
        st.write(basic_approach.basic_algorithm)
        st.write("Brute Force Code:")
        response_dict = code_editor(basic_approach.basic_code)
        st.write("Time and Space Complexity:")
        st.write(basic_approach.basic_time_complexity)
        st.write(basic_approach.basic_space_complexity)
        time.sleep(20)
        if st.button("unlock sub-optimized."):
            sub_optimal_app=suboptimal_agent.run(basic_approach).content
            st.write("sub-optimal-approach: ")
            st.write(sub_optimal_app.suboptimal_approach)
            st.write("sub-optimal-algorithm: ")
            st.write(sub_optimal_app.suboptimal_algorithm)
            querry={"role":"user",
            "content":f"sub_optimal_algorithm:{sub_optimal_app.suboptimal_algorithm},sub_optimal_approach:{sub_optimal_app.suboptimal_approach},problem_statement:{sub_optimal_app.problem_statement},basic_approach:{sub_optimal_app.basic_code}"}
            time.sleep(20)
            sub_optimal_codes=sub_agent.run(querry).content
            # run and test the code
            test_query = f"Code:\n{sub_optimal_codes.sub_optimal_code}\n\nTest Cases:\n{basic_approach.examples}"
            test_results = code_runner.run(test_query)
            st.write("sub-optimal-code is running by the agent:")
            # Then format results
            format_query = f"Code: {sub_optimal_codes.sub_optimal_code}\nTest Results: {test_results.content}\nTest Cases: {basic_approach.examples}"
            sub_optimal_code_verified = code_verify_agent.run(format_query).content
            st.write("sub_optimal_code_verified: ")
            response_dict = code_editor(sub_optimal_code_verified.final_debuged_suboptimized_code)
            st.write("Time and Space Complexity:")
            st.write(sub_optimal_code_verified.time_space_complexity)
            time.sleep(20)
            if st.button("Unlock Optimal: "):
                optimal_approachs=optimal_agent_enhanced.run(sub_optimal_codes).content
                optimal_ap_code=optimal_code_agent.run(optimal_approachs).content
                st.write("Optimal Approach: ")
                st.write(optimal_approachs.optimal_approach)
                st.write("Optimal Algorithm: ")
                st.write(optimal_approachs.optimal_algorithm)
                st.write("Optimal Code is running by the agent: ")
                test_query = f"Code:\n{optimal_ap_code.optimal_code}\n\nTest Cases:\n{basic_approach.examples}"
                test_results = code_runner.run(test_query)
                format_query = f"Code: {optimal_ap_code.optimal_code}\nTest Results: {test_results.content}\nTest Cases: {basic_approach.examples}"
                optimal_code_verified = code_verify_agent.run(format_query).content
                response_dict = code_editor(optimal_code_verified.final_debuged_suboptimized_code)
                st.write("Time and Space Complexity:")
                st.write(optimal_code_verified.time_space_complexity)
                



