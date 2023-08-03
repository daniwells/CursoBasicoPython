def factorial(n, show=False):
    """
    :param n: Number to be factored.
    :param show: (optional) if it is False, don't return anything, but if it is True, return the account.
    :return: Ruturn the factorial value of number "n"
    """
    p = 1
    for c in range(n, 0, -1):
        p = p * c

    if show == True:
        for e in range(n, 1, -1):
            print(f' {e} X', end='')
        print(' 1 ', end='')
        print('=', end=' ')

    return p



print(factorial(10, True))
help(factorial)