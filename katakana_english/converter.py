import json

DICTIONARY_FILE = "katakana_words.json"
UNKNOWN_FILE = "unknown_words.txt"


def load_dictionary():
    with open(DICTIONARY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_dictionary(dictionary):
    with open(DICTIONARY_FILE, "w", encoding="utf-8") as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=2)


def save_unknown_word(word):
    with open(UNKNOWN_FILE, "a", encoding="utf-8") as file:
        file.write(word + "\n")


def convert_sentence(sentence):
    dictionary = load_dictionary()
    words = sentence.split()
    result = []

    for word in words:
        if word in dictionary:
            result.append(dictionary[word])
        else:
            result.append(f"[{word}]")
            save_unknown_word(word)

    return " ".join(result)


def add_word(katakana, english):
    dictionary = load_dictionary()
    dictionary[katakana] = english
    save_dictionary(dictionary)