def get_num_words(text):
    return len(text.split())

def get_characters_count(text):
    dict = {}
    for char in text:
        ch = char.lower()
        if ch not in dict:
            dict[ch] = 1
        else:
            dict[ch] += 1
    return dict

def get_sorted_list_from_dictionary(dict):
    list = []
    for ch in dict:
        tmp = {
            "char": ch,
            "num": dict[ch]
        }
        list.append(tmp)

    def sort_on(d):
        return d["num"]

    list.sort(reverse=True, key=sort_on)

    return list
