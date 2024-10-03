score = 0
lives = 3
obsitical = -1
player_x,player_y = 0,0
direction= input("enter your direction")
def move_player(direction):
    global player_x,player_y

    if direction == "up":
        player_y = player_y + 1

    elif direction == "down":
        player_y = player_y - 1

    elif direction == "left":
        player_x= player_x - 1

    elif direction == "right":
        player_x = player_x +1

    else:
        print("inavlid move")

def loose_life():
    global lives
    if lives > 0:
        lives = lives - 1
        print(f' remaining lives {lives}')
    else:
        print("GAME OVER")

def gain_scores(points):
    global score
    score = score + points
    print(f'your scocores {points} your score is now {score}')
    
    
        
while lives > 0:
    print("STARTING GAME")
    

    #
    gain_scores(100)
    print(score)

    #

    loose_life()
    print(lives)

    #

    move_player(direction)
    print(player_x,player_y)

    #

    gain_scores(90)
    print(score)

    #

    loose_life()
    print(f'lives left{lives}')
    
