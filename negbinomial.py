import math

storage = dict()
def C(n, k):
    if (k==0) or (k == n):
        return 1
    if (k == 1):
        return n
    if (n,k) in storage:
        return storage[(n,k)]
    storage[(n, k)] = C(n - 1, k - 1) + C(n - 1, k)
    return storage[(n, k)] 

def prob(n, p, r):
    assert r > 0
    assert n >= r
    assert 0 < p <= 1
    return C(n-1, r-1) * (p ** r) * ((1-p) ** (n - r))

def infoMeasure(n, p, r):
    return - math.log2(prob(n, p, r))

def sumProb(N, p, r):
    sum = 0
    for x in range(r, N + 1):
        sum += prob(x, p, r)
    return sum

def approxEntropy(N, p, r):
    sum = 0
    for x in range(r, N + 1):
        sum += infoMeasure(x, p, r) * prob(x, p, r)
    return sum
