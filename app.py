import streamlit as st
from api_calling import promtOptimize

# 1. Page Setup
st.set_page_config(page_title="AI Prompt Optimizer", page_icon="🪄", layout="wide")
st.title("AI Prompt Optimizer")
st.caption("Transform vague prompts into highly effective instructions.")

# 2. Sidebar for API Configuration
with st.sidebar:
    st.header("Settings")
    model_choice = st.selectbox("Select Model", ["gemini-flash-latest", "gemini-3.8-flash", "gemini-3.7-flash", "gemini-3.5-flash-lite"])
    tone_choice = st.selectbox("Optimization Tone", ["Professional", "Creative", "Strict/Technical"])

    # 3. User Input
user_prompt = st.text_area("✍️ Paste your raw prompt here:", height=150, placeholder="e.g., write an email to my boss asking for a raise")

if st.button("Optimize Prompt ✨", type="primary"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt to optimize.")
    else:
        with st.spinner("Refining your prompt..."):
            try:
                optimized_result = promtOptimize(model_choice, user_prompt, tone_choice)

                st.success("Done!")
                st.markdown(optimized_result)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")


