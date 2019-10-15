import csv
import os
import translate

# Options for input_lang and output_lang
German = 'de'
English = 'en'


def translate_list(wordlist, input_lang, output_lang, file_dest):
    """
    Takes a list of words as a .csv file with 1 column and writes a new .csv file with the translation of
    the words in the second column.
    :param wordlist: path to a .csv file of words
    :param input_lang: The language of the input file
    :param output_lang: The language to which to translate the words
    :param file_dest: The path to which to write the new .csv file
    """

    # read input file
    with open(wordlist, 'r') as csvfile:
        reader = csv.reader(csvfile)
        vocablist = list(reader)

    # create translator
    translator = translate.Translator(from_lang=input_lang, to_lang=output_lang)

    # translate
    for row in vocablist:
        row.append(translator.translate(row[0]))

    # write resulting vocab list to .csv file
    with open(file_dest + '/' + os.path.splitext(os.path.basename(wordlist))[0] + '.csv', 'w+', newline='',
              encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in vocablist:
            writer.writerow(row)