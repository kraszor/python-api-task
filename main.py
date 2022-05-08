from output_class import Output


def main():
    while True:
        num = input("Enter an integer between 5 and 20 " +
                    "to get your random words: ")
        try:
            number = int(num)
        except ValueError:
            print("It is not an integer! Try again!")
            continue
        if number < 5 or number > 20:
            print("The number is not between 5 and 20! Try again!")
            continue
        print("It may take a few seconds...\n")
        output = Output(number)
        output.get_num_words()
        print(f'\nYour {number} random words:\n')
        output.display_random_words()
        output.get_music_from_word()
        print("The songs connected with your random words:\n")
        print(output)
        decision = input("Press any key + Enter if you want to try again\n" +
                         "Press q + Enter if you want to exit\n")
        if decision == 'q':
            break


if __name__ == "__main__":
    main()
