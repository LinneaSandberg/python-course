import text

# TODO: Write a Python program that accepts a filename from the user and prints the extension of the file.
def extension_name(filename):
    if '.' in filename:
        return filename.rsplit('.', 1)[1]
    else:
        return "No file exstension in name."

filename = "01.jpeg"
print(f"File extension: {extension_name(filename)}")


# TODO: Write a Python program that counts the number character "p" (or any given character) occurs in a string.
def counts_p(text, char):
    if char in text:
        return text.count(char)

char = "."
print(f'The character "{char}" occurred {counts_p(text.lorem, char)} times.')


# TODO: Write a Python program that replaces all e-s in a string with 3 and all o-s with 0.
def replace_chars(text):
    return text.replace("e", "3").replace("o", "0")

print(f"Replaced text {replace_chars(text.hello)}")