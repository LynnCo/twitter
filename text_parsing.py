import re
import nltk
import subprocess
from nltk.corpus import stopwords

def remove_punctuation_regex(string):
    string = re.sub(r'[.,\'<>\"#%^~?!*-]', '', string)
    return string

def remove_short_words(string):
    string = re.sub(r'\b[A-Z]{1,2}\b', '', string, flags=re.IGNORECASE)
    return string

def remove_RTs(string):
    string = re.sub(r'\bRT\b', '', string, flags=re.IGNORECASE)
    return string

def remove_mentions(string):
    string = re.sub(r'@.+?\b', '', string, flags=re.IGNORECASE)
    return string

def remove_links(string):
    string = re.sub(r'http.*\b', string)
    return string

# !!! completely breaks with nonenglish words
# def remove_non_words(string):
#     string = re.sub(r'\b![A-Z]+\b', '', string, flags=re.IGNORECASE)
#     return string

def remove_punctuation_from_list(word_list):
    word_list = [word for word in word_list if not re.match(r'^([.,\'<>\"#%^~?!*-])*$', word, flags=re.IGNORECASE)]
    return word_list

def remove_stop_words_from_list(word_list):
    word_list = [word for word in word_list if word not in set(stopwords.words('english'))]
    return word_list

def create_poem(twitter):
    timeline = [str(x['text']) for x in  twitter.get_home_timeline(count=200, trim_user=True)]
    filename = 'words/{}.txt'.format(twitter.verify_credentials()['screen_name'])
    print('made file for {}'.format(filename))
    with open(filename, 'w') as f:
        for line in timeline:
            line = remove_RTs(line)
            line = remove_mentions(line)
            line = remove_links(line)
            f.write(line+'\n')
    subprocess.call('prosaic corpus loadfile {}'.format(filename), shell=True)
