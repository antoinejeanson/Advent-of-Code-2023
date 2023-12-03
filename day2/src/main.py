import dataclasses

with open("input.txt", "r") as f:
    data = f.readlines()

# Part 1

sum = 0
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
    for play in draws_grouped:
        for d in play:
            cubes_count = int(d[0])
            color = d[1].replace(",", "").strip()

            print(color, cubes_count)
        
            if color == 'red' and cubes_count > 12:
                game_is_valid = False
                print('red invalid')

            if color == 'green' and cubes_count > 13:
                game_is_valid = False
                print('green invalid')

            if color == 'blue' and cubes_count > 14:
                game_is_valid = False
                print('blue invalid')

    if game_is_valid:
        sum += game_id
        print("Valid !")
    else:
        print("Invalid !")
    
    print('sum : ' + str(sum))

    print()

print(sum)