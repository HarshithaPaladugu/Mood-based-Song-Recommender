import streamlit as st
from mood_detector_new import detect_mood
from youtube_searcher_new import search_youtube_music

# Set page config
st.set_page_config(page_title=" Mood-Based Song Recommender", layout="centered")

# Title
st.title("Mood-Based Song Recommender")

# Description
st.markdown("Type a journal entry and select your language to get music that matches your mood!")

# Input: Journal Entry
user_input = st.text_area("How are you feeling today?", height=100)

# Dropdown: Language
languages = [
    "English", "Hindi", "Telugu", "Tamil", "Kannada", "Malayalam",
    "Punjabi", "Marathi", "Gujarati", "Bengali", "Urdu", "Odia"
]
selected_language = st.selectbox("Choose Language", languages)

# Submit Button
if st.button("Get Recommendations"):
    if not user_input.strip():
        st.warning("Please enter how you're feeling.")
    else:
        with st.spinner(" Detecting mood..."):
            mood = detect_mood(user_input)
            st.success(f"Detected Mood: **{mood.title()}**")

        with st.spinner("Fetching YouTube music..."):
            songs = search_youtube_music(mood, selected_language)

        if songs:
            st.markdown("### Top 3 Recommendations")
            for video in songs:
                st.markdown(f"**{video['title']}**")
                st.image(video['thumbnail'], use_column_width=True)
                st.markdown(f"[ Watch on YouTube]({video['url']})", unsafe_allow_html=True)
                st.markdown("---")
        else:
            st.error("No music recommendations found. Try a different mood or language.")
