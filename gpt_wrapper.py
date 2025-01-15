#this file contains gpt connection

from openai import OpenAI
import streamlit as st
import requests

api_key = st.secrets["api_key"]
client = OpenAI(api_key=api_key)

#function that generates text chat-gpt answer to the given prompt
def generate_text(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    st.write(completion.choices[0].message.content)

#function that generates the chat-gpt image link to the given prompt
def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url=response.data[0].url

    image_response=requests.get(image_url)

    with open("otter.png","wb") as file:
        file.write(image_response.content)