# -*- coding: utf-8 -*-

import argparse, math
from colors import COLORS, RESET

# https://en.wikipedia.org/wiki/Block_Elements
upticks = u'▁▂▃▄▅▆▇█'

def _get_version():
    with open('VERSION','r') as f:
        return f.read().strip()


def _handle_negatives(numbers):
    """
        Add the minimum negative number to all the numbers in the
        such that all the elements become >= 0
    """
    min_number = min(filter(lambda x : type(x)==int,numbers))
    if min_number < 0:
        return [x+abs(min_number) if type(x)==int else x for x in numbers]
    else:
        return numbers


def _draw_tickgram(numbers):
    """
        Takes a list of integers and generate the equivalent list 
        of ticks corresponding to each of the number
    """
    max_number = max(filter(lambda x : type(x)==int,numbers))
    # If the maxium number is 0, then all the numbers should be 0
    # coz we have called handle_negatives prior to this function
    if max_number == 0 :
        return upticks[0]*len(numbers)
    else:
        normalized_numbers = [ float(x)/max_number if type(x)==int else x for x in numbers ]
        upticks_indexes = [ int(math.ceil(x*len(upticks))) if type(x)==float else x for x in normalized_numbers ]
        return ''.join([ ' ' if type(x)==str else upticks[x-1] if x != 0 else upticks[0] for x in upticks_indexes ])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='patanga argument parser')
    parser.add_argument('-c',
                        dest='color',
                        action='store',
                        type=str,
                        required=False,
                        choices=COLORS.keys(),
                        help="Valid colors are {0}".format('\n'.join(COLORS.keys()))
                        )
    parser.add_argument('-v',
                        action='version',
                        version='patanga {}'.format(_get_version()))
    commandline_options, input_numbers = parser.parse_known_args()
    # Convert strings to integers if possible
    numbers = []
    for x in input_numbers:
        try:
            numbers.append(int(x))
        except ValueError:
            numbers.append(x)
    if commandline_options.color:
        print(u"{0}{1}{2}".format(COLORS[commandline_options.color],
                                 _draw_tickgram(_handle_negatives(numbers)),
                                 RESET
                                 )
             )
    else:
        print(_draw_tickgram(_handle_negatives(numbers)))