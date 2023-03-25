def encode(password):

    password_list = list(password)
    encoded_password_str = ""

    for element in password_list:
        element = int(element)
        element += 3
        if element > 9:
            element %= 10
        encoded_password_str += str(element)
    return encoded_password_str


def decoded(password):
    password_list = list(password)
    decoded_password_str = ""

    for element in password_list:
        element = int(element)
        element -= 3
        if element < 0:
            element += 10
        decoded_password_str += str(element)
    return decoded_password_str


def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")


def main():

    menu()
    option = int(input("Please enter an option: "))

    while True:
        if option == 1:
            og_password = input("Please enter your password to encode: ")
            encoded_password = encode(og_password)
            print("Your password has been encoded and stored!\n")
            menu()
            option = int(input("Please enter an option: "))
        elif option == 2:
            decoded_password = decoded(encoded_password)    # j work w her own variable
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
            menu()
            option = int(input("Please enter an option: "))
        elif option == 3:
            break

if __name__ == "__main__":
    main()