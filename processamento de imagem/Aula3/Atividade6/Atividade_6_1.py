from PIL import Image
import math

imglenna = Image.open('Lenna.png')
imgLennaCinza = imglenna.convert('L')
imgLennaCinza.show()

img = Image.new('L', (1000, 1000) , 'BLACK')

h = imgLennaCinza.size[0]
w = imgLennaCinza.size[1]   
        
for linha in range(h):
    for coluna in range(w):
        pixel = imgLennaCinza.getpixel((linha, coluna))
        Y = int(coluna * math.sin(45) + linha * math.cos(45))
        X = int((coluna * math.cos(45) - linha * math.sin(45)))
        if X < 0:
            X = X *(-1)
        img.putpixel((int(X/2) + 100, int(Y/2) + 100), pixel)
        
img.show()
img.save('img1.png')
