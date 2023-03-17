import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from pytube import YouTube

root = tk.Tk()
root.geometry("400x200")
root.resizable(False, False)
root.iconbitmap("C:/Users/hp/Desktop/python/tkinter stuff/yt-icon.ico")
root.title("Youtube Downloader")

tk.Label(root, text="Hello :)\nWelcome to Youtube Downloader.\n").pack()

url = tk.StringVar()

# Link frame
link = ttk.Frame(root)
link.pack(padx=10, pady=10, fill='x', expand=True)

# Link
link_label = ttk.Label(link, text="Enter the Youtube link:\n")
link_label.pack(fill='x', expand=True)

link_entry = ttk.Entry(link, textvariable=url)
link_entry.pack(fill='x', expand=True)
link_entry.focus()


# download button
def download_video_clicked():
    print("Welcome to Youtube Downloader.")
    showinfo(
        title='Information',
        message='Download has began!'
    )
    yt = YouTube(f"{url}")
    stream = yt.streams.get_by_itag(22)
    size = round(stream.filesize / 10 ** 6, 2)

    print(f"Downloading {yt.title}, \n Length: {yt.length} seconds, \n Size: {size} MBs")


download_icon = tk.PhotoImage(file="C:/Users/hp/Desktop/python/tkinter stuff/download icon.png")

download_button = ttk.Button(
    root,
    image=download_icon,
    text='Download',
    compound=tk.LEFT,
    command=download_video_clicked
)

download_button.pack(ipadx=5, ipady=5, expand=True)

# Exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True,
    side="left"
)

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()

