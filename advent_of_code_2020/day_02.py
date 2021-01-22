# https://adventofcode.com/2020/day/2
import re

def split_line_into_primitives(line):
    min_occurrence, max_occurrence, letter, password = re.split(": | |-", line.rstrip())
    return int(min_occurrence), int(max_occurrence), letter, password


def puzzle_part1(password_list):
    count = 0
    for item in password_list:
        test = item[3].count(item[2])
        if (test >= item[0] and test <= item[1]):
            count += 1
    return count
        

def puzzle_part2(password_list):
    count = 0
    for item in password_list:
            if ((item[3][item[0] - 1] == item[2]) ^ (item[3][item[1] - 1] == item[2])):
                count += 1
    return count


def open_file(file_name):
    with open(file_name) as puzzle_input:
        password_database = []
        for line in puzzle_input:
            password_database.append(line)

    explicit_password_database = map(split_line_into_primitives, password_database)

    return list(explicit_password_database)

def main():

    input_file = "./advent_of_code_2020/input_day02.txt"

    password_list = open_file(input_file)

    print ("The solution for the 1st part of the puzzle:")
    print (puzzle_part1(password_list))
    print ()
    print ("The solution for the 2nd part of the puzzle:")
    print (puzzle_part2(password_list))


if __name__ == "__main__":
    main()