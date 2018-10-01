from PIL import Image

imagemLenna = Image.open('Lenna.png')
imagemLennaCinza = imagemLenna.convert('L')

h , w = imagemLennaCinza.size

img = Image.new('L', (h, w), 'BLACK')

for i in range(h):
    for j in range(w):
        pixel = int(imagemLennaCinza.getpixel((i, j)) / 2)
        img.putpixel((i,j) , pixel)

img.show()  
img.save('f6.png')  
