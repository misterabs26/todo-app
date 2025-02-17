# def get_average():
#     #store the contents of the file in a list
#     with open("bonus_files/data.txt", 'r') as file:
#         data = file.readlines()
#
#
#     numbers = []  #separate list for the numbers
#
#     #separating string and numbers
#     # if the item is number, append it to a separate list
#     # if the item is a string, convert it to float then append to numbers list
#     # if it is not convertable to float, then ignore it using pass keyword
#     for item in data:
#
#         if isinstance(item, (float,int)):
#             numbers.append(item)
#
#         elif isinstance(item, str):
#             try:
#                 number = float(item)
#                 numbers.append(number)
#             except ValueError:
#                 pass
#
#     #computing the average
#     average = sum(numbers)/len(numbers)
#     return average
#
# #testing the code
# list_average = get_average()
# print(list_average)



def strength(password):
    result = []

    pw_len = len(password) > 7
    result.append(pw_len)

    #if password has uppercase
    has_upper = any(char.isupper() for char in password)
    result.append(has_upper)

    # if password has digits
    has_digit = any(char.isdigit() for char in password)
    result.append(has_digit)

    if all(result):
        status = "Strong Pasword"
    else:
        status = "Weak Password"
    return status

pw = input("Enter your password: ")
strength(pw)


def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)
