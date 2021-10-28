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
    grid_lst1 = []
    for _ in range(3):
        grid_lst.append([])

    for i in grid_lst:
        for _ in range(3):
            i.append(random.choice(alpha).upper())
    print("Your letters are:", grid_lst)
    for i in grid_lst:
        for j in i:
            grid_lst1.append(j.lower())
    return grid_lst1


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
            line = line[:-2]  # last two chr are \n
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


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pure_user_words = []
    for i in user_words:
        if words_comparison(letters, list(i)) and (i not in words_from_dict):
            pure_user_words.append()
    return pure_user_words


def results():
    """puts the results into result.txt file"""
    letters = generate_grid()

    with open("result.txt", "w") as result_file:
        input_words = get_user_words()
        allowed_words = get_words("en.txt", letters)
        for i in input_words:
            if i in allowed_words:
                result_file.write(i + "\n")

        result_file.write("The words not from dictionary:" + "\n")
        for i in input_words:
            if not (i in allowed_words):
                result_file.write(i + "\n")


if __name__ == "__main__":
    results()
