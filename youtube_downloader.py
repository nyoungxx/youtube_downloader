# Import the necessary classes and functions from pytubefix.
from pytube import YouTube
from pytube import on_progress

def main():
    # Prompt the user for the YouTube URL.
    url = input("Enter YouTube URL: ")

    try:
        # Create a YouTube object.
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback=on_progress)

        # Print the title of the video to confirm that the YouTube object is working.
        print("Downloading:", yt.title)

        # Get the highest resolution progressive stream available.
        stream = yt.streams.get_highest_resolution()

        # Download the video to the current working directory.
        stream.download()
        print("Download completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")

