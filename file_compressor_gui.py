import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress:", tooltip="Choose files to compress")
input1 = sg.Input(tooltip="Choose files to compress")
choose_button1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select destination folder:", tooltip="Choose target folder")
input2 = sg.Input(tooltip="Choose target folder")
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor by TB",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button]])

window.read()
window.close()