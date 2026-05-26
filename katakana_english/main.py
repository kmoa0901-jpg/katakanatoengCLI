from converter import convert_sentence, add_word, load_dictionary


def show_menu():
    print("\n=== Katakana English Converter ===")
    print("1. Convert sentence")
    print("2. Add new word")
    print("3. Show dictionary")
    print("4. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose 1-4: ")

        if choice == "1":
            sentence = input("Enter katakana English: ")
            result = convert_sentence(sentence)
            print("Result:", result)

        elif choice == "2":
            katakana = input("Katakana word: ")
            english = input("English word: ")
            add_word(katakana, english)
            print("Saved!")

        elif choice == "3":
            dictionary = load_dictionary()
            for katakana, english in dictionary.items():
                print(katakana, "=>", english)

        elif choice == "4":
            print("Bye!")
            break

        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()