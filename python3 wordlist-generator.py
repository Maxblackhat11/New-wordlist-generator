#!/usr/bin/env python3

import sys
import itertools
import string
from termcolor import colored

def generate_wordlist(inputs):
    """Generate a wordlist based on provided inputs."""
    wordlist = set()

    # Generate variations of each input
    for item in inputs:
        wordlist.add(item.lower())
        wordlist.add(item.upper())
        wordlist.add(item.capitalize())
        
        # Generate combinations with symbols
        for symbol in string.punctuation:
            wordlist.add(item + symbol)
            wordlist.add(symbol + item)

    # Generate combinations and permutations of inputs
    for r in range(2, len(inputs) + 1):
        for combination in itertools.combinations(inputs, r):
            combined = ''.join(combination)
            wordlist.add(combined)
            wordlist.add(combined.lower())
            wordlist.add(combined.upper())

    return wordlist

def save_wordlist(wordlist, filename):
    """Save the generated wordlist to a file."""
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(f"{word}\n")
    print(colored(f"Wordlist saved to {filename}", 'green'))

def main():
    print(colored("Wordlist Generator", 'cyan', attrs=['bold']))

    if len(sys.argv) < 3:
        print(colored("Usage: python wordlist_generator.py <filename> <input1> <input2> ...", 'red'))
        sys.exit(1)

    filename = sys.argv[1]
    inputs = sys.argv[2:]

    wordlist = generate_wordlist(inputs)
    save_wordlist(wordlist, filename)

if __name__ == "__main__":
    main()
