__author__ = 'inctrl'

from module import *

def main():

    TodayTraining = ThisStudy()  # Declare a 'ThisStudy' class.
    TodayTraining.main_prompt_screen()  # Prompt a start message.
    TodayTraining.ask_the_group()  # Ask the group
    TodayTraining.ask_the_dic()  # Ask the dictionary
    TodayTraining.ask_the_mode()  # Ask the mode
    TodayTraining.read_file()  # Read Target Language and Supporting Language files
    TodayTraining.study_loop_main()  # The main loop file.

pass

if __name__ == '__main__':
    main()