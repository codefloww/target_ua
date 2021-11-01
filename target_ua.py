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

def get_words():
    pass

def get_user_words():
    pass

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
