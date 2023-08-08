# Nickname Generator

# Write a function, nicknameGenerator that takes a string name as an argument and returns the first 3 or 4 letters as a nickname.

# If the 3rd letter is a consonant, return the first 3 letters.


# nickname("Robert") //=> "Rob"
# nickname("Kimberly") //=> "Kim"
# nickname("Samantha") //=> "Sam"
# If the 3rd letter is a vowel, return the first 4 letters.

# nickname("Jeannie") //=> "Jean"
# nickname("Douglas") //=> "Doug"
# nickname("Gregory") //=> "Greg"
# If the string is less than 4 characters, return "Error: Name too short".

# Notes:

# Vowels are "aeiou", so discount the letter "y".
# Input will always be a string.
# Input will always have the first letter capitalised and the rest lowercase (e.g. Sam)



def solution(name):
# If the string is less than 4 characters, return "Error: Name too short"
    if len(name) <4:
        return "Error: Name too short"
    first_letter = name[:3]
    third_letter = name[2]
    if third_letter in 'aeiou':
        return name[:4]
    return first_letter


