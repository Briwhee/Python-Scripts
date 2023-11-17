#download music from youtube to computer

from pytube import YouTube

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the videos audio
    yd = yt.streams.filter(only_audio=True)

    # Download the video to the current directory (remove this and the argument)
    yd[0].download("/Users/Brian/Desktop/Downloaded Music")
   
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))