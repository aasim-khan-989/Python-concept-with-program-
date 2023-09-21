"""  STONE PAPER SCISSORS GAME    """
import random
for i in range(6):
    player = input('Your turn: Enter Stone paper or Scissor\nor enter stop for existing the game\n')
    player = player.lower()
    if player == 'stop':
        print('THANKS FOR PLAYING GAME')
        break
    computer = random.randint(1, 3)
    if computer == 1:
        computer = 'stone'
    elif computer == 2:
        computer = 'paper'
    else:
        computer = 'scissor'
    print('Computer turn: Computer has enter :', computer)
    def game(x, y):
        if player == 'stone':
            if computer == 'scissor':
                return "YOU WIN!!!!"
            elif computer == 'paper':
                return 'YoU LOSE!!!'
            else:
                return " IT'S A DRAW"
        elif player == 'paper':
            if computer == 'stone':
                return "YOU WIN!!!!"
            elif computer == 'scissor':
                return 'YAU LOSE!!!'
            else:
                return " IT'S A DRAW"
        elif player == 'scissor':
            if computer == 'paper':
                return "YOU WIN!!!!"
            elif computer == 'stone':
                return 'YAU LOSE!!!'
            else:
                return " IT'S A DRAW"
        else:
            return"You have enter wrong input try again."
    print(game(1, 2))
else:
    print('Take rest and play after some time')
