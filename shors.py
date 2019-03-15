from numpy.random import randint
from assets import FactorClass

# Global variables
top = 10 ** 15  # upper limit of the integer to be factored
sample_size = 10  # num of integers in a sample for finding a period


def main():
    for i in range(5):
        n = randint(top * 0.9, top)  # integer to be factor
        randint_set = FactorClass.sample(n, sample_size)
        factors = FactorClass.euclidean(n, randint_set)
        if factors is not None:
            p, q = factors
        else:
            # print("-> Euclidean algorithm failed")
            try:
                # proceed to modular exponentiation
                p, q = FactorClass.modexp(n, randint_set)
            except KeyboardInterrupt:
                print('\n-> Program interrupted by User')
                quit()
            except:
                # print("-> Modular exponentiation failed for N =", n)
                p, q = 1, n

        print("{} = {} x {}".format(n, p, q))
        pass


if __name__ == '__main__':
    print()
    main()
