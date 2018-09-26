import matplotlib.pyplot as pl
from PIL import Image

imglenna = Image.open('Lenna.png')
img = Image.new('L', (imglenna.size[0] , imglenna.size[1]), 'BLACK')

w = imglenna.size[0]
h = imglenna.size[1]

histograma = [0] * 256

def intensidade(tupla = ()):
    r,g,b = tupla
    m = int( (r+g+b) / 3)
    return m

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

for linha  in range(h):
    for coluna in  range(w):
        X = intensidade(imglenna.getpixel((linha, coluna)))
        histograma[X] += 1
        
pl.plot(histograma)
pl.show()

Gmaior = maiorElemento(histograma)
Gmenor = menorElemento(histograma)
