__author__ = 'mac'

# import csv
# import os
#
# print(os.path.isfile('test.csv'))
#
# with open('test.csv', 'w', newline='') as fp:
#    a = csv.writer(fp, delimiter=',')
#    # a = csv.writer(fp)
#    data = [['Me', 'You'],
#            ['293', '219'],
#            ['54', '13']]
#    a.writerows(data)
#
# import csv
# with open('test.csv', 'r+') as csvfile:
#    spamreader = csv.reader(csvfile)
#    for row in spamreader:
#        print(row)

# from wordnik import *
# import wordnik
# apiUrl = 'http://api.wordnik.com/v4'
# apiKey = 'YOUR API KEY HERE'
# client = swagger.ApiClient(apiKey, apiUrl)
#
# wordApi = WordApi.WordApi(client)
# example = wordApi.getTopExample('irony')
# print example.text
#
# #
# from nltk.corpus import wordnet
# # Get a collection of synsets (synonym sets) for a word
# synsets = wordnet.synsets('potato' )
# # Print the information
# for synset in synsets:
#     print("-" * 10)
#     print("Name:", synset.name)
#     print("Lexical Type:", synset.lexname)
#     print("Lemmas:", synset.lemma_names)
#     print("Definition:", synset.definition)
#     # for example in synset.examples:
#     #     print("Example:", example)

from module import *
import numpy


TodayTraining = ThisStudy()

ass = 'the table has been turned. '

print ('Last char', ass[len(ass)-1])
print (ass[len(ass)-1]==' ')
print ('length of ass, before', len(ass))
print (TodayTraining.delete_blank(ass))
css = TodayTraining.delete_blank(ass)
print ('length of ass, after', len(TodayTraining.delete_blank(ass)))


bss = 'the table has been turned.'
print (ass)
print (css)
print ('Is this True?', bss == css )

ga = ':param steady_message: This message lingers on the top of the screen, while every time you type a sentences.'
print ('length of ga', len(ga))

kp = numpy.arange(0,1,0.1)
print (list(kp))
print ('result of round', np.around(kp, decimals=3) )

print ('Lin Alg  out:', TodayTraining.lin_reg_out(100))

print (list(numpy.linspace(0, 1, 0.2)))


fuck = [1, 2]

print('True???:' ,1 in fuck)
