def count_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}
    for c in text.lower():
        if not c in characters:
            characters[c] = 0
        characters[c] += 1
    return expand_character_counts(characters)

def sort_on(dict):
    return dict["num"]

def expand_character_counts(characters):
    sorted_list = []
    for k in characters:
        sorted_list.append({"char": k, "num": characters[k]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list