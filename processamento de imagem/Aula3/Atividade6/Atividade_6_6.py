from PIL import Image

imagemlenna = Image.open('Lenna.png')
imagemLennaCinza = imagemlenna.convert('L')

img = Image.new('L', (imagemLennaCinza.size[0], imagemLennaCinza.size[1]), 'BLACK')

h , w = imagemLennaCinza.size

for i in range(h):
    for j in range(w):
         pixel = imagemLennaCinza.getpixel((i, j))
         img.putpixel((i , j), 255 - pixel)
         
img.show()
img.save('img6.png')
