def get_num_words(text):
    splitText = text.split()
    return len(splitText)

def get_char_count(text):
    char_dict = {}
    lowerText = text.lower()
    for char in lowerText:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def sort_on(dict):
    return dict["count"]

def create_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            dict_row = {"char": char, "count": count}
            char_list.append(dict_row)
    char_list.sort(reverse=True, key=sort_on)
    return char_list