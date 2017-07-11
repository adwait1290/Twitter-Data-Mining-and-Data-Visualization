# # Print most common words in a corpus collected from Twitter
# #
# # Full description:
# # http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
# # http://marcobonzanini.com/2015/03/09/mining-twitter-data-with-python-part-2/
# # http://marcobonzanini.com/2015/03/17/mining-twitter-data-with-python-part-3-term-frequencies/
# #
# # Run:
# # python twitter_most_common_words.py <filename.jsonl>

# import sys
# import json
# from collections import Counter
# import re
# from nltk.corpus import stopwords
# import string
 
# punctuation = list(string.punctuation)
# stop = stopwords.words('english') + punctuation + ['rt', 'via', '.', '\u2026']
 
# emoticons_str = r"""
#     (?:
#         [:=;] # Eyes
#         [oO\-]? # Nose (optional)
#         [D\)\]\(\]/\\OpP] # Mouth
#     )"""
 
# regex_str = [
#     emoticons_str,
#     r'<[^>]+>', # HTML tags
#     r'(?:@[\w_]+)', # @-mentions
#     r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
#     r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
#     r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
#     r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
#     r'(?:[\w_]+)', # other words
#     r'(?:\S)' # anything else
# ]
    
# tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
# emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
# def tokenize(s):
#     return tokens_re.findall(s)
 
# def preprocess(s, lowercase=False):
#     tokens = tokenize(s)
#     if lowercase:
#         tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
#     return tokens


# if __name__ == '__main__':
#     fname = sys.argv[1]

#     with open(fname, 'r') as f:
#         count_all = Counter()
#         for line in f:
#             tweet = json.loads(line)
#             tokens = preprocess(tweet['text'])
#             count_all.update(tokens)
# print(count_all.most_common(5))

# Chap02-03/twitter_term_frequency.py
import sys
import string
import json
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

def process(text, tokenizer=TweetTokenizer(), stopwords=[]):
    """Process the text of a tweet:
    - Lowercase
    - Tokenize
    - Stopword removal
    - Digits removal
    Return: list of strings
    """
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    # If we want to normalize contraction, uncomment this
    tokens = normalize_contractions(tokens)
    return [tok for tok in tokens if tok not in stopwords and not tok.isdigit()]

def normalize_contractions(tokens):
    """Example of normalization for English contractions.
    Return: generator
    """
    token_map = {
        "i'm": "i am",
        "you're": "you are",
        "it's": "it is",
        "we're": "we are",
        "we'll": "we will",
    }
    for tok in tokens:
        if tok in token_map.keys():
            for item in token_map[tok].split():
                yield item
        else:
            yield tok

if __name__ == '__main__':
    tweet_tokenizer = TweetTokenizer()
    punct = list(string.punctuation)
    stopword_list = stopwords.words('english') + punct + ['rt', 'via', '\u2026', 'twitter','president','account','—','\'','u','us','https','new','one','says','get','#trump','donald','like','weeks','...','\"','\"','de']

    fname = sys.argv[1]
    tf = Counter()
    with open(fname, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            tokens = process(text=tweet.get('text', ''),
                             tokenizer=tweet_tokenizer,
                             stopwords=stopword_list)
            tf.update(tokens)
        for tag, count in tf.most_common(30):
            print("{}: {}".format(tag, count))
