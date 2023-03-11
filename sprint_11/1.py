import time


def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp 

time_start = time.time()

get_least_primes_linear(10000000)

time_finish = time.time()
time_span = time_finish - time_start
print(f'{time_span} seconds') 