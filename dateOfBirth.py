def birthday(s, d, m):
    count = 0
    tot = 0
    for i in range(len(s)):
        tot = sum(s[i:m+i])
        # print(s[i:m+i], sum(s[i:m+i]))
        if tot == d:
            count += 1

    return count


print(birthday([4], 4, 1))
print(birthday([1, 2, 1, 3, 2], 3, 2))
