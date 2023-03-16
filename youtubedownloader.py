import re
from pytube import YouTube


def download_video():
    print("Welcome to Youtube Downloader: \n Type Q to exit.")
    while True:
        link = input(">> Copy paste YT link: ")
        if link.lower() == "q":
            break

        # # Validate input link using regex
        # if not re.match(r'^https?:\/\/(www\.)?youtube\.com\/watch\?v=[\w-]{11}$', link):
        #     raise re.error("Invalid YouTube link. Please enter a valid YouTube video link.")

        yt = YouTube(link)
        stream = yt.streams.get_by_itag(22)
        size = round(stream.filesize / 10 ** 6, 2)

        print(f"Downloading {yt.title}, \n Length: {yt.length} seconds, \n Size: {size}MBs")

        stream = yt.streams.get_by_itag(22)
        stream.download()
        print("Download Complete :)")

    print("Exiting program.")


download_video()


# https://youtu.be/uAOR6ib95kQ


# raise RegexMatchError
# pytube.exceptions.RegexMatchError

# https://youtu.be/jinBlY9BpJ0

def on_progress(progress):
    # This function will be called periodically with progress information
    print("Upload %d%% complete" % progress)


# Build the resource object for the new video
video = YouTubeVideo(title='My Video', file_path='my_video.mp4')

# Upload the video, passing the on_progress function as a callback
video.upload(on_progress_callback=on_progress)
