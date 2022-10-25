def print_upper_words(words, starts_with=""):
    """ Takes a list of words and letters the words should start with
        Prints words that start with specified letters in uppercase

        Prints all words if no starts_with is provided
    """
    if starts_with == "":
        for word in words:
            print(word.upper())
    else:
        for word in words:
            if word[0] in starts_with:
                print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  starts_with={"h", "y"})
