import streamlit as st
import random

# Flashcard data
flashcards = [
    ("あ", "a"), ("い", "i"), ("う", "u"), ("え", "e"), ("お", "o"),
    ("か", "ka"), ("き", "ki"), ("く", "ku"), ("け", "ke"), ("こ", "ko"),
    ("さ", "sa"), ("し", "shi"), ("す", "su"), ("せ", "se"), ("そ", "so"),
    ("た", "ta"), ("ち", "chi"), ("つ", "tsu"), ("て", "te"), ("と", "to"),
    ("な", "na"), ("に", "ni"), ("ぬ", "nu"), ("ね", "ne"), ("の", "no"),
    ("は", "ha"), ("ひ", "hi"), ("ふ", "fu"), ("へ", "he"), ("ほ", "ho"),
    ("ま", "ma"), ("み", "mi"), ("む", "mu"), ("め", "me"), ("も", "mo"),
    ("や", "ya"), ("ゆ", "yu"), ("よ", "yo"),
    ("ら", "ra"), ("り", "ri"), ("る", "ru"), ("れ", "re"), ("ろ", "ro"),
    ("わ", "wa"), ("を", "wo"), ("ん", "n"),
]

# Shuffle the flashcards
random.shuffle(flashcards)

# Web app UI
st.title("Japanese Flashcard App")
st.write("Practice your Hiragana and Katakana!")

# State for current card index
if "index" not in st.session_state:
    st.session_state.index = 0

# Show the current flashcard
if st.session_state.index < len(flashcards):
    character, pronunciation = flashcards[st.session_state.index]
    st.subheader(f"What is the pronunciation of: **{character}**?")

    # Input box for the answer
    user_answer = st.text_input("Your Answer:")

    # Submit button
    if st.button("Submit"):
        if user_answer.lower().strip() == pronunciation:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. The correct pronunciation is: **{pronunciation}**")
        # Move to the next flashcard
        st.session_state.index += 1
else:
    st.write("Congratulations! You've completed all flashcards!")

# Reset button
if st.button("Restart"):
    st.session_state.index = 0
    random.shuffle(flashcards)
