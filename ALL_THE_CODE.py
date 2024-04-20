import requests
import webbrowser

def get_latest_video_url(api_key, channel_id):
    url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=1"
    response = requests.get(url)
    data = response.json()
    video_id = data["items"][0]["id"]["videoId"]
    return f"https://www.youtube.com/watch?v={video_id}"

def open_latest_video_in_chrome(api_key, channel_id):
    latest_video_url = get_latest_video_url(api_key, channel_id)
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # Modify the path if necessary
    webbrowser.get(chrome_path).open(latest_video_url)

# Replace these with your own API key and Linus Tech Tips channel ID
api_key = "YOUR_API_KEY"
channel_id = "UCXuqSBlHAE6Xw-yeJA0Tunw"  # Linus Tech Tips channel ID

open_latest_video_in_chrome(api_key, channel_id)
