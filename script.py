
from datetime import datetime
import random

# Завдання 1

def get_days_from_today(date):
    try:
        today = datetime.today().date()
        date_object = datetime.strptime(date, "%Y-%m-%d").date()
        date_delta = date_object - today
        print(date_delta)
    except Exception as e:
        print(f'Сталася помилка: {e}')


# Завдання 2

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or not (min <= quantity <= max):
        return []
    selected_numbers = random.sample(range(min, max), quantity)
    return selected_numbers

