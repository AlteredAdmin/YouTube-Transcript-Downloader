from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import requests
import re
import os

def get_video_id(youtube_url):
    """
    Extract the video ID from a YouTube URL.
    Args:
        youtube_url (str): The YouTube URL.
    Returns:
        str: The extracted video ID or None if not found.
    """
    pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, youtube_url)
    return match.group(1) if match else None

def get_video_title(video_id):
    """
    Get the title of the YouTube video.
    Args:
        video_id (str): The YouTube video ID.
    Returns:
        str: The title of the video or "Unknown" if not found.
    """
    url = f"https://www.youtube.com/watch?v={video_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        matches = re.findall(r'<title>(.*?)</title>', response.text)
        return matches[0].replace(" - YouTube", "") if matches else "Unknown"
    except requests.RequestException as e:
        print(f"Error fetching video title: {e}")
        return "Unknown"

def download_transcript(video_id):
    """
    Download the transcript and return as a string.
    Args:
        video_id (str): The YouTube video ID.
    Returns:
        str: The transcript text or an empty string if an error occurs.
    """
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_generated_transcript(['en'])

        formatter = TextFormatter()
        transcript_text = formatter.format_transcript(transcript.fetch())

        # Remove timecodes and speaker names
        transcript_text = re.sub(r'\[\d+:\d+:\d+\]', '', transcript_text)
        transcript_text = re.sub(r'<\w+>', '', transcript_text)
        return transcript_text
    except Exception as e:
        print(f"Error downloading transcript: {e}")
        return ""

def main():
    youtube_url = input("Enter the YouTube video link: ")
    video_id = get_video_id(youtube_url)

    if video_id:
        transcript_text = download_transcript(video_id)
        if transcript_text:
            video_title = get_video_title(video_id)
            file_name = f"{video_id}_{video_title}.txt"
            file_name = re.sub(r'[\\/*?:"<>|]', '', file_name)  # Remove invalid characters

            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(transcript_text)

            print(f"Transcript saved to {file_name}")
        else:
            print("Unable to download transcript.")
    else:
        print("Invalid YouTube URL.")

if __name__ == "__main__":
    main()
