from pytube import *
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *
from threading import *

# total size container
file_size = 0

# updating percentage on start Button

# file_handle=None
def progress(stream=None,chunk=None,remaining=None):
    file_downloaded = (file_size-remaining)
    per = (file_downloaded/file_size) * 100
    dBtn.config(text="{:00.0f}% Downloaded".format(per))


def startDownload():
    global file_size
    try:
        url = urlField.get()
        # change button text
        dBtn.config(text="Please Wait...")
        dBtn.config(state=DISABLED)
        path_to_save_video = "E:\\Download"
        # path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return
        # creating youtube object with url
        ob = YouTube(url, on_progress_callback=progress)

        # strms = ob.streams.all()

        # for s in strms:
        # print(s)

        strm = ob.streams.get_highest_resolution()
        file_size = strm.filesize
        vTitle.config(text=strm.title)
        vTitle.pack(side=TOP)
        # print(strm)
        # print(strm.filesize)
        # print(strm.title)
        # print(ob.description)

        # downloading the video
        strm.download(path_to_save_video)
        # print("Download Done.")
        dBtn.config(text="Start Download")
        dBtn.config(state=NORMAL)
        showinfo("Download Done","Downloaded Successfully")
        urlField.delete(0,END)
        vTitle.pack_forget()

    except Exception as e:
        print(e)
        print("Error")

def startDownloadThread():
    thread = Thread(target=startDownload)
    thread.start()


# Starting GUI Building


root = Tk()

# setting the title
root.title("My Youtube Downloader")

# set the icon

root.iconbitmap('icon.ico')

root.geometry("600x450")

# heading icon
file = PhotoImage(file='img.png')
headingIcon = Label(root, image=file)
headingIcon.pack(side=TOP,pady=10)

# url textfield

urlField = Entry(root,font=("verdana",18),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10,pady=20)

# download button
dBtn = Button(root, text="Start Download",font=("verdana",18),relief="ridge",command=startDownloadThread)
dBtn.pack(side=TOP,pady=20)


# video Title

Title = Label(root, text = "Title", font=("verdana",18))
Title.pack(side=TOP)

vTitle = Label(root, text="Video Title", font=("verdana",12))


root.mainloop()
