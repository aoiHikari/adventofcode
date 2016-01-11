#!/usr/bin/python


must_not_contain = ["ab", "cd", "pq", "xy"]
vowels = ["a","e","i","o","u"]

def fp_satisfies_three_vowels(word):
    vowels_count = 0
    for char in word:
        if char in vowels:
            vowels_count += 1
    return vowels_count >= 3

def fp_satisfies_double_letter(word):
    last_char = 0
    for char in word:
        if last_char == char:
            return True
        last_char = char
    return False

def fp_satisfies_last_rule(word):
    for must_not_be_there in must_not_contain:
        if must_not_be_there in word:
            return False
    return True

def solve_part_one():
    nice_words = 0
    with open("input.txt") as input_file:
        for word in input_file:
            print "First part word: {0}, 1: {1}, 2: {2}, 3: {3}".format(word.strip(), fp_satisfies_three_vowels(word), fp_satisfies_double_letter(word), fp_satisfies_last_rule(word))
            if fp_satisfies_three_vowels(word) and fp_satisfies_double_letter(word) and fp_satisfies_last_rule(word):
                nice_words += 1

    print "Nice words {0}".format(nice_words)

def sp_satisfies_pair_rule(word):
    last_char = ''
    current_char = ''
    for i, char in enumerate(word):
        if last_char == '':
            last_char = char
        elif current_char == '':
            current_char = char
        else:
            if last_char + current_char in word[i:len(word)]:
                return True
            last_char = current_char
            current_char = char
    return False

def sp_satisfies_letter_rule(word):
    letter = ''
    for i, char in enumerate(word):
        if i + 2 < len(word):
            letter = char
            if letter == word[i+2]:
                return True

    return False

def solve_part_two():
    nice_words = 0
    with open("input.txt") as input_file:
        for word in input_file:
            print "Second part word: {0}, 1: {1}, 2: {2}".format(word.strip(), sp_satisfies_pair_rule(word), sp_satisfies_letter_rule(word))
            if sp_satisfies_pair_rule(word) and sp_satisfies_letter_rule(word):
                nice_words += 1

    print "Nice words {0}".format(nice_words)


def main():
    solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()
