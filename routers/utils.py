import random
import string


def generate_random_word(length=10):
    letters = string.ascii_letters  # Все буквы (заглавные и строчные)
    random_word = ''.join(random.choice(letters) for _ in range(length))
    return random_word