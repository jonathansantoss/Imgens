from PIL import Image
import math

imagemLenna = Image.open('Lenna.png')
imagemLennaCinza = imagemLenna.convert('L')

h, w = imagemLennaCinza.size

img = Image.new('L', (h,w), 'BLACK')

histograma = [0] * 256


a1G1 = 0.0
u1G1 = 0.0

a2G2 = 0.0
u2G2 = 0.0

lista = []

def grupo1():
     a1 = 0.0
     u1 = 0.0
     for i in range(1,int(len(histograma) / 2)):
         if i > 0 and histograma[i] > 0:
             P = (i / histograma[i])
             a1 = a1 + P
         if i > 0 and histograma[i] > 0:
             P = (i / histograma[i])
             u1 += (i * P / a1)
             
     lista.insert(0,a1)
     lista.insert(1,u1)

def grupo2():
     a2 = 0.0
     u2 = 0.0
     for i in range( len(histograma)):
         if (i + 1) < len(histograma) and histograma[i+1] > 0:
             P = ((i+1) / histograma[i+1])
             a2 += P 
     for j in range( len(histograma)):
         if (j + 1) < len(histograma) and histograma[j+1] > 0:
             P = (j / histograma[j+1])
             u2 += (j * P / a2)
                    
     lista.insert(2,a2)
     lista.insert(3,u2)
     
def Total():
    a1 = lista[0]
    u1 = lista[1]
    a2 = lista[2]
    u2 = lista[3]
    ut = a1 * u1 + a2 * u2
    return ut


for i in range(h):
    for j in range(w):
        pixel = imagemLennaCinza.getpixel((i, j))
        histograma[int(pixel)] += 1       


grupo1()
grupo2()
T = lista[0] * (math.pow((lista[1] - Total()), 2)) + lista[2] * (math.pow((lista[3] - Total()), 2))
t = math.sqrt(T)

for i in range(h):
    for j in range(w):
        pixel = imagemLennaCinza.getpixel((i , j))
        if t > pixel:
            img.putpixel((i,j), 255)
        else:
            img.putpixel((i,j), 0)

img.show()