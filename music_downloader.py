# Import the required packages for the program
import pytube
import PySimpleGUI as psg
import os

# Creating App object
class music_download:
    # Constructing object
    def __init__(self):
        psg.theme('DarkPurple1')
        # Layout
        layout = [
            # Row 1
            [psg.Text('Download Youtube:', size=(17, 0),
                     font='Consolas', key='-text-')],
            # Row 2
            [psg.Text('Link:', size=(6, 0), font='Consolas', key='-link-'),
             psg.Input('', size=(30, 1), font='Consolas', key='-box-')],
            # Row 3
            [psg.Radio('Convert to MP3', "RADIO1", default=True, key='-mp3-'),
             psg.Radio('Convert to MP4', "RADIO1", key='-mp4-')],
            # Row 4
            [psg.Button('Download', size=(10, 1),
                       font='Consolas', key='-download-')]
        ]
        # Window
        self.window = psg.Window('Music Downloader').Layout(layout)
        # Timeout
        self.window.read(timeout=1)
        # File auxiliars
        self.file = ''
        self.new_file = ''

    # Method to download songs
    def downloading(self):
        while True:
            if self.values['-box-'] != '':
                audio = pytube.YouTube(
                    self.values['-box-']).streams.filter(only_audio=True)[0]
                self.file = audio.download('musics')
                break
            else:
                psg.popup('Please, enter a link!')

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
        self.event, self.values = self.window.Read()
        if self.event in (None, psg.WIN_CLOSED):  # Closing app
            exit(0)
        if self.event in ('-download-'):
            music_download.downloading(self)
            music_download.convert_mp3(
                self) if self.values['-mp3-'] == True else music_download.convert_mp4(self)
            psg.popup('Download succesfully completed!!')
        self.window.Close()


# Running program
while True:
    m_d = music_download()
    m_d.running()
