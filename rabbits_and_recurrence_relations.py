def _fibonacci(k, n):
    if n == 1 or n == 2:
        return 1
    else:
        return _fibonacci(k, n-1) + _fibonacci(k, n-2) * k

def rabbits_and_recurrence_relations(n, k):
    return _fibonacci(k, n)

if __name__ == '__main__':
    n = 32
    k = 5
    print(rabbits_and_recurrence_relations(n, k))