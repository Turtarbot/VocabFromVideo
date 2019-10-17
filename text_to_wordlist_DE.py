# Copyright (C) 2019  Patricia C. Zauleck

import os
import spacy
import csv


def text_to_wordlist(filepath):
    """
    Takes a file of German text and converts it into a list of all basic forms of the words used in the text.
    Duplicates are removed and the list saved to a .csv file.
    :param filepath: Path of a textfile as a string
    :return: Path to the created .csv file as a string
    """

    # load german language model
    # tagger, parser and text categorizer are disabled because they are not needed
    nlp_german = spacy.load("de_core_news_sm", disable=['tagger', 'parser', 'textcat'])

    # open textfile
    textfile = open(filepath, 'r')
    text = textfile.read()

    # convert text to spacy
    tokens = nlp_german(text)

    # write word baseforms to a list, skip duplicates
    # numbers, whitespaces and punctuation are ignored
    wordlist = []
    for token in tokens:
        if not token.is_space and not token.is_digit and not token.is_punct:
            if token.lemma_ not in wordlist:
                wordlist.append(token.lemma_)

    # write resulting list to .csv file in one column
    if not os.path.exists('tmp'):
        os.mkdir('tmp')
    wordlist_path = 'tmp/' + os.path.splitext(os.path.basename(filepath))[0] + '.csv'
    with open(wordlist_path, 'w+', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for word in wordlist:
            writer.writerow([word])

    return wordlist_path
