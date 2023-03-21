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

def main():

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

    option = int(input("Please enter an option: "))

    while option != 3:
        if option == 1:
            og_password = input("Please enter your password to encode: ")
            encoded_password = encode(og_password)
            print("Your password has been encoded and stored!")
        elif option == 3:
            break
        break

if __name__ == "__main__":
    main()