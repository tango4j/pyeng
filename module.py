# -*-coding:utf-8 -*-
__author__ = 'inctrl'
from display import *
import datetime
import calendar
import random
import math
import os.path
import csv
import numpy as np
from numpy.linalg import inv

from display import *

class ThisStudy:
    def __init__(self):

        self.mode = 0  # Study mode variable
        self.group_index_out = 0  # Group index
        self.dic_index_out = 0  # Dictionary index within a group
        self.filename = '' # Dictionary index within a group
        self.number_of_group = 2

        # The coefficient to calculate the number of blank
        self.min_level = 2
        self.max_level = 5
        self.min_sent_length = 20
        self.max_sent_length = 120

        # The variables from the log file:
        self.csv_dictionary = {}

        # The field names.
        self.fieldnames = []

        # The current list of class: ThisStudy
        self.list_kor = []
        self.list_eng = []
        self.list_log = []

        pass

    def lin_reg_out(self, in_len):  # Linear regression function to set the level of sentence reconstruction.

        Y = np.array([[self.min_level],
                      [self.max_level]])
        A = np.array([[1, self.min_sent_length],
                      [1, self.max_sent_length]])

        coeff = np.dot(inv(A), Y)  # Linear regression

        out_level = coeff[1] * in_len + coeff[0]

        return out_level

    def sentence_eraser(self, list_eng, degree):
        '''
        The module that blanks the sentence.

        :param list_eng:
        :param degree:
        :return erased_sent:
        :return key_words:

        '''
        split_sent = list_eng.split()  # Split the sentence with regard to spacing.
        len_sent = len(split_sent)  # Length of the splited sentence
        num_of_erase = int(math.floor(len_sent * degree))  # the number of blanks to be erased.
        ones_zeros = [1] * num_of_erase + [0] * (len_sent - num_of_erase)
        random.shuffle(ones_zeros)
        key_words = []

        for idx, words in enumerate(split_sent):
            if ones_zeros[idx] == 1:
                key_words.append(split_sent[idx])  # append the splited words.
                split_sent[idx] = '_' * len(split_sent[idx])  # Blank the word with the same length of underlines.

        erased_sent = ' '.join(split_sent)  # Put together all the erased splited words.
        key_words = ' '.join(key_words)  # Put together all the splited keywords.

        return erased_sent, key_words

    def word_classifier(self, mytext):
        pass

    def sentence_shuffler(self, list_eng):

        split_sent = list_eng.split()
        random.shuffle(split_sent)
        shuffle_out = ' | '.join(split_sent)
        shuffle_out = '| ' + shuffle_out + ' |'
        return shuffle_out

    def read_dic_table(self):
        '''
        inctrl:
        This function contains list of dictionary names.
        Modify 'pyEng_dic' if you want to change the dictionary.

        :param my_date: The day of the week which has an index range of 0 to 6.
        :return pyEng_dic[my_date]: Return a dictionary name.
        '''

        # The keys for dictionaries.
        pyEng_dic = [['paper_ex1',
                      'wiki_edu1',
                      'esst2_file',
                      'wiki_tec1',
                      'brain_drain',
                      'capitalism',
                      'esst3_file'],
                     
                     ['article1',
                      'short_rand1',
                      'short_rand2',
                      'short_rand3',
                      'short_rand4',
                      'short_rand5',
                      'short_rand6'],

                     ['brain_drain2',
                      'esst1_file',
                      'randex_L0',
                      'randex_L1',
                      'RoteLearning',
                      'wiki_Korea',
                      'wiki_Korea']
                     ]

        pyEng_folder = ['textdata0',
                        'textdata1',
                        'textdata2',
                        'textdata3',]

        # Sets field names for the logfile
        self.fieldnames = ['Total Trials', 'Completed Trials', 'Recent date', 'F4', 'F5']

        self.number_of_group = len(pyEng_dic)

        return pyEng_dic, pyEng_folder, self.fieldnames


    def make_csv(self, total_path_name):

        pyEng_dic, pyEng_folder, fieldnames = self.read_dic_table()

        try:
            with open(total_path_name, 'w') as myfile:

                mydict = dict()
                for idx, item in enumerate(fieldnames):
                    mydict.update({fieldnames[idx]:0})

                # mydict = {fieldnames[0]: 0, 'Completed Trials': 0 }
                writer = csv.DictWriter(myfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(mydict)

        except IOError:
            print_screen('An error has occurred trying to create the flie:', total_path_name)

    def read_csv(self, group_num, idx ):

        pyEng_dic, pyEng_folder, _ = self.read_dic_table()

        group_index_out = group_num
        filename = pyEng_dic[group_index_out - 1][idx - 1]

        # Read CSV file from the directory.
        total_path_csv = str(os.getcwd()) + '/' + pyEng_folder[
            group_index_out - 1] + '/' + filename + '_rec.csv'  # index - 1 to fit into python list index

        # Open CSV file using 'read' mode.
        try:
            with open(total_path_csv, 'r') as myfile:
                reader = csv.reader(myfile)
                rowNR=0
                for row in reader:
                    print(row)
                    # row_in_string = ''.join(str(e) for e in row)
                    if rowNR ==0:  # First row is item names. Get the names of items.
                        print('row1',row)
                        item_names = row

                    elif rowNR ==1:  # Second row is numbers. Get the numbers and make list.
                        print('row2',row)
                        values = row
                        self.csv_dictionary = dict(zip(item_names, values))
                    rowNR = rowNR + 1

                    # print(row[0])
                    # print_screen('Row from CSV File', str(rowNR), row)

        except IOError:
            print_screen('An error occurred trying to read the flie:', total_path_csv)



        # return out_list
        pass

    def write_csv(self, group_num, idx ):

        pyEng_dic, pyEng_folder, _ = self.read_dic_table()

        group_index_out = group_num
        filename = pyEng_dic[group_index_out - 1][idx - 1]

        # Read CSV file from the directory.
        total_path_csv = str(os.getcwd()) + '/' + pyEng_folder[
            group_index_out - 1] + '/' + filename + '_rec.csv'  # index - 1 to fit into python list index

        # Open CSV file using 'WRITE' mode.
        try:
            with open(total_path_csv, 'w', newline='') as myfile:
                write_log = csv.writer(myfile)

                row1 = self.fieldnames
                write_log.writerow(row1)

                row2 = [self.csv_dictionary['Total Trials'],
                        self.csv_dictionary['Completed Trials'],
                        self.csv_dictionary['Recent date'],
                        self.csv_dictionary['F4'],
                        self.csv_dictionary['F5']]
                write_log.writerow(row2)

        except IOError:
            print_screen('An error has occurred trying to write the flie:', total_path_csv)

        # return out_list
        pass

    def date_func(self):
        '''
        inctrl:
        Call datetime function and module to return date information.
        :return the day of the week, date info (all of them), index of the day of the week:
        '''

        my_date = datetime.datetime.today().weekday()
        today = str(datetime.datetime.today())
        weekofday = calendar.day_name[my_date]

        return weekofday, today, my_date

    def main_prompt_screen(self):
        '''
        inctrl:
        This function prints out the necessary commands for users:
        Displays the date of today and the dictionary according to the day

        :return message:
        '''

        clear_screen()

        # Call the data_func to get date information
        weekofday, today, my_date = self.date_func()
        pyEng_dic, pyEng_folder, _ = self.read_dic_table()

        # print_screen out the list of all dictionaries.
        for idx, item in enumerate(pyEng_dic):
            # If there is no log file, create one.
            self.csv_check_dic_group(idx + 1, item)

            # Display all the dictionaries on the screeen.
            self.display_dic_group(idx + 1, item)

        message = 'Today is ' + weekofday + ": " + today[:10]
        print_screen(message)

        return message

    def read_file(self):
        '''
        inctrl:
        Read files from 'textdata' folder.
        :return 0:
        '''

        weekofday, today, my_date = self.date_func()

        pyEng_dic, pyEng_folder, _ = self.read_dic_table()

        self.filename = pyEng_dic[self.group_index_out - 1][
            self.dic_index_out - 1]  # index - 1 to fit into python list index
        total_path = str(os.getcwd()) + '/' + pyEng_folder[
            self.group_index_out - 1] + '/' + self.filename + '.txt'  # index - 1 to fit into python list index
        total_path_kor = str(os.getcwd()) + '/' + pyEng_folder[
            self.group_index_out - 1] + '/' + self.filename + '_kor' + '.txt'  # index - 1 to fit into python list index
        total_path_csv = str(os.getcwd()) + '/' + pyEng_folder[
            self.group_index_out - 1] + '/' + self.filename + '_rec.csv'  # index - 1 to fit into python list index

        '''
        Open a Korean list and a English list.
        Save both lists into each variable.
        '''

        list_eng, list_kor = ['', '']

        self.read_csv(self.group_index_out, self.dic_index_out)

        ### Temporary Code ###
        print_screen('\n\n')
        print_screen('Total path: ', os.path.isfile(total_path))
        print_screen('Total path lang2: ', os.path.isfile(total_path_kor))
        print_screen('Total path csv: ', os.path.isfile(total_path_csv))
        print_screen(os.getcwd())

        input("Press Enter to continue...")

        # Load the file for Lang1(eng).
        try:
            with open(total_path, mode='r', encoding='cp949') as f_eng:
                self.list_eng = f_eng.readlines()
                f_eng.close()

        except IOError:
            print_screen('An error occurred trying to read the flie:', total_path)

        # Load the file for Lang2(kor).
        try:
            with open(total_path_kor, mode='r', encoding='cp949') as f_kor:
                self.list_kor = f_kor.readlines()
                f_kor.close()

        except IOError:
            print_screen('An error occurred trying to read the flie:', total_path_kor)

        # If there is no csv file, create a csv file that logs the status of the file/study.
        # if os.path.isfile(total_path_csv) == 0:



            # Make a csv log file.

        # self.make_csv(total_path_csv)

        return list_eng, list_kor,

    def question_with_sanity_check(self, bd):

        while 1:

            print_screen('Type an index.')
            dic_index = prompt_question()

            if dic_index in str(bd):

                idx_out = int(dic_index)
                break

            else:
                print_screen('You have entered an absurd number. Please do it again.')

        return idx_out

    def delete_blank(self, p_string):

        lstr = len(p_string)
        if lstr != 0:
            k = lstr - 1  # Get rid of the last index.
            stc = ' '

            while stc == ' ':
                stc = p_string[k]
                k -= 1
                if k == 0:
                    break

            out_string = p_string[0:(k + 2)]  # Return a string without blank at the end of the sentence.

        elif lstr == 0:
            out_string = ''

        return out_string


    def ask_the_group(self):
        '''
        Ask a question to user to select a DIC.
        :return dic_idx_out:
        '''

        print_screen('Choose the dictionary group.')

        # The possible range of dictionary indexes.
        dic_bd = list(range(1, self.number_of_group + 1))
        self.group_index_out = self.question_with_sanity_check(dic_bd)

        return self.group_index_out

    def ask_the_dic(self):
        '''
        Ask a question to user to seleprint_screenct a DIC.
        :return dic_idx_out:
        '''

        clear_screen()

        # print_screen out the list of all dictionaries.

        weekofday, today, my_date = self.date_func()
        pyEng_dic, pyEng_folder, _ = self.read_dic_table()

        idx = self.group_index_out
        # self.check_csv_dic_group(idx, pyEng_dic[idx - 1])
        self.display_dic_group(idx, pyEng_dic[idx - 1])

        # The possible range of dictionary indexes.

        print_screen('Choose the dictionary.')
        dic_bd = list(range(1, 8))
        self.dic_index_out = self.question_with_sanity_check(dic_bd)

        return self.dic_index_out


    def ask_the_mode(self):

        clear_screen()

        self.mode_str = ['[1] Standard', '[2] Review', '[3] Check mode']
        print_screen('Type a model of study loop...')
        print_screen(self.mode_str[0])
        print_screen(self.mode_str[1])
        print_screen(self.mode_str[2])

        mode_bd = list(range(1, len(self.mode_str) + 1))  # Set the range of mod

        self.mode = self.question_with_sanity_check(mode_bd)

        return self.mode

    def csv_check_dic_group(self, group_num, pyEng_dic_part):

        pyEng_dic, pyEng_folder, _ = self.read_dic_table()

        print_screen('CSV check and write for Group:' + str(group_num))
        for idx, item in enumerate(pyEng_dic_part):

            filename = pyEng_dic_part[
                idx - 1]  # index - 1 to fit into python list index

            total_path_csv = str(os.getcwd()) + '/' + pyEng_folder[
                group_num - 1] + '/' + filename + '_rec.csv'  # index - 1 to fit into python list index

            wd = str(calendar.day_name[idx])


            # self.completed_trials, self.total_trials = read_log_file(group_num, idx)
            if os.path.isfile(total_path_csv)==1:
                # self.make_csv(total_path_csv)
                pass
            else:
                self.make_csv(total_path_csv)
            # print_screen('[ ' + str(idx + 1) + ' : ' + wd + ' ]: ' + item + 'complete' + '/' + 'total_trial')

        print_screen('\n')


    def display_dic_group(self, group_num, pyEng_dic_part):

        print_screen('Group:' + str(group_num))
        for idx, item in enumerate(pyEng_dic_part):
            wd = str(calendar.day_name[idx])
            # complete, total_trial = read_log_file(group_num, idx)
            print_screen('[ ' + str(idx + 1) + ' : ' + wd + ' ]: ' + item + 'complete' + '/' + 'total_trial')

        print_screen('\n')

    def study_loop_main(self):

        # Study loop starts, so we update csv file.
        self.csv_dictionary['Recent date'] = str(datetime.datetime.today())
        self.csv_dictionary['Total Trials'] = str( int(self.csv_dictionary['Total Trials']) + 1 )

        # Update the CSV file.
        self.write_csv(self.group_index_out, self.dic_index_out)

        list_eng = self.list_eng
        list_kor = self.list_kor

        '''
        inctrl:
        :param steady_message: This message lingers on the top of the screen, while every time you type a sentences.
        :param list_eng: The list that contains English sentences.
        :param list_kor: The list that contains Korean sentences.
        :return: 0
        '''

        len_list = [len(list_eng), len(list_kor)]

        # assert (len_list[0]==len_list[1]), 'Error: The length of list_eng and list_kor must be the same.'

        flag = 1
        line_count = 0

        weekofday, today, my_date = self.date_func()
        # print_screen('Today is', weekofday[:]+'.')

        clear_screen()

        print_screen('[SYSTEM] Train Dictionary:[', self.filename, ']')
        print_screen('[SYSTEM] Mode of Loop:[', self.mode_str[self.mode - 1], ']')
        print_screen('[SYSTEM] Press ENTER to start.\n')
        input()

        clear_screen()

        while flag:

            '''
            inctrl:
            # The main studyloop #
            When the index of loop is in the loop,
            pop out question sentences.
            Firstly, pop out a Korean sentence (question).
            Secondly, display a model answer in English.
            '''

            if line_count < len_list[1]:  # Until we reach the end of the file.

                '''
                2-1.Display shuffled sentence.
                '''
                # mytext = nltk.word_tokenize(list_eng[line_count])
                # print_screen(str(nltk.pos_tag(mytext)))

                current_sentence = self.delete_blank(list_eng[line_count][:-1])
                len_sent = len(current_sentence)
                regressed_level = self.lin_reg_out(len_sent)
                wrong = 1

                regressed_er = np.arange(0.3, 1, (1 / regressed_level))  # The regressed level of blank.

                if self.mode == 1:
                    sent_er = regressed_er

                elif self.mode == 2:
                    sent_er = [0]

                elif self.mode == 3:
                    sent_er = regressed_er

                    print_screen(list_kor[line_count][:-1])  # Display the current Korean text (the current bullet)

                    # Display the index.
                    print_screen('[SYSTEM] This is bullet [' + str(line_count + 1) + '/' + str(len_list[1]) + '].')
                    print_screen('[SYSTEM] If you are certain, type in the sentence in English.')

                    input_val = prompt_type(line_count, len_list)
                    if input_val == current_sentence:
                        wrong = 0

                    else:
                        wrong = 1
                '''
                Sentence Learning Loop Start
                '''

                if self.mode in [1, 2] or (wrong == 1 and self.mode == 3):
                    for idx, degree in enumerate(sent_er):

                        clear_screen()  # Clear the screen

                        print_screen(list_kor[line_count][:-1])  # Display the current Korean text (the current bullet)
                        # Display the index.
                        print_screen('[SYSTEM] This is bullet [' + str(line_count + 1) + '/' + str(len_list[1]) + '].')
                        print_screen('[SYSTEM] Sentence blank level ' + str(idx + 1) + ' out of ' + str(len(sent_er)))
                        if self.mode == 3:
                            print_screen('[SYSTEM] Incorrect answer. Study mode has been activated.')

                        erased_sent, key_words = self.sentence_eraser(current_sentence,
                                                                      degree)  # Randomly blank the sentence.
                        shuffled_key_words = self.sentence_shuffler(key_words)  # Show shuffled words.

                        print_screen(shuffled_key_words + '\n')
                        print_screen(erased_sent + '\n')
                        input_val = self.delete_blank(prompt_type(line_count, len_list))

                '''
                3.Pop out the model answer in English if the last answer is wrong:
                '''
                if input_val != self.delete_blank(current_sentence):
                    self.correct_sentence(list_eng, line_count, len_list)

                clear_screen()
                if line_count < len_list[1]:
                    line_count += 1  # Heading to the next sentence.

            '''
            inctrl:
            # End of the studyloop #
            When the index of loop reaches the end,
            pop out a message that asks an intend to restart the loop.
            And I put some lines to prevent error cases.
            '''

            if line_count >= len_list[1]:  # End of study loop condition.

                # Update the CSV file.
                self.write_csv(self.group_index_out, self.dic_index_out)

                # Display messages.
                print_screen('This is end of the bullet. Do you want to repeat the training loop?')
                yon = input()

                if yon in ['y', 'Y', 'yes', 'Yes', 'YES']:
                    line_count = 0
                    clear_screen()

                elif yon in ['n', 'N', 'No', 'no', 'NO']:
                    print_screen('Abort pyEng.')
                    print_screen('Good bye! \n')
                    flag = 0

                else:

                    pass
        # Modify CSV file if the whole study loop has finished.
        if line_count >= len_list[1]:
            self.csv_dictionary['Completed Trials'] = str(int(self.csv_dictionary['Completed Trials']) + 1)
            self.write_csv(self.group_index_out, self.dic_index_out)


        return 0

    def correct_sentence(self, list_eng, line_count, len_list):

        print_screen('\n[SYSTEM] The correct answer:')
        print_screen(list_eng[line_count][:-1])
        input_val = prompt_type(line_count, len_list)
