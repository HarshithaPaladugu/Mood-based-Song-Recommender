import requests

YOUTUBE_API_KEY = 'AIzaSyC6k3YoIPDmJ4xmTprFXygBZO7lRn8eQxg'  # Replace with your actual API key

def search_youtube_music(mood, language="English", max_results=3):
    search_query = f"{mood} mood {language} music"
    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": search_query,
        "type": "video",
        "maxResults": max_results,
        "key": YOUTUBE_API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        videos = []
        for item in data.get('items', []):
            title = item['snippet']['title']
            video_id = item['id']['videoId']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            thumbnail = item['snippet']['thumbnails']['high']['url']
            videos.append({
                "title": title,
                "url": video_url,
                "thumbnail": thumbnail
            })
        return videos

    except Exception as e:
        print(f"Error: {e}")
        return []
