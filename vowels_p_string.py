"""
Write a function that takes a string s, iterates through it,
and collects all 0-based positions of vowels in it to a list.
For example, print(solution("Hello WORLD")) should output [1, 4, 7]
"""


def solution(s):
    x = ["a", "i", "e", "o", "u", "A", "I", "E", "O", "U"]
    vlistp = []
    for i in range(len(s)):
        if s[i] in x:
            vlistp.append(i)

    return vlistp


# eg:
s = "Hello WORLD"
print(solution(s))
