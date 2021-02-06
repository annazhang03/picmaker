def makepic():
    rgb = "{a} {b} {c} "
    pic = open('image.ppm', 'w')
    pic.write('P3 500 500 255\n')
    for i in range(500):
        for j in range(500):
            x = i if i % 2 == 0 else i + 1
            l = [x ** 2 + j ** 2 + x * j, x ** 2 + j ** 2 + j, x ** 2 + j ** 2 + x]
            l = [a % 256 for a in l]
            pic.write(rgb.format(a = l[0], b = l[1], c = l[2]))
        pic.write('\n')
    pic.close()

makepic()