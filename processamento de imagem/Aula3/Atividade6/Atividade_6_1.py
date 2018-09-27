from PIL import Image
import math

imglenna = Image.open('Lenna.png')
imgLennaCinza = imglenna.convert('L')
imgLennaCinza.show()

<<<<<<< HEAD
h,w = imgLennaCinza.size

=======
>>>>>>> ef2531a18b472080c0258ede7529478cd1fa44fc
img = Image.new('L', (1000, 1000) , 'BLACK')
img2 = Image.new('L', (w,h) , 'BLACK')  

for linha in range(h):
    for coluna in range(w):
        pixel = imgLennaCinza.getpixel((coluna, linha))
        img2.putpixel((int(coluna / 4) + 300 , int(linha / 4)+300), pixel)
        
img2.show()
        
for linha in range(h):
    for coluna in range(w):
        pixel = img2.getpixel((coluna, linha))
        Y = int(coluna * math.sin(45) + linha * math.cos(45))
        X = int((coluna * math.cos(45) - linha * math.sin(45)))
        if X < 0:
            X = X * (-1)
        img.putpixel((int(X / 2) + 100, int(Y / 2) + 100), pixel)
        
img.show()
img.save('img1.png')
