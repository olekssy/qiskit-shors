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
