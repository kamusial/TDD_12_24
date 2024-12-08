def fizzbuss(i):
    if isinstance(i, (int, float)) and i > 0:
        i = int(i)
        if i % 15 == 0:
            return 'FizzBuzz'
        elif i % 3 == 0:
            return 'Fizz'
        elif i % 5 == 0:
            return 'Buzz'
        return i
    return None

# 9 % 3 == 0