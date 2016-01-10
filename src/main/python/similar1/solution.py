#!/usr/bin/python

global alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

def generate_matrix(input_string, size_of_matrix):
    print "Size: {0}".format(size_of_matrix)
    matrix = [[0 for x in range(size_of_matrix)] for x in range(size_of_matrix)]
    location_in_word = 0;
    for y in range(size_of_matrix):
        for x in range(size_of_matrix):
             matrix[y][x] = input_string[location_in_word]
             location_in_word = (location_in_word + 1) % len(input_string)
    return matrix

def print_matrix(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            print matrix[y][x],
        print

def lexicographically_superior_word(current, applicant):
    if len(applicant) > len(current):
        return applicant
    if len(applicant) == len(current):
        lexicographical_applicant = 0
        lexicographical_current = 0
        for i in range(len(applicant)):
            lexicographical_applicant += alphabet.index(applicant[i])
            lexicographical_current += alphabet.index(current[i])
        if(lexicographical_applicant < lexicographical_current):
            return applicant
    return current

def get_longest_for_line_both_directions(line):
    longest_word = ""
    longest_horizontal_positive = get_longest_for_line(line)
    inverted = list(line)
    inverted.reverse()
    longest_horizontal_negative = get_longest_for_line(inverted)

    longest_word = lexicographically_superior_word(longest_word, longest_horizontal_positive)
    longest_word = lexicographically_superior_word(longest_word, longest_horizontal_negative)

    print "positive longest: {0}, negative longest: {1}".format(longest_horizontal_positive, longest_horizontal_negative)
    return longest_word

def get_longest_for_line(line):
    current_longest = ""
    longest_word = ""

    for i in range(len(line)):
        current_char = line[i]
        current_index = alphabet.index(current_char)

        if len(current_longest) == 0:
            current_longest = current_char
        else:
            last_char = current_longest[len(current_longest)-1]
            last_index = alphabet.index(last_char)
            if last_index < current_index:
                current_longest = current_longest + current_char
            else:
                longest_word = lexicographically_superior_word(longest_word, current_longest)
                current_longest = current_char

    longest_word = lexicographically_superior_word(longest_word, current_longest)
    return longest_word

def column(matrix, i):
    return [row[i] for row in matrix]

def get_longest(matrix):
    longest_word = ""
    current_longest = ""
    for row in matrix:
        longest_word = get_longest_for_line_both_directions(row)

    for col_index in range(len(matrix[0])):
        col = column(matrix, col_index)
        column_longest = get_longest_for_line_both_directions(col)
        longest_word = lexicographically_superior_word(longest_word, column_longest)

    return longest_word

def main():
    input_string = raw_input("What is the string? ")
    size_of_matrix = raw_input("What is the size of the matrix? ")
    matrix = generate_matrix(input_string, int(size_of_matrix))

    longest_vertical = get_longest(matrix)

    print_matrix(matrix)
    print longest_vertical


if __name__ == "__main__":
    main()
