# VocabFromVideo
A simple tool to create a vocabulary list from a video (Youtube link). Currently just a command line prototype.

It takes a Youtube URL or textfile and creates a list of all the words used in the video or text. The words are then saved in a .csv file together with their translation. This .csv file can then for example be directly imported into Anki so you can practise exactly the words needed to understand your chosen video/text.

Currently, the tool is at pre-alpha state and not conveniently usable. The speech recognition as well as translation services used do not work with 100% accuracy, so the results will be far from perfect.

At the moment it is only possible to make lists translating a __German__ video or text to __English__.
## Getting Started
How to install and run this tool.
### Prerequisites
Make sure you have Python 3.5 or later.
In addition you need the following packages:
* [spacy](https://pypi.org/project/spacy/)
* [translate](https://pypi.org/project/translate/)
* [youtube_dl](https://pypi.org/project/youtube_dl/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

youtube_dl is dependent on having either [FFmpeg](https://www.ffmpeg.org/) or [Libav](https://libav.org/) installed and added to your PATH.

I am using SpeechRecognition with PocketSphinx, which means that to use German text recognition a German language model and dictionary have to be added manually. To do so download 
* cmusphinx-voxforge-de.lm.bin
* cmusphinx-voxforge-de.dic
* cmusphinx-de-voxforge-5.2.tar.gz

[HERE](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/German/)

Now go to your speech_recognition/pocketsphinx-data folder and create a new folder called "de-DE". Put the first two files in the folder. Deep in "cmusphinx-de-voxforge-5.2.tar.gz" is a folder called "voxforge.cd_cont_6000".

`cmusphinx-de-voxforge-5.2.tar\cmusphinx-de-voxforge-5.2\cmusphinx-cont-voxforge-de-r20171217\model_parameters\voxforge.cd_cont_6000`

Rename "voxforge.cd_cont_6000" to "acoustic-model" and place it into your created "de-DE" folder.
### Running VocabFromVideo
Assuming you have Python added to your PATH, run start.py in it's folder with the following arguments:

`python start.py source destination DE EN`

Your source should be a Youtube URL (of a video with spoken German).
The destination should be a local path to wherever you want your .csv vocabulary file.

## Additional Options
Instead of a Youtube video you might want to use a text file as source. To do so, you have to change the input type by adding the `-t T` or `--input-type T` parameter (T for Text, default is Y for Youtube).

If the tool is not working you can also increase verbosity by setting the -v flag.

`python start.py source destination -t T DE EN -v`

## License
This project is licensed under the GNU General Public License v3.0
