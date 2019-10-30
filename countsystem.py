def co(x, y):
    lst = []
    while x > 0:
        x1 = x % y
        x = x // y
        lst.insert(0, str(x1))
    return ''.join(lst)


print(co(x=int(input('Enter the number: ')),
         y=int(input('Enter the system: '))))
