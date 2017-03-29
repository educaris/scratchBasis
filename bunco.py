import random

player1_dice = []
player2_dice = []

for i in range(3):
    player1_dice.append(random.randint(1,6))
    player2_dice.append(random.randint(1,6))

print("speler 1 heeft gerold" + str(player1_dice))
print("speler 2 heeft gerold" + str(player2_dice))

if sum(player1_dice) == sum(player2_dice):
    print("gelijk spel")
elif sum(player1_dice) > sum(player2_dice):
        print("player 1 wint")
else:
        print("player 2 wint")
