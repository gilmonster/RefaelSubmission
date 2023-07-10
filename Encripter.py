import random

def scramble():
    '''
    Returns 2 dictionaries containing only lowercase English letters.
    The first dictionary is the encryption, where the key is the correct letter and the value is the letter it is coded to.
    The second dictionary is the decryption, which works the other way around.
    :return: 2 dictionaries containing only lowercase English letters
    '''
    encryption_dict = {}
    decryption_dict = {}

    # Initialization of letter list
    letter_list = []
    for i in range(ord("z") - ord("a") + 1):
        letter_list.append(chr(ord("a") + i))

    # Creation of encryption
    for i in range(len(letter_list) - 1):
        letter_idx = random.randint(1, len(letter_list) - 1)
        # Will generate an index within the current range

        encryption_dict[chr(ord("a") + i)] = letter_list[letter_idx]
        decryption_dict[letter_list[letter_idx]] = chr(ord("a") + i)

        del letter_list[letter_idx]
        # Delete the currently added letter from the list of letters

    return encryption_dict, decryption_dict

def encryption_converter(string, dict1):
    '''
    Use a dict of lowercase letters (only!) to encrypt or decrypt a message (string).
    Characters that are not lowercase letters will not be changed.
    :param string: String
    :param dict1: Dictionary of only lowercase letters
    :return: A converted string according to the dict.
    '''
    converted_string = ""
    for letter in string:
        if letter >= "a" and letter <= "z":
            converted_string += dict1[letter]
        else:
            converted_string += letter
    return converted_string

def main():
    encryption = {}
    decryption = {}
    encryption, decryption = scramble()

    gil = "did i get the job?"
    string = encryption_converter(gil, encryption)
    print("Encrypted:", string)
    string = encryption_converter(string, decryption)
    print("Decrypted:", string, "\n")

    while string != "0":
        string = input("Please enter a message to encrypt. To end the program, enter 0: ")
        if string != "0":
            converted_string = encryption_converter(string, encryption)
            print("Your encrypted message:", converted_string)
            action = input("If you want to get the decryption, enter 1. Otherwise, enter any other character: ")
            if action == "1":
                print("Your decrypted message:", encryption_converter(converted_string, decryption))
            action = input("To see encryption dictionary, enter 1. Otherwise, enter any other character: ")
            if action == "1":
                print(encryption)

main()

#spelling checked using AI tool