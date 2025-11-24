import text

# TODO: Write a Python program that counts the number of vowels and consonants in a input string.
def counts_vowels(text):
    vowels = "aeiouy"
    count = 0
    small_text = text.lower()

    for char in small_text:
        if char in vowels:
            count += 1
    return count

print(f"The text contains {counts_vowels(text.hello)} vowels.")


# TODO: Write a Python program that takes a specific substring of string from a given start and end position.
def extract_substring(text, start, end):
    if end is None:
        end = len(text)

    if start < 0 or end > len(text):
        raise ValueError("Invalid positions to extract")
    return text[start:end]

text = ("This is a valid string, hallo!!")
start, end = 24, 31
print(f"This is the extracted string: {extract_substring(text, start, end)}")


# TODO: Write a Python program that count the number of words in an input sentence.
def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = ("This is a valid sentence, hallo!!")
print(f"{count_words(sentence)}")


# TODO: Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def change_first_char_except_first(string):
    first_char = string[0]
    modified_string = first_char + string[1:].replace(first_char, '$')
    return modified_string

string = ("hellotherhhhe")
print(f"{change_first_char_except_first(string)}")