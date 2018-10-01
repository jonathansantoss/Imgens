from PIL import Image

imagem = Image.open('Lenna.png')
imagemCinza = imagem.convert('L')
imagemCinza.show()

h , w = imagemCinza.size

img = Image.new('L', (h, w), 'BLACK')

for i in range(h):
    for j in range(w):
        pixel = imagemCinza.getpixel((i, j))
        img.putpixel((i , j), int( pixel + (pixel * 0.10)) )

img.show()