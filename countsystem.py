def co(x):
    lst = []
    while x > 0:
        x1 = x % 2
        x = x // 2
        lst.insert(0, str(x1))
    return ''.join(lst)


print(co(x=int(input('Enter the number: '))))

