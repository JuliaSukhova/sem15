import os
import logging
import argparse

# Создаем директорию, если ее нет
log_dir = 'Log'
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(filename=os.path.join(log_dir, 'log_2.log'),
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке '
                           '{lineno} функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def decor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'аргументы функции: {args}, результат функции: {result}')
        return result

    return wrapper


@decor
def power(x, y):
    return x ** y


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate power of a number')
    parser.add_argument('base', type=int, help='Base number')
    parser.add_argument('exponent', type=int, help='Exponent number')

    args = parser.parse_args()

    result = power(args.base, args.exponent)
    print(result)

