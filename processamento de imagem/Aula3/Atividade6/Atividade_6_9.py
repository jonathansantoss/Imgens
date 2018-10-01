from PIL import Image

imagemLenna = Image.open('img4.png')
imagemLennaCinza = imagemLenna.convert('L')
imagemLennaCinza.show()

img = Image.new('L', (imagemLennaCinza.size[0] , imagemLennaCinza.size[1]), 'BLACK')

h , w = imagemLennaCinza.size


def media(x , y):
    pixel1 = imagemLennaCinza.getpixel((x, y + 1))
    pixel2 = imagemLennaCinza.getpixel((x, y - 1))
    pixel3 = imagemLennaCinza.getpixel((x + 1 , y))
    pixel4 = imagemLennaCinza.getpixel((x - 1, y))
    pixel5 = imagemLennaCinza.getpixel((x + 1, y + 1))
    pixel6 = imagemLennaCinza.getpixel((x - 1, y + 1))
    pixel7 = imagemLennaCinza.getpixel((x + 1, y - 1))
    pixel8 = imagemLennaCinza.getpixel((x - 1, y - 1))
    pixel9 = imagemLennaCinza.getpixel((x, y))
    
    m = int((pixel1 + pixel2 + pixel3 + pixel4 + pixel5 + pixel6 + pixel7 + pixel8 + pixel9) / 9)
    
    return m


for i in range(1 , int(h - 1)):
    for j in range(1, int(w - 1)):
        pixel = media(i, j)
        img.putpixel((i, j), int(pixel))
        
img.show()
img.save('img9.png')
