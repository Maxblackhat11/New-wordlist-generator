import itertools
import string

def generate_wordlist(name, surname, birthdate, partner_name, partner_birthdate, include_numbers=False, include_symbols=False):
    # Initialize the wordlist
    wordlist = set()
    
    # Basic combinations
    basic_words = [name, surname, birthdate, partner_name, partner_birthdate]
    
    # Add basic combinations to the wordlist
    for word in basic_words:
        wordlist.add(word)
        wordlist.add(word.lower())
        wordlist.add(word.upper())
        wordlist.add(word.capitalize())

    # Add number combinations if required
    if include_numbers:
        for num in range(10):
            for word in basic_words:
                wordlist.add(f"{word}{num}")
                wordlist.add(f"{num}{word}")

    # Add symbol combinations if required
    if include_symbols:
        symbols = string.punctuation
        for symbol in symbols:
            for word in basic_words:
                wordlist.add(f"{word}{symbol}")
                wordlist.add(f"{symbol}{word}")

    # Generate combinations of lowercase letters
    if include_numbers or include_symbols:
        chars = string.ascii_lowercase
        if include_numbers:
            chars += string.digits
        if include_symbols:
            chars += string.punctuation

        for length in range(1, 4):  # Adjust length for complexity
            for combination in itertools.product(chars, repeat=length):
                wordlist.add(''.join(combination))

    return wordlist

def main():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    birthdate = input("Enter your birth date (YYYYMMDD): ")
    partner_name = input("Enter your partner's name: ")
    partner_birthdate = input("Enter your partner's birth date (YYYYMMDD): ")
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    wordlist = generate_wordlist(name, surname, birthdate, partner_name, partner_birthdate, include_numbers, include_symbols)
    
    # Save to file
    with open('wordlist.txt', 'w') as f:
        for word in sorted(wordlist):
            f.write(f"{word}\n")
    
    print(f"Wordlist generated with {len(wordlist)} entries and saved to 'wordlist.txt'.")

if __name__ == "__main__":
    main()
