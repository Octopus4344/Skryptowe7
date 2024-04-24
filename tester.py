import logging

from zad_3 import PasswordGenerator

formatter = logging.Formatter('%(message)s')

logging.basicConfig(level=logging.INFO)

for handler in logging.root.handlers:
    handler.setFormatter(formatter)

passwordGenerator = PasswordGenerator(9, 9)

print(passwordGenerator.__next__())
print(passwordGenerator.__next__())
print(passwordGenerator.__next__())

for password in passwordGenerator:
    print(password)
