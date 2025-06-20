import subprocess

def detect_mood(user_text):
    if not user_text.strip():
        return "neutral"

    prompt = (
        "Classify the following text into one of the moods from this list: "
        "[happy, sad, angry, chill, romantic, anxious, spiritual]. "
        "Just return the mood as a single word.\n\n"
        f"Text: {user_text}"
    )

    try:
        result = subprocess.run(
            ["ollama", "run", "gemma3:1b"],  # replace 'gemma3:1b' with exact name if needed
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30
        )

        output = result.stdout.decode("utf-8", errors="ignore").lower()

        # List of supported moods
        allowed_moods = ["happy", "sad", "angry", "chill", "romantic", "anxious", "spiritual"]

        # Match any allowed mood word that appears in output
        for mood in allowed_moods:
            if mood in output:
                return mood

        return "neutral"

    except subprocess.TimeoutExpired:
        return "neutral"
    except Exception as e:
        print(f"Mood detection failed: {e}")
        return "neutral"
