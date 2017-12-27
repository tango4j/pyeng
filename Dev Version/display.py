__author__ = 'inctrl'

import os.path


def clear_screen():
    '''
    Clear the current screen.
    This module has been built to future use of GUI units.

    :return:
    '''

    os.system('clear')
    return 0


def print_screen(*args):
    '''
    Print module:
    This module has been built to future use of GUI units.

    :param input_str:
    :return:
    '''

    # input_str = ''.join(args)
    input_str = ','.join([str(i) for i in args])
    print(input_str)

    return 0

def prompt_type(line_count, len_list):
    '''
    This module is for the input prompt and type input.

    :param line_count:
    :param len_list:
    :return input_val:
    '''

    if line_count == (len_list[1]-1):
        print_screen ('')

    print_screen('Type in:')
    input_val = input()

    return input_val # Return the value that was received by the user.

def prompt_question():
    '''

    :return input val:
    '''

    # print_screen('Type in:')
    input_val = input()

    return input_val # Return the value that was received by the user.
