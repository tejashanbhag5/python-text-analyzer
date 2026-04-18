# function to analyze text
def text_analyzer(text):
    vowels = 0
    consonants = 0
    digits = 0
    spaces = 0

    for ch in text.lower():
        if ch in "aeiou":
            vowels += 1
        elif ch.isdigit():
            digits += 1
        elif ch == " ":
            spaces += 1
        elif ch.isalpha() and ch not in "aeiou":
            consonants += 1

    return vowels, consonants, digits, spaces


# input
text = input("enter a text:")

# function call
v, c, d, s = text_analyzer(text)

# output
print("vowels:", v)
print("consonants:", c)
print("digits:", d)
print("spaces:", s)
