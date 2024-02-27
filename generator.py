import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[int, None, None]:
    for number in re.finditer(r'\b\d+\b', text):
        yield int(number.group())

def sum_profit(text: str, func: Callable) -> int:
    return sum(func(text))

test_text = "Цей рік був успішним, наш прибуток склав 5000, витрати були на рівні 3000, отже чистий прибуток становить 2000."
print("Числа у тексті:", list(generator_numbers(test_text)))
print("Сума прибутків:", sum_profit(test_text, generator_numbers))
