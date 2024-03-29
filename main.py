def encode(password):

    password_list = list(password)  # turn int input into list
    encoded_password_str = ""   # empty string to add new password to

    for element in password_list:
        element = int(element)
        element += 3    # add three to each number
        if element > 9: # if the added element is greater than 9, just take second value
            element %= 10
        encoded_password_str += str(element)    # concatenate to empty string
    return encoded_password_str


def decoded(password):
    # for elizabeth!!
    decoded_password = ""
    for element in password:
        element = int(element)
        element -= 3
        decoded_password += str(element)
    return decoded_password


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
            decoded_password = decoded(encoded_password)  # j work w her own variable
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
            menu()
            option = int(input("Please enter an option: "))
        elif option == 3:
            break

if __name__ == "__main__":
    main()