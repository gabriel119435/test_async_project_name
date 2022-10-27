from datetime import datetime


def print_instant(text):
    print(text, datetime.now().second, datetime.now().microsecond)
