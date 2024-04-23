from zad_3 import PasswordGenerator

passwordGenerator = PasswordGenerator(9, 9)

print(passwordGenerator.__next__())
print(passwordGenerator.__next__())
print(passwordGenerator.__next__())

for password in passwordGenerator:
    print(password)
