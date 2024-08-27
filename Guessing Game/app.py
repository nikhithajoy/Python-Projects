import streamlit as st
import random

# Function to initialize the game
def init_game():
    if 'number_to_guess' not in st.session_state:
        st.session_state.number_to_guess = random.randint(1, 100)
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0

# Function to reset the game
def reset_game():
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.feedback = ""

# Function to handle guesses
def guess_number(user_guess):
    st.session_state.attempts += 1
    difference = abs(st.session_state.number_to_guess - user_guess)
    
    if user_guess < st.session_state.number_to_guess:
        if difference > 20:
            st.session_state.feedback = "🌡️ Way too low. Try a much higher number."
        elif difference > 10:
            st.session_state.feedback = "⬆️ Too low. Try a bit higher."
        else:
            st.session_state.feedback = "🔼 Slightly low. You're very close!"
    elif user_guess > st.session_state.number_to_guess:
        if difference > 20:
            st.session_state.feedback = "🌡️ Way too high. Try a much lower number."
        elif difference > 10:
            st.session_state.feedback = "⬇️ Too high. Try a bit lower."
        else:
            st.session_state.feedback = "🔽 Slightly high. You're very close!"
    else:
        st.session_state.feedback = f"🎉 Congratulations! You guessed the number {st.session_state.number_to_guess} correctly in {st.session_state.attempts} attempts."
        st.balloons()

# Initialize the game
init_game()

# Streamlit app layout with enhanced UI
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f0f0;
    }
    h1 {
        color: #4CAF50;
        text-align: center;
    }
    <style>
    label[for="number"] {
        color: #4CAF50;
        font-size: 18px;
        font-weight: bold;
    }
    .stTextInput > div > input {
        font-size: 18px;
        padding: 10px;
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        border: 2px solid #4CAF50;
    }
    .stTextInput > label {
        color: #4CAF50;
        font-size: 18px;
    }
    .stMarkdown p {
        color: #4CAF50;
        font-size: 18px;
    }
    .stButton > button {
        font-size: 18px;
        padding: 10px;
        margin-top: 20px;
        width: 100%;
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
    }
    .feedback {
        font-size: 20px;
        color: #333333;
        text-align: center;
        margin-top: 20px;
    }
    .attempts {
        text-align: center;
        font-size: 20px;
        color: #333333;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔢 Random Number Guessing Game")
st.write(
    """
    **I'm thinking of a number between 1 and 100. Can you guess it?**
    """
)

# Input for user guess with styled input box
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, format="%d")

# Columns for guess and reset buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("💡 Guess"):
        guess_number(user_guess)
        st.markdown(f"<div class='feedback'>{st.session_state.feedback}</div>", unsafe_allow_html=True)

with col2:
    if st.button("🔄 Reset Game"):
        reset_game()
        st.write("Game has been reset. Try guessing again!")

# Display the number of attempts with style
st.markdown(
    f"""
    <div class="attempts">
    Number of attempts: <strong>{st.session_state.attempts}</strong>
    </div>
    """,
    unsafe_allow_html=True
)
