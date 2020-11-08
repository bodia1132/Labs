import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def my_bro(x):
	return print(list(range(0, 101, 2)) if x else list(range(1, 101, 2)))