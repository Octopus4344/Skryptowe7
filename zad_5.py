from functools import cache

from zad_4 import fibonacci
from zad_4 import print_sequence


def make_generator_mem(f):
    @cache
    def memoized_f(n):
        return f(n)

    def generator():
        n = 1
        while True:
            yield memoized_f(n)
            n += 1

    return generator


if __name__ == "__main__":
    elements = 37
    fibonacci_generator_mem = make_generator_mem(fibonacci)

    print("Memoized generator:")
    print_sequence(fibonacci_generator_mem, elements)
    print("Memoized generator 2nd run:")
    print_sequence(fibonacci_generator_mem, elements)
