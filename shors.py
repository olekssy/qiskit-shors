import random
import sys
from assets import FactorClass

# Global variables
order = 3
limit = 10 ** order  # upper limit of the integer to be factored
sample_size = 10  # num of integers in a sample for finding a period
recursion_limit = 1000
iterations = 3


def main(limit, sample_size):
    try:
        n = random.randint(10 ** (order - 1), limit)
        randint_set = FactorClass.sample(n, sample_size)
        p = FactorClass.euclidean(n, randint_set)
        if p is not None:
            q = int(n / p)
        else:
            print("-> Euclidean algorithm failed")
            # proceed to modular exponentiation
            p = FactorClass.modexp(n, randint_set)
            if p is not None:
                q = int(n / p)
            else:
                print("-> Modexp algorithm failed")
                p, q = 1, n
    except KeyboardInterrupt:
        p, q = 1, n
        print('\n-> Program interrupted by User')
        quit()
    except OverflowError as message:
        q = 'q'
        print('Unable to find second factor q = n / p, because', message)
    except RecursionError as message:
        p, q = 1, n
        recursion_limit = sys.getrecursionlimit()
        print(message, recursion_limit)
        print('If exception persists, increase the recursion depth '
              'limit manually in Global variables')
    finally:
        print("{} x {} = {}\n".format(p, q, n))


if __name__ == '__main__':
    print()
    sys.setrecursionlimit(recursion_limit)
    for i in range(iterations):
        main(limit, sample_size)
