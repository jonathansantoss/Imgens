from PIL import Image

imagemLenna = Image.open('Lenna.png')
imagemLennaCinza = imagemLenna.convert('L')
imagemLennaCinza.show()

img = Image.new('L', (imagemLennaCinza.size[0] , imagemLennaCinza.size[1]), 'BLACK')

h , w = imagemLennaCinza.size

for i in range(h):
    for j in range(w):
        pixel = imagemLennaCinza.getpixel((i, j))
        img.putpixel((i, j), int(pixel + (pixel * 0.10)))
        
img.show()
img.save('img10.png')