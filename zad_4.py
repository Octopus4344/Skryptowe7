def make_generator(f):
    def generator():
        n = 1
        while True:
            yield f(n)
            n += 1

    return generator


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def print_sequence(generator, elements):
    for i, number in enumerate(generator()):
        print(f"{i + 1}: {number}")
        if i == elements - 1:
            break


if __name__ == "__main__":
    elements = 15

    print("Fibonacci numbers:")
    fibonacci_generator = make_generator(fibonacci)
    print_sequence(fibonacci_generator, elements)

    print("\nFactorial numbers:")
    factorial_generator = make_generator(factorial)
    print_sequence(factorial_generator, elements)

    print("\nArithmetic sequence:")
    arithmetic_sequence = lambda n: 2 * n + 12
    arithmetic_sequence_generator = make_generator(arithmetic_sequence)
    print_sequence(arithmetic_sequence_generator, elements)

    print("\nGeometric sequence:")
    geometric_sequence = lambda n: 2 ** n
    geometric_sequence_generator = make_generator(geometric_sequence)
    print_sequence(geometric_sequence_generator, elements)

    print("\nPower sequence:")
    power_sequence = lambda n: n ** 2
    power_sequence_generator = make_generator(power_sequence)
    print_sequence(power_sequence_generator, elements)

    print("\nHarmonic sequence:")
    harmonic_sequence = lambda n: 1 / n
    harmonic_sequence_generator = make_generator(harmonic_sequence)
    print_sequence(harmonic_sequence_generator, elements)
