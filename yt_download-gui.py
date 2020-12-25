import tkinter as tk 
from tkinter import *
from pytube import YouTube
from pytube import *
from tkinter import messagebox, filedialog 
 
def Widgets(): 
    link_label = Label(root,  
                       text = "YouTube link: ", 
                       bg = "#DABB24",
                       font = (6)) 
    link_label.grid(row = 1, 
                    column = 0, 
                    pady = 10, 
                    padx = 10,
                    ipadx = 2,
                    ipady = 2) 
   
    link_text = Entry(root, 
                          width = 55,
                          textvariable = video_link) 
    link_text.grid(row = 1,  
                       column = 1, 
                       pady = 10, 
                       padx = 10,
                       ipadx = 4,
                       ipady = 4,
                       columnspan = 2) 
   
    destination_label = Label(root,  
                              text = "Destination: ", 
                              bg = "#DABB24",
                              font = (6)) 
    destination_label.grid(row = 2, 
                           column = 0, 
                           pady = 5, 
                           padx = 5,
                           ipadx = 2,
                           ipady = 2) 
   
    destinationText = Entry(root, 
                                 width = 45, 
                                 textvariable = download_path) 
    destinationText.grid(row = 2,  
                        column = 1, 
                        pady = 15, 
                        padx = 15,
                        ipadx = 4,
                        ipady = 4,) 
   
    browse_B = Button(root,  
                      text = "Browse", 
                      command = Browse, 
                      width = 12, 
                      bg = "grey",
                      font = 1) 
    browse_B.grid(row = 2, 
                  column = 2, 
                  pady = 2, 
                  padx = 2,
                  ipadx = 2,
                  ipady = 2) 
   
    Download_B = Button(root, 
                        text = "Download",  
                        command = Download,  
                        width = 20, 
                        font = 2,
                        bg = "grey") 
    Download_B.grid(row = 3, 
                    column = 1, 
                    pady = 12, 
                    padx = 3)

def Browse():
    # initialdir 
    # argument is optional retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_directory = filedialog.askdirectory(initialdir = "YOUR DIRECTORY PATH") 
    # Displaying the directory in the entry box
    download_path.set(download_directory) 

def Download(): 
    Youtube_link = video_link.get() 
      
    # select the optimal location for saving file's 
    download_folder = download_path.get() 
    getVideo = YouTube(Youtube_link) 
    videoStream = getVideo.streams.first() 
    videoStream.download(download_folder) 

    messagebox.showinfo("SUCCESSFULLY",  
                        "DOWNLOADED AND SAVED IN\n" 
                        + download_folder) 

root = tk.Tk() 
   
root.geometry("625x325") 
root.resizable(False, False) 
root.title("YouTube Video Downloader") 
root.config(background="crimson") 
   
# Creating the tkinter Variables 
video_link = StringVar() 
download_path = StringVar() 

Widgets() 

root.mainloop() 
