"""module that handles the target_ua game"""
import random


def generate_grid():
    """Generates list of lists of letters - i.e. grid for the game.
    e.g. [['ж', 'л, 'р'], ['с', 'о', 'к'], ['р', 'т', 'і']]

    Returns:
        list[list[str]]: playing grid of letters
        str: part of language to guess words from
    """
    alphabet = [
        "а",
        "б",
        "в",
        "г",
        "ґ",
        "д",
        "е",
        "є",
        "ж",
        "з",
        "и",
        "і",
        "ї",
        "й",
        "к",
        "л",
        "м",
        "н",
        "о",
        "п",
        "р",
        "с",
        "т",
        "у",
        "ф",
        "х",
        "ц",
        "ч",
        "ш",
        "щ",
        "ь",
        "ю",
        "я",
    ]
    letters_grid = [
        [alphabet[random.randint(0, 32)] for _ in range(3)] for _ in range(3)
    ]
    # check whether 5 different letters appear in grid
    unique = ""
    for row in range(3):
        for col in range(3):
            if letters_grid[row][col] not in unique:
                unique += letters_grid[row][col]
    if len(unique) < 5:
        letters_grid = generate_grid()

    part = random.choice(["noun", "verb", "adjective", "adverb"])

    return letters_grid, part


def display_grid(letters_grid, part) -> None:
    """Displays playing grid of letters

    Args:
        letters_grid (list[list[str]]): grid of letters
    """
    grid = ""
    for i in range(len(letters_grid)):
        grid += " ".join(letters_grid[i]) + "\n"
    print(grid[:-1])
    print(part)


def get_words(file: str, letters):
    """gets all words from file(1 word per line) that
    are legit

    Args:
        f (str): file to get words from
        letters (list[str]): letters of grid

    Returns:
        list[tuple(str,str)]: list of words that are with rules
    """
    legal_words = []
    with open(file, "r") as dictionary:
        for word in dictionary.readlines():
            stop = word.index(" ") if word[0] != " " else 1
            part_lang = word[stop + 1 : -1]
            if "/n" in part_lang or "noun" in part_lang:
                part_lang = "noun"
            elif "/v" in part_lang or "verb" in part_lang:
                part_lang = "verb"
            elif "/adj" in part_lang or "adj" in part_lang:
                part_lang = "adjective"
            elif "adv" in part_lang:
                part_lang = "adverb"
            if (
                check_rules(letters, word[:stop])
                and word[:stop].lower() not in legal_words
            ):
                legal_words.append((word[:stop].lower(), part_lang))
    for word in legal_words:
        if word[0] == "":
            legal_words.remove(word)
    return legal_words


def count_appearances(word: str):
    """Checks how many appearance of each letter in word

    Args:
        word (str): word to check

    Returns:
        list[tuple]: list of tuples('letter', appearances)
    """
    counter_letter = []
    word = word.lower()
    for i in range(len(word)):
        if i == 0:
            counter_letter.append((word[i], word.count(word[i])))
        elif word[i] not in word[:i] and i != 0:
            counter_letter.append((word[i], word.count(word[i])))
    return counter_letter


def check_rules(letters, word) -> bool:
    """checks whether word is legit due to rules of target game

    Args:
        letters (list[str]): letters of grid
        word ([type]): word to check for correctness

    Returns:
        bool: correctness of wor according to rules
    """
    correct = False
    if len(word) <= 5 and letters[4] in word.lower():
        correct = True
        count_word = count_appearances(word.lower())
        for appearance in count_word:
            if appearance[0] not in letters or appearance[1] > letters.count(
                appearance[0]
            ):
                correct = False
                break
    return correct

def check_user_words(user_words, language_part: str, letters, dict_of_words):
    """[summary]

    Args:
        user_words (list): all words from user
        language_part (str): part of language which is needed
        letters (list): letters of grid
        dict_of_words (list): all words from dictionary within rules

    Returns:
        list: [description]
    """
    if letters == letters:
        why = 0
    why += 1
    why -= 1
    correct_user_words = []
    missed_words = []
    for dict in dict_of_words:
        if dict[0] not in user_words and dict[1] == language_part:
            missed_words.append(dict[0])
        elif dict[0] in user_words and dict[1] == language_part:
            correct_user_words.append(dict[0])
    return correct_user_words, missed_words


def main() -> None:
    """maintains a full process of game"""
    grid, language_part = generate_grid()
    display_grid(grid, language_part)
    letters = [grid[i][j] for i in range(len(grid)) for j in range(len(grid[i]))]
    legal_words = get_words("base.lst", letters)
    user_words = get_user_words()
    correct_words, missed_words = check_user_words(
        user_words, language_part, letters, legal_words
    )
    results(correct_words, missed_words, "results.txt")


if __name__ == "__main__":
    main()
