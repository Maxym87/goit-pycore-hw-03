
from datetime import datetime
import random
import re

# Task 1

def get_days_from_today(date):
    try:
        today = datetime.today().date()
        date_object = datetime.strptime(date, "%Y-%m-%d").date()
        date_delta = date_object - today
        print(date_delta)
    except Exception as e:
        print(f'Сталася помилка: {e}')


# Task 2

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or not (min <= quantity <= max):
        return []
    selected_numbers = random.sample(range(min, max), quantity)
    return selected_numbers

# Task 3


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(phone_number):
    pattern = r'[^0-9]'
    repl = ''
    formated_numbers = re.sub(pattern, repl, phone_number)
    if not formated_numbers.startswith('38'):
        formated_numbers = '+38' + formated_numbers.lstrip('0')
    else: formated_numbers = '+' + formated_numbers
    return formated_numbers

