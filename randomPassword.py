import string
import random

lowercase_alphabets = list(string.ascii_lowercase)  # store all lowercase letters in a list
random.shuffle(lowercase_alphabets)  # randomly shuffle the list

uppercase_alphabets = list(string.ascii_uppercase)  # store all uppercase letter in a list
random.shuffle(uppercase_alphabets)  # randomly shuffle the list

numbers_list = list(range(10))  # store numbers from 0 to 9
string_numbers_list = [str(i) for i in numbers_list]  # to convert a list of integers to a list of strings

symbols_list = ['$', '#', '&', '@']
random.shuffle(symbols_list)  # randomly shuffle the list

password_list = []  # an empty list


def lowercase():
    random_lowercase = random.choice(lowercase_alphabets)
    password_list.append(random_lowercase)
    return password_list


def uppercase():
    random_uppercase = random.choice(uppercase_alphabets)
    password_list.append(random_uppercase)
    return password_list


def numbers():
    random_number = random.choice(string_numbers_list)
    password_list.append(random_number)
    return password_list


def symbols():
    random_symbol = random.choice(symbols_list)
    password_list.append(random_symbol)
    return password_list


def password():
    try:
        password_length = int(input('Enter the password length : '))
        if 0 <= password_length < 6:
            print('The password length must be at least 6 ')
            password()
        elif password_length < 0:
            print('Please enter a positive number')
            password()
        elif password_length >= 6:  # create the password
            for i in range(password_length):
                if len(password_list) < password_length:
                    lowercase()
                    if len(password_list) < password_length:
                        uppercase()
                        if len(password_list) < password_length:
                            numbers()
                            if len(password_list) < password_length:
                                symbols()

                else:
                    random.shuffle(password_list)
                    list_to_string = ''.join(password_list)
                    print('Your password is : ', list_to_string)
                    break

    except:  # to handle wrong user input
        print('Invalid input, please enter an integer number')
        password()


password()

# resource
# https://datagy.io/python-list-alphabet/#growMeSearch=list%20of%20symbol
# https://stackoverflow.com/questions/58871412/how-to-convert-a-list-of-numbers-to-a-list-of-strings
