def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2,result):
            if result % i == 0:
                return (f'Простое \n{result}')
            else:
                return (f'Составное \n{result}')

    return wrapper


@is_prime
def sum_three(i,j,k):
    return i+j+k


result = sum_three(2, 3, 6)
print(result)
