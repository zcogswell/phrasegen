# Phrase Generator
This is a script to generate XKCD style passphrases, but includes mixed case words, numbers, and symbols.

This is not intended to be used for any password.

For passwords entered infrequently, a standard random string password generator with a manager is better.

This is intended for passwords that should be very difficult to brute force, but memorable enough to not require a password manager.

Passwords generated take on a form like:
`!thankful{umbrageGATE0` or `3CONVIVIAL"delirious|iv7`

The passphrase's length is printed after the passphrase and a tab

## Requirements
*nix based OS

Python >= 3.6

Internet connection for word dictionary

## Usage
phrasegen.py [-h] [-w WORDS] [-p PHRASES] [-U URL] [-n] [-s]

optional arguments:
  -h, --help            show this help message and exit

  -w WORDS, --words WORDS

                        Number of words in phrase

  -p PHRASES, --phrases PHRASES

                        Number of phrases to print

  -U URL, --url URL     Dictionary URL

  -n, --num             Bans numbers
  
  -s, --sym             Bans symbols