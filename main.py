import tkinter
import customtkinter
# from pytube import YouTube
from pytubefix import YouTube

def startDownload():
    try:
        ytLink= link.get()
        # print(ytLink)
        ytObject= YouTube(ytLink, on_progress_callback=on_progress)
        # print(ytObject)
        video= ytObject.streams.get_lowest_resolution()
        # ytObject.streams <-- give back all the video resulutions incase i want to choose one later on

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except Exception as e:
        finishLabel.configure(text="Download Error", text_color="red")
        print(f"Error: {e}")  # Print out the actual error
    
def on_progress(stream, chunk, bytes_remaning):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaning
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    print(percentage_of_completion)    

    # Update progress bar
    progessBar.set(float(percentage_of_completion) / 100)

# System settings
customtkinter.set_appearance_mode("dark") # Set dark theme
customtkinter.set_default_color_theme("blue") # Optional: change the color theme

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI elements
title = customtkinter.CTkLabel(app, text="insert a youtube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finish downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progessBar = customtkinter.CTkProgressBar(app, width=400)
progessBar.set(0)
progessBar.pack(padx=10, pady=10)
# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10) 

# Run app
app.mainloop()