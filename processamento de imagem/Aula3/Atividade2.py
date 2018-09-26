from PIL import Image

imgLenna = Image.open('Lenna.png')
img = Image.new('L', (imgLenna.size[0],imgLenna.size[1]), 'BLACK')

w = imgLenna.size[0]
h = imgLenna.size[1]

def intensidade(tupla = ()):
    r,g,b = tupla
    m = int( (r+g+b) / 3 )
    return m


for i in range(w):
    for j in range(h):
        X = intensidade( imgLenna.getpixel((i,j)) )
        
        if j < w:
            mod  = int(j % 2)
            if mod == 0:
                img.putpixel((i, j + 1), X)
            else:
                img.putpixel((i, j - 1), X)
            
img.show()