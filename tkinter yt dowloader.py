import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from pytube import YouTube

root = tk.Tk()
root.geometry("400x200")
root.resizable(False, False)
root.title("Youtube Downloader")

tk.Label(root, text="Hello :)\nWelcome to Youtube Downloader.\n").pack()
url = str(tk.StringVar())

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
def download_clicked():
    yt = YouTube(link_entry.get())
    stream = yt.streams.get_by_itag(22)
    size = round(stream.filesize / 10 ** 6, 2)
    showinfo(
        title='Information',
        # message='Downloading',
        message=f'Downloading {yt.title},\nLength: {yt.length} seconds,\nSize: {size} MBs.\nDownload has began!'
    )
    try:
        stream.download()
        showinfo(
            title='Download Status',
            message="Download Complete!"
        )

    except:
        showinfo(
            title='Download Status',
            message="Download Incomplete!"
        )


download_button = ttk.Button( root, text='Download', compound=tk.LEFT, command=download_clicked)

download_button.pack(ipadx=5, ipady=5, expand=True)

# Exit button
exit_button = ttk.Button(root, text='Exit', command=lambda: root.quit())

exit_button.pack( ipadx=5, ipady=5, expand=True)

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()
