import re
import random
import sys
from clasificador import Clasificador

'''
Sanitization involves removing all non-letter characters and removing
words consisting in one only letter
'''
def sanitize_classified_messages(messages):
    regex = re.compile('[^a-zA-Z]')

    for i in range (len(messages)):
        messages[i] = regex.sub(' ', messages[i])
        messages[i] = re.sub(' +', ' ', messages[i])
        # TODO: convert message to lowercase
        messages[i] = ' '.join([
            w for w in messages[i].split() if len(w) > 1
        ])

    return messages

def debug_messages(messages):
    for message in messages:
        print("=================")
        print(message)
        print("\n")

def remove_elements(messages,index):
    del messages[0:index + 1]
    return messages

ham_messages = []
spam_messages = []

with open('corpus.txt') as f:
    for line in f: 
        # print(line, end='')
        value = line.split('\t')

        if value[0] == 'ham':
            ham_messages.append(value[1])
        else:
            spam_messages.append(value[1])

spam_messages = sanitize_classified_messages(spam_messages)
ham_messages = sanitize_classified_messages(ham_messages)

random.shuffle(spam_messages)
random.shuffle(ham_messages)

# print(len(ham_messages))

# TODO:  Optimize with method 

# Build ham messages list
training_percentage = round(len(ham_messages) * 0.8)
ham_training_messages = [ham_messages[i] for i in range(training_percentage)]
ham_messages = remove_elements(ham_messages, training_percentage)

cv_percentage = round(len(ham_messages) / 2)
ham_cross_validation_messages = [ham_messages[i] for i in range(cv_percentage)]
ham_messages = remove_elements(ham_messages,cv_percentage)
ham_test_messages = ham_messages

# Build spam messages list
training_percentage = round(len(spam_messages) * 0.8)
spam_training_messages = [spam_messages[i] for i in range(training_percentage)]
spam_messages = remove_elements(spam_messages,training_percentage)

cv_percentage = round(len(spam_messages) / 2)
spam_cross_validation_messages = [spam_messages[i] for i in range(cv_percentage)]
spam_messages = remove_elements(spam_messages,cv_percentage)
spam_test_messages = spam_messages

# clasificador = Clasificador(ham_training_words, spam_training_words)

clasificador = Clasificador(
    ['play sports today', 'went play sports', 'secret sports event', 'sports is today', 'sports cost money'],
    ['offer is secret', 'click secret link', 'secret sports link']
)

# TODO: Implementar clasificador.get_performance(test_messages_dict, k)
#   test_messages_dict: [
#     ('Test message 1', spam),
#     ('Test message 1', spam),
#     ('Test message 1', spam),
#     ('Test dsa 1', ham),
#     ('Test message', ham),
#     ('Test mesadfgasd 1', ham),
#   ]
#
#   1. Clasificar cada mensaje, agregar la lista P 1 si acerto con type, y 0 si no acerto
#   2. retornar la suma de valores divido el total de elementos
#       [1, 0, 0, 0, 1, 0]: Performance: 2 / 6

# print(clasificador.getPerformance(['ham test message 1', 'ham test message 2'], ham, 1))
# print(clasificador.getPerformance(['spam test message 1', 'spam test message 2'], spam, 1))

# TODO (forma chafa): Definir un listado de 10 valores diferentes para k
#   Iterar sobre cada valor de k, obteniendo el performance para spam y ham
#   Devolver el K que genere los valores más altos de spam y ham

# TODO get_best_k_performance(x1, x2, iteracion):
#   0. Si iteracion == maxIteraciones:
#       if (clasificador.getPerformance(messagesList, x1) > clasificador.getPerformance(messagesList, x2))
#           return x1
#       else
#           return x2
#
#   1. Calcular un x3 intermedio (promedio de x1 y x2)
# 
#   2. Computar clasificador.getPerformance(messagesList, P) para [x1, x2, x3]
# 
#   3. Si los dos mas grandes son x1 y x3, retornar get_best_k_performance(x1, x3, iteracion + 1)
# 
#   4. Si los dos más grandes son x2 y x3, retornar get_best_k_performance(x2, x3, iteracion + 1)
# 
#   5. Si los dos más grandes son x1 y x2, reteornar get_best_k_performance(max(x1, x2), x3, iteracion + 1)
