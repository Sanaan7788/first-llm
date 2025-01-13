import streamlit as st

st.title("Welcome to my first LLM request")
st.header("OpenAI API")
openai_prompt=st.text_input("Please type your prompt")

if st.button("Send"):
    #gpt methods
    st.success("Content Generated!")
else:
    st.warning("Please insert a prompt")

st.divider()

st.header("Gemini API")
gemini_prompt=st.text_input("Please type your prompt", key="gemini-prompt")
gemini_tokens=st.number_input("Please select number of tokens")
if st.button("Send", key=2):
    #gpt methods
    st.success("Content Generated!")
else:
    st.warning("Please insert a prompt")