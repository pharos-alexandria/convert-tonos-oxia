# convert-tonos-oxia
Convert Modern Greek “tonos” to Ancient Greek “oxia” in UTF-8 encoded plaintext files with Ancient Greek text.

Sometimes in Ancient Greek texts, for example from the TLG or aquired through [Tesseract](https://github.com/tesseract-ocr), the letter α, ε, η, ι, ο, υ, and ω with acute accent are encoded according to the Greek and Coptic code chart (i.e. with “tonos”), but should be encoded according to the Greek Extended code chart (i.e. with “Oxia”).   

The script therefore replaces the following:

| Tonos        |   | Oxia          |   |
|--------------|---|---------------|---|
| U+03AC (940) | ά | U+1F71 (8049) | ά |
| U+03AD (941) | έ | U+1F73 (8051) | έ |
| U+03AE (942) | ή | U+1F75 (8053) | ή |
| U+03AF (943) | ί | U+1F77 (8055) | ί |
| U+03CC (972) | ό | U+1F79 (8057) | ό |
| U+03CD (973) | ύ | U+1F7B (8059) | ύ |
| U+03CE (974) | ώ | U+1F7D (8061) | ώ |

It takes two arguments: infile and outfile. Use as follows:

```python3 convert-tonos-oxia.py infile.txt outfile.txt```

## Note!
The Unicode Consortium normalizes to the lower code point letters (i.e. tonos), so it's better *not* to use this script.
Cf. https://wiki.digitalclassicist.org/Greek_Unicode_duplicated_vowels, https://en.wikipedia.org/wiki/Greek_diacritics#Unicode, and https://jktauber.com/articles/python-unicode-ancient-greek/.
