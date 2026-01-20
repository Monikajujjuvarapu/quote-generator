import streamlit as st
import random

# Page config
st.set_page_config(
    page_title="Motivation Generator",
    page_icon="🌸",
    layout="centered"
)

# Pastel CSS
st.markdown("""
    <style>
        body {
            background-color: #fff6fb;
        }
        .main {
            background-color: #fff6fb;
        }
        .quote-box {
            background-color: #fde2f3;
            padding: 25px;
            border-radius: 20px;
            text-align: center;
            font-size: 22px;
            color: #5a2a6e;
            font-weight: 500;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        }
        .stButton>button {
            background-color: #f7b2d9;
            color: white;
            border-radius: 30px;
            padding: 10px 30px;
            font-size: 18px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #f48fb1;
        }
    </style>
""", unsafe_allow_html=True)

# Quotes list
quotes = [
    "You are doing better than you think 🌷",
    "Small steps still move you forward ✨",
    "Be proud of how far you’ve come 💖",
    "Your effort matters, even on quiet days 🌸",
    "You don’t need to rush — growth is happening 🌼",
    "Soft hearts still carry strong souls 🌙",
    "Today is a good day to believe in yourself 🌈",
    "You are allowed to grow at your own pace 🦋"
]

# Title
st.markdown("<h1 style='text-align:center; color:#6a0572;'>🌸 Motivation Generator 🌸</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#8e4a7c;'>Click the button for a little encouragement</p>", unsafe_allow_html=True)

# Session state
if "quote" not in st.session_state:
    st.session_state.quote = random.choice(quotes)

# Quote display
st.markdown(f"<div class='quote-box'>{st.session_state.quote}</div>", unsafe_allow_html=True)

st.write("")
st.write("")

# Button
if st.button("✨ New Motivation ✨"):
    st.session_state.quote = random.choice(quotes)
