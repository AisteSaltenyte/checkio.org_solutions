# HOME


# In a given text you need to sum the numbers. Only separated numbers should be counted. 
# If a number is part of a word it shouldn't be counted.
# The text consists from numbers, spaces and english letters
# Input: A string.
# Output: An int.

def sum_numbers(text: str) -> int:
    splitted_text = text.split()
    counted_numbers = []
    for item in splitted_text:
        if item.isnumeric():
            counted_numbers.append(item)
    sum_of_numbers = 0
    for number in counted_numbers:
        sum_of_numbers += int(number)
    return sum_of_numbers

# or
def sum_numbers(text: str) -> int:
    sum_of_numbers = 0
    for item in text.split():
        if item.isnumeric():
            sum_of_numbers += int(item)
    return sum_of_numbers





# You are given an array of integers. You should find the sum of the integers with even indexes (0th, 2nd, 4th...). 
# Then multiply this summed number and the final element of the array together. 
# Don't forget that the first element has an index of 0.
# For an empty array, the result will always be 0 (zero).
# Input: A list of integers.
# Output: The number as an integer.

def checkio(array: list) -> int:
    even_index_numbers_sum = 0
    if array != []:
        for number in range(0, len(array), 2):
            even_index_numbers_sum += array[number]
        final_sum = even_index_numbers_sum * array[-1]
        return final_sum
    else:
        return 0

# or
def checkio(array: list) -> int:
    even_index_numbers_sum = 0
    if len(array) != 0:
        for number in range(0, len(array), 2):
            even_index_numbers_sum += array[number]
        even_index_numbers_sum *= array[-1]
    return even_index_numbers_sum




# Let's teach the Robots to distinguish words and numbers.
# You are given a string with words and numbers separated by whitespaces (one space). 
# The words contains only letters. You should check if the string contains three words in succession. 
# For example, the string "start 5 one two three 7 end" contains three words in succession.
# Input: A string with words.
# Output: The answer as a boolean.

def checkio(words: str) -> bool:
    split_text = words.split()
    words_count = 0
    for item in split_text:
        if item.isalpha():
            words_count += 1
        elif item.isnumeric():
            words_count = 0

        if words_count == 3:
            return True
    return False





# You are given a string where you have to find its first word.
# When solving a task pay attention to the following points:
# * There can be dots and commas in a string.
# * A string can start with a letter or, for example, a dot or space.
# * A word can contain an apostrophe and it's a part of a word.
# * The whole text can be represented with one word and that's it.
# Input: A string.
# Output: A string.

def first_word(text: str) -> str:
    return text.replace(",", " ").replace(".", " ").split()[0]




# You are given two dates as an array with three numbers - a year, month and day. 
# For example: 19 April 1982 will be (1982, 4, 19). You should find the difference in days between the given dates. 
# For example between today and tomorrow = 1 day. 
# The difference will always be either a positive number or zero, so don't forget about the absolute value.
# Input: Two dates as tuples of integers.
# Output: The difference between the dates in days as an integer.
# Precondition: Dates between 1 january 1 and 31 december 9999. Dates are correct.

from datetime import date
def days_diff(a, b):
    f_date = date(*a)
    l_date = date(*b)
    number_of_days = (l_date - f_date)
    return abs(number_of_days.days)




# You need to count the number of digits in a given string.
# Input: A Str.
# Output: An Int.

def count_digits(text: str) -> int:
    number_of_digits = 0
    for item in text:
        if item.isnumeric():
            number_of_digits += 1
    return number_of_digits




# In a given string you should reverse every word, but the words should stay in their places.
# Input: A string.
# Output: A string.
# Precondition: The line consists only from alphabetical symbols and spaces.

def backward_string_by_word(text: str) -> str:
    if text != '':
        split_text = text.split(" ")
        reverse_string = []
        for word in split_text:
            reverse_word = word[::-1]
            reverse_string.append(reverse_word)
        return " ".join(reverse_string)
    else:
        return ''




# One of the robots is charged with a simple task: to join a sequence of strings into one sentence to produce 
# instructions on how to get around the ship. But this robot is left-handed and has a tendency to joke around 
# and confuse its right-handed friends.
# You are given a sequence of strings. You should join these strings into a chunk of text where the initial 
# strings are separated by commas. As a joke on the right handed robots, you should replace all cases of the 
# words "right" with the word "left", even if it's a part of another word. All strings are given in lowercase.
# Input: A sequence of strings.
# Output: The text as a comma-separated string.
# Precondition: 0 < len(phrases) < 42

def left_join(phrases: tuple) -> str:
    string = ",".join(phrases)
    replaced_phrase = string.replace("right", "left")
    return replaced_phrase




# You are given a string and two markers (the initial and final). You have to find a substring enclosed between 
# these two markers. But there are a few important conditions:
# * The initial and final markers are always different.
# * If there is no initial marker, then the first character should be considered the beginning of a string.
# * If there is no final marker, then the last character should be considered the ending of a string.
# * If the initial and final markers are missing then simply return the whole string.
# * If the final marker comes before the initial marker, then return an empty string.
# Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
# Output: A string.
# Precondition: can't be more than one final marker and can't be more than one initial. Marker can't be an empty string

def between_markers(text: str, begin: str, end: str) -> str:
    if begin in text and end in text:
        start = text.find(begin) + len(begin)
        ending = text.find(end)
        substring = text[start:ending]
        return substring
    elif begin not in text and end not in text:
        return text
    elif begin not in text:
        ending = text.find(end)
        substring = text[0:ending]
        return substring
    elif end not in text:
        start = text.find(begin) + len(begin)
        substring = text[start:]
        return substring


# You have a table with all available goods in the store. The data is represented as a list of dicts
# Your mission here is to find the TOP most expensive goods. The amount we are looking for will be given 
# as a first argument and the whole data as the second one
# Input: int and list of dicts. Each dicts has two keys "name" and "price"
# Output: the same as the second Input argument.

from heapq import nlargest
def bigger_price(limit: int, data: list) -> list:
    top_items = nlargest(limit, data, key=lambda item: item["price"])
    return top_items




# You are given a non-empty list of integers (X). For this task, you should return a list consisting of only 
# the non-unique elements in this list. To do so you will need to remove all unique elements (elements which 
# are contained in a given list only once). When solving this task, do not change the order of the list. 
# Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
# Input: A list of integers.
# Output: An iterable of integers.

def checkio(data: list) -> list:
    new_list = []
    for number in data:
        if data.count(number) > 1:
            new_list.append(number)
    return new_list




# In this mission your task is to determine the popularity of certain words in the text.
# At the input of your function are given 2 arguments: the text and the array of words the popularity 
# of which you need to determine.

# When solving this task pay attention to the following points:
# * The words should be sought in all registers. This means that if you need to find a word "one" 
# then words like "one", "One", "oNe", "ONE" etc. will do.
# * The search words are always indicated in the lowercase.
# * If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.
# Input: The text and the search words array.
# Output: The dictionary where the search words are the keys and values are the number of times when those 
# words are occurring in a given text.
# Precondition: The input text will consists of English letters in uppercase and lowercase and whitespaces.

def popular_words(text: str, words: list) -> dict:
    splitted_text = text.lower().split()
    counted_words = {}
    for word in words:
        if word in splitted_text:
            counted_words[word] = splitted_text.count(word)
        elif word not in splitted_text:
            counted_words[word] = 0
    return counted_words




# You are given two strings and you have to find an index of the second occurrence of the 
# second string in the first one.
# Let's go through the first example where you need to find the second occurrence of "s" 
# in a word "sims". It’s easy to find its first occurrence with a function index or find which 
# will point out that "s" is the first symbol in a word "sims" and therefore the index of the first 
# occurrence is 0. But we have to find the second "s" which is 4th in a row and that means that the 
# index of the second occurrence (and the answer to a question) is 3.
# Input: Two strings.
# Output: Int or None

def second_index(text: str, symbol: str) -> int:
    start = text.find(symbol)
    if start == -1:
        return None
    elif start >=0:
        index = text.find(symbol, start + 1)
        if index == -1:
            return None
        else:
            return index
