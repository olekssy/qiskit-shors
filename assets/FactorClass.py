import sys
import warnings
import random

warnings.filterwarnings('error', "", RuntimeWarning)


def sample(n, sample_size):
    """Define sample of int divisors for finding period"""
    low = 2
    top = 4096
    sample = []
    if top > n:
        top = n
    for i in range(sample_size):
        integer = random.randrange(low, top)
        sample.append(integer)
    return sorted(sample)


def gcd(a, b):
    """Euclidean algorith of finding GCD"""
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)


def euclidean(n, int_set):
    """Factoring composite int via Euclidean algorithm"""
    for a in int_set:
        try:
            p = gcd(n, a)
            if 1 < p < n:
                return p
        except RecursionError as message:
            recursion_limit = sys.getrecursionlimit()
            print(message, recursion_limit)
            sys.setrecursionlimit(recursion_limit * 2)
            print('Recursion depth limit is set to', sys.getrecursionlimit(
            ))
            continue


# TODO period func, which returns list of periods that matches
#  co-primes and make possible to select the smallest r for a**r
def period(n, a):
    """Compute the period of a^kmod n)"""
    remainder_list = []
    k = 1
    while True:
        r = len(remainder_list)
        if r > 128:
            return None
        remainder = a ** k % n
        if remainder in remainder_list:
            return r
        else:
            remainder_list.append(remainder)
            k += 1


# TODO set list of periods as arg of modexp(), s.t. can parse from QFT
def modexp(n, int_set):
    """Function computes p * q = N from the period of the mod exp
    function"""
    global q
    for a in int_set:
        r = period(n, a)
        if r is None:
            continue
        elif r % 2 == 0:
            try:
                p = gcd(n, int(a ** (r / 2) - 1))
                if p != 1 and p != n:
                    return p
            except RuntimeWarning:
                print("RuntimeWarning: int64 < [{} exp "
                      "{}]".format(a, int(r / 2)))
                continue
