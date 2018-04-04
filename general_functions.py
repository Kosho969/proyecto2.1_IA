import re
'''
Sanitization involves removing all non-letter characters and removing
words consisting in one only letter
'''
def sanitize_classified_messages(messages):
    regex = re.compile('[^a-zA-Z]')
    result = []

    for i in range (len(messages)):
        messages[i] = regex.sub(' ', messages[i])
        messages[i] = re.sub(' +', ' ', messages[i])
        messages[i] = ' '.join([
            w for w in messages[i].split() if len(w) > 1
        ])
        messages[i] = messages[i].lower()

    return messages

def debug_messages(messages):
    for message in messages:
        print("=================")
        print(message)
        print("\n")

def remove_elements(messages,index):
    del messages[0:index + 1]
    return messages

def write_message(messages,name):
    outF = open(name, "w")
    for line in messages:
      # write line to output file
      outF.write(line)
      outF.write("\n")
    outF.close()

def convert_to_list(file_name):
    messages = []

    with open(file_name) as f:
        for line in f: 
            # print(line, end='')
            messages.append(line)

    return messages