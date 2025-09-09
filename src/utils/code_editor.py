try:
    from code_editor import code_editor
except ImportError:
    def code_editor(code, lang="python", theme="default", key=None, focus=False):
        """Fallback code editor using streamlit text_area"""
        import streamlit as st
        return {"text": st.text_area("Code Editor", value=code, height=300, key=key)}