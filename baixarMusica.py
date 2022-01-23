from pytube import YouTube

#     -- Menu --
print('Olá bem vindo ao Youtube Video Dowloader')
link = input(print('Por favor insira o link do video/musica que deseja baixar'))

#     -- Qual formato o usuario deseja-- 
print('Otimo ! agora, em qual formato deseja baixar ? ')
print('1 - Musica')
opcaoFormato = input(print('2-  Video'))
opcaoQualidade = 0
        
numero = int(opcaoFormato)

# -- função para baixar video com qualidade baixa ou alta
def getNumeroQualidade():
        print('Qual qualidade deseja baixar ? ')
        print('1- baixa')
        opcaoQualidade = input(print('2- Alta'))
        numeroOpcaoQualidade = int(opcaoQualidade)
        if numeroOpcaoQualidade == 3:
            musicaLink = YouTube(link)
            stream = musicaLink.streams.get_lowest_resolution
            stream.download()
        elif numeroOpcaoQualidade == 4:
            musicaLink = YouTube(link)
            stream = musicaLink.streams.get_highest_resolution
            stream.download()
        pass

if numero == 1:
    musicaLink = YouTube(link)
    stream = musicaLink.streams.get_audio_only() 
    stream.download()
elif numero == 2:
    getNumeroQualidade()
pass


