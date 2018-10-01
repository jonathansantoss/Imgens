from PIL import Image

imagemLenna = Image.open('Lenna.png')
imagemLennaCinza = imagemLenna.convert('L')
imagemLennaCinza.show()

img = Image.new('L', (imagemLennaCinza.size[0], imagemLennaCinza.size[1]), 'BLACK')

h , w = imagemLennaCinza.size

histograma = [0] * 256


def Maior():
    valorMaior = 0
    m = 0
    for i in range(len(histograma)):
        if histograma[i] > valorMaior:
            valorMaior = histograma[i]
            m = i
            
    return m


def Menor():
    valorMenor = histograma[0]
    m = 0
    for i in range(len(histograma)):
        if histograma[i] < valorMenor:
            valorMenor = histograma[i]
            m = i
            
    return m


for i in range(h):
    for j in range(w):
        pixel = imagemLennaCinza.getpixel((i, j))
        histograma[int(pixel)] += 1
        
for i in range(h):
    for j in range(w):
        maior = Maior()
        menor = Menor()
        pixel = (imagemLennaCinza.getpixel((i, j)) - maior) * ((128) / (maior - menor)) + 128
        img.putpixel((i , j), int(pixel)) 

img.show()
img.save('img8.png')