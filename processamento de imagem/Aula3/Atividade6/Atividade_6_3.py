from PIL import Image

imagemLenna = Image.open('Lenna.png')
imagemLennaCinza = imagemLenna.convert('L')

img = Image.new('L', (imagemLenna.size[0], imagemLenna.size[1]), 'BLACK')

h, w = imagemLennaCinza.size

for i in range(h):
    for j in range(w):
        
        pixel = imagemLennaCinza.getpixel( (i , w - (j + 1) ) )
        img.putpixel((i, j), pixel)
        
img.show()
img.save('img3.png')
