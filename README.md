# read_to_me

This is a simple website reader. It will create MP3 audio with the text of some article on a website. You can also translate this article and create translated MP3 audio.

## Use

You need to clone this repository on your machine, install Python, install the dependencies that are in the requirements.txt file, and execute the read_to_me.py file with Python passing the necessary arguments.

## Arguments

- 1st: Website with text to create the audio.
- 2nd: Website language with the text.
- 3rd: The MP3 file with the audio text of the site.
- 4th: (OPTIONAL) If you want to translate the text, and create the MP3 with the translated audio, enter the lingauem code in this argument.

## Available Languages To Create Audio MP3

The 2nd argument is the languages available for creating the MP3 audio file.
The available languages are:

- af = Afrikaans
- sq = Albanian
- ar = Arabic
- hy = Armenian
- bn = Bengali
- bs = Bosnian
- ca = Catalan
- hr = Croatian
- cs = Czech
- da = Danish
- nl = Dutch
- en = English
- eo = Esperanto
- et = Estonian
- tl = Filipino
- fi = Finnish
- fr = French
- de = German
- el = Greek
- gu = Gujarati
- hi = Hindi
- hu = Hungarian
- is = Icelandic
- id = Indonesian
- it = Italian
- ja = Japanese
- jw = Javanese
- kn = Kannada
- km = Khmer
- ko = Korean
- la = Latin
- lv = Latvian
- mk = Macedonian
- ml = Malayalam
- mr = Marathi
- my = Myanmar (Burmese)
- ne = Nepali
- no = Norwegian
- pl = Polish
- pt = Portuguese
- ro = Romanian
- ru = Russian
- sr = Serbian
- si = Sinhala
- sk = Slovak
- es = Spanish
- su = Sundanese
- sw = Swahili
- sv = Swedish
- ta = Tamil
- te = Telugu
- th = Thai
- tr = Turkish
- uk = Ukrainian
- ur = Urdu
- vi = Vietnamese
- cy = Welsh
- zh-cn = Chinese (Mandarin/China)
- zh-tw = Chinese (Mandarin/Taiwan)
- en-us = English (US)
- en-ca = English (Canada)
- en-uk = English (UK)
- en-gb = English (UK)
- en-au = English (Australia)
- en-gh = English (Ghana)
- en-in = English (India)
- en-ie = English (Ireland)
- en-nz = English (New Zealand)
- en-ng = English (Nigeria)
- en-ph = English (Philippines)
- en-za = English (South Africa)
- en-tz = English (Tanzania)
- fr-ca = French (Canada)
- fr-fr = French (France)
- pt-br = Portuguese (Brazil)
- pt-pt = Portuguese (Portugal)
- es-es = Spanish (Spain)
- es-us = Spanish (United States)

Available languages are the languages allowed by the gTTS library, which is used to create the MP3 audio file.

Source: [https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang](https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang "https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang")

## Languages Available For Translation

The 4th argument is the languages available for translation.
The available languages are:

- af = afrikaans
- sq = albanian
- am = amharic
- ar = arabic
- hy = armenian
- az = azerbaijani
- eu = basque
- be = belarusian
- bn = bengali
- bs = bosnian
- bg = bulgarian
- ca = catalan
- ceb = cebuano
- ny = chichewa
- zh-cn = chinese (simplified)
- zh-tw = chinese (traditional)
- co = corsican
- hr = croatian
- cs = czech
- da = danish
- nl = dutch
- en = english
- eo = esperanto
- et = estonian
- tl = filipino
- fi = finnish
- fr = french
- fy = frisian
- gl = galician
- ka = georgian
- de = german
- el = greek
- gu = gujarati
- ht = haitian creole
- ha = hausa
- haw = hawaiian
- iw = hebrew
- hi = hindi
- hmn = hmong
- hu = hungarian
- is = icelandic
- ig = igbo
- id = indonesian
- ga = irish
- it = italian
- ja = japanese
- jw = javanese
- kn = kannada
- kk = kazakh
- km = khmer
- ko = korean
- ku = kurdish (kurmanji)
- ky = kyrgyz
- lo = lao
- la = latin
- lv = latvian
- lt = lithuanian
- lb = luxembourgish
- mk = macedonian
- mg = malagasy
- ms = malay
- ml = malayalam
- mt = maltese
- mi = maori
- mr = marathi
- mn = mongolian
- my = myanmar (burmese)
- ne = nepali
- no = norwegian
- ps = pashto
- fa = persian
- pl = polish
- pt = portuguese
- pa = punjabi
- ro = romanian
- ru = russian
- sm = samoan
- gd = scots gaelic
- sr = serbian
- st = sesotho
- sn = shona
- sd = sindhi
- si = sinhala
- sk = slovak
- sl = slovenian
- so = somali
- es = spanish
- su = sundanese
- sw = swahili
- sv = swedish
- tg = tajik
- ta = tamil
- te = telugu
- th = thai
- tr = turkish
- uk = ukrainian
- ur = urdu
- uz = uzbek
- vi = vietnamese
- cy = welsh
- xh = xhosa
- yi = yiddish
- yo = yoruba
- zu = zulu
- fil = Filipino
- he = Hebrew

The languages available are the languages translated by the googletrans library, which is used to perform the translations.

Source: [https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages](https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages "https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages")

## Example

`git clone https://github.com/aronkst/read_to_me.git`

`cd read_to_me`

`pip install -r requirements.txt`

`python read_to_me.py "example.com" "en" "audio.mp3"`

`python read_to_me.py "example.com" "en" "audio.mp3" "pt"`

## Instruções em Português

[https://github.com/aronkst/read_to_me/blob/master/README_PT.md](https://github.com/aronkst/read_to_me/blob/master/README_PT.md "https://github.com/aronkst/read_to_me/blob/master/README_PT.md")
