#importing the time module
import time
import getpass


class Hangman():

    def __init__(self, answer):
        self.answer = answer
    
    def play(self):
        name = input("\nWhat is your name? ")
        print("\nHello {}, Time to play hangman!".format(name))
        time.sleep(1)
        print("\nStart guessing...")
        time.sleep(0.5)
        guesses = ''
        turns = 10

        while turns > 0:         

            failed = 0  
            print("\n")           
            for char in answer:      
                if char in guesses:    
                    print(char)   
                else:
                    print("_")     
                    failed += 1    
            
            print("\nYou have", + turns, 'more guesses')
  
            if failed == 0:        
                print("\n Contratulations {}, You won!".format(name))
                break  

            guess = input("\n{}, Guess a character: ".format(name))
            guesses += guess                    
            if guess not in answer:  
                turns -= 1        
                print("\nWrong")    
                print("\nYou have", + turns, 'more guesses')
                if turns == 0:
                   print("You Lose")
                   print("The answer was {}".format(answer))

answer = getpass.getpass(prompt="\nPlease securely enter the asnwer to this game:")
game = Hangman(answer)
game.play()  