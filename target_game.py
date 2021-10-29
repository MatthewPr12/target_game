"""target game: try to write all words possible from the letters given"""
from typing import List
import random
import string


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    alpha = string.ascii_lowercase
    grid_lst = []
    for _ in range(3):
        grid_lst.append([])

    for i in grid_lst:
        for _ in range(3):
            i.append(random.choice(alpha).upper())
    print("Your letters are:", grid_lst)
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
    """checks if the word is possible to be written with the given letters"""
    for i in grid:
        if i in word:
            word.remove(i)
    if not word:
        return True
    return False


def get_words(file_name: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """

    with open(file_name, "r") as file1:
        list_of_words = []
        for line in file1:
            line = line[:-1].lower()  # last chr is \n
            if len(line) >= 4 and letters[4] in line:
                # compare the grid and words
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


def get_pure_user_words(user_words: List[str], letters: List[str],
                        words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pure_user_words = []
    for i in user_words:
        i = i.lower()
        if len(i) >= 4 and letters[4] in i:
            if words_comparison(letters, list(i)) and (i not in words_from_dict):
                pure_user_words.append(i)
    return pure_user_words


def results():
    """puts the results into result.txt file"""
    letters1 = generate_grid()
    letters = []
    for i in letters1:
        for j in i:
            letters.append(j.lower())

    with open("result.txt", "w") as result_file:
        input_words = get_user_words()
        allowed_words = get_words("en", letters)
        for i in input_words:
            if i in allowed_words:
                result_file.write(i + "\n")

        result_file.write("The words not from dictionary:" + "\n")
        for i in input_words:
            if i not in allowed_words:
                result_file.write(i + "\n")


if __name__ == "__main__":
    results()
