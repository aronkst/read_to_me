import sys
from gtts import gTTS, lang
from newspaper import Article
from googletrans import Translator, LANGUAGES

if len(sys.argv) <= 3 or len(sys.argv) >= 6:
    print('Invalid arguments.')
    print('  1°: Website with text to create the audio.')
    print('  2°: Website language with the text.')
    print('  3°: The MP3 file with the audio text of the site.')
    print('  4°: (OPTIONAL) If you want to translate the text, and create '
          'the MP3 with the translated audio, enter the lingauem code in '
          'this argument.')
    exit()

site_with_article = sys.argv[1]
original_language = sys.argv[2]
mp3_file = sys.argv[3]

if original_language not in lang.tts_langs().keys():
    print('Invalid arguments.')
    print('  Language to create audio is invalid.')
    exit()

language_to_translate = original_language
mp3_audio_language = original_language

if len(sys.argv) == 5:
    language_to_translate = sys.argv[4]

    if language_to_translate not in LANGUAGES.keys():
        print('Invalid arguments.')
        print('  Language to translate text is invalid.')
        exit()

    if language_to_translate not in lang.tts_langs().keys():
        print('Invalid arguments.')
        print('  The language for translating text must also be one of the '
              'languages available for creating audio, and this language is '
              'not available for translating and creating audio.')
        exit()

    language_to_translate = language_to_translate
    mp3_audio_language = language_to_translate

article = Article(site_with_article)
article.download()
article.parse()

text = article.title + '\n' + article.text

if original_language != language_to_translate:
    translator = Translator()
    text_translated = translator.translate(text, src=original_language,
                                           dest=language_to_translate)
    text = text_translated.text

tts = gTTS(text, lang=mp3_audio_language)
tts.save(mp3_file)
