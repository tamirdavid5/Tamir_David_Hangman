HANGMAN_PHOTOS = [
    "x-------x",
    "x-------x\n|\n|\n|\n|\n|",
    "x-------x\n|       |\n|       0\n|\n|\n|",
    "x-------x\n|       |\n|       0\n|       |\n|\n|",
    "x-------x\n|       |\n|       0\n|      /|\\\n|\n|",
    "x-------x\n|       |\n|       0\n|      /|\\\n|      /\n|",
    "x-------x\n|       |\n|       0\n|      /|\\\n|      / \\\n|"
]

def print_hangman(num_of_tries):
    """
    Return a string which describes the picture of the hangman for the number of tries
    :param num_of_tries: number of wrong tries
    :type num_of_tries: int
    :return: a string which describes the number of tries
    :rtype: str
    """
    return HANGMAN_PHOTOS[num_of_tries-1]
