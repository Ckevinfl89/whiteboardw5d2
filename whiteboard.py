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


def solution(name):
    vowels = ['a','e','i','o','u']
    if(len(name)) <4:
        return "Error: Name too short"

    if name[2] in vowels:
        return name[:4]
    else:
        return name[:3]
    

    def solution(str):
    vowels = ['a','e','i','o','u']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
    empty_list = []
    if len(str) < 4:
        return "Error: Name too short"
    for index, value in enumerate(str):
        if index == 2 and value.lower() in vowels:
            return str[:index+2]
        elif index == 2 and value.lower() in consonants:
            return str[:index+1]
        
        def solution(name):
            return 'Error: Name too short' if len(name) < 4 else (name[:4] if name[2] in 'aeiou' else name[:3])