"""
Practice with Recursion
Author: Jose Renteria
CS210 Winter 2023

"""

import time


def findSum(A: list, N: int):
    if N <= 0: # base case
        return 0
    return findSum(A, N - 1) + A[N - 1]
    # Recursive call, performs the findSum operation on the next value, plus the previous value


if __name__ == '__main__':
    # Recursion can provide simple solutions, works great with small inputs

    A = [1, 2, 3]
    start_time = time.time()
    print(f"Recursive Sum = {findSum(A, len(A))}")
    ret1 = time.time() - start_time
    print("--- %s ms---" % (ret1*1000))

    # Let's find the recursion depth
    # maximum number of nested calls

    # call
    #   call
    #       call
    #           call

    # n number of times
    B = []
    for i in range(997): # can not do it more than 996 times. This may seem like a lot. But it really isn't
        B.append(i)

    start_time = time.time()
    print(f"Recursive Sum = {findSum(B, len(B))}")
    ret2 = time.time() - start_time
    print("--- %s ms ---" % (ret2*1000))

    print(f"That is {round(ret2/ret1)}x slower for that second calculation")
