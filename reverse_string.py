# reverse string
def f():
    st = "hello"
    reverse = ""
    for x in range(len(st) - 1, -1, -1):
        reverse = reverse + st[x]
    print(reverse)


f()
