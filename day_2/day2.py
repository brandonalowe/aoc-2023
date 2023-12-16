import numpy as np
def part1():
    bag = {
        'r' : 12,
        'g' : 13,
        'b' : 14
    } 

    try:
        f = open("/Users/brandon/AOC/aoc-2023/day_2/puzzle.txt", "r")
        puzzle_input = f.read()
    except:
        return 
#     puzzle_input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
    
    split_lines = puzzle_input.split('\n')
    games = {}
    sum_of_ids = 0

    for l in split_lines:
        failed = False
        game, sets = l.split(":")[0].split(" ")[1], l.split(":")[1]

        for s in sets.split(";"):
            for c in  s.split(","):
                c = c.lstrip(" ").rstrip(" ")
                num_cubes, col = c.split(" ")
                if int(num_cubes) > bag[col[0]]:
                    games[game] = 0
                    failed = True

        if failed != True:
            games[game] = 1

    for g in games:
        if games[g] == 1:
            sum_of_ids += int(g)
        # print(games)
        # print(game[-1], sets)
    print (sum_of_ids)

def part2():
    try:
        f = open("/Users/brandon/AOC/aoc-2023/day_2/puzzle.txt", "r")
        puzzle_input = f.read()
    except:
        return 
#     puzzle_input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
    
    split_lines = puzzle_input.split('\n')
    games = {}
    sum_of_ids = 0

    for l in split_lines:
        game, sets = l.split(":")[0].split(" ")[1], l.split(":")[1]

        min_cubes = {}

        for s in sets.split(";"):
            for c in  s.split(","):
                c = c.lstrip(" ").rstrip(" ")
                num_cubes, col = c.split(" ")

                if col[0] not in min_cubes.keys():
                    min_cubes[col[0]] = int(num_cubes)
                else:
                    if min_cubes[col[0]] < int(num_cubes):
                        min_cubes[col[0]] = int(num_cubes)
        
        games[game] = np.prod([val for val in min_cubes.values()])

    sum_of_powers = sum(games.values())
        # print(games)
        # print(game[-1], sets)
    print (sum_of_powers)

if __name__ == "__main__":
    part2()
