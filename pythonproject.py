import random
class pos_of_player:
    def posistion(pos,ladder,snake):
        while pos<=50:
            a=random.randint(1,6)
            print("the dice value is  "+str(a))
            pos+=a

            if pos>50:
                pos=pos-a
                print("the dice value is higher then required")
            if pos==50:
                print("it reached end")
                break
            if pos in ladder.keys():
                pos=ladder[pos]
                print("it climed laddder")
            elif pos in snake.keys():
                pos=snake[pos]
                print("it hit a snake")
            else:
                pass

            print(str(pos)+"  "+"posistion of player")
class Snakeandladder:
    def __init__(self):
        ladder={7:10,18:23,29:49}
        snake={18:5,29:10,49:1}
        pos=1
        pos_of_player.posistion(pos,ladder,snake)
obj=Snakeandladder()
