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

def prob(n, p, N):
    assert n >= 0
    assert 0 < p <= 1
    assert N >= n
    return (p ** n) * ((1-p) ** (N-n)) * C(N,n)

def infoMeasure(n, p, N):
    return - math.log2(prob(n, p, N))

def sumProb(N, p):
    """
    Ham tinh tong xac suat cua cac truong hop xay ra => ket qua = 1
    """
    sum = 0
    for x in range(0, N + 1):
        sum += prob(x, p, N)
    return sum

def approxEntropy(N, p):
    sum = 0
    for x in range(0, N + 1):
        sum += infoMeasure(x, p, N) * prob(x, p, N)
    return sum