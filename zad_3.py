import logging
import random
import string

from zad_6 import log


@log(logging.INFO)
class PasswordGenerator:
    def __init__(self, length, count, charset=string.ascii_letters + string.digits):
        self.length = length
        self.count = count
        self.charset = charset

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration()
        self.count -= 1
        return ''.join(random.choice(self.charset) for _ in range(self.length))
