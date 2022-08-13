import sys


def count_word(s: str):
    lower_count = 0
    upper_count = 0
    for i in s:
        if i.islower():
            lower_count += 1
        else:
            upper_count += 1
    return max(lower_count + upper_count * 2, lower_count * 2 + upper_count + 1)


lines = sys.stdin.readlines()

n = int(lines[0])

res = []

for i in range(2, len(lines)):
    res.append(count_word(lines[i]))
print(res)
