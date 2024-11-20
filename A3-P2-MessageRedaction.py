#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:     
#Student Name:  


    # YOUR CODE STARTS HERE, each line must be indented (one tab)
def remove_letters(sentence, letters_to_remove):
    """
    Replaces all occurrences of specified letters in the sentence with underscores.
    :param sentence: str, the sentence to modify
    :param letters_to_remove: list of str, letters to replace
    :return: tuple (modified_sentence, count_replaced)
    """
    count_replaced = 0
    modified_sentence = ""

    for char in sentence:
        if char.lower() in letters_to_remove:
            modified_sentence += "_"
            count_replaced += 1
        else:
            modified_sentence += char

    return modified_sentence, count_replaced


def main():
    print("Welcome to the Letter Removal Program!")
    print("Type 'quit' to exit the program.\n")

    while True:
        # Step 1: Get the sentence from the user
        sentence = input("Enter a sentence or phrase: ")
        if sentence.lower() == "quit":
            print("Goodbye!")
            break

        # Step 2: Get the letters to remove
        letters_input = input("Enter a comma-separated list of letters to remove: ")
        letters_to_remove = [letter.strip().lower() for letter in letters_input.split(",") if letter.strip()]

        # Validate input
        if not letters_to_remove:
            print("No valid letters entered. Try again.\n")
            continue

        # Step 3: Process the sentence
        modified_sentence, count_replaced = remove_letters(sentence, letters_to_remove)

        # Step 4: Display the results
        print(f"\nModified Sentence: {modified_sentence}")
        print(f"Total letters replaced: {count_replaced}\n")


if __name__ == "__main__":
    main()







    # YOUR CODE ENDS HERE

main()