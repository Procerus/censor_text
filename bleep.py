from cs50 import get_string
import sys


def main(argv):
    # Checks to make sure there is a file name as an argument after the program
    try:
        sys.argv[1] == None
    except IndexError:
        print("Usage: python " + sys.argv[0] + " dictionary")
        exit(1)
    # Checks if there is more then one argument and informs user to only use one
    if len(argv) > 2:
        print("Usage: python " + sys.argv[0] + " dictionary")
        exit(1)
    # Opens file and initializes banned variable that holds the words and the list that contains all of them
    f = open(sys.argv[1], "r")
    banned = " "
    banned_list = []
    # Adds all the banned words to a list and closes the file
    while banned != "":
        banned = f.readline()
        banned_list.append(banned.split("\n")[0])
    f.close()
    # Gets user input for the sentence that the user will censor and initializes the censored variable
    print("What message would you like to censor?")
    uncensored = input()
    censored = False
    # The outermost for loop goes through each word of the users input string being seperated by spaces
    for i in range(0, len(uncensored.split(" "))):
        # The inner for loop checks the word with each of the banned words to check if it is banned or not
        for j in range(0, len(banned_list)):
            # If the word is a banned word it prints out the equivalent length in stars and makes censored true
            if uncensored.split(" ")[i].lower() == banned_list[j]:
                stars = ""
                for k in range(0, len(banned_list[j])):
                    stars = stars + "*"
                print(stars, end=" ")
                censored = True
            # If the censored is not true and it went through the whole list it will print the word
            elif j == len(banned_list) - 1 and censored == False:
                print(uncensored.split(" ")[i], end=" ")
        # Reinitializes the censored to false
        censored = False

    print()


if __name__ == "__main__":
    main(sys.argv)

