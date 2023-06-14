import requests
import streamlit as st

api_key = "ZzhtEOjGHLCK5mDRcW6Dh0WjS7muc9ZU4VqmqV5T"

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)

content = response.json()

photo_title = content["title"]
photo_desc = content["explanation"]
photo_url = requests.get(content["url"])

# st.set_page_config(layout="wide")
st.header(f"{photo_title}")

with open("image.jpg", "wb") as file:
    file.write(photo_url.content)

st.image("image.jpg")

st.write(f"{photo_desc}")
