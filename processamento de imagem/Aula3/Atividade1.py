from PIL import Image

imgLenna = Image.open('Lenna.png')
novaimgLenna = Image.new('L', (imgLenna.size[0], imgLenna.size[1]), 'BLACK')

w = imgLenna.size[0]
h = imgLenna.size[1]


lista = [0] * 256
count = 255

def intensidade(tupla = ()):
    r,g,b = tupla
    m = int( (r+g+b) / 3 )
    return m

for k in range(255):
    lista[k] = count
    count = count - 1 

for i in range(w):
    for j in range(h):
        X = intensidade(imgLenna.getpixel((i, j)) )
        novaimgLenna.putpixel((i, j), lista[X])
        
novaimgLenna.show()