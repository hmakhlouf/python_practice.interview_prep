# reverse string
def solution(s):
    reverse = ""
    for i in range(len(s) - 1, -1, -1):
        reverse = reverse + s[i]
    return reverse


s = "hello"
print(solution(s))


