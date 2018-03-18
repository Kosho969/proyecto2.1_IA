import re
import random

def sanitize_classified_messages(messages):
    regex = re.compile('[^a-zA-Z]')
    for i in range (len(messages)):
        messages[i] = regex.sub(' ',messages[i])
        messages[i] = re.sub(' +',' ',messages[i])
        messages[i] = ' '.join( [w for w in messages[i].split() if len(w)>1] )
    return messages

def debug_messages(messages):
    for message in messages:
        print("=================")
        print(message)
        print("\n")

def remove_elements(messages,index):
    del messages[0:index+1]
    return messages

def 

ham_messages = []
spam_messages = []

with open('corpus.txt') as f:
    for line in f: 
        print(line, end='')
        value = line.split('\t')
        if value[0] == 'ham':
            ham_messages.append(value[1])
        else:
            spam_messages.append(value[1])

spam_messages = sanitize_classified_messages(spam_messages)
ham_messages = sanitize_classified_messages(ham_messages)

random.shuffle(spam_messages)
random.shuffle(ham_messages)

print(len(ham_messages))

# TODO :  Optimize with method 
training_percentage = round(len(ham_messages)*0.8)

ham_training_messages = [ham_messages[i] for i in range(training_percentage)]
ham_messages = remove_elements(ham_messages,training_percentage)

cv_percentage = round(len(ham_messages)/2)
ham_cross_validation_messages = [ham_messages[i] for i in range(cv_percentage)]
ham_messages = remove_elements(ham_messages,cv_percentage)

ham_test_messages = ham_messages

training_percentage = round(len(spam_messages)*0.8)

spam_training_messages = [spam_messages[i] for i in range(training_percentage)]
spam_messages = remove_elements(spam_messages,training_percentage)

cv_percentage = round(len(spam_messages)/2)
spam_cross_validation_messages = [spam_messages[i] for i in range(cv_percentage)]
spam_messages = remove_elements(spam_messages,cv_percentage)

spam_test_messages = spam_messages

print(len(ham_training_messages))
print(len(ham_cross_validation_messages))
print(len(ham_test_messages))


print(len(spam_training_messages))
print(len(spam_cross_validation_messages))
print(len(spam_test_messages))


