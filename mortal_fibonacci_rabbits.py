import numpy as np

def _mortal_fib_list(n: int, m: int) -> list:
    if n == 1:
        result = np.zeros(shape=m, dtype=int)
        result[0] = 1
        return result
    else:
        previous_list = _mortal_fib_list(n-1, m)
        newborn = np.sum(previous_list[1:])
        previous_list[1:] = previous_list[:-1]
        previous_list[0] = newborn
        return previous_list

def mortal_fibonacci_rabbits(n: int, m: int):
    result_list = _mortal_fib_list(n,m)
    return np.sum(result_list)

if __name__ == '__main__':
    n = 81
    m = 18
    result = mortal_fibonacci_rabbits(n,m)
    print(result)