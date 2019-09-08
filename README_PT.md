# read_to_me

Este é um simples leitor de sites. Ele irá criar um áudio MP3 com o texto de algum artigo de um site. Também é possível traduzir este artigo e criar o áudio MP3 traduzido.

## Utilização

É preciso clonar este repositório em sua maquina, instalar o Python, instalar as dependências que estão no arquivo requirements.txt e executar o arquivo read_to_me.py com o Python passando os argumentos necessários.

## Argumentos

- 1 °: Site com texto para criar o áudio.
- 2 °: Idioma do site com o texto.
- 3 °: O arquivo MP3 com o texto em áudio do site.
- 4 °: (OPCIONAL) Se você deseja traduzir o texto e criar o MP3 com o áudio traduzido, digite o código do idioma neste argumento.

## Idiomas Disponíveis Para Criar o MP3 do Audio

O 2° argumento são os idiomas disponíveis para criar o arquivo MP3 do áudio.
Os idiomas disponíveis são:

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

Os idiomas disponíveis são os idiomas permitidos pela biblioteca gTTS, que é a utilizada para criar o arquivo MP3 do áudio.

Fonte: [https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang](https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang "https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang")

## Idiomas Disponíveis Para Tradução

O 4° argumento são os idiomas disponíveis para tradução.
Os idiomas disponíveis são:

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

Os idiomas disponíveis são os idiomas traduzidos pela biblioteca googletrans, que é a utilizada para realizar as traduções.

Fonte: [https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages](https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages "https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages")

## Exemplo

`git clone https://github.com/aronkst/read_to_me.git`

`cd read_to_me`

`pip install -r requirements.txt`

`python read_to_me.py "example.com" "en" "audio.mp3"`

`python read_to_me.py "example.com" "en" "audio.mp3" "pt"`

## English Instructions

[https://github.com/aronkst/read_to_me/blob/master/README.md](https://github.com/aronkst/read_to_me/blob/master/README.md "https://github.com/aronkst/read_to_me/blob/master/README.md")
