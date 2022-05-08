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

        # output code here

        decision = input("Press any key + Enter if you want to try again\n" +
                         "Press q + Enter if you want to exit\n")
        if decision == 'q':
            break


if __name__ == "__main__":
    main()
