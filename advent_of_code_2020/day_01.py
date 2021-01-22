# https://adventofcode.com/2020/day/1

def puzzle_part1(int_array):
    for i in range(len(int_array)):
        for j in range(i+1, len(int_array)):
            if (int_array[i] + int_array[j] == 2020):
                return int_array[i] * int_array[j]

def puzzle_part2(int_array):
    for i in range(len(int_array)):
        for j in range(i+1, len(int_array)):
            for k in range(j+1, len(int_array)):
                if (int_array[i] + int_array[j] + int_array[k] == 2020):
                    return int_array[i] * int_array[j] * int_array[k]


def main():
    with open('./advent_of_code_2020/input_day01.txt') as puzzle_input:
        expences = []
        for line in puzzle_input:
            expences.append(int(line))

    print ("The solution for the 1st part of the puzzle:")
    print (puzzle_part1(expences))
    print ()
    print ("The solution for the 2nd part of the puzzle:")
    print (puzzle_part2(expences))


if __name__ == "__main__":
    main()