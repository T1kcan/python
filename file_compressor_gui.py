import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress:", tooltip="Choose files to compress")
input1 = sg.Input(tooltip="Choose files to compress")
choose_button1 = sg.FileBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:", tooltip="Choose target folder")
input2 = sg.Input(tooltip="Choose target folder")
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("File Compressor by TB",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed!")

window.close()