from pytube import YouTube

def download_video():
    print("Welcome to Youtube Downloader.\n Type Q to exit.")
    while True:
        link = input(">> Copy paste YT link: ")
        if link.lower() == "q":
            break

        yt = YouTube(f'{link}')
        print(link, yt)
        stream = yt.streams.get_by_itag(22)
        size = round(stream.filesize / 10 ** 6, 2)

        print(f"Downloading {yt.title}, \n Length: {yt.length} seconds, \n Size: {size}MBs")

        stream.download()
        print("Download Complete :)")

    print("Exiting program.")


download_video()