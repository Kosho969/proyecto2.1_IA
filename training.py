import re

def sanitize_classified_messages(messages):
    regex = re.compile('[^a-zA-Z]')
    for message in messages:
        message[1] = regex.sub(' ',message[1])
        message[1] = re.sub(' +',' ',message[1])
        message[1] = ' '.join( [w for w in message[1].split() if len(w)>1] )
    return messages

ham_messages = []
spam_messages = []

with open('test.txt') as f:
    for line in f: 
        print(line, end='')
        value = line.split('\t')
        if value[0] == 'ham':
            ham_messages.append(value)
        else:
            spam_messages.append(value)

print('SPAM: \n', spam_messages)
spam_messages = sanitize_classified_messages(spam_messages)

print('HAM: \n', ham_messages)
print('SPAM: \n', spam_messages)

