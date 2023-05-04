def check_valid_input(guess: str, old_guesses: set) -> bool:
    """
    Check if a guess is valid and hasn't been made before.

    :param guess: A string representing the guess.
    :type guess: str
    :param old_guesses: A set of letters that were previously guessed.
    :type old_guesses: set
    :return: True if guess is a single English letter that hasn't been guessed before; False otherwise.
    :rtype: bool
    """
    return guess.isalpha() and len(guess) == 1 and guess.lower() not in old_guesses
