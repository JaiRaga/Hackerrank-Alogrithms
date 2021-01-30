def extraLongFactorials(n, store={}):
    print("store", store)
    if n in store:
        print("YES")
        return store[n]
    if n == 1:
        return 1
    store[n] = n * extraLongFactorials(n-1, store)

    return store[n]


print(extraLongFactorials(5))
print(extraLongFactorials(15))
print(extraLongFactorials(25))
print(extraLongFactorials(45))
