"""3. Write a program that takes a string and counts the number of vowels in it."""

word= input('enter the word:')

def vowel(str):
    count=0
    for char in str:
        if char in 'aeiouAEIOU':
            count += 1

    return print(count)

vowel(word)