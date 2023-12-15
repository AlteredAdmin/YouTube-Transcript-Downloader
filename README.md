# YouTube Transcript Downloader

This repository contains a Python script for downloading transcripts from YouTube videos. The script extracts video IDs from provided YouTube URLs, fetches video titles, and downloads the transcripts, saving them as text files.

## Features

- Extract video ID from YouTube URLs.
- Fetch the title of the YouTube video.
- Download and save video transcripts in English.
- Error handling for robust execution.

## Prerequisites

To run this script, you need Python installed on your system along with a few dependencies. The dependencies are listed in `requirements.txt`.

### Dependencies

- `youtube_transcript_api`
- `requests`

Install these using the following command:

```bash
pip install -r requirements.txt
```

## How to Use

1. **Clone the Repository**: Clone this repository to your local machine or download the script.

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```

2. **Run the Script**: Navigate to the script's directory and run it.

    ```bash
    cd your-repo-name
    python youtube_transcript_downloader.py
    ```

3. **Enter YouTube URL**: When prompted, enter the full YouTube video URL.

4. **Transcript File**: The script will download the transcript and save it as a text file in the same directory.

## Script Overview

- `get_video_id(youtube_url)`: Extracts the video ID from a YouTube URL.

- `get_video_title(video_id)`: Fetches the title of a YouTube video given its ID.

- `download_transcript(video_id)`: Downloads the video's transcript.

- `main()`: The main function that orchestrates the URL input, transcript download, and file saving process.

## Error Handling

The script includes error handling to manage issues such as:
- Invalid YouTube URLs.
- Network errors during video title fetching.
- Problems in downloading or processing transcripts.

## Support the Developer
If you found this helpful, please consider:
- **Buymeacoffee:** [Link](http://buymeacoffee.com/alteredadmin)
