from ossdev import Vector


def main():
    a = Vector([0, 1, 2, 3, 4])
    b = Vector([4, 3, 2, 1, 0])
    print('Vector a: %s' % a)
    print('Vector b: %s' % b)
    print('Vector a+2: %s' % (a+2))
    print('Vector a+b: %s' % (a+b))
    print('len a: %s' % len(a))
    print('length a: %s' % a.length())
    print('reverse a: %s' % reversed(a))
    a[1] = 42
    print('a[1]=42: %s' % a)


if __name__ == '__main__':
    main()
