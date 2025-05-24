def get_num_words(text):
    words = text.split();

    return len(words);

def get_num_characters(text):
    num_characters = {};

    lower_text = text.lower();
    for i in range(0, len(text)):
        if lower_text[i] not in num_characters:
            num_characters[lower_text[i]] = 0

        num_characters[lower_text[i]] += 1

    return num_characters;

def sort_on(dict):
    return dict["num"]

def sort_num_characters(characters):
    char_list = [];

    for char in characters:
        char_list.append({"char": char, "num": characters[char]})

    return char_list.sort(reverse=True, key=sort_on)


