# Import the required packages for the program
from pytube import YouTube 
import PySimpleGUI as sg
import os
import time

# Creating App object
class music_download:
    # Constructing object
    def __init__(self):
        sg.theme('DarkPurple1')

        # Main Window Layout
        main_layout = [
            # Row 1
            [sg.Text('Download Youtube:', size=(17, 0),
                     font='Consolas', key='-text-')],
            # Row 2
            [sg.Text('Link:', size=(6, 0), font='Consolas', key='-link-'),
             sg.Input('', size=(30, 1), font='Consolas', key='-box-')],
            # Row 3
            [sg.Radio('Convert to MP3', "RADIO1", default=True, key='-mp3-'),
             sg.Radio('Convert to MP4', "RADIO1", key='-mp4-')],
            # Row 4
            [sg.Button('Download', size=(10, 1),
                       font='Consolas', key='-download-')]
        ]

        # Main Window
        self.main_window = sg.Window('Music Downloader').Layout(main_layout)
        # Timeout
        self.main_window.read(timeout=1)
        # File auxiliars
        self.file = ''
        self.new_file = ''

    # Method to download songs
    def downloading(self):
        while True:
            try:
                yt = YouTube(self.values['-box-']);
                audio = yt.streams.filter(only_audio=True)[0]
                self.file = audio.download('musics')
                break
            except:
                sg.popup('Please, enter a valid link!')
                break
              
    # Method to convert to .mp3 extension
    def convert_mp3(self):
        base, extension = os.path.splitext(self.file)
        extension = '.mp3'
        self.new_file = base + extension
        os.rename(self.file, self.new_file)

        # Method to convert to .mp4 extension
    def convert_mp4(self):
        base, extension = os.path.splitext(self.file)
        extension = '.mp4'
        self.new_file = base + extension
        os.rename(self.file, self.new_file)

    # Method to run the app
    def running(self):
        self.event, self.values = self.main_window.Read()
        if self.event in (None, sg.WIN_CLOSED):  # Closing app
            exit(0)
        if self.event in ('-download-'):
            music_download.downloading(self)
            try:
                music_download.convert_mp3(self) if self.values['-mp3-'] == True else music_download.convert_mp4(self)
                sg.popup('Download succesfully completed!!')
            except:
               pass
        self.main_window.Close()

# Running program
while True:
    m_d = music_download()
    m_d.running()
