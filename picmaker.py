# create 500x500 image
def makepic():
    rgb = "{a} {b} {c} "
    pic = open('image1.ppm', 'w')
    pic.write('P3 500 500 255\n')
    for i in range(500):
        for j in range(500):
            l = [i ** 2 + j ** 2 + i * j, i ** 2 + j ** 2 + j + 200, i ** 2 + j ** 2 + i + 200]
            pic.write(rgb.format(a = l[0], b = l[1], c = l[2]))
        pic.write('\n')
    pic.close()

makepic()