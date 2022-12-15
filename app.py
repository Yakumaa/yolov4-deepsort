# from fileinput import filename
import tkinter as tk
from tkinter import filedialog, Text
import os

root= tk.Tk()
videos = []

def addVideo():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                    filetypes=(("all files", "*.*"), ("executables", "*.exe")))
    videos.append(filename)
    print(filename)
    for video in videos:
        label = tk.Label(frame, text=video, bg= "gray")
        label.pack()

def startCount():
    for video in videos:
        os.startfile(video)

canvas = tk.Canvas(root, height= 700, width= 700, bg="black")
canvas.pack()

frame = tk.Frame(root, bg= "white")
frame.place(relwidth = 0.8, relheight= 0.8, relx= 0.1, rely= 0.1)

openFile = tk.Button(root, text="Open File", padx= 10,
                     pady= 5, fg= "white", bg= "black", command=addVideo)
openFile.pack()

startCount = tk.Button(root, text="Start", padx= 10, pady= 5, fg= "white", bg= "black", command= startCount)
startCount.pack()

root.mainloop()