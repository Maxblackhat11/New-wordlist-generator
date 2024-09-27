import itertools
import string

def generate_wordlist(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    character_set = ''
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("At least one character type must be selected.")

    return (''.join(word) for word in itertools.product(character_set, repeat=length))

def main():
    print("Welcome to the Wordlist Generator!")
    
    length = int(input("Enter the length of the words: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    wordlist = generate_wordlist(length, use_uppercase, use_lowercase, use_numbers, use_symbols)

    output_file = input("Enter the output filename (e.g., wordlist.txt): ")
    with open(output_file, 'w') as f:
        for word in wordlist:
            f.write(f"{word}\n")

    print(f"Wordlist generated and saved to {output_file}")

if __name__ == "__main__":
    main()
