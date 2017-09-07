# LibIndic Syllabifier


[![Build Status](https://travis-ci.org/libindic/syllabalizer.svg?branch=master)](https://travis-ci.org/libindic/syllabalizer)
[![Coverage Status](https://coveralls.io/repos/github/libindic/syllabalizer/badge.svg?branch=master)](https://coveralls.io/github/libindic/syllabalizer?branch=master)


LibIndic's syllabifier module may be used to split words into their constituent
syllables. It currently works for Malayalam, Kannada, Bengali, Tamil, Hindi and
English.

## Installation
1. Clone the repository `git clone https://github.com/libindic/syllabalizer.git`
2. Change to the cloned directory `cd syllabalizer`
3. Run setup.py to create installable source `python setup.py sdist`
4. Install using pip `pip install dist/libindic-syllabifier*.tar.gz`

## Usage
```
>>> from libindic.syllabifier import Syllabifier
>>> instance = Syllabifier()
>>> result = instance.syllabify(u"കാര്യക്ഷമത")
>>> for syllable in result:
...     print(syllable)
...
കാ
ര്യ
ക്ഷ
മ
ത
```

For more details read the [docs](http://indicsyllabifier.rtfd.org/)
