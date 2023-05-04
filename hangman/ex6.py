from ex5 import check_valid_input
 
def try_update_letter_guessed(input_string, old_letter_guessed):
    """
    This function checks if the input string is a valid letter and updates the list of previously guessed letters.
    :param input_string: A string that needs to be checked if it's a valid letter.
    :type input_string: str
    :param old_letter_guessed: A list of letters that were previously guessed.
    :type old_letter_guessed: list
    :return: A boolean value of True if the list of guessed letters is updated, False otherwise.
    :rtype: bool
    """
    lowered_input = input_string.lower()
    if check_valid_input(lowered_input, old_letter_guessed):
        old_letter_guessed += lowered_input
        return True
    else:
        return False