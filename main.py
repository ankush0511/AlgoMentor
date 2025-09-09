import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini
from notes import Notes_team
from code_editor import code_editor
import time
import os
from dotenv import load_dotenv
load_dotenv()
from problem_analyzer import leetcode_team
from qution_finder import question_finder
from sub_optimized_agent import suboptimal_agent, sub_agent
from code_verify import code_runner, code_verify_agent
from optimal_agent import optimal_code_agent, optimal_agent_enhanced

st.set_page_config(page_title="AlgoMentor", layout="wide", initial_sidebar_state="expanded")

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

    /* Notes Mentor Specific Styling */
    .notes-mentor-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 0%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
    }

    .code-input-section {
        background: linear-gradient(145deg, #000000, #e2e8f0);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }

    .preview-section {
        background: linear-gradient(145deg, #000000, #f1f5f9);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }

    .notes-output-section {
        background: linear-gradient(145deg, #000000, #f8fafc);
        padding: 2rem;
        border-radius: 15px;
        border: 2px solid #e5e7eb;
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
        margin: 2rem 0;
    }

    .character-count {
        background: linear-gradient(90deg, #3b82f6, #1d4ed8);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        display: inline-block;
        margin-top: 0.5rem;
    }

    .download-section {
        background: linear-gradient(135deg, #10b981, #059669);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        text-align: center;
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

# Notes Mentor session states
if 'notes_input_code' not in st.session_state:
    st.session_state.notes_input_code = ""
if 'notes_generated' not in st.session_state:
    st.session_state.notes_generated = False
if 'generated_notes' not in st.session_state:
    st.session_state.generated_notes = ""
if 'notes_lang' not in st.session_state:
    st.session_state.notes_lang = "python"
if 'notes_theme' not in st.session_state:
    st.session_state.notes_theme = "default"


with st.sidebar:
    options=st.selectbox("What you like to do!",("DSA Menotr","Notes Mentor"))

if options=="DSA Menotr":

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

else:
        
    st.markdown("""
    <div class="notes-mentor-header">
        <h1>📚 Notes Mentor</h1>
        <p>Transform your code into comprehensive study notes!</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar for settings
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Language selection
        lang_options = ["python", "c_cpp", "java", "javascript", "c"]
        selected_lang = st.selectbox("Programming Language:", lang_options, 
                                   index=lang_options.index(st.session_state.notes_lang) if st.session_state.notes_lang in lang_options else 0,
                                   key="notes_lang_select")
        st.session_state.notes_lang = selected_lang
        
        # Theme selection
        theme_options = ["default", "dark", "light"]
        selected_theme = st.selectbox("Editor Theme:", theme_options, 
                                    index=theme_options.index(st.session_state.notes_theme) if st.session_state.notes_theme in theme_options else 0,
                                    key="notes_theme_select")
        st.session_state.notes_theme = selected_theme
        
        
        st.markdown("---")
        st.markdown("💡 **Tips:**\n- Paste your code and press Ctrl+Enter\n- Use clear variable names for better analysis\n- Include comments for complex logic")

    # Main content area
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
        <div class="code-input-section">
            <h3>📝 Code Input</h3>
        </div>
        """, unsafe_allow_html=True)
        
        response_dict = code_editor(
            st.session_state.notes_input_code, 
            lang=selected_lang, 
            key="code_input", 
            theme=selected_theme,
            focus=True
        )
        input_code = response_dict["text"]
        st.session_state.notes_input_code = input_code
        
        # Show character count
        if input_code:
            st.markdown(f'<div class="character-count">Characters: {len(input_code)}</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="preview-section">
            <h3>🔍 Quick Preview</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if input_code.strip():
            st.code(input_code[:200] + "..." if len(input_code) > 200 else input_code, language=selected_lang)
        else:
            st.info("Code preview will appear here...")

    # Action buttons
    col_btn1, col_btn2 = st.columns([1, 1])

    with col_btn1:
        generate_btn = st.button("🚀 Generate Notes", type="primary")

    with col_btn2:
        clear_btn = st.button("🗑️ Clear")

    if clear_btn:
        st.session_state.notes_input_code = ""
        st.session_state.notes_generated = False
        st.session_state.generated_notes = ""
        st.rerun()

    if generate_btn:
        if not input_code.strip():
            st.error("⚠️ Please enter some code before submitting.")
        else:
            try:
                # Progress tracking
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                status_text.text("🔄 Analyzing code structure...")
                progress_bar.progress(25)
                time.sleep(0.5)
                
                status_text.text("🧠 Generating comprehensive notes...")
                progress_bar.progress(50)
                
                resp = Notes_team.run(input_code, markdown=True).content
                progress_bar.progress(75)
                
                api_key = os.getenv('GOOGLE_API_KEY')
                if not api_key:
                    st.error("🔑 Google API key not found. Please check your .env file.")
                else:
                    status_text.text("✨ Finalizing notes...")
                    agent = Agent(markdown=True, model=Gemini(id="gemini-2.0-flash", api_key=api_key))
                    final_resp = agent.run(resp)
                    
                    progress_bar.progress(100)
                    status_text.text("✅ Notes generated successfully!")
                    
                    # Display results
                    st.markdown("---")
                    st.markdown("""
                    <div class="notes-output-section">
                        <h3>📖 Generated Notes</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Store generated notes in session state
                    st.session_state.generated_notes = final_resp.content
                    st.session_state.notes_generated = True
                    
                    # Clear progress indicators
                    progress_bar.empty()
                    status_text.empty()
                    
            except AttributeError as e:
                st.error(f"❌ Error accessing response content: {str(e)}")
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                st.info("💡 Try refreshing the page or checking your internet connection.")
    
    # Display generated notes if available
    if st.session_state.notes_generated and st.session_state.generated_notes:
        st.markdown("---")
        st.markdown("""
        <div class="notes-output-section">
            <h3>📖 Generated Notes</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Display formatted notes
        st.markdown(st.session_state.generated_notes)
        
        # Download section
        st.markdown("""
        <div class="download-section">
            <h4>📥 Download Your Notes</h4>
        </div>
        """, unsafe_allow_html=True)
        
        col_dl1, col_dl2 = st.columns(2)
        with col_dl1:
            st.download_button(
                label="📥 Download Markdown",
                data=st.session_state.generated_notes,
                file_name=f"dsa_notes_{int(time.time())}.md",
                mime="text/markdown"
            )
        with col_dl2:
            if st.button("🗑️ Clear Notes"):
                st.session_state.notes_generated = False
                st.session_state.generated_notes = ""
                st.rerun()

    # Footer
    st.markdown("---")
    st.markdown("<div style='text-align: center; color: gray;'>Made with ❤️ for DSA learners</div>", unsafe_allow_html=True)