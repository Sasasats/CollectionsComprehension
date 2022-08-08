SPACE = ' '
EVEN = "четное"
ODD = "нечетное"
START_RANGE = 1
END_SMALL_RANGE = 20
END_NORMAL_RANGE = 50
END_LARGE_RANGE = 1000
Y = 'Y'
SMALL_Y = 'y'

if __name__ == '__main__':
    devider = 7
    result = [
        x
        for x in range(START_RANGE, END_LARGE_RANGE + 1)
        if x % devider == 0
    ]
    print(f'Task 1: {result}')

    devider = 3
    result = [
        int(x / devider)
        if x % devider == 0
        else int(str(x) + str(x))
        for x in range(START_RANGE, END_LARGE_RANGE + 1)
    ]
    print(f'Task 2: {result}')

    hello_world_with_spaces = "  hel l o      world   "
    not_space_characters = [
        x
        for x in hello_world_with_spaces
        if x != SPACE
    ]
    print(f'Task 3: {len(hello_world_with_spaces) - len(not_space_characters)}')

    string_with_many_y_words = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
    words_starting_with_y = [
        x
        for x in string_with_many_y_words.split(SPACE)
        if x.startswith(Y) or x.startswith(SMALL_Y)
    ]
    print(f'Task 4: {words_starting_with_y}')

    separator = ', '
    strange_string = "hi, 3.44, 535  "
    result = [
        (i, x)
        for i, x in enumerate(strange_string.split(separator))
    ]
    print(f'Task 5: {result}')

    string_containing_numbers = "In 1984 there were 13 instances of a protest with over 1000 people attending"
    numbers = [
        x
        for x in string_containing_numbers.split(SPACE)
        if x.isdigit()
    ]
    print(f'Task 6: {numbers}')

    result = [
        EVEN
        if x % 2 == 0
        else ODD
        for x in range(START_RANGE, END_SMALL_RANGE + 1)
    ]
    print(f'Task 7: {result}')

    common_string = "The trickiest part of learning list comprehension for me was really understanding the syntax."
    word_length = 4
    short_words = [
        x
        for x in
        common_string.split(SPACE)
        if len(x) < word_length
    ]
    print(f'Task 8: {short_words}')

    start_range_for_prime_numbers = 2
    prime_numbers = [
        x
        for x in range(start_range_for_prime_numbers, END_NORMAL_RANGE + 1)
        if all(x % y != 0 for y in range(start_range_for_prime_numbers, x))
    ]
    print(f'Task 9: {prime_numbers}')
