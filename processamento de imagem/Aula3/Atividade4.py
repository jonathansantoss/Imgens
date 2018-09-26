import matplotlib.pyplot as pl
from PIL import Image

imglenna = Image.open('Lenna.png')
imglennaCinza = imglenna.convert('L')
imglennaCinza.show()

img = Image.new('L', (imglenna.size[0] , imglenna.size[1]), 'BLACK')

w = imglenna.size[0]
h = imglenna.size[1]

histograma = [0] * 256

def maiorElemento(lista = []):
    elementoMaior = 0
    posicaoMaior  = 0
    for i in range(256):
        if lista[i] > posicaoMaior:
            elementoMaior = i
            posicaoMaior = lista[i]
    return elementoMaior

def menorElemento(lista = ()):
    posicaoMenor = lista[0]
    elementoMenor = 0
    for i in range(256):
        if lista[i] < posicaoMenor:
            posicaoMenor = lista[i] 
            elementoMenor = i
    return elementoMenor

def maiorMatriz():
    elementoMaior = 0
    for i in range(h):
        for j in range(w):
            X = imglennaCinza.getpixel( (i,j) )
            if X > elementoMaior:
                elementoMaior = X
    return elementoMaior 

def menorMatriz():
    elementoMenor = imglennaCinza.getpixel((0,0))
    for i in range(h):
        for j in range(w):
            X = imglennaCinza.getpixel( (i,j) )
            if X < elementoMenor:
                elementoMenor = X
    return elementoMenor

for linha  in range(h):
    for coluna in  range(w):
        X = imglennaCinza.getpixel((linha, coluna))
        histograma[X] += 1
        
pl.plot(histograma)
pl.show()

Gmaior = maiorElemento(histograma)
Gmenor = menorElemento(histograma)
            
Fmaior = maiorMatriz()
Fmenor = menorMatriz()

for height in range(h):
    for width in range(w):
        X = imglennaCinza.getpixel((height, width))
        G = int( (Gmaior - Gmenor) / (Fmaior - Fmenor) * (X - Fmenor) + Gmenor )
        img.putpixel((height,width), G)
        
        
img.show()