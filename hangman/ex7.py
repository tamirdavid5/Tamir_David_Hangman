def show_hidden_word(secret_word: str, letters_guessed: list) -> str:
    """Return a string partially disclosing the secret word with only the guessed letters and gaps.

    :param secret_word: The secret string to guess.
    :param letters_guessed: The list of letters that were previously guessed.
    :return: A string revealing the guessed letters of the secret word and gaps in between.
    """
    return " ".join(char if char.lower() in letters_guessed else "_" for char in secret_word)

def check_win(secret_word: str, letters_guessed: list) -> bool:
    """Check if all letters of the secret word are guessed.

    :param secret_word: The secret string to guess.
    :param letters_guessed: The list of letters that were previously guessed.
    :return: A boolean indicating whether the secret word has been guessed.
    """
    return all(char.lower() in letters_guessed for char in secret_word)

