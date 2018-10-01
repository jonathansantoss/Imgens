from PIL import Image

img = Image.new('L', (100,100), 'BLACK')

for i in range(1,100):
    for j in range(1,100):
        if i >=40  and  i <= 60 and j >= 5 and j <= 94 :
            img.putpixel((i,j), 255)
        else:
            img.putpixel((i,j), 0)
            
img.show()

for i in range(1,100):
    for j in range(1,100):
        if i >=5  and  i <= 94 and j >= 40 and j <= 60 :
            img.putpixel((i,j), 255)
        else:
            img.putpixel((i,j), 0)
            
img.show()
