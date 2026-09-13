#khởi động
import random
RPS = ["rock", "paper", "scissors"]
#def tù tì
def rule(player, bot):
    if player == bot:
        print("hòa rồi")
    elif (player == RPS[0] and bot == RPS[1] or player == RPS[1] and bot == RPS[2] or player == RPS[2] and bot == RPS[0]):
        print("you lose")
    else:
        print("you win")
#def vận hành
def game(number):
    for x in range(number):
        bot = random.choice(RPS)
        while True:
            player = input("hãy chọn rock or paper or scissors ")
            if player not in ["rock", "paper", "scissors"]:
                print("không hợp lệ")
                continue
            break
        rule(player, bot)
while True:
    try:
        tra_loi = float(input("bạn muốn chơi mấy ván "))
        if tra_loi <= 0 or tra_loi % 1 != 0:
            print("byeee")
            break
        number = int(tra_loi)
        game(number)
    except ValueError:
        print("bug")
        continue

                
        
        
    
 