c = 0
def dynamicfibo():
    cache = {}

    def fibo(n):
        global c
        c += 1
        if n in cache:
            return cache[n]
        else:
            if n<2:
                return 1
            else:
                cache[n] =  fibo(n-1)+fibo(n-2)
                return cache[n]
    return fibo

fastfibo = dynamicfibo()
print(fastfibo(100))
print(c)