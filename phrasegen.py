#!/usr/bin/env python3
import urllib.request, urllib.error, secrets, string, sys
from argparse import ArgumentParser

def parse_arguments():
    """Runs argparse

    Returns:
        argparse.Namespace -- collection of args from cmd line
    """
    parser = ArgumentParser()
    parser.add_argument('-w', '--words', default='3', help='Number of words in phrase')
    parser.add_argument('-p', '--phrases', default='10', help='Number of phrases to print')
    parser.add_argument('-u', '--url', help='Dictionary URL')
    parser.add_argument('-n', '--num', action='store_false', help='Bans numbers')
    parser.add_argument('-s', '--sym', action='store_false', help='Bans symbols')
    args = parser.parse_args()
    if not args.words.isnumeric():
        print('words argument not numeric', file=sys.stderr)
        sys.exit(1)
    if not args.phrases.isnumeric():
        print('phrases argument not numeric', file=sys.stderr)
        sys.exit(1)
    return args

def valid_phrase(phrase, args):
    """ Checks generated passphrase for validity against script arguments

    Arguments:
        phrase {string} -- passphrase being checked
        args {dict} -- program arguments

    Returns:
        bool -- True if passed checks, False otherwise
    """
    if any(c.isupper() for c in phrase): # upper case
        if any(c.islower() for c in phrase): # lower case
            if any(c.isdigit() for c in phrase) or not args.num: # number
                if any(c in string.punctuation for c in phrase) or not args.sym: # letter
                    return True
    return False

def main():
    """ Main function
    Gathers dictionary from URL, generates passphrases, and prints passphrases
    """

    conf = parse_arguments()
    if conf.url:
        try:
            response = urllib.request.urlopen(conf.url)
            words = response.read().decode().splitlines()
        except urllib.error.URLError:
            print('web request failure', file=sys.stderr)
            sys.exit(2)
    else:
        try:
            with open('/usr/share/dict/words', 'r') as f:
                words = f.read().splitlines()
        except OSError:
            print('no dictionary file', file=sys.stderr)
            sys.exit(3)
        
    nonalpha = ''
    if conf.num:
        nonalpha += string.digits
    if conf.sym:
        nonalpha += string.punctuation
    #nonalpha = string.digits + string.punctuation
    for i in range(int(conf.phrases)):
        pw = ''
        while not valid_phrase(pw, conf):
            # rerolls passphrase until valid
            pw = ''
            if secrets.randbits(1) == 1 and len(nonalpha) > 0:
                # 50% chance of number or symbol at beginning versus letter
                pw += secrets.choice(nonalpha)
            for j in range(int(conf.words)):
                if secrets.randbits(1) == 0:
                    pw += secrets.choice(words).upper()
                else:
                    pw += secrets.choice(words).lower()
                if secrets.randbits(1) == 1 and len(nonalpha) > 0:
                    # 50% chance of number or symbol between words and at the end
                    pw += secrets.choice(nonalpha)
        print(pw + '\t' + str(len(pw)))

if __name__ == "__main__":
    main()
