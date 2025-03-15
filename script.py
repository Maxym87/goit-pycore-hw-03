
from datetime import datetime, timedelta
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


def normalize_phone(phone_number):
    pattern = r'[^0-9]'
    repl = ''
    formated_numbers = re.sub(pattern, repl, phone_number)
    if not formated_numbers.startswith('38'):
        formated_numbers = '+38' + formated_numbers.lstrip('0')
    else: formated_numbers = '+' + formated_numbers
    return formated_numbers

# Task 4

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        else: 
            birthday = birthday.replace(year=today.year)

        if today <= birthday <= today + timedelta(days=7):
            if birthday.weekday() == 5:
                birthday += timedelta(days=2)
            elif birthday.weekday() == 6:
                birthday += timedelta(days=1)
            
            upcoming_birthdays.append({'name': user['name'], 'congratulation_date': birthday.strftime("%Y.%m.%d")})

    return upcoming_birthdays
