from PIL import Image

imagemLenna = Image.open('img4.png')
imagemLennaCinza = imagemLenna.convert('L')
imagemLennaCinza.show()

img = Image.new('L', (imagemLennaCinza.size[0] , imagemLennaCinza.size[1]), 'BLACK')

h , w = imagemLennaCinza.size


def mediana(x , y):
    pixel1 = imagemLennaCinza.getpixel((x, y + 1))
    pixel2 = imagemLennaCinza.getpixel((x, y - 1))
    pixel3 = imagemLennaCinza.getpixel((x + 1 , y))
    pixel4 = imagemLennaCinza.getpixel((x - 1, y))
    pixel5 = imagemLennaCinza.getpixel((x + 1, y + 1))
    pixel6 = imagemLennaCinza.getpixel((x - 1, y + 1))
    pixel7 = imagemLennaCinza.getpixel((x + 1, y - 1))
    pixel8 = imagemLennaCinza.getpixel((x - 1, y - 1))
    pixel9 = imagemLennaCinza.getpixel((x, y))
    
    listaPixel = []
    listaPixel.insert(0, pixel1)
    listaPixel.insert(1, pixel2)
    listaPixel.insert(2, pixel3)
    listaPixel.insert(3, pixel4)
    listaPixel.insert(4, pixel5)
    listaPixel.insert(5, pixel6)
    listaPixel.insert(6, pixel7)
    listaPixel.insert(7, pixel8)
    listaPixel.insert(8, pixel9)
    listaPixel.sort()
    
    posicao = len(listaPixel) / 2
    m = listaPixel[int(posicao)]
    
    return m

for i in range(1 , int(h - 1)):
    for j in range(1, int(w - 1)):
        pixel = mediana(i, j)
        img.putpixel((i, j), int(pixel))
        
img.show()
img.save('img5.png')

