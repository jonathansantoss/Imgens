# Ideia é pegar a imagem  deixa com 513X513 em volta com os valores 0 e depois passar filtro

from PIL import Image

imglenna = Image.open('Lenna.png')
imglennaCinza = imglenna.convert('L')
imglennaCinza.show()

img = Image.new('L', (imglennaCinza.size[0], imglennaCinza.size[1]), 'BLACK')

h = imglennaCinza.size[0]
w = imglennaCinza.size[1]

mascara = ([ [1, 1, 1], [1, 1, 1], [1, 1, 1]])

for i in range(h):
    for j in range(w):
        
        for linha in range(3):
            for coluna in range(3):
                X1 = imglenna.getpixel((linha, coluna))
