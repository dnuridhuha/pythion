# lengkapi fungsi di bawah ini
def akar_kuadrat(x, threshold):
    a = x
    xi = a / 2
    jalan = True

    while(jalan):
        xSebelum = xi
        xi = (xSebelum + (a/xSebelum))/2

        err = (xi - xSebelum)/xi

        if (abs(err) < threshold):
            jalan = False

    hasil = xi
    return hasil

if __name__ == '__main__':
    print(akar_kuadrat(256, 0.1))
