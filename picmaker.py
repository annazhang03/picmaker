def makepic():
    rgb = "{a} {b} {c} "
    pic = open('image1.ppm', 'w')
    pic.write('P3 500 500 255\n')
    for i in range(500):
        for j in range(500):
            x = i if i % 2 == 0 else i + 1
            y = j if j % 2 == 0 else j + 1
            l = [x ** 2 + y ** 2 + x * y, x ** 2 + y ** 2 + y, x ** 2 + y ** 2 + x]
            pic.write(rgb.format(a = l[0], b = l[1], c = l[2]))
        pic.write('\n')
    pic.close()

makepic()