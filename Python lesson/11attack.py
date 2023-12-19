import random

playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 0:
        playerhp = 0
    print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp)

    if playerhp == 0:
        print("You have died.")

    if 50 >= playerhp >= 1:
        print("You have low health. You've been teleported to the nearest inn.")
        break
