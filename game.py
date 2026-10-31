from random import randint, shuffle
import sys

width = 0
depth = 0

print("welcome to the haunted house")
difficulty = input("What difficulty do you want? easy, medium, hard or hell: ")
if difficulty == "easy":
    width_size = 2
    depth_size = 1
    house = [["main hall"],["exit"]]
    ghost_max_HP = 80
    player_max_HP = 120
elif difficulty == "medium":
    width_size = 3
    depth_size = 2
    ghost_max_HP = 100
    player_max_HP = 100
    house = [["main hall", "study"],["library", "master bedroom"],["dining room", "exit"]]
elif difficulty == "hard":
    width_size = 4
    depth_size = 3
    ghost_max_HP = 120
    player_max_HP = 80
    house = [["library", "master bedroom", "big cupboard"], ["main hall", "study", "pokemon card room"], ["dining room", "exit", "classroom"], ["gaming room", "model train room", "big room"]]
elif difficulty == "hell":
    width_size = 5
    depth_size = 5
    house = [["library", "master bedroom", "big cupboard", "swimming pool room", "guest bedroom"],["main hall", "study", "pokemon card room", "TV room", "ghost's bedroom"],["dining room", "exit", "classroom", "computer science room", "hall"],["gaming room", "model train room", "big room", "maths room", "laboratory"],["dog's bedroom", "Laptop room", "ping pong room", "children's play area", "nutella eating room"]]
    ghost_max_HP = 150
    player_max_HP = 80

for i in range(len(house)):
    shuffle(house[i-1])
shuffle(house)

location = house[0][0]

moves = [["attck", 35], ["block", 0], ["heal", 20]]
ghost_HP = ghost_max_HP
player_HP = player_max_HP

def ghost_battle(ghost_max_HP, ghost_HP, player_max_HP, player_HP):
    while ghost_HP > 0 and player_HP > 0:
        player_blocked = False
        ghost_blocked = False
        player_move = input("would you like to attack, block or heal?: ")
        if player_move == "block":
            player_blocked = True
        ghost_move = randint(0,2)
        if ghost_move == 0:
            if player_blocked:
                print("the ghost's attack was blocked")
            else:
                player_HP -= moves[0][1]
                print("the ghost attacked you")
        elif ghost_move == 1:
            ghost_blocked = True
            print("the ghost blocked")
        elif ghost_move == 2:
            print("the ghost healed itself")
            ghost_HP += moves[2][1]
            if ghost_HP > ghost_max_HP:
                ghost_HP = ghost_max_HP
        player_blocked = False
        if player_move == "attack":
            if ghost_blocked:
                print("your attack was blocked by the ghost")
            else:
                ghost_HP -= moves[0][1]
                print("You attacked the ghost")
        elif player_move == "block":
            print("you blocked")
        elif player_move == "heal":
            player_HP += moves[2][1]
            if player_HP > player_max_HP:
                player_HP = player_max_HP
                print("You healed yourself")
        ghost_blocked = False
        if ghost_HP <= 0 and player_HP <= 0:
            print("the ghost and you killed each other")
            sys.exit()
        elif ghost_HP <= 0:
            print("the ghost died")
            pass
        elif player_HP <= 0:
            print("the ghost killed you")
            sys.exit()
        print("ghost hp:", ghost_HP, "/", ghost_max_HP)
        print("player hp:", player_HP, "/", player_max_HP)

while location != "exit":
    ghost = randint(0, 2)
    print("you are currently in the", location)
    if ghost > 1:
        print("you found a ghost!")
        print("the ghost challenged you to battle!")
        ghost_battle(ghost_max_HP, ghost_HP, player_max_HP, player_HP)
    direction = input("right, left, forward or backward: ")
    if direction == "right":
        width += 1
        width = width % width_size
    elif direction == "left":
        width -= 1
        width = width % width_size
    elif direction == "forward":
        depth += 1
        depth = depth % depth_size
    elif direction == "backward":
        depth -= 1
        depth = depth % depth_size
    location = house[width][depth]

print("you escaped !")