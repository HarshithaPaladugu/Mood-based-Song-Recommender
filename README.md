# Mood-based-Song-Recommender
Recommends 3 music or songs based on the emotion in the input text and the language chosen.

#  Mood-Based Song Recommender using LLM and YouTube API

This is a Streamlit-based application that recommends songs from YouTube based on the **user’s emotional state**, detected from a journal-style input. It combines the power of a local **Large Language Model (LLM)** (e.g., `gemma3:1b` via [Ollama](https://ollama.com)) with the **YouTube Data API** to deliver personalized music suggestions across multiple Indian languages.

---

##  Workflow Overview

1. ** User Input (Journal Entry):**
   - The user types a short sentence about how they’re feeling.
   - Example: _"I feel anxious about tomorrow's interview."_  

2. ** Language Selection:**
   - The user selects a preferred language (e.g., Hindi, Tamil, English).

3. ** Mood Detection (LLM via Ollama):**
   - The text input is sent as a prompt to a local LLM (e.g., `gemma3:1b`).
   - The model returns a detected mood: `happy`, `sad`, `angry`, `chill`, `romantic`, `anxious`, or `spiritual`.

4. ** YouTube Music Search:**
   - Using the detected mood and selected language, a YouTube search query is formed:
     ```
     "{mood} mood {language} music"
     ```
   - Example: `"romantic mood Telugu music"`

5. **🎶 Song Recommendation:**
   - The YouTube Data API fetches top 3 matching videos.
   - Each song includes:
     - Title
     - Thumbnail preview
     - Link to play on YouTube

6. ** Streamlit Output:**
   - The app displays the mood, thumbnails, song titles, and clickable links in a clean UI.

---

## 🛠 Technologies Used

- **Python 3.10+**
- [Streamlit](https://streamlit.io/) – for frontend
- [Ollama](https://ollama.com/) – to run local LLMs (e.g., `gemma3:1b`)
- **YouTube Data API v3** – to fetch music video results
- **Requests** – to make API calls

---

##  How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt

### 2. Pull & Start Ollama

```bash
ollama pull gemma3:1b
ollama run gemma3:1b
```

### 3. Set Your YouTube API Key

Open `youtube_searcher_new.py` and replace:

```python
YOUTUBE_API_KEY = 'your-key-here'
```

### 4. Launch the App

```bash
streamlit run app.py
```

---

## Supported Languages

* English, Hindi, Telugu, Tamil, Kannada, Malayalam, Punjabi, Marathi, Gujarati, Bengali, Urdu, Odia

---

## Folder Structure

```
├── app.py                  # Streamlit app
├── mood_detector_new.py    # Mood classification using LLM
├── youtube_searcher_new.py # YouTube API music fetch
├── requirements.txt
└── README.md
```



