def minus(x, y):
    return (x - y) & 0xFF


def bitreverse(x):
    return int("{:08b}".format(x)[::-1], 2)


def figureout(xs):
    res = []
    for i in range(0, len(xs)):
        val = ord(xs[i])
        rev = bitreverse(val)
        prev = 256
        if i > 0:
            prev = bitreverse(ord(xs[i - 1]))

        res.append(minus(prev, rev))

    return res


print(figureout("Hello, World!\n"))
