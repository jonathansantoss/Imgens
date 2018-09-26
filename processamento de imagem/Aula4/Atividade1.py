'''
Created on 24 de set de 2018

@author: jonathan
'''
from PIL import Image

imagem = Image.open('Lenna.png')

w = imagem.size[0]
h = imagem.size[1]

img = Image.new( 'L', (imagem.size[0],imagem.size[1]), "black") # Cria uma imgem em tonz de cinza

T = 60 # Threshold

for i in range(h):
    for j in range(w):
        r,g,b = imagem.getpixel((i, j))
        x = int((r+g+b) / 3)
        if x > T:
            img.putpixel((i, j), 255)
        else:
            img.putpixel((i , j), 0)

img.save('imgT60.png')            
img.show();