import math

def prob(n, p):
    assert n > 0
    assert 0 <= p <= 1
    return p * ((1-p)**(n-1))

def infoMeasure(n, p):
    return - math.log2(prob(n, p))

def sumProb(N, p):
    "k biet viet j ca"
    sum = 0
    for x in range(0, N + 1):
        sum += prob(x, p)
    return sum

def approxEntropy(N, p):
    sum = 0
    for x in range(1, N + 1):
        sum += infoMeasure(x, p) * prob(x, p)
    return sum
