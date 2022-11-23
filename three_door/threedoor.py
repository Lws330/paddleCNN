import random


def play(change):
    prize = random.randint(0,2)
    guess = random.randint(0,2)
    if guess == prize:
        if change:
            return False
        else:
            return True
    else:
        if change:
            return True
        else:
            return False


def winRate(change, N):
    win = 0
    for i in range(N):
        if(play(change)):
            win += 1
    print("中奖率为{}".format(win / N))
N = 1000000
print("每次换门的中奖概率：")
winRate(True,N)
print("每次都不换门的中奖概率：")
winRate(False,N)