import streamlit as st
from uuid import uuid4
from problem_analyzer import leetcode_team
from qution_finder import question_finder
from sub_optimized_agent import suboptimal_agent, sub_agent
from code_verify import code_runner, code_verify_agent
from optimal_agent import optimal_code_agent, optimal_agent_enhanced

st.set_page_config(page_title="DSA Assistant", layout="wide", initial_sidebar_state="expanded")

# Updated CSS for improved code block rendering and accessibility
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=F Brinkmann Code:wght@400;500&display=swap');

    body {
        font-family: 'Inter', sans-serif;
        background-color: #f0f2f6;
    }

    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 0%);
        padding: 2.5rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    .main-header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .main-header p {
        font-size: 1.25rem;
        opacity: 0.9;
    }

    .step-card {
        background: #000000;
        padding: 2rem;
        border-radius: 12px;
        border-left: 6px solid #4f46e5;
        margin: 1.5rem 0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
            
            
    .step-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    }

    .complexity-metric {
        background: linear-gradient(45deg, #ec4899, #3b82f6);
        color: white;
        padding: 1.25rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.75rem 0;
        font-weight: 500;
    }

    .algorithm-box {
        background: #f9fafb;
        border: 2px solid #e5e7eb;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        font-size: 0.95rem;
    }

    .success-box {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        font-weight: 500;
    }

    .stButton > button {
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.75rem 2.5rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        width: 100%;
    }

    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 16px rgba(79, 70, 229, 0.3);
        background: linear-gradient(90deg, #3b82f6 0%, #6d28d9 100%);
    }

    .stButton > button:focus {
        outline: none;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.3);
    }

    .sidebar .sidebar-content {
        background: #1f2937;
        color: white;
        padding: 1rem;
        border-radius: 10px;
    }

    .progress-bar {
        background: #e5e7eb;
        border-radius: 10px;
        height: 10px;
        overflow: hidden;
        margin: 0.5rem 0;
    }

    .progress-fill {
        background: linear-gradient(90deg, #4f46e5, #7c3aed);
        height: 100%;
        transition: width 0.5s ease;
    }

    /* Enhanced code block styling */
    .stCodeBlock {
        background: #1f2937;
        color: #e5e7eb;
        padding: 1rem;
        border-radius: 8px;
        font-family: 'Fira Code', monospace;
        font-size: 0.9rem;
        line-height: 1.5;
        border: 1px solid #374151;
    }

    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #e5e7eb;
        font-size: 1rem;
        padding: 1rem;
    }

    .stTextArea textarea:focus {
        border-color: #4f46e5;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'basic_done' not in st.session_state:
    st.session_state.basic_done = False
if 'sub_optimal_done' not in st.session_state:
    st.session_state.sub_optimal_done = False
if 'optimal_done' not in st.session_state:
    st.session_state.optimal_done = False

# Calculate progress
progress = sum([st.session_state.basic_done, st.session_state.sub_optimal_done, st.session_state.optimal_done]) / 3 * 100

# Header
st.markdown("""
<div class="main-header">
    <h1>🚀 DSA Assistant</h1>
    <p>Your AI-powered companion for mastering Data Structures & Algorithms</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 📊 Progress Tracker")
    st.markdown(f"<div class='progress-bar'><div class='progress-fill' style='width: {progress}%'></div></div>", unsafe_allow_html=True)
    st.markdown(f"**Progress**: {int(progress)}%")
    st.markdown(f"✅ Basic Approach: {'Done' if st.session_state.basic_done else 'Pending'}")
    st.markdown(f"✅ Sub-Optimal: {'Done' if st.session_state.sub_optimal_done else 'Pending'}")
    st.markdown(f"✅ Optimal Solution: {'Done' if st.session_state.optimal_done else 'Pending'}")
    
    st.divider()
    st.markdown("## 💡 Tips")
    st.info("Start with a clear problem statement for best results.", icon="ℹ️")
    st.warning("Each step builds on the previous one.", icon="⚠️")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📝 Problem Statement")
    query = st.text_area(
        "Enter your DSA problem here:",
        height=150,
        placeholder="Paste your LeetCode problem or describe the algorithm challenge...",
        help="Provide a clear problem description for accurate solutions."
    )

with col2:
    st.markdown("### 🎯 Quick Actions")
    if st.button("🔍 Find Similar Problems", use_container_width=True):
        if query:
            with st.spinner("Searching for similar problems..."):
                similar = question_finder.run(query)
                st.success("Found similar problems!", icon="✅")
    
    if st.button("🧹 Clear All", use_container_width=True):
        st.session_state.clear()
        st.rerun()

if query:
    # Basic Approach Section
    st.markdown("""
    <div class="step-card">
        <h2>🎯 Step 1: Basic Approach</h2>
        <p>Let's start with the fundamental brute-force solution</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔓 Unlock Basic Approach", type="primary", use_container_width=True):
        with st.spinner("Analyzing problem and generating basic approach..."):
            basic_approach = leetcode_team.run(query).content
            st.session_state.basic_approach = basic_approach
            st.session_state.basic_done = True
    
    if st.session_state.basic_done:
        basic_approach = st.session_state.basic_approach
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 📋 Problem Analysis")
            st.info(basic_approach.problem_statement)
            
            st.markdown("#### 🧠 Approach")
            st.write(basic_approach.basic_approach)
            
        with col2:
            st.markdown("#### ⚡ Complexity")
            st.metric("Time Complexity", basic_approach.basic_time_complexity)
            st.metric("Space Complexity", basic_approach.basic_space_complexity)
        
        st.markdown("""
        <div class="algorithm-box">
            <h4>🔢 Algorithm Steps</h4>
        </div>
        """, unsafe_allow_html=True)
        st.code(basic_approach.basic_algorithm, language="text")
        
        st.markdown("#### 💻 Brute Force Code")
        st.code(basic_approach.basic_code, language="python")


        # Sub-Optimal Section
        st.markdown("""
        <div class="step-card">
            <h2>⚡ Step 2: Sub-Optimal Solution</h2>
            <p>Now let's optimize our approach for better performance</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔓 Unlock Sub-Optimal", type="primary", use_container_width=True):
            with st.spinner("Optimizing approach..."):
                sub_optimal_app = suboptimal_agent.run(basic_approach).content
                query_data = {
                    "role": "user",
                    "content": f"sub_optimal_algorithm:{sub_optimal_app.suboptimal_approach},sub_optimal_approach:{sub_optimal_app.suboptimal_approach},problem_statement:{sub_optimal_app.problem_statement},basic_approach:{sub_optimal_app.basic_code}"
                }
                sub_optimal_codes = sub_agent.run(query_data).content
                
                # Test code
                test_query = f"Code:\n{sub_optimal_codes.sub_optimal_code}\n\nTest Cases:\n{basic_approach.examples}"
                test_results = code_runner.run(test_query)
                format_query = f"Code: {sub_optimal_codes.sub_optimal_code}\nTest Results: {test_results.content}\nTest Cases: {basic_approach.examples}"
                sub_optimal_code_verified = code_verify_agent.run(format_query).content
                
                st.session_state.sub_optimal_verified = sub_optimal_code_verified
                st.session_state.sub_optimal_app = sub_optimal_app
                st.session_state.sub_optimal_done = True
        
        if st.session_state.sub_optimal_done:
            sub_optimal_verified = st.session_state.sub_optimal_verified
            sub_optimal_app = st.session_state.sub_optimal_app
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### 🎯 Optimized Approach")
                st.success(sub_optimal_app.suboptimal_approach)
                
            with col2:
                st.markdown("#### ⚡ Improved Complexity")
                st.metric("Time complexity", sub_optimal_verified.time_complexity)
                st.metric("Time complexity", sub_optimal_verified.space_complexity)
            
            st.markdown("""
            <div class="algorithm-box">
                <h4>🔢 Sub-Optimal Algorithm</h4>
            </div>
            """, unsafe_allow_html=True)
            st.code(sub_optimal_app.suboptimal_algorithm, language="text")
            
            st.markdown("#### 💻 Sub-Optimal Code")
            st.code(sub_optimal_verified.final_debuged_suboptimized_code, language="python")
            
            # Optimal Section
            st.markdown("""
            <div class="step-card">
                <h2>🏆 Step 3: Optimal Solution</h2>
                <p>Finally, let's achieve the most efficient solution possible</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🔓 Unlock Optimal Solution", type="primary", use_container_width=True):
                with st.spinner("Finding the most optimal solution..."):
                    optimal_approaches = optimal_agent_enhanced.run(st.session_state.sub_optimal_verified).content
                    optimal_ap_code = optimal_code_agent.run(optimal_approaches).content
                    
                    # Test optimal code
                    test_query = f"Code:\n{optimal_ap_code.optimal_code}\n\nTest Cases:\n{basic_approach.examples}"
                    test_results = code_runner.run(test_query)
                    format_query = f"Code: {optimal_ap_code.optimal_code}\nTest Results: {test_results.content}\nTest Cases: {basic_approach.examples}"
                    optimal_code_verified = code_verify_agent.run(format_query).content
                    
                    st.session_state.optimal_verified = optimal_code_verified
                    st.session_state.optimal_approaches = optimal_approaches
                    st.session_state.optimal_done = True
            
            if st.session_state.optimal_done:
                optimal_verified = st.session_state.optimal_verified
                optimal_approaches = st.session_state.optimal_approaches
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("#### 🏆 Optimal Approach")
                    st.success(optimal_approaches.optimal_approach)
                    
                with col2:
                    st.markdown("#### ⚡ Best Complexity")
                    st.metric("Time complexity", optimal_verified.time_complexity)
                    st.metric("space Complexity", optimal_verified.space_complexity)
                
                st.markdown("""
                <div class="algorithm-box">
                    <h4>🔢 Optimal Algorithm</h4>
                </div>
                """, unsafe_allow_html=True)
                st.code(optimal_approaches.optimal_algorithm, language="text")
                
                st.markdown("#### 💻 Optimal Code")
                st.code(optimal_verified.final_debuged_suboptimized_code, language="python")
                
                st.balloons()
                st.success("🎉 Congratulations! You've mastered this problem with all optimization levels!", icon="🎉")

else:
    st.markdown("### 👋 Welcome to DSA Assistant!")
    st.markdown("Enter a problem statement above to get started with your algorithmic journey.")
    
    # Example problems
    st.markdown("#### 📚 Try these example problems:")
    examples = [
        "Two Sum: Given an array of integers and a target sum, return indices of two numbers that add up to target.",
        "Binary Search: Search for a target value in a sorted array.",
        "Fibonacci: Calculate the nth Fibonacci number.",
        "House Robber: Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police."
    ]
    
    for i, example in enumerate(examples, 1):
        if st.button(f"Example {i}: {example[:70]}...", key=f"ex_{i}", use_container_width=True):
            st.session_state.example_query = example
            st.rerun()
