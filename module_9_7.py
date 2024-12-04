def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        is_prime = True
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                is_prime = False
        if is_prime == True:
            return (f'Простое\n{result}')

        else:
            return (f'Составное\n{result}')

    return wrapper


@is_prime
def sum_three(i, j, k):
    return i + j + k


result = sum_three(2, 3, 0)
print(result)
