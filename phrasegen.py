#!/usr/bin/env python3
import urllib.request, secrets, string

WORD_URL = 'http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
NUM_WORDS = 3
NUM_PHRASES = 10

#TODO add arguments for NUM_WORDS, if numbers or symbols

def valid_phrase(phrase):
    if any(c.isupper() for c in phrase):
        if any(c.islower() for c in phrase):
            if any(c.isdigit() for c in phrase):
                if any(c in string.punctuation for c in phrase):
                    return True
    return False

def main():
    response = urllib.request.urlopen(WORD_URL)
    words = response.read().decode().splitlines()
    nonalpha = string.digits + string.punctuation
    pw = symbol = ''
    for i in range(NUM_PHRASES):
        while not valid_phrase(pw):
            pw = ''
            if secrets.randbits(1) == 1:
                pw += secrets.choice(nonalpha)
            for j in range(NUM_WORDS - 1):
                if secrets.randbits(1) == 0:
                    pw += secrets.choice(words).upper()
                else:
                    pw += secrets.choice(words).lower()
                pw += secrets.choice(nonalpha)
            if secrets.randbits(1) == 0:
                pw += secrets.choice(words).upper()
            else:
                pw += secrets.choice(words).lower()
            if secrets.randbits(1) == 0:
                pw += secrets.choice(nonalpha)
        print(pw + '\t' + str(len(pw)))
        pw = ''

if __name__ == "__main__":
    main()