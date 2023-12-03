with open("input.txt", "r") as f:
    data = f.readlines()

sum_part1 = 0
sum_part2 = 0

for line in data:
    game_id = int(line.split(" ")[1][:-1])
    
    draws = line.split(":")[1].split(";")
    draws = [draw.strip() for draw in draws]
    draws = [draw.split(" ") for draw in draws]

    # Group draws by 2
    draws_grouped = []
    for d in draws:
        plays_count = len(d) // 2
        current_play = []
        for play in range(plays_count):
            current_play.append(d[play*2:play*2+2])
        draws_grouped.append(current_play)
    
    print(game_id, draws_grouped)

    game_is_valid = True

    # For part 2
    max_red = 0
    max_green = 0
    max_blue = 0

    for play in draws_grouped:
        for d in play:
            cubes_count = int(d[0])
            color = d[1].replace(",", "").strip()

            print(color, cubes_count)
        
            if color == 'red':
                if cubes_count > 12:
                    game_is_valid = False
                    print('red invalid')
                if cubes_count > max_red:
                    max_red = cubes_count

            if color == 'green':
                if cubes_count > 13:
                    game_is_valid = False
                    print('green invalid')
                if cubes_count > max_green:
                    max_green = cubes_count

            if color == 'blue':
                if cubes_count > 14:
                    game_is_valid = False
                    print('blue invalid')
                if cubes_count > max_blue:
                    max_blue = cubes_count
            
    power = max_red * max_green * max_blue
    print('power : ' + str(power))
    sum_part2 += power

    if game_is_valid:
        sum_part1 += game_id
        print("Valid !")
    else:
        print("Invalid !")
    
    print('sum : ' + str(sum_part1))

    print()

print(sum_part1)
print(sum_part2)