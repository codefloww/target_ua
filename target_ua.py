"""module that handles the target_ua game"""
import random


def generate_grid():
    """Generates list of lists of letters - i.e. grid for the game.
    e.g. ['ж', 'л, 'р','в','о']

    Returns:
        list[str]: playing grid of letters
        str: part of language to guess words from

    >>> len(generate_grid())
    5
    >>> type(generate_grid())
    <class 'list'>
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
    letters_grid = [alphabet[random.randint(0, 32)] for _ in range(5)]
    # check whether 5 different letters appear in grid
    unique = ""
    for letter in range(5):
        if letters_grid[letter] not in unique:
            unique += letters_grid[letter]
    if len(unique) < 5:
        letters_grid = generate_grid()

    return letters_grid


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

    >>> get_words('base.lst', ['є'])
    [('євнух', 'noun'), ('єврей', 'noun'), ('євро', 'noun'), ('єгер', 'noun'), ('єдваб', 'noun'), \
('єзуїт', 'noun'), ('єлей', 'noun'), ('ємний', 'adjective'), ('ємно', 'adverb'), \
('єна', 'noun'), ('єнот', 'noun'), ('єпарх', 'noun'), ('єресь', 'noun'), ('єри', 'noun'), \
('єрик', 'noun'), ('єрик', 'noun'), ('єство', 'noun'), ('єті', 'noun'), ('єхида', 'noun')]
    >>> get_words('base.lst', ['ь','ґ'])
    [('ґаблі', 'noun'), ('ґава', 'noun'), ('ґавин', 'adjective'), ('ґазда', 'noun'), \
('ґалій', 'noun'), ('ґандж', 'noun'), ('ґандж', 'noun'), ('ґанок', 'noun'), ('ґара', 'noun'), \
('ґвалт', 'noun'), ('ґевал', 'noun'), ('ґедз', 'noun'), ('ґедзь', 'noun'), ('ґзимс', 'noun'), \
('ґлей', 'noun'), ('ґміна', 'noun'), ('ґніт', 'noun'), ('ґо', 'noun'), ('ґолда', 'noun'), \
('ґонт', 'noun'), ('ґонта', 'noun'), ('ґрата', 'noun'), ('ґрати', 'noun'), ('ґрис', 'noun'), \
('ґроно', 'noun'), ('ґрунт', 'noun'), ('ґуґля', 'noun'), ('ґудзь', 'noun'), ('ґуля', 'noun')]
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
            else:
                part_lang = ""
            if (
                check_rules(letters, word[:stop])
                and word[:stop].lower() not in legal_words
                and part_lang != ""
            ):
                legal_words.append((word[:stop].lower(), part_lang))
    for word in legal_words:
        if word[0] == "":
            legal_words.remove(word)
    return legal_words


def check_rules(letters, word) -> bool:
    """checks whether word is legit due to rules of target game

    Args:
        letters (list[str]): letters of grid
        word ([type]): word to check for correctness

    Returns:
        bool: correctness of wor according to rules
    """
    correct = False
    for letter in letters:
        if len(word) <= 5 and word[0].lower() == letter:
            correct = True
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

    >>> check_user_words([], "adverb", ['ш', 'ь', 'т', 'і', 'х'], get_words("base.lst", ['ш', 'ь', 'т', 'і', 'х']))  # pylint: disable=line-too-long
    ([], ['ізнов', 'інак', 'інако', 'інде', 'іноді', 'іще', 'тамки', 'темно', 'тепер', 'тепло', \
'тихо', 'тихше', 'тоді', 'торік', 'точно', 'тричі', 'трохи', 'туго', 'туди', 'тудою', 'тужно', \
'тут', 'тутки', 'тюпки', 'тяжко', 'хапко', 'хибко', 'хижо', 'хирно', 'хитро', 'хмуро', 'хором', \
'худо', 'хутко', 'шумко', 'шумно'])
    >>> check_user_words(['гаяти', 'гнати', 'ініціалізація', 'узяти', 'щавель'], "verb", ['ю', 'щ', 'я', 'ц', 'г'], get_words("base.lst", ['ю', 'щ', 'я', 'ц', 'г']))  # pylint: disable=line-too-long
    (['гаяти', 'гнати'], ['гнити', 'гнути', 'гоїти', 'грати', 'гріти', 'густи', \
'юшити', 'явити', 'яріти', 'ячати'])
    """
    if letters == letters:
        why = 0
    why += 1
    why -= 1
    correct_user_words = []
    missed_words = []
    for word in dict_of_words:
        if word[0] not in user_words and word[1] == language_part:
            missed_words.append(word[0])
        elif word[0] in user_words and word[1] == language_part:
            correct_user_words.append(word[0])
    return correct_user_words, missed_words


def get_user_words():
    """gets user words(1 per enter) until '' not entered

    Returns:
        list[str]: list of words from user
    """
    user_words = []
    word = "hi"
    print("Try to find some words)")
    while word != "":
        word = input()
        user_words.append(word)
    return user_words[:-1]


def results(correct_words, missed_words: str):
    """prints result of game to user and saves result in results.txt

    Args:
        words (list[str]): words from user
        legal_words (list[str]): words from dictionary that are legit
        pure_words (list[str]): words that legit to rules but not in dictionary
        file (str): file to save results to(will be created if don't exist)

    Returns:
        str: 5-line of results in results.txt
    """
    score = len(correct_words)
    print("Your score:" + str(score))
    print("Correct words:\n", correct_words)
    print("You missed:\n", missed_words)


def main() -> None:
    """maintains a full process of game"""
    grid = generate_grid()
    language_part = random.choice(["noun", "verb", "adjective", "adverb"])
    display_grid(grid, language_part)
    letters = [grid[i][j] for i in range(len(grid)) for j in range(len(grid[i]))]
    legal_words = get_words("base.lst", letters)
    user_words = get_user_words()
    correct_words, missed_words = check_user_words(
        user_words, language_part, letters, legal_words
    )
    results(correct_words, missed_words)


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
    main()
