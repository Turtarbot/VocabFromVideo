# Copyright (C) 2019  Patricia C. Zauleck

import youtube_dl
import speech_recognition
import os

# language code for CMUSphinx text recognition
lang = "de-DE"

# arguments for youtube downloader
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'outtmpl': 'tmp/%(id)s.%(ext)s',
    # 'writesubtitles': ''
    # 'logger': MyLogger(),
    # 'progress_hooks': [my_hook],
}


def youtube_to_text(url):
    """
    Takes a Youtube URL of a video in German, downloads the video's sound and saves it in a .wav file.
    The Audio is used for CMUSphinx Speech Recognition and the resulting text saved in a file.
    :param url: The URL of a Youtube Video as a string
    :return: The path of the created text file as a string
    """

    if not os.path.exists('tmp'):
        os.mkdir('tmp')

    # download video
    youtube_dl.YoutubeDL(ydl_opts).download([url])

    # CMUSphinx speech recognition on audio file
    print("Starting speech recognition")
    filepath = "tmp/" + os.path.splitext(os.listdir('tmp')[0])[0] + ".wav"
    audio_file = speech_recognition.AudioFile(filepath)
    recognizer = speech_recognition.Recognizer()
    with audio_file as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_sphinx(audio, language=lang)

    # write recognized text to file
    text_path = "tmp/" + os.path.splitext(os.path.basename(filepath))[0] + ".txt"
    text_file = open(text_path, "w+")
    text_file.write(text)
    text_file.close()

    return text_path
