'''
Created on 24 de set de 2018

@author: jonathan
'''


import random
from PIL import Image
from builtins import range


imagemLenna = Image.open('Lenna.png')
imagemLenna.show()

imagemTonsCinza = imagemLenna.convert('L')
imagemTonsCinza.show()


imgNovaLenna = Image.new('L', (imagemTonsCinza.size[0], imagemTonsCinza.size[1]), 'BLACK')

T = 8 #Threshold

h = imagemTonsCinza.size[0]
w = imagemTonsCinza.size[1]

hAl = random.randrange(int(h))
wAl = random.randrange(int(w)) 


def media(tupla = ()):
    r,g,b  = tupla
    m = int((r+g+b) / 3)
    return m


def cinza(tupla):
    ass = tupla
    #m = int( (r+g+b) /3) 
    return ass

#def marca(n1 , n2):
#    lista = [n1,n2,True]
#    return lista

def recurse(x, y):
    
    t = y + 1
    t1 = x + 1
    
    if t >= 510 | t1 >= 510:
        return 0
        
    
    m1 = cinza(imagemTonsCinza.getpixel( (x, y) ) )
    m2 = cinza(imagemTonsCinza.getpixel( (x, t) ) )
    subM = m1 - m2
    
    if subM <= T:
        imgNovaLenna.putpixel((x,y), 255)
        recurse(x, y + 1)
    if T < subM:
        imgNovaLenna.putpixel((x, y), 0)
        recurse(x, y + 1)



a = recurse(wAl, hAl)
imgNovaLenna.show()                    
                    