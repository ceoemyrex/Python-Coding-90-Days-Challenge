# Project:
#- Write a script that reads a text file and counts how many lines and words are in the file.


def count_lines_and_words(filepath):
    """
    Counts the number of lines and words in a text file.

    Args:
        filepath: The path to the text file.

    Returns:
        A tuple containing the number of lines and words, or None if an error occurs.
        Prints an error message to the console if there is an error.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:  #encoding handles various character sets
            lines = file.readlines()
            line_count = len(lines)

            word_count = 0
            for line in lines:
                words = line.split()  #splits the line into words based on whitespace
                word_count += len(words)

            return line_count, word_count

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except IOError:
        print(f"Error: Could not read file at {filepath}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    try:
        filepath = input("Enter the path to the text file: ")
        result = count_lines_and_words(filepath)

        if result:
            line_count, word_count = result
            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")

    except EOFError:
        print("\nInput ended.")
    except Exception as e:
        print(f"An unexpected error occurred during input: {e}")