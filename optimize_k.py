import random
import sys
from clasificador import Clasificador
from general_functions import *




ham_training_messages = convert_to_list('train_ham.txt')
spam_training_messages = convert_to_list('train_spam.txt')
ham_cross_validation_messages = convert_to_list('cv_ham.txt')
spam_cross_validation_messages = convert_to_list('cv_spam.txt')

clasificador = Clasificador(ham_training_messages, spam_training_messages)

# clasificador = Clasificador(
#     ['play sports today', 'went play sports', 'secret sports event', 'sports is today', 'sports cost money'],
#     ['offer is secret', 'click secret link', 'secret sports link']
# )

test_messages_dict = [(message, clasificador.SPAM_MESSAGE) for message in spam_cross_validation_messages]

for message in ham_cross_validation_messages:
    test_messages_dict.append((message, clasificador.HAM_MESSAGE))

#print(clasificador.get_performance(test_messages_dict, 2))

optimizations = []
k = 0.001
for i in range(0, 1000):
    optimizations.append((clasificador.get_performance(test_messages_dict, k), k))
    k += 0.01
    print(optimizations[-1])

