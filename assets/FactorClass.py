#  MIT License
#
#  Copyright (c) 2019 Oleksii Lialka
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

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
