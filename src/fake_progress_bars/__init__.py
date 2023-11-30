from time import sleep
from random import uniform


def progress_bar(time: int, size=100, step=1, label='', variability=0.0, progress='#', remaining='-', outside='|', percentage=True):
    '''
    Creates a fake progress bar.

    :param int time: The amount of time the progress bar takes to complete.
    :param int size: The size of the progress bar in characters.
    :param int step: The amount the progress increases every step.
    :param str label: The label before the progress bar, succeeded by ": ".
    :param float variability: The amount of change allowed in the time of each step. This property is limited to the time times the step divided by the size to keep the time consistent.
    :param str progress: The character used to represent the current progress of the progress bar.
    :param str remaining: The character used for the remaining percentage of the progress bar.
    :param str outside: The character used as the border on either side of the progress bar.
    :param bool percentage: Whether the percentage competed should be shown on the right side of the progress bar.
    '''

    amount = 0
    for x in range(round(size / step)):
        amount += step
        print(
            f'{label}{"" if label == "" else ": "}{outside}{progress * amount}{remaining * (size - amount)}{outside} {f"{round(amount / size * 100)}%" if percentage else ""}', end='\r')
        sleep_time = time * step / size
        smallest = min(variability, sleep_time)
        sleep(sleep_time + uniform(-smallest, smallest))
    print(
        f'{label}{"" if label == "" else ": "}{outside}{progress * amount}{remaining * (size - amount)}{outside} {f"{round(amount / size * 100)}%" if percentage else ""}')
