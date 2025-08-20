import random
import time

turns_per_difficulty = {1: 10, 2: 20, 3: 25}
Gym_Leader_difficulty = 1
Elite_Four_difficulty = 2
Champion_difficulty = 3
Gym_and_Elite4_nmbr_types = 4
Champion_nmbr_types = 6
typings_classic = {'normal': 0, 'grass': 1, 'bug': 2, 'fire': 3, 'water': 4, 'ice': 5, 'electric': 6, 'flying': 7, 'fighting': 8,
           'psychic': 9, 'ghost': 10, 'dark': 11, 'poison': 12, 'rock': 13, 'ground': 14, 'steel': 15, 'fairy': 16, 'dragon': 17}
typings_alt = {'normie': 0, 'weed': 1, 'cockroach': 2, 'oven': 3, 'wet': 4, 'brrr': 5, 'zap': 6, 'high': 7, 'john cena': 8,
               'mental': 9, 'boo': 10, 'sasuke': 11, 'alcohol': 12, 'hard': 13, 'down': 14, 'chainz': 15, 'winx': 16, 'xX_cool_type_Xx': 17}
effectiveness_matrix = [[-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0.5, 1, 0.5, 1, 1],
                        [1, -1, 0.5, 0.5, 2, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 2, 2, 0.5, 1, 0.5],
                        [1, 2, -1, 0.5, 1, 1, 1, 0.5, 0.5, 2, 0.5, 2, 0.5, 1, 1, 0.5, 0.5, 1],
                        [1, 2, 2, -1, 0.5, 2, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 2, 1, 0.5],
                        [1, 0.5, 1, 2, -1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5],
                        [1, 2, 1, 0.5, 0.5, -1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 0.5, 1, 2],
                        [1, 0.5, 1, 1, 2, 1, -1, 2, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0.5],
                        [1, 2, 2, 1, 1, 1, 0.5, -1, 2, 1, 1, 1, 1, 0.5, 1, 0.5, 1, 1],
                        [2, 1, 0.5, 1, 1, 2, 1, 0.5, -1, 0.5, 0, 2, 0.5, 2, 1, 2, 0.5, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 2, -1, 1, 0, 2, 1, 1, 0.5, 1, 1],
                        [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, -1, 0.5, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 0.5, 2, 2, -1, 1, 1, 1, 1, 0.5, 1],
                        [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, -1, 0.5, 0.5, 0, 2, 1],
                        [1, 1, 2, 2, 1, 2, 1, 2, 0.5, 1, 1, 1, 1, -1, 0.5, 0.5, 1, 1],
                        [1, 0.5, 0.5, 2, 1, 1, 2, 0, 1, 1, 1, 1, 2, 2, -1, 2, 1, 1],
                        [1, 1, 1, 0.5, 0.5, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, -1, 2, 1],
                        [1, 1, 1, 0.5, 1, 1, 1, 1, 2, 1, 1, 2, 0.5, 1, 1, 0.5, -1, 2],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, -1]]

def init():
    difficulty = input("What difficulty do you want to play in ? (1: Gym Leader; 2: Elite Four; 3: Champion)\n")
    try:
        difficulty = int(difficulty)
        if not (difficulty in [Gym_Leader_difficulty, Elite_Four_difficulty, Champion_difficulty]):
            return -1, -1
    except ValueError:
        return -1, -1
    typing = input("What kind of types do you want to play with ? (1: Classic, 2: Alternatives)\n")
    try:
        typing = int(typing)
    except ValueError:
        return -1, -1
    if typing == 1:
        choice = typings_classic
    elif typing == 2:
        choice = typings_alt
    else:
        return -1, -1

    return difficulty, choice

def loop(turns, difficulty, typings):
    number_types = Champion_nmbr_types if difficulty == Champion_difficulty else Gym_and_Elite4_nmbr_types
    foe_types = [random.randrange(18) for _ in range(number_types)]
    print(f"Foe has chosen their {number_types} types.")
    for k in range(turns):
        print(f"{turns-k} turns remaining...")
        print(f"Select your {number_types} types:\n---")
        for typing in typings.keys():
            print(f"{typing}({str(typings[typing])}), ", end='')
        print("\n---")
        player_types = input("Your types (in the form \"Number" + ".Number"*(Champion_nmbr_types-1 if difficulty == Champion_difficulty else Gym_and_Elite4_nmbr_types-1) + "\") : ").split('.')
        while not parse_types(player_types, difficulty):
            print("Error when parsing types, please retry:")
            player_types = input("Your types (in the form \"Number" + ".Number"*(Champion_nmbr_types-1 if difficulty == Champion_difficulty else Gym_and_Elite4_nmbr_types-1) + "\") : ").split('.')

        time.sleep(0.5)
        print('')

        player_success = compare_types(typings, player_types, foe_types, order= True if difficulty == 1 else False)
        if player_success:
            print("Victory !!!")
            return True

        time.sleep(0.5)
        print('')

    print("Defeat !!!")
    return True


def parse_types(types, difficulty):
    number_types = Champion_nmbr_types if difficulty == Champion_difficulty else Gym_and_Elite4_nmbr_types
    if types == ['']:
        types[0] = random.randrange(18)
        for k in range(1, number_types):
            types.append(random.randrange(18))
        return True
    if len(types) != number_types:
        return False
    for type in types:
        try:
            int(type)
        except ValueError:
            return False
    return True


def compare_types(typings, player_types, foe_types, order):
    player_types = [int(x) for x in player_types]
    if player_types == foe_types:
        return True

    useless_count, not_very_effective_count, effective_count, very_effective_count, same_count = 0, 0, 0, 0, 0
    for index in range(len(player_types)):
        effectiveness = effectiveness_matrix[player_types[index]][foe_types[index]]
        player_type = list(typings.keys())[player_types[index]]
        match effectiveness:
            case 0:
                if order:
                    print(f"Your type n°{index+1}({player_type}) is useless against mine.")
                else:
                    useless_count += 1
            case 0.5:
                if order:
                    print(f"Your type n°{index+1}({player_type}) is not very effective against mine.")
                else:
                    not_very_effective_count += 1
            case 1:
                if order:
                    print(f"Your type n°{index+1}({player_type}) is effective against mine.")
                else:
                    effective_count += 1
            case 2:
                if order:
                    print(f"Your type n°{index+1}({player_type}) is very effective against mine.")
                else:
                    very_effective_count += 1
            case -1:
                if order:
                    print(f"Your type n°{index+1}({player_type}) is the same as mine !")
                else:
                    same_count += 1
            case _:
                print("Error when matching effectiveness")
                return False
        player_types[index] = player_type

    if not order:
        print(f"Your types: {player_types}")
        if useless_count > 0:
            print(f"Among your types there are {useless_count} that are useless against mines.")
        if not_very_effective_count > 0:
            print(f"Among your types there are {not_very_effective_count} that are not very effective against mines.")
        if effective_count > 0:
            print(f"Among your types there are {effective_count} that are effective against mines.")
        if very_effective_count > 0:
            print(f"Among your types there are {very_effective_count} that are very effective against mines.")
        if same_count > 0:
            print(f"Among your types there are {same_count} that are the same as mines !")


if __name__ == '__main__':
    difficulty_choice, typing_choice = init()
    if difficulty_choice == -1 or typing_choice == -1:
        print("Error while initializing game")
    else:
        loop(turns=turns_per_difficulty[difficulty_choice], difficulty=difficulty_choice, typings=typing_choice)



"""
    // TODO
    # dialogues en mode pkmn
"""