#Takes book as test and prints the word count
def word_count(text:str) -> str:
    wordcount = len(text.split())
    print(f"{wordcount} words found in the document")
    return wordcount
def character_count(text: str) -> dict:
    dictionary = {}
    for char in text.lower():
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

def sort_on(items: dict):
    return items["num"]

    # Takes a dictionary of character counts and returns a sorted list of dicts
def sorted_char_counts(character_count: dict) -> list:
    char_list = []
    char_dictionary = {}
    for char in character_count:
        char_dictionary = {}
        #Following 2 lines create both the key and the key value for the temporary dictionary
        char_dictionary["char"] = char
        char_dictionary["num"] = character_count[char]
        char_list.append(char_dictionary)
    char_list.sort(reverse=True, key=sort_on)
    return char_list


    
