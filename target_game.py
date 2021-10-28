from typing import List
import random
import string


def generate_grid() -> List[str]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    alpha = string.ascii_lowercase
    grid_lst = []
    for i in range(9):
        grid_lst.append(random.choice(alpha))
    return grid_lst


# def tuple_creator(lst):
#     lst_of_tuples = []
#     for iter_1 in lst:
#         num_of_occ = lst.count(iter_1)
#         lst_of_tuples.append(tuple([iter_1, num_of_occ]))
#         lst_of_tuples = sorted(list(set(lst_of_tuples)))
#
#     return lst_of_tuples


def words_comparison(grid, word):
    for i in grid:
        if i in word:
            word.remove(i)
    if not word:
        return True
    return False


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """

    with open(f, "r") as file1:
        list_of_words = []
        for line in file1:
            line = line[:-2]
            if len(line) >= 4 and letters[4] in line:
                # compare the lists of tuples
                if words_comparison(letters, list(line)):
                    list_of_words.append(line)

    return list_of_words


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words = input()
    lst_user_words = user_words.split()
    return lst_user_words


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass


print(get_words('en.txt', ["a", "r", "o", "n", "e", "t", "g", "h", "i"]))
