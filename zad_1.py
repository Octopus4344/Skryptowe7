from match import match
from typing import List, Dict


def acronym(my_list: List[str]) -> str:
    match my_list:
        case ([]):
            return ''
        case ('', *other_words):
            return '' + acronym(other_words)
        case (first_word, *other_words):
            return first_word[0].upper() + acronym(other_words)


def acronym_with_mapping(my_list: List[str]) -> str:
    return ''.join(map(lambda x: x[0], filter(lambda x: x, my_list))).upper()


def median(my_list: List[float]) -> float:
    match my_list:
        case ([first_middle_number, second_middle_number]):
            return (first_middle_number + second_middle_number) / 2
        case ([middle_number]):
            return middle_number
        case (first_number, *middle, last_number):
            return median(middle)


def square_root(x: float, epsilon: float) -> float:
    def inner_square_root(x, y, epsilon):
        match (y >= 0, abs(y * y - x) < epsilon):
            case (True, True):
                return y
            case (True, False):
                return inner_square_root(x, (y + x / y) / 2, epsilon)
            case (False, _):
                return None

    return inner_square_root(x, x, epsilon)


def make_alpha_dic(sentence: str):
    return dict(map(lambda char: (char, list(filter(lambda word: char in word, sentence.split()))),
                    sorted(set(''.join(sentence.split())))))


def flatten(my_list):
    match my_list:
        case (first, *rest):
            match isinstance(first, list):
                case True:
                    return flatten(first) + flatten(rest)
                case False:
                    return [first] + flatten(rest)
        case []:
            return []


print(acronym(["Centralne", "Biuro", "Antykorupcyjne"]))
print(acronym_with_mapping(["Centralne", "Biuro", "Antykorupcyjne"]))
print(median([1, 2, 3, 4, 5]))
print(square_root(3.0, 0.1))
print(make_alpha_dic("on i ona"))
print(flatten([[1,4],2,3,[5,6]]))
