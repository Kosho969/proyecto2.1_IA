
import random
import sys
from clasificador import Clasificador
from general_functions import *

ham_training_messages = convert_to_list('train_ham.txt')
spam_training_messages = convert_to_list('train_spam.txt')

original_messages = convert_to_list('test_file.txt')
messages_to_classify = sanitize_classified_messages(original_messages)
original_messages = convert_to_list('test_file.txt')

print(original_messages[-1])
print(messages_to_classify[-1])

clasificador = Clasificador(ham_training_messages, spam_training_messages)

results = []
for i in range(len(messages_to_classify)):
    probability = clasificador.classify_message(messages_to_classify[i], clasificador.SPAM_MESSAGE, 0.001)
    if probability >= 0.7:
        results.append('spam\t{}'.format(original_messages[i]))
    else:
        results.append('ham\t{}'.format(original_messages[i]))

write_message(results, "results.txt")