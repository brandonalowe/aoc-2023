def main():
    num_dict = {
        'one' : '1' ,
        'two': '2' ,
        'three': '3', 
        'four' : '4', 
        'five': '5' ,
        'six' : '6' ,
        'seven': '7', 
        'eight': '8', 
        'nine'  : '9' 
    }
    key_list = list(num_dict.keys())
    calibration_results = []
    try:
        f = open("/Users/brandon/AOC/aoc-2023/day_1/puzzle_a.txt", "r")
        puzzle_input = f.read()
    except:
        return 
    # puzzle_input = 'five2two7hstbbqzrninegbtwo2'
    # \ntwo1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen'

    split_lines = puzzle_input.split('\n')
    for l in split_lines:
        tmp = ''

        for i, char in enumerate(l):
            if char.isalpha() and i != len(l) - 2:
                for k in key_list:
                    if l[i:i + len(k)] == k:
                        tmp += num_dict[k]
            if char.isnumeric():
                tmp += char
        print(l, tmp)
        line_cali = tmp[0] + tmp[-1]
        calibration_results.append(int(line_cali))
    print(calibration_results)
    print(sum(calibration_results))

if __name__ == "__main__":
    main()