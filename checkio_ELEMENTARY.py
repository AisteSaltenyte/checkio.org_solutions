#ELEMENTARY

# You should return a given string in reverse order.
# Input: A string.
# Output: A string.

def backward_string(val: str) -> str:
    return val[::-1]




# Try to find out how many zeros a given number has at the end.
# Input: A positive Int
# Output: An Int.

def end_zeros(num: int) -> int:
    num_str = str(num)
    num_str = backward_string(num_str)
    count = 0
    for i in num_str:
        if i == "0": 
            count = count + 1
        else: 
            break
    return count





# Not all of the elements are important. 
# What you need to do here is to remove from the list all of the elements before the given one.
# For the illustration we have a list [1, 2, 3, 4, 5] and we need to remove all elements that go before 3 - which is 1 and 2.
# We have two edge cases here: 
# (1) if a cutting element cannot be found, then the list shoudn't be changed. 
# (2) if the list is empty, then it should remain empty.
# Input: List and the border element.
# Output: Iterable (tuple, list, iterator ...).

def remove_all_before(items: list, border: int) -> list:
    if border not in items:
        return items
    else: 
        index = items.index(border)
        return items[index:]




# In a given list the first element should become the last one. 
# An empty list or list with only one element should stay the same.
# Input: List.
# Output: Iterable.

def replace_first(items: list) -> list:
    if len(items) == 0:
        return items
    first_item = items[0]
    cut_items = items[1:]
    cut_items.append(first_item)
    return cut_items




# You have a number and you need to determine which digit in this number is the biggest.
# Input: A positive int.
# Output: An Int (0-9).

def max_digit(number: int) -> int:
    new_list = list(str(number))
    return int(max(new_list))
    # str - integer to string
    # list - sting to list
    # int - string to integer




# Split the string into pairs of two characters. 
# If the string contains an odd number of characters, 
# then the missing second character of the final pair should be replaced with an underscore ('_').
# Input: A string.
# Output: An iterable of strings.

def split_pairs(a):
    new_list = []  # creating empty list, which will be appended later
    string_length = len(a) # lenght of the string
    string_range = range(0, string_length, 2) 
    #list of indexes of the string (0 - where to start, string_length - where to end, 2 steps)
    for i in string_range:
        if i < string_length -1: # checks if it is not the end of the string
            new_list.append(a[i] + a[i+1]) 
            # filling in empty list with pairs: every second simbol + simbol next to it
        else:
            new_list.append(a[i] + "_") # if it is the last simbol, then "_" is added
    return new_list
print(split_pairs("dgdgegergrt"))  # test 
print(split_pairs("knjhtg"))   # test






# Check if a given string has all symbols in upper case. 
# If the string is empty or doesn't have any letter in it - function should return True.
# Input: A string.
# Output: a boolean.

def is_all_upper(text: str) -> bool:
    if text.isupper():
        return text.isupper()
    elif text == (''):
        return True
    elif text.isspace():
        return True
    elif text.isnumeric():
        return text.isnumeric()
    else:
        return False




# You have a string that consist only of digits. 
# You need to find how many zero digits ("0") are at the beginning of the given string.
# Input: A string, that consist of digits.
# Output: An Int.

def beginning_zeros(number: str) -> int:
    zeroes_count = []
    for item in number:
        if item == "0":
            zeroes_count.append(item)
        else:
            break
    return len(zeroes_count)

# or
def beginning_zeros(number: str) -> int:
    count = 0
    while (count < len(number)):
        if number[count] != '0':
            return count
        count += 1
    return count




# Find the nearest value to the given one.
# You are given a list of values as set form and a value for which you need to find the nearest one.
# For example, we have the following set of numbers: 4, 7, 10, 11, 12, 17, and we need to find the nearest 
# value to the number 9. If we sort this set in the ascending order, 
# then to the left of number 9 will be number 7 and to the right - will be number 10. But 10 is closer than 7, 
# which means that the correct answer is 10.
# A few clarifications:
# * If 2 numbers are at the same distance, you need to choose the smallest one;
# * The set of numbers is always non-empty, i.e. the size is >=1;
# * The given value can be in this set, which means that it’s the answer;
# * The set can contain both positive and negative numbers, but they are always integers;
# * The set isn’t sorted and consists of unique numbers.
# Input: Two arguments. A list of values in the set form. The sought value is an int.
# Output: Int.

def nearest_value(values: set, one: int) -> int:
    nearest = None
    min_distance = None
    for item in values:
        if min_distance is None or abs(item - one) < min_distance:
            min_distance = abs(item - one) 
            nearest = item
        elif abs(item - one) == min_distance and item < nearest:
            nearest = item
    return nearest




# You are given a string and two markers (the initial one and final). 
# You have to find a substring enclosed between these two markers. But there are a few important conditions.
# This is a simplified version of the Between Markers mission.
# * The initial and final markers are always different.
# * The initial and final markers are always 1 char size.
# * The initial and final markers always exist in a string and go one after another.
# Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
# Output: A string.
# Precondition: There can't be more than one final and one initial markers.

def between_markers(text: str, begin: str, end: str) -> str:
    begining = text.find(begin) 
    ending = text.find(end)
    between = text[(begining + 1):ending]
    return between




# For the input of your function, you will be given one sentence. 
# You have to return a corrected version, that starts with a capital letter and ends with a period (dot).
# Pay attention to the fact that not all of the fixes are necessary. 
# If a sentence already ends with a period (dot), then adding another one will be a mistake.
# Input: A string.
# Output: A string.
# Precondition: No leading and trailing spaces, text contains only spaces, a-z A-Z , and .

def correct_sentence(text: str) -> str:
    first_letter = text[0]
    if text[-1] != ".": 
        text += "."
    if first_letter.islower():
        text = text.replace(first_letter, first_letter.upper(), 1)
    return text



# Check if the given number is even or not. 
# Your function should return True if the number is even, and False if the number is odd.

def is_even(num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False