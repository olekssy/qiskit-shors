import math
import random

from numpy import random


def sample(n, sample_size):
    """Define sample of int divisors for finding period"""
    low = 2
    top = 512
    if top > n:
        top = n
    sample = random.randint(low, top, size=sample_size)
    return sorted(sample)


def euclidean(n, int_set):
    """Factoring composite int via Euclidean algorithm"""
    for a in int_set:
        p = math.gcd(n, a)
        if 1 < p < n:
            return p


def period(n, a):
    """Compute period of a^kmod n)"""
    r = 1
    modexp = a
    while modexp != 1:
        r += 1
        modexp = (modexp * a) % n
        if r > 64:
            return None
    return r


def modexp(n, int_set):
    """Function computes p * q = N from the period of the mod exp
    function"""
    global q
    for a in int_set:
        r = period(n, a)
        if r is None:
            continue
        elif r % 2 == 0:
            p = math.gcd(n, int(a ** (r / 2) - 1))
            if p != 1 and p != n:
                return p
