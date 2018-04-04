from collections import Counter
import functools

class Clasificador():

    SPAM_MESSAGE = 1;

    HAM_MESSAGE = 0;

    def __init__(self, ham_messages_list, spam_messages_list):
        self.ham_messages_list = ham_messages_list
        self.spam_messages_list = spam_messages_list
        self.ham_words_frequence_dictionary = self.generate_word_bank(ham_messages_list)
        self.spam_words_frequence_dictionary = self.generate_word_bank(spam_messages_list)

    def generate_word_bank(self, messages):
        words = []

        for message in messages:
            words.extend(message.split(' '))

        return Counter(words)

    '''
    Returns the ocurrences of word in the dictionary defined by type (ham or spam)
    '''
    def count_word_ocurrences_of_type(self, word, type):
        if (type == self.SPAM_MESSAGE):
            return self.spam_words_frequence_dictionary[word]
        else:
            return self.ham_words_frequence_dictionary[word]

    '''
    Returns the amount of words (with their ocurrences) in the dictionary defined by type
    '''
    def count_total_ocurrences_of_type(self, type):
        if (type == self.SPAM_MESSAGE):
            return sum(self.spam_words_frequence_dictionary.values())
        else:
            return sum(self.ham_words_frequence_dictionary.values())

    '''
    Returns the amount of distinct words both in spam and ham
    '''
    def count_distinct_words(self):
        return len(self.ham_words_frequence_dictionary + self.spam_words_frequence_dictionary)

    def get_messages_list(self, type):
        if (type == self.SPAM_MESSAGE):
            return self.spam_messages_list
        else:
            return self.ham_messages_list

    def get_count_messages(self):
        return len(self.spam_messages_list) + len(self.ham_messages_list)

    '''
    Return the probability of a message being that word, given message is of
    type type (total probability)
    '''
    def get_probability_of_word(self, message, type, k):
        # Whats the probability of any message of being of type 'type'
        if (message == None):
            return (len(self.get_messages_list(type)) + k) / (self.get_count_messages() + k * 2)

        return (
            (self.count_word_ocurrences_of_type(message, type) + k)
                / (
                    self.count_total_ocurrences_of_type(type)
                        + k * self.count_distinct_words()
                )
        )

    def get_inverse_type(self, type):
        if (type == self.SPAM_MESSAGE):
            return self.HAM_MESSAGE
        else:
            return self.SPAM_MESSAGE

    def classify_message(self, message, type, k):
        N = message.split(' ')

        # Multiplicatoria_{p in N} (clasificar(p, X)) * clasificar(null, X, K)
        upperFactor = functools.reduce(
            lambda x, y: x * y,
            [self.get_probability_of_word(word, type, k) for word in N]
        ) * self.get_probability_of_word(None, type, k)

        # Multiplicatoria_{p in N} (clasificar(p, !X)) * clasificar(null, !X, K)
        lowerFactor = functools.reduce(
            lambda x, y: x * y,
            [self.get_probability_of_word(word, self.get_inverse_type(type), k) for word in N]
        ) * self.get_probability_of_word(None, self.get_inverse_type(type), k)
        # print(upperFactor)
        # print(lowerFactor)

        return upperFactor / (upperFactor + lowerFactor)

    def get_performance(self,test_messages,k):
        successes = []
        for i in range(len(test_messages)):
            probability = self.classify_message(test_messages[i][0],self.SPAM_MESSAGE, k)
            type_of_message = test_messages[i][1]
            if probability >= 0.7:
                if(type_of_message == 1):
                    successes.append(1)
                else:
                    successes.append(0)
            else:
                if(type_of_message == 0):
                    successes.append(1)
                else:
                    successes.append(0)
        #print(successes)
        return successes.count(1)/len(successes)
