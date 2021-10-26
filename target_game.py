from typing import List


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    pass


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    grid_tuples = []
    for j in letters:
        num_of_occ = letters.count(j)
        grid_tuples.append(tuple([j, num_of_occ]))
        grid_tuples = sorted(list(set(grid_tuples)))

    with open(f, "r") as file1:
        for line in file1:
            if len(line) >= 4 and letters[4] in line:
                word_tuples = []
                for i in line:
                    num_of_occ1 = line.count(i)
                    word_tuples.append(tuple([i, num_of_occ1]))
                    word_tuples = sorted(list(set(word_tuples)))
                # compare the lists of tuples


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    pass


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass
