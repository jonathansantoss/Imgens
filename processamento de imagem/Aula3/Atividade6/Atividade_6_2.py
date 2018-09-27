from PIL import Image
import math

imglenna = Image.open('Lenna.png')
imgLennaCinza = imglenna.convert('L')
imgLennaCinza.show()

img = Image.new('L', (3000, 3000) , 'BLACK')

h = imgLennaCinza.size[0]
w = imgLennaCinza.size[1]   

for linha in range(h):
    for coluna in range(w):
        pixel = imgLennaCinza.getpixel((linha, coluna))
        Y = int( (coluna * math.sin(90) + linha* math.cos(90)))
        X = int((coluna * math.cos(90) -  linha* math.sin(90))) # O valor vai est� negativo
        
        X1 = 0
        if X == 0:
            X1 = 999
        else:
            X1 = 999 + X
        img.putpixel((int(X1 / 2) + 50, int(Y / 2) + 320), pixel)
        
img.show()
img.save('img2.png')