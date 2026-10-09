from google import genai
import os
from dotenv import load_dotenv

# load virtual environment
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# prompt enhancer
def promtOptimize(model, user_prompt, tone_choice):

    prompt = """You are an expert Prompt Engineer. Optimize the user's prompt making it {tone_choice}. Your task is to take a raw, poorly structured user prompt and optimize it into a highly effective, clear, and context-rich prompt that will yield perfect results from any LLM.

    Follow these strict rules when optimizing the prompt:
    1. Define the Role: Assign a specific, expert persona to the LLM (e.g., "You are an expert data analyst...").
    2. Establish Context: Explain the background or objective of the task.
    3. Provide Clear Instructions: Break down the task into logical, sequential steps.
    4. Specify Constraints: Clearly state what NOT to do, tone requirements, or length limits.
    5. Define the Output Format: Use Markdown, JSON, bullet points, or tables depending on the intent.

    Return your response in this exact Markdown structure:

    ### 🚀 Optimized Prompt
    [Insert the fully rewritten, ready-to-copy prompt here]

    ### 💡 What Was Changed & Why
    * **Role/Persona:** [Briefly explain the persona added]
    * **Structure:** [Explain how you reorganized the instructions]
    * **Clarity:** [Explain any ambiguous terms you fixed]"""
    

    # prompt = f"You are an expert Prompt Engineer. Optimize the user's prompt making it {tone_choice}. Follow structured prompt engineering frameworks (Role, Context, Task, Constraints, Output Format)."


    response = client.models.generate_content(
        model=model,
        contents=[user_prompt, prompt]
    )
    return response.text