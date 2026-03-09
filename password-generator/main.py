#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

def take_list(char_list, value):
    return random.choices(char_list, k = value)

chosen_letters = take_list(letters, nr_letters)
chosen_numbers = take_list(numbers, nr_numbers)
chosen_symbols = take_list(symbols, nr_symbols)
#lists of chosen characters created

blank = ""
def randomize(char_list, char_str):
    for i in char_list:
        char_str += i
    return char_str #developing a string of chosen lists
user_letters = randomize(chosen_letters, blank)
user_numbers = randomize(chosen_numbers, blank)
user_symbols = randomize(chosen_symbols, blank)
normal_passwd = user_letters + user_numbers + user_symbols
print(normal_passwd)

#generating randomised password
list_passwd = list(normal_passwd)
random.shuffle(list_passwd)
random_passwd = ""
for i in list_passwd:
    random_passwd += i
print(random_passwd)
    
