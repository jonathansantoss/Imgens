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
        
        if i < w:
            mod  = int(i % 2)
            if mod == 0:
                img.putpixel((i + 1, j), X)
            else:
                img.putpixel((i - 1, j), X)
            
img.show()