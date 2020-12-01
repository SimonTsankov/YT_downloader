from pytube import YouTube
import PySimpleGUI as sg

video_list=[]

file_list_column=[
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
    [sg.Text("Path where to save files to:")],
    [sg.In(size=(25, 1), key="-PATH-") ],
    [sg.Button("ADD URL")],
    [sg.Button("DOWNLOAD")],
    [sg.Button("Clear")],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)


while True:
    event, values = window.read()
    if values["-PATH-"]=="":
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
                v = YouTube(video)
                stream = v.streams.get_by_itag(22)
                print("Downloading video ",x)
                stream.download(path)
                print("Done")
        except:
            window['-LIST-'].update(["Wrong url or path"])
    if event=="Clear":
        video_list.clear()
        window['-LIST-'].update(video_list)

