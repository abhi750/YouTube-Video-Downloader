import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pytube import YouTube
from tkinter import messagebox
from PIL import ImageTk,Image

folderName = ""
fileSizeInBytes = 0
MaxFileInBytes = 0

'''
Function:
 To check video is downloadable or not
 To get video File title and print it
'''
def checkUrl():
    global videoName, videoSize,Name
    video = youtubeEntry.get()  # VIDEO = ENTERED URL
    try:
        if len(video) > 1:
            yt = YouTube(video)
            videoName = yt.title
            Name = videoName
            videoFileName.config(text=Name)
        else:
            videoFileName.config(text="Server Error.., Please try another video ")
    except:
        videoFileName.config(text="Server Error.., Please try another video ")

'''
Function:
To get memory location where downloaded file has to be store
'''
def openDirectry():
    global FolderName
    FolderName = filedialog.askdirectory()
    if len(FolderName) > 1:
        fileLocationLabelError.config(text=FolderName, fg="green")
    else:
        fileLocationLabelError.config(text="please choose folder", fg="red")

'''
Function:
 fetch user entered URL
 fetch user video quality choice
 it shows message of downloading video file
 take user specified location to store video file 
 and download and save that file to specified location 
'''

def downloadFile():

    global selectVideo
    messagebox.showinfo(title="YouTube Downloader", message="Please wait.. Video is Downloading...")   # MESSAGEBOX SHOWING DOWNLOADING MESSAGE
    choice = youtubeChoices.get()     # FETCHING VIDEO QUALITY SELECTED BY USER
    video = youtubeEntry.get()  # VIDEO = ENTERED URL
    if len(video) > 1:
        youtubeEntryError.config(text="")
        yt = YouTube(video)
        print(yt.title, "at", FolderName)

        if choice == downloadChoices[0]:    # FOR HIGH QUALITY
            print("video is downloading....")
            loadingLabel.config(text="video file downloading...")
            selectVideo = yt.streams.filter(progressive=True).order_by('resolution').desc().first()

        elif choice == downloadChoices[1]:    # FOR MEDIUM QUALITY
            print("144p video is downloading....")
            loadingLabel.config(text="video file downloading...")
            selectVideo = yt.streams.filter(progressive=True, file_extension="mp4").last()

        elif choice == downloadChoices[2]:      # FOR LOW QUALITY
            print("3gp video is downloading....")
            loadingLabel.config(text="video file downloading...")
            selectVideo = yt.streams.filter(file_extension="3gp").first()

        elif choice == downloadChoices[3]:       # FOR AUDIO FILE ONLY
            print("audio file is downloading....")
            loadingLabel.config(text="Music file downloading...")
            selectVideo = yt.streams.filter(only_audio=True).first()



        selectVideo.download(FolderName)
        print("Download on : {}".format(FolderName))
        complete()

        messagebox.showwarning(title="YouTube Downloader", message="Video Downloaded..")

    else:
        youtubeEntryError.config(text="please paste youtube link", fg="red")


def complete():
    loadingLabel.config(text="Download complete")



def about():
    win1 = tk.Toplevel()
    win1.title("About")
    win1.resizable(0, 0)
    win1.iconbitmap(r'C:\Users\jarvis\PycharmProjects\final_project\youicon.ico')
    var = tk.StringVar()
    my_img = ImageTk.PhotoImage(Image.open("aboutimg.png"))
    my_label = tk.Label(win1, image=my_img)
    my_label.grid(pady=(10,10))
    def closeWin1():
        win1.destroy()
    closeButton = tk.Button(win1, text="Home", width=10, command=closeWin1)
    closeButton.grid()
    win1.mainloop()
# DECLARING MAIN FRAME FOR AN APP

root = tk.Tk()
root.title("Youtube Video Downloader")  # TITLE FOR APP
root.resizable(0, 0)

root.iconbitmap(r'C:\Users\jarvis\PycharmProjects\final_project\youicon.ico')
root.grid_columnconfigure(0, weight=1)

# FIRST HEADING

youtubeLinkLabel = tk.Label(root, text="Please paste Youtube link here..", fg="blue", font=("Times New Roman", 30))
youtubeLinkLabel.grid(padx=(10, 10))

# URL ENTRY SPACE FRO USER

youtubeEntryVar = tk.StringVar()
youtubeEntry = ttk.Entry(root, width=50, textvariable=youtubeEntryVar)
youtubeEntry.grid(pady=(10, 10))

# check button to check youtube URL

checkButton = tk.Button(root, text="check", width=10, bg="green", command=checkUrl)
checkButton.grid(pady=(10, 40))

# space to print youtube file name

videoFileName = tk.Label(root, text="", font=("Agency FB", 20))
videoFileName.grid(pady=(10, 10))

# ERROR SPACE FOR PROVIDING URL OF VIDEO

youtubeEntryError = tk.Label(root, fg="red", text="", font=("Agency FB", 30))
youtubeEntryError.grid(pady=(0, 10))

# LABEL FOR ASKING WHERE TO SAVE VIDEO FILE

SaveLabel = tk.Label(root, text="where to download file?", fg="blue", font=("Agency FB", 20, "bold"))
SaveLabel.grid()

# OPENING DIRECTORY FOR USER TO CHOOSE SPACE

SaveEntry = tk.Button(root, width=20, bg="green", fg="white", text="Choose Folder", font=("Arial", 15),
                      command=openDirectry)
SaveEntry.grid()

# ERROR FOR NOT CHOOSING PROPER PLACE TO SAVE VIDEO FILE

fileLocationLabelError = tk.Label(root, text="", font=("Agency FB", 20))
fileLocationLabelError.grid(pady=(0, 0))

# CHOOSING VIDEO QUALITY THAT USER WANT TO SAVE

youtubeChooseLabel = tk.Label(root, text="please choose what to download:", font=("Agency FB", 20))
youtubeChooseLabel.grid()


# CREATING COMBO BOX FOR AVAILABLE OPTION

downloadChoices = ["Best Quality",
                   "Medium Quality",
                   "Low Quality",
                   "Audio file (mp3)"]
youtubeChoices = ttk.Combobox(root, values=downloadChoices)
youtubeChoices.grid()
# CREATING DOWNLOAD BUTTON

downloadButton = tk.Button(root, text="Download", width=15, bg="green", command=downloadFile)
downloadButton.grid()

infoButton = tk.Button(root, text="About", width=10, bg="green", command=about)
infoButton.grid()

# DIRECTOR OF AN APP

loadingLabel = ttk.Label(root, text="App developed by Abhishek!!!!", font=("Arial", 10))
loadingLabel.grid()

root.mainloop()
