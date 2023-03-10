"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)

def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums

def get_odd_indices(items):
    result = []

    for index, item in enumerate(items):
        if index % 2 != 0:
            result.append(item)
    return result
    

def print_as_numbered_list(items):
    i = 1
    
    for item in items:
        print(f'{i}. {item}')

        i += 1

def get_range(start, stop):

    nums = []

    for num in range(start, stop):
        nums.append(num)
    return nums

def censor_vowels(word):
    chars = ""
    vowels = 'aeiou'
    
    for letter in word:
        if letter in vowels:
            chars += '*'
        else:
            chars += letter

    return str(chars)


def snake_to_camel(string):
    pass  # TODO: replace this line with your code
    camel_case = ""

    for word in string.split('_'):
        camel_case += (f'{word[0].upper()}{word[1:]}')

    return str(camel_case)


def longest_word_length(words):
    
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest


def truncate(string):
    pass  # TODO: replace this line with your code
    result = []

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)

    return ''.join(result)


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
