import random
import string
from faker import Faker

fake = Faker()

def generate_email(cohort_number=None):
    name = fake.first_name().lower()
    surname = fake.last_name().lower()
    cohort = cohort_number or random.randint(1, 99)
    random_digits = ''.join(random.choices(string.digits, k=3))
    domains = ['yandex.ru', 'gmail.com', 'mail.ru', 'yahoo.com']

    return f"{name}_{surname}_{cohort}_{random_digits}@{random.choice(domains)}"

def generate_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def generate_name():
    return fake.first_name()