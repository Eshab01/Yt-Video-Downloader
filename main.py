import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

# Download function
def download_video():
    url = url_entry.get()
    folder = folder_path.get()
    
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    
    if not folder:
        messagebox.showerror("Error", "Please select a download folder")
        return
    
    try:
        ydl_opts = {'outtmpl': f'{folder}/%(title)s.%(ext)s'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

# Folder picker
def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

# UI Setup
app = tk.Tk()
app.title("YouTube Video Downloader")
app.geometry("500x300")
app.resizable(False, False)

# URL Entry
tk.Label(app, text="Enter YouTube URL:").pack(pady=5)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

# Folder Select
tk.Label(app, text="Select Download Folder:").pack(pady=5)
folder_path = tk.StringVar()
folder_button = tk.Button(app, text="Choose Folder", command=select_folder)
folder_button.pack(pady=5)

folder_display = tk.Entry(app, textvariable=folder_path, width=50, state='readonly')
folder_display.pack(pady=5)

# Download Button
download_button = tk.Button(app, text="Download Video", command=download_video)
download_button.pack(pady=20)

app.mainloop()
