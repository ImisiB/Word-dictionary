print("YOU CAN TYPE IN ONLY FIVE WORDS: 'earth', 'nigeria', 'cloth', 'car', 'pilot' ")
print("TO QUIT, TYPE 'quit'")
print()

def main():
    word_dictionary = {
        "earth": "A planet in space",
        "nigeria": "A country in Africa",
        "cloth": "A material used to cover your body",
        "car": "A vehicle used for transportation",
        "pilot": "A person who flies an airplane",
    }
    
    while True:
        word_option = input("Enter a word: ")
        if word_option in word_dictionary:
            print(word_option,":",word_dictionary[word_option])
            print()
        elif word_option == "quit":
            print("Thanks for using the word-dictionary")
            print("Program ended")
            quit()
        elif word_option == "":
            print("Please type in a word")
            print()
        elif word_option not in word_dictionary :
            print(word_option,"isn't part of this dictionary remember, you can type in only five words: 'earth', 'nigeria', 'cloth', 'car', 'pilot' ")
            print()


main()
