def choose_word(file_name, n_):
    '''Return the number of unique words and the n_th word in a text file containing words only.
    :param file_name: Name of the text file containing lists of words (may include repetitions).
    :type file_name:  string
    :param n_: Index of the word in a list of unique words in the file [1,n_words].
    :type n_:  int
    :return: Number of unique words in the file and the chosen word.
    :rtype: tuple
    '''
    # Read the file and split its contents into a list of words
    with open(file_name, 'r') as f:
        word_list = f.read().split()

    # Use set() to get the unique words and count them
    unique_words = set(word_list)
    num_unique_words = len(unique_words)

    # Calculate the index of the chosen word and return the tuple
    chosen_word_index = (n_ - 1) % len(word_list)
    return num_unique_words, word_list[chosen_word_index]