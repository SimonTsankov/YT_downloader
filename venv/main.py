from pytube import YouTube
import PySimpleGUI as sg
import os
video_list=[]

URL_list_column=[
    [
        sg.Text("Urls"),
        sg.In(size=(25, 1), enable_events=True, key="-INPUT-")
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-LIST-"
        )
    ],
]
image_viewer_column = [
    [sg.Checkbox(
        'mp4 720p',
        key='mp4_720',
        enable_events=True)
    ],
    [sg.Checkbox(
        'mp4 480p',
        key='mp4_480',
        enable_events=False)
    ],
    [sg.Checkbox(
        'mp3',
        key='mp3',
        enable_events=False)
    ],

    [sg.Text("Path where to save files to:")],
    [sg.In(size=(25, 1), key="-PATH-")],
    [sg.Button("ADD URL")],
    [sg.Button("DOWNLOAD")],
    [sg.Button("Clear")],
]

layout = [
    [
        sg.Column(URL_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("YtDownloader Viewer", layout)


while True:
    event, values = window.read()
    if values["-PATH-"] =="":
        window["-PATH-"].update("D:\Pictures\Camera Roll")
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event=="ADD URL":
        video_list.append(values['-INPUT-'])
        window['-INPUT-'].update("")
        window['-LIST-'].update(video_list)
    if event=="DOWNLOAD":
       try:
            path=values['-PATH-']
            for x, video in enumerate(video_list):
                v720 = YouTube(video)
                v480 = YouTube(video)
                vmp3 = YouTube(video)

                if values['mp4_720']==True:
                    stream = v720.streams.get_by_itag(22)
                    print(f"Downloading video {x}...")
                    out_file=stream.download(path)
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '_720p.mp4'
                    os.rename(out_file, new_file)
                    print("Done")
                if values['mp4_480']==True:
                   stream_mp4_480 = v480.streams.get_by_itag(135)
                   print(f"Downloading video {x}...")
                   out_file=stream_mp4_480.download(path)
                   base, ext = os.path.splitext(out_file)
                   new_file = base + '_480p.mp4'
                   os.rename(out_file, new_file)
                   print("Done")
                if values['mp3']==True:
                    stream_mp3 = vmp3.streams.get_by_itag(140)
                    print(f"Downloading video {x}...")
                    out_file = stream_mp3.download(path)
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '_audio.mp3'
                    os.rename(out_file, new_file)

                    print("Done")
       except:
           window['-LIST-'].update(["Wrong url or path"])
    if event=="Clear":
        video_list.clear()
        window['-LIST-'].update(video_list)

