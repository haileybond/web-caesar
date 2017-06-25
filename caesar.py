def encrypt(text, rot):
    new_string = ""                                         #first, initialize a new string
    for eachChar in text:                                   #for each character in the string:
        newChar = rotate_character(eachChar, rot)           #use the rotate function to assign a new character
        new_string = new_string + newChar                   #add the new character to the blank string
    return new_string                                       #after we iterate through all the characters in the string, return the new string

#Tests for encrypt!
#print(encrypt("A", 13))	            #n
#print(encrypt("abcd", 13))	            #nopq
#print(encrypt("LaunchCode",	13))	#YnhapuPbqr
#print(encrypt("LaunchCode",	1))	    #MbvodiDpef
#print(encrypt("Hello, World!",	5))	    #Mjqqt, Btwqi!

def main():
    text = input("Type a message:")
    print(text)
    rot = int(input("Rotate by:"))
    print(rot)
    encrypted_message = encrypt(text, rot)
    print(encrypted_message)

if __name__ == "__main__":
    main()

def alphabet_position(character):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alphabet.index(lower)

def rotate_string_13(text):

    rotated = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in text:
        rotated_idx = (alphabet_position(char) + 13) % 26
        if char.isupper():
            rotated = rotated + alphabet[rotated_idx].upper()
        else:
            rotated = rotated + alphabet[rotated_idx]

    return rotated

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_idx = (alphabet_position(char) + int(rot) % 26)

    if char.isupper():
        return alphabet[rotated_idx].upper()
    else:
        return alphabet[rotated_idx]

def rotate_string(text, rot):

    rotated = ''

    for char in text:
        if char.isalpha():
            rotated = rotated + rotate_character(char, rot)
        else:
            rotated = rotated + char

    return rotated