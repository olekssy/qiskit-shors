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

import random
import sys
from assets import FactorClass

# Global variables
order = 3
limit = 10 ** order  # upper limit of the integer to be factored
sample_size = 10  # num of integers in a sample for finding a period
recursion_limit = 1000  # sys default set to 1000
seed = 3


def main():
    n = random.randint(10 ** (order - 1), limit)
    randint_set = FactorClass.sample(n, sample_size)
    p = FactorClass.euclidean(n, randint_set)
    try:
        if p is not None:
            q = int(n / p)
        else:
            print("-> Euclidean algorithm failed")
            p = FactorClass.modexp(n, randint_set)
            if p is not None:
                q = int(n / p)
            else:
                p, q = 1, n
                print("-> Classical Modexp failed")
    except OverflowError as message:
        q = 'q'
        print('Unable to find second factor q = n / p, because', message)
        if p is None:
            p = 'p'

    print("{} x {} = {}".format(p, q, n))


if __name__ == '__main__':
    print()
    sys.setrecursionlimit(recursion_limit)
    for i in range(seed):
        main()
