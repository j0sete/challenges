import math


# integer to binary
def i2b(n):
    binary = []

    if n == 0:
        binary.append(0)
    else:
        found = False

        while not found:
            binary.append(n % 2)
            c = int(n / 2)
            if c > 0:
                n = int(c)
            else:
                found = True

    return binary


def g(m, n, k):
    """
    For this case, using powers of 2, we know that:
        k = (2 ** alpha) + ((2 ** 0) * (1 + sum(i:0...t: 2 ** p_i))) + sum(i: 0...k', 2 ** 0)

    :param m: Number of tribbles per group
    :param n: Number of tribbles' groups
    :param k: Total population
    :return: Returns the number of hours it takes n groups of m Tribbles to form a total population of k
    """
    if (m * n) == k:
        return 0  # If m * n is k, we already have the population
    else:
        if m > 1 and k % m > 0:
            return -1  # if k cannot be divided by m, it is impossible to achieve the k population exactly
        elif m > 1:
            return g(1, n, k / m)  # reduce the problem
        else:
            if n > 1:
                a3 = n - 2
                alpha = int(math.log2(k - (a3 + 1)))
                a1 = 2 ** alpha
                a2 = k - a1 - a3 - 1
                a2_binary = i2b(a2)
                active_bits = sum([b for b in a2_binary if b == 1])
                return active_bits + alpha
            elif (k & (k - 1)) == 0:
                return math.log2(k)
            else:
                return 1 + g(m, n + 1, k)  # we add a new group, what means, 1 hour to create it


if __name__ == '__main__':
    # print(g(1, 1, 1))
    # print(g(1, 1, 2))
    # print(g(1, 1, 4))
    # print(g(2, 2, 12))
    # print(g(3, 1, 7))
    # print(g(5, 10, 500))
    # print(g(13, 1234, 13131313))
    print(g(35, 33, 10670846278085))
