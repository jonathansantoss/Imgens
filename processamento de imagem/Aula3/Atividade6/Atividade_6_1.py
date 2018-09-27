from PIL import Image
import math

imglenna = Image.open('Lenna.png')
imgLennaCinza = imglenna.convert('L')
imgLennaCinza.show()


img = Image.new('L', (1000, 1000) , 'BLACK')
img2 = Image.new('L', (imgLennaCinza.size[0], imgLennaCinza.size[1]) , 'BLACK')

h = imgLennaCinza.size[0]
w = imgLennaCinza.size[1]   

for linha in range(h):
    for coluna in range(w):
        r,g,b = imglenna.getpixel((linha, coluna))
        pixel = int((r+g+b)/3)
        img2.putpixel((int(coluna/2) , int(linha/2)), pixel)
        
img2.show()
        
for linha in range(h):
    for coluna in range(w):
        pixel = img2.getpixel((linha, coluna))
        Y = int(coluna * math.sin(45) + linha * math.cos(45))
        X = int((coluna * math.cos(45) - linha * math.sin(45)))
        if X < 0:
            X = X *(-1)
        img.putpixel((int(X/2) + 100, int(Y/2) + 100), pixel)
        
img.show()
img.save('img1.png')
