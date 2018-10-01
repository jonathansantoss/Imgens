from PIL import Image

imagem = Image.open('X255.png')
imagemCinza = imagem.convert('L')
imagemCinza.show()

img = Image.new('L', (512, 512), 'BLACK')

h , w = imagemCinza.size

for i in range(h):
    for j in range(w):
        pixel = imagemCinza.getpixel((i, j))
        img.putpixel((int(i * 2), int(j * 2)), pixel)

img.show()
