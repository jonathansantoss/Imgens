from PIL import Image
import math

imglenna = Image.open('Lenna.png')
imgLennaCinza = imglenna.convert('L')
imgLennaCinza.show()

h, w = imgLennaCinza.size

img = Image.new('L', (1000, 1000) , 'BLACK')
img2 = Image.new('L', (int((w) * 1.5), int((h) * 1.5)) , 'BLACK')  

for linha in range(h):
    for coluna in range(w):
        pixel = imgLennaCinza.getpixel((coluna, linha))
        img2.putpixel((int(coluna) + 25   , int(linha) + 25), pixel)
        
img2.show()
        
for linha in range(h):
    for coluna in range(w):
        pixel = img2.getpixel((coluna, linha))
        Y = int(coluna * math.sin(45) + linha * math.cos(0.5))
        X = int((coluna * math.cos(0.5) - linha * math.sin(45)))
        
        if X < 0:
            X = 500 + X
            img.putpixel((int(X / 2 + 250) , int(Y / 2 + 250)), pixel)
            
        else:
            X = 500 + X
            img.putpixel((int(X / 2 + 250) , int(Y / 2 + 250)), pixel)
        
img.show()
img.save('img1.png')
