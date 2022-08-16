import PySimpleGUI as sg
from pytube import YouTube, Playlist

def executar_download(link, path, pl):
    if pl == True:
        playlist = Playlist(link)
        for url in playlist:
            video = YouTube(url)
            video.streams.get_audio_only().download(output_path=path)
    else:
        video = YouTube(link)
        video.streams.get_audio_only().download(output_path=path)

layout = [
    [sg.Text('Informe o link do YouTube  '), sg.InputText(), sg.Checkbox('Playlist', default=False, key='pl')],
    [sg.Text('Informe a pasta para Salvar'), sg.InputText(), sg.FolderBrowse()],
    [sg.Button('Baixar'), sg.Button('Cancelar')]
         ]
janela = sg.Window("ConversorMP3 Youtube", layout)

while True:
    event, values = janela.Read()
    if event == 'Cancelar' or event == sg.WIN_CLOSED:
        break
    elif event == 'Baixar':
        executar_download(values[0], values[1], values['pl'])
        sg.popup_ok("Download concluido com sucesso!")
janela.Close()