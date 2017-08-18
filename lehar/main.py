# -*- coding: utf-8 -*-

# https://github.com/darxtrix/lehar
# author @darxtrix

import argparse, math, os, sys

# https://en.wikipedia.org/wiki/Block_Elements
upticks = u'▁▂▃▄▅▆▇█'

RESET = '\033[0m'

COLORS = {
    'black' : '\033[30m',
    'red' : '\033[31m',
    'green' : '\033[32m',
    'orange' : '\033[33m',
    'blue' : '\033[34m',
    'purple' : '\033[35m',
    'cyan' : '\033[36m',
    'light_grey' : '\033[37m',
    'dark_grey' : '\033[90m',
    'light_red' : '\033[91m',
    'light_green' : '\033[92m',
    'yellow' : '\033[93m',
    'light_blue' : '\033[94m',
    'pink' : '\033[95m',
    'light_cyan' : '\033[96m'
}

SUPPORTED_COLORS = COLORS.keys()

def _get_version():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path,'VERSION'),'r') as f:
        return f.read().strip()

def _sanitize_numbers(uncleaned_numbers):
    """
        Convert strings to integers if possible
    """
    cleaned_numbers = []
    for x in uncleaned_numbers:
        try:
            cleaned_numbers.append(int(x))
        except ValueError:
            cleaned_numbers.append(x)
    return cleaned_numbers


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


def draw(numbers,color=None):
    numbers = _sanitize_numbers(numbers)
    if len(numbers) == 0:
        return u""
    if color:
        return u"{0}{1}{2}".format(COLORS[color],
                                 _draw_tickgram(_handle_negatives(numbers)),
                                 RESET
                                 )
    else:
        return _draw_tickgram(_handle_negatives(numbers))


def main():
    parser = argparse.ArgumentParser(description='lehar argument parser')
    parser.add_argument('-c',
                        dest='color',
                        action='store',
                        type=str,
                        required=False,
                        choices=SUPPORTED_COLORS,
                        help="Valid colors are {0}".format(' '.join(COLORS.keys()))
                        )
    parser.add_argument('-v',
                        action='version',
                        version='lehar {}'.format(_get_version())
                        )
    # When the input is piped in or redirected from a file 
    if not sys.stdin.isatty(): 
        # argparse reads from a list in format ["-c","yellow","1","2"."3","4","5"] but read gives single chars
        commandline_options, input_numbers = parser.parse_known_args(sys.stdin.read().rstrip().split(" "))
        # Perform cleaning of commandline options to rempve spaces/new_lines
        input_numbers = [x.strip() for x in input_numbers]
        input_numbers = list(filter(lambda x : x!='',input_numbers))
    else:
        commandline_options, input_numbers = parser.parse_known_args()

    # Exit if no data supplied 
    if len(input_numbers) == 0:
        sys.stdout.write("No data supplied, exiting.\n")
        sys.exit(0)

    numbers = _sanitize_numbers(input_numbers)
    if commandline_options.color:
        print(u"{0}{1}{2}".format(COLORS[commandline_options.color],
                                 _draw_tickgram(_handle_negatives(numbers)),
                                 RESET
                                 )
             )
    else:
        print(_draw_tickgram(_handle_negatives(numbers)))


if __name__ == '__main__':
    main()
