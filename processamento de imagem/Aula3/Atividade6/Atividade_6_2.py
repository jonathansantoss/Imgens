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
        img2.putpixel((int(coluna / 2) + 128   , int(linha / 2) + 128), pixel)
        
img2.show()
        
for linha in range(h):
    for coluna in range(w):
        pixel = img2.getpixel((coluna, linha))
        Y = int(coluna * math.sin(90) + linha * math.cos(90))
        X = int((coluna * math.cos(90) - linha * math.sin(90)))
        
        img.putpixel((int(X / 2 + 342) , int(Y / 2 + 680)), pixel)
img.show()
img.save('img2.png')
