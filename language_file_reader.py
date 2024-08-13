import csv
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []

    with open('languages.csv', 'r') as in_file:
        in_file.readline()  # Skip the header
        for line in in_file:
            parts = line.strip().split(',')
            reflection = parts[2] == "Yes"
            language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]))
            languages.append(language)

    for language in languages:
        print(language)


if __name__ == "__main__":
    main()






