class Jumper:
    """A jumper is a person who jumps from aircraft. The responsibility of Jumper is to keep track of their parachute."""

    def __init__(self):
        self.chute = []
        self.chute.append(r"  ___  ")
        self.chute.append(r" /___\ ")
        self.chute.append(r" \   / ")
        self.chute.append(r"  \ /  ")
        self.chute.append(r"   0   ")
        self.chute.append(r"  /|\  ")
        self.chute.append(r"  / \  ")
        self.chute.append(r"       ")
        self.chute.append(r"^^^^^^^")

    #if guess does not match a letter this will delete a portion of the chute.
    def cut_line(self):
        self.chute.pop(0)

    # 0 is still found then the game will continue
    def is_alive(self):
        if '  \ /  ' in self.chute:
            return True
        else:
            print(
                "\n   X   ",
                "\n  /|\  ",
                "\n  / \  ",
                "\n       ",
                "\n^^^^^^^",
                "\nYou Lose"
                )
            return False


    #displays chute
    def get_chute(self):
        print()
        for lines in self.chute:
            print(lines)

class Target:
    """A target is a word the jumper is trying to guess. The responsibility of Target is to keep track of the letters in the word and those that have been guessed."""

    #Create the target word.
    def __init__(self):
        self.letters = ['w', 'u', 't', 'a', 'n', 'g']#put the deisired word in seperate letters
        self.guesses = ['-', '-', '-', '-', '-', '-'] #put the same abount of underscores or dashes as letters in the word

        #create string variable
        self.word = ""
        self.blanks = ""

        #for char in self.letters:
            #self.word += char
        
        #for dash in self.guesses:
            #self.blanks += dash

    def has_letter(self, guess):
        for index, letter in enumerate(self.letters):
            if guess == letter:
                self.guesses[index] = guess
        return guess in self.letters

    
    def is_found(self):
        if self.guesses == self.letters:
            print("\nYou Win!!")
            return True

    def get_guesses(self):
        print(' '.join(self.guesses))

class Trainer:
    """A trainer is a person who trains jumpers. The responsibility of Trainer is to control the sequence of the jump."""
    
    def start_jump(self):
        jumper = Jumper()
        target = Target()

        while jumper.is_alive() and not target.is_found():
            guess = input("\n Guess a letter: ")
            if target.has_letter(guess) != True:
                jumper.cut_line()
            
            target.get_guesses()
            jumper.get_chute()

        
            
    

if __name__ == "__main__":
    trainer = Trainer()
    trainer.start_jump()
