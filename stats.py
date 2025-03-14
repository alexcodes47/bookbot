def count_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def count_characters(text):
    char_list = list(text)
    character_dict = {}
    for i in range(0,len(char_list)):
        char_list[i] = char_list[i].lower()
        if char_list[i] not in character_dict:
            character_dict[f"{char_list[i]}"] = 1
        else:
            character_dict[f"{char_list[i]}"] += 1
    return character_dict

def sort_on(item):
    return item["count"]

def get_sorted_char_counts(char_dict):
    char_list = [{"char": char, "count": count} for char, count in char_dict.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list