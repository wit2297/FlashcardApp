import streamlit as st
import random

# Flashcard data
flashcards = {
    "あ": "a",
    "い": "i",
    "う": "u",
    "え": "e",
    "お": "o",
    "か": "ka",
    "き": "ki",
    "く": "ku",
    "け": "ke",
    "こ": "ko",
}

# Initialize session state for current card, choices, and feedback
if "current_card" not in st.session_state:
    st.session_state.current_card = None
if "choices" not in st.session_state:
    st.session_state.choices = []
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# Function to pick a new card and generate choices
def new_flashcard():
    st.session_state.current_card = random.choice(list(flashcards.items()))
    correct_answer = st.session_state.current_card[1]
    
    # Generate 5 random incorrect options
    all_values = list(flashcards.values())
    all_values.remove(correct_answer)
    incorrect_options = random.sample(all_values, 5)
    
    # Combine correct answer with incorrect options and shuffle
    st.session_state.choices = incorrect_options + [correct_answer]
    random.shuffle(st.session_state.choices)
    st.session_state.feedback = ""

# Function to check the selected answer
def check_answer(selected_option):
    if selected_option == st.session_state.current_card[1]:
        st.session_state.feedback = "✅ Correct!"
    else:
        st.session_state.feedback = "❌ Incorrect, try again!"

# Main app layout
st.title("Flashcard Quiz")

# Display current flashcard
if st.session_state.current_card is None:
    new_flashcard()

st.subheader(f"What is the pronunciation of: {st.session_state.current_card[0]}")

# Display answer choices as buttons
for choice in st.session_state.choices:
    if st.button(choice):
        check_answer(choice)

# Display feedback
if st.session_state.feedback:
    st.write(st.session_state.feedback)

# Next button to move to the next flashcard
if st.session_state.feedback == "✅ Correct!":
    if st.button("Next Flashcard"):
        new_flashcard()
