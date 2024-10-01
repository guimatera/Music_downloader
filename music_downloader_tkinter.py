import os
from mutagen import File
from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
import glob
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

class MusicDownloadApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Music Downloader')
        self.root.geometry('800x200')
        self.pady = 5

        # Initialize radio button variable
        self.radio_var = tk.StringVar(value='mp3')

        # Main Frame
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Layout Widgets
        self.label = tk.Label(frame, text='Download YouTube:', font='Consolas')
        self.label.grid(row=0, column=0, padx=5, pady=self.pady, sticky='w')

        self.link_label = tk.Label(frame, text='Link:', font='Consolas')
        self.link_label.grid(row=1, column=0, padx=5, pady=self.pady, sticky='w')

        self.link_entry = tk.Entry(frame, width=60, font='Consolas')
        self.link_entry.grid(row=1, column=0, padx=100, pady=self.pady, sticky='w')

        self.mp3_radio = tk.Radiobutton(frame, text='Convert to MP3', value='mp3', variable=self.radio_var, font='Consolas')
        self.mp3_radio.grid(row=2, column=0, padx=5, pady=self.pady, sticky='w')

        self.mp4_radio = tk.Radiobutton(frame, text='Convert to MP4', value='mp4', variable=self.radio_var, font='Consolas')
        self.mp4_radio.grid(row=2, column=0, padx=200, pady=self.pady, sticky='w')

        self.download_button = tk.Button(frame, text='Download', command=self.download, font='Consolas')
        self.download_button.grid(row=3, column=0, padx=5, pady=self.pady)



    def download(self):
        link = self.link_entry.get()
        format = self.radio_var.get()
        try:
            yt = YouTube(link)
            if format == 'mp3':
                self.convert_mp3(yt)
            else:
                self.convert_mp4(yt)
            messagebox.showinfo('Success', 'Download successfully completed!')
        except Exception as e:
            messagebox.showerror('Error', e)

    def convert_mp3(self, yt):
        audio = yt.streams.filter(file_extension='mp4')
        file = audio.first().download('musics')
        base,extension = os.path.splitext(file)
        new_file = base + '.mp3'
        os.rename(file, new_file)
        print(new_file)

        #song = File(new_file)
        #song['artist'] = yt.author
        #song.save()


    def convert_mp4(self, yt):
        video = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        video.download('videos')

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicDownloadApp(root)
    root.mainloop()