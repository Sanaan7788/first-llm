import streamlit as st
from gpt_wrapper import generate_text
from gemini_wrapper import generate_gemini_text

#openai input UI
st.title("Welcome to my first LLM request")
st.header("OpenAI API")
openai_prompt=st.text_input("Please type your prompt")
if st.button("Send"):
    generate_text(openai_prompt)
    st.success("Content Generated!")
else:
    st.warning("Please insert a prompt")

st.divider()

#gemini input UI
st.header("Gemini API")
gemini_prompt=st.text_input("Please type your prompt", key="gemini-prompt")
gemini_tokens=st.number_input("Please select number of tokens", min_value=0, max_value=1000)
if st.button("Send", key=2):
    generate_gemini_text(gemini_prompt,gemini_tokens)
    st.success("Content Generated!")
else:
    st.warning("Please insert a prompt")