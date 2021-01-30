def jumpingOnClouds(c):
    count = 0
    i = 0

    while True:
        if i+2 < len(c) and c[i+2] == 0:
            count += 1
            i = i+2
            print('count: ', count, 'jumps:', 2, 'increment:', i)
        elif i+1 < len(c) and c[i+1] == 0:
            count += 1
            i = i+1
            print('count: ', count, 'jumps:', 1, 'increment:', i)

        if i == len(c) - 1:
            return count


print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))
# print(jumpingOnClouds())
# print(jumpingOnClouds())
