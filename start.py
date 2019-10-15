import shutil
import argparse
import sys
import wordlist_to_vocablist as translator


def delete_tmp():
    """
    Delete temporary files.
    """
    shutil.rmtree('tmp')


def run():
    """

    """
    # define command line arguments
    parser = argparse.ArgumentParser(
        description='Create vocabulary lists as CSV files from Youtube videos or text files.')
    parser.add_argument('source', help="The URL or filepath from which to create a vocabulary list.")
    parser.add_argument('destination', help='The folder in which to store the created CSV file.')
    parser.add_argument('input_language', choices=["DE"])
    parser.add_argument('output_language', choices=["EN"])
    parser.add_argument('-t', '--input_type', default='Y', choices=['Y', 'T'], \
                        help='Specifies whether the input is a Youtube URL (Y) or a Textfile (T)',
                        metavar='input_type')
    parser.add_argument('-debug', default=False, type=bool, choices=[True, False], metavar='debug')

    args = parser.parse_args()

    if args.input_language == 'DE':
        input_language = translator.German
    else:
        print("invalid input language")
        sys.exit(-1)

    if args.output_language == 'EN':
        output_language = translator.English
    else:
        print("invalid output language")
        sys.exit(-1)

    # if the input is a Youtube URL, create a textfile form the video
    if args.input_type:
        if input_language == translator.German:
            from youtube_to_text_DE import youtube_to_text
        try:
            print("Starting youtube_to_text")
            textfile = youtube_to_text(args.source)
        except:
            if args.debug:
                print(sys.exc_info())
            else:
                delete_tmp()
                print("error in youtube_to_text")
            sys.exit(-1)
    else:
        textfile = args.source

    # create list of basic words from text
    if input_language == translator.German:
        from text_to_wordlist_DE import text_to_wordlist
    try:
        print("Starting text_to_wordlist")
        wordlist = text_to_wordlist(textfile)
    except:
        if args.debug:
            print(sys.exc_info())
        else:
            delete_tmp()
            print("error in text_to_wordlist")
        sys.exit(-1)

    # translate list of words and save as an Anki compatible .csv file
    try:
        print("Starting translation")
        translator.translate_list(wordlist, input_language, output_language, args.destination)
    except:
        if args.debug:
            print(sys.exc_info())
        else:
            delete_tmp()
            print("error in wordlist_to_vocablist")
        sys.exit(-1)

    # delete temporary files
    delete_tmp()

    print("Finished")


if __name__ == '__main__':
    run()
