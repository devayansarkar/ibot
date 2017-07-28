"""importing required modules"""
import re
import collections

def words_in_file(text):
    """finds all words in the corpus"""
    return re.findall('[a-z]+',text.lower())

def train(features):
    """trains the model with text from corpus"""
    model = collections.defaultdict(lambda: 1)
    for feature in features:
        model[feature] += 1
    return model

NWORDS = train(words_in_file(open('corpus.txt',encoding='utf8').read()))
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def correct_text(text):
    """splits the text into string and corrects it word by word"""
    words = text.split()
    for word in words:
        corrected_word = correct_word(word)
        if corrected_word is not word:
           text = text.replace(word,corrected_word)
    return text

def correct_word(word):
    """corrects word by word"""
    candidates = known_word([word]) or known_word(known_with_one_edit(word)) or  known_with_two_edits(word) or [word]
    return max(candidates, key=NWORDS.get)

def known_word(words):
    """known words"""
    return set(w for w in words if w in NWORDS)

def known_with_one_edit(word):
    """known with one edit"""
    s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in s if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in s for c in ALPHABET if b]
    inserts    = [a + c + b     for a, b in s for c in ALPHABET]
    return set(deletes + transposes + replaces + inserts)

def known_with_two_edits(word):
    """known with two edits"""
    return set(e2 for e1 in known_with_one_edit(word) for e2 in known_with_one_edit(e1) if e2 in NWORDS)