import string


def name_formatter(name):
    similiar_letters = {
        'A': 'А',
        'B': 'В',
        'C': 'С',
        'E': 'Е',
        'H': 'Н',
        'K': 'К',
        'M': 'М',
        'O': 'О',
        'P': 'Р',
        'T': 'Т',
        'X': 'Х',
        'a': 'а',
        'c': 'с',
        'e': 'е',
        'k': 'к',
        'o': 'o',
        'p': '',
        'x': 'х',
        'y': 'у',
    }
    formatted_name = name.lower()
    for symbol in string.punctuation:
        formatted_name = formatted_name.replace(symbol, '')
    for en_letter, ru_letter in similiar_letters.items():
        formatted_name.replace(en_letter, ru_letter)
    formatted_name = formatted_name.replace(' ', '')
    return formatted_name
