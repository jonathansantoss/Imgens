from PIL import Image
import math

imglenna = Image.open('Lenna.png')
imgLennaCinza = imglenna.convert('L')
imgLennaCinza.show()

h, w = imgLennaCinza.size

img = Image.new('L', (1000, 1000) , 'BLACK')
img2 = Image.new('L', (750, 750) , 'BLACK')  

for linha in range(h):
    for coluna in range(w):
        pixel = imgLennaCinza.getpixel((linha, coluna))
        img2.putpixel((int(linha) + 25   , int(coluna) + 25), pixel)
        
img2.show()
        
for linha in range(h):
    for coluna in range(w):
        pixel = img2.getpixel((linha, coluna))

        cos = math.cos(math.pi / 2)
        sin = math.sin(math.pi / 2)
        
        Y = int(linha * sin + coluna * cos)
        X = int((linha * cos - coluna * sin))
        
        if X < 0:
            X = X + img.size[0]
            img.putpixel((int(X / 2) + 100, int(Y / 2) + 100), pixel)
            
img.show()
img.save('img2.png')
