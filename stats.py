from collections import Counter

def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_chars_count(book_text):

    chars_dict = Counter(book_text.lower())

    return dict(chars_dict)

def sort_on(items):
    return items["num"]

def get_sorted_list_of_dicts(char_dict):
    output = []
    for key, value in char_dict.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        output.append(new_dict)
    output.sort(key=sort_on, reverse=True)
    return output