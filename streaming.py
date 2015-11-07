import twython
from env import TWITTER_ENV
# from text_parsing import *

class WordContainer(object):

    def __init__(self):
        self.words = {}

    def add_string(self, string):
        # print(string) # preprocessed string
        string = string.lower()
        string = remove_RTs(string)
        # print(string) # postprocessed string
        self.count_words(string)

    def count_words(self, word_list):
        for word in string.split():
            try:
                self.words[word] += 1
            except KeyError:
                self.words[word] = 1
        print(sorted(self.words.items(), key=lambda item: item[1]))

class PrintStreamer(twython.TwythonStreamer):

    def on_success(self, data):
        if 'text' in data:
            print(data['text'])

    def on_error(self, status_code, data):
        print('error status code: {}\n{}'.format(status_code, data))

class ContainerStreamer(twython.TwythonStreamer):

    def on_success(self, data):
        if 'text' in data:
            self.container.add_string(data['text'])

    def on_error(self, status_code, data):
        print('error status code: {}\n{}'.format(status_code, data))

# stream = ContainerStreamer(*TWITTER_ENV)
# stream.container = WordContainer()

stream = PrintStreamer(*TWITTER_ENV)

if __name__ == '__main__':
    stream.user()
