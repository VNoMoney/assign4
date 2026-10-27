# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Vincent Zhu")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the 3 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close'])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT")
    st.bar_chart(df['Volume'])

# Tab 4: I love creative liberty
# Hangman - Maybe you got bored of staring at stats all day, I dunno. Here's a game of hangman.

import random
import streamlit as st

WORDS = [
    "PETERWYSOCKI", "ASSIGNMENT4", "VINCENTZHU",
    "COLLAB", "STREAMLIT", "MICROSOFT",
    "FINANCIAL", "ANALYTIC"
]

st.title("Hangman")
st.write("Its hangman. You know how to play.")

# Initialize a new game
if "word" not in st.session_state:
    st.session_state.word = random.choice(WORDS)
    st.session_state.guessed = set()
    st.session_state.mistakes = 0

word = st.session_state.word
guessed = st.session_state.guessed

st.subheader(
    " ".join(letter if letter in guessed else "_"
             for letter in word)
)

st.write(f"Wrong guesses: {st.session_state.mistakes}/6")

# Display letters as buttons
for row in range(0, 26, 7):
    cols = st.columns(7)
    for i, letter in enumerate(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[row:row + 7]
    ):
        with cols[i]:
            if st.button(
                letter,
                key=letter,
                disabled=letter in guessed
            ):
                guessed.add(letter)
                if letter not in word:
                    st.session_state.mistakes += 1
                st.rerun()

# Check game status
if all(letter in guessed for letter in word):
    st.success(f"Congratz! The word was {word}!")
elif st.session_state.mistakes >= 6:
    st.error(f"Game over! The word was {word}.")

if st.button("🔄 New Game"):
    st.session_state.word = random.choice(WORDS)
    st.session_state.guessed = set()
    st.session_state.mistakes = 0
    st.rerun()
