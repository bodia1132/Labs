import argparse
from modules import common
import logging


FORMAT = '%(asctime)-15s %(name)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger()
parser = argparse.ArgumentParser(description='Приклад передачі аргументів у Python програму.')
parser.add_argument('-o', '--optional', dest='opt', type=str, help='Цей параметр є вибірковим.')
parser.add_argument('-l', '--logs', dest='logs', action='store_true',
                    help='Якщо виконати команду з цим параметром будуть виводитись логи.')


def main(text):
    print(f"We are in the {__name__}")
    print(common.get_current_date().now())
    if text:
        print("З консолі було передано аргумент\n", 10*"=", f">> {text} <<", 10*"=")


def how_to_write_logs():
    logger.info("Тут буде просто інформативне повідомлення")
    logger.warning("Це Warning повідомлення")
    logger.error("Це повідомлення про помилку")

def my_bro2():
    try:
        print("Спробуємо вийти за межі масиву.")
        ar = ['0', '1', '2']
        print(ar[5])
    except IndexError:
        logger.error("Це повідомлення про помилку")
    else:
        logger.info("Тут буде просто інформативне повідомлення")
    finally:
        print("Ось такий результат.\n")

if __name__ == '__main__':
    args = parser.parse_args()
    if args.logs:
        how_to_write_logs()
    else:
        main(args.opt)
    print(common.get_current_platform())
    a = True
    common.my_bro(a)
    my_bro2()