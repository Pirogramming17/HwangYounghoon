import random

def brGame(player, num):
    if player == 'player':
        while True:
            try:
                count = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
                count = int(count)
                if count < 1 or count > 3:
                    raise Exception("1,2,3 중 하나를 입력하세요")
                break
            except ValueError:
                print("정수를 입력하세요")
            except Exception as e:
                print(e)
    else:
        count = random.randint(1,3)

    for _ in range(count):
        num += 1
        print(f"{player} : {num}")
        if num == 31:
            break
    return num

num = 0

while True:
    num = brGame('computer', num)
    if num == 31:
        print("player win!")
        break

    num = brGame('player', num)
    if num == 31:
        print("computer win!")
        break
