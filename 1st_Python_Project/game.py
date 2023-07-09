import random
randno = random.randint(1, 3)

def gamewin(comp, your_turn):
        
        if comp == your_turn:
                return None

        elif comp == 's':
                if your_turn == 'w':
                        return False
                elif your_turn == 'g':
                        return True
                
                elif comp == 'w':
                        if your_turn == 's':
                                return True
                        elif your_turn == 'g':
                                return False
                        
                        elif comp == 'g':
                                if your_turn == 's':
                                        return False
                                elif your_turn == 'w':
                                        return True
                        

print("Computer Turn: Snake(s) , Water(w) , Gun(g): ?\n")
# print(randno)
if randno == 1:
    comp = 's' 
elif randno == 2: 
        comp = 'w'
elif randno == 3:
            comp = 'g'

your_turn = input("Your Turn: Snake(s) , Water(w) , Gun(g): ?\n")
game = gamewin(comp , your_turn)

print(f"Computer Chose {comp}")
print(f"You Chose {your_turn}")

if game == None:
        print('The game is tie!')
elif game:
        print('You win!')
else:
        print('You lose!')