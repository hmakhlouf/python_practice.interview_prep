s = "hello"

print("------------")
print(len(s))

print("------------")
print(range(len(s)))

print("------------")
for i in range(len(s)):
    print(i, s[i])


print("------------")
print(range(len(s)-1))


print("------------")
for y in range(len(s)-1):
    print(y, s[y])


print("------------")
for x in range(len(s)-1, -1, -1):
    print(x, s[x])