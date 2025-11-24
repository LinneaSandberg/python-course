# TODO: Write a Python program that takes a sentence and returns the longest word and its length.
def longest_word(sentence):
    words = sentence.split()
    longest = []

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

sentence = "Hello Hellost Hellofallerulla hej"
print(f"Longest: {longest_word(sentence)}")


# TODO: Write a Python program to find the first repeated word in a given string.
def find_repeated_word(sentence):
    small_sentence = sentence.lower()
    words = small_sentence.split()
    repeated = []

    for word in words:
        if word in repeated:
            return word
        else:
            repeated.append(word)

sentence = "hej Hellost Hellofallerulla HEJ"
print(f"Repeated: {find_repeated_word(sentence)}")


# TODO: Write a Python program that takes a string and removes any excess white spaces between the words of the sentence. In other words, ensure that there is only a single whitespace between the words in the string.
def remove_excess_whitespace(sentence):
    words = sentence.split()
    return " ".join(words)

sentence = "Hello   world  this is  awkward  "
print(f"Fixed sentence: {remove_excess_whitespace(sentence)}")