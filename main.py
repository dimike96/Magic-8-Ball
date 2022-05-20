# Simple magic 8 ball program

# Imports
import random

# Empty list to add possible answers to
possible_results = []

# Setting up a class for the outcomes
class Outcome:
    def __init__(self, result, type):
        self.result = result
        self.type = type

# Definining the outcomes and adding them to the possible_results list
ans1 = Outcome("It is certain.", 'affirmative')
possible_results.append(ans1)

ans2 = Outcome("It is decidedly so.", 'affirmative')
possible_results.append(ans2)

ans3 = Outcome("Without a doubt.", 'affirmative')
possible_results.append(ans3)

ans4 = Outcome("Yes - definitely.", 'affirmative')
possible_results.append(ans4)

ans5 = Outcome("You may rely on it.", 'affirmative')
possible_results.append(ans5)

ans6 = Outcome("As I see it, yes.", 'affirmative')
possible_results.append(ans6)

ans7 = Outcome("Most likely.", 'affirmative')
possible_results.append(ans7)

ans8 = Outcome("Outlook good.", 'affirmative')
possible_results.append(ans8)

ans9 = Outcome("Yes.", 'affirmative')
possible_results.append(ans9)

ans10 = Outcome("Signs point to yes.", 'affirmative')
possible_results.append(ans10)

ans11 = Outcome("Reply hazy, try again.", 'neutral')
possible_results.append(ans11)

ans12 = Outcome("Ask again later.", 'neutral')
possible_results.append(ans12)

ans13 = Outcome("Better not tell you now.", 'neutral')
possible_results.append(ans13)

ans14 = Outcome("Cannot predict now.", 'neutral')
possible_results.append(ans14)

ans15 = Outcome("Concentrate and ask again.", 'neutral')
possible_results.append(ans15)

ans16 = Outcome("Don't count on it.", 'negative')
possible_results.append(ans16)

ans17 = Outcome("My reply is no.", 'negative')
possible_results.append(ans17)

ans18 = Outcome("My sources say no.", 'negative')
possible_results.append(ans18)

ans19 = Outcome("Outlook not so good.", 'negative')
possible_results.append(ans19)

ans20 = Outcome("Very doubtful.", 'negative')
possible_results.append(ans20)

# The function that randomly choses from the possible_results list, with display text and a quit option
def Magic_Ball():
    while True:
        try:
            print("Welcome to the hyper intelligent python magic 8 ball!!!")
            print(' ')
            user_text = input("Please enter your query to reveal your prediction! (Enter 'Q' to exit) ")
            if (user_text == 'Q') or (user_text == 'q'):
                print("Goodbye and good fortunes!")
                print(' ')
                break
            else:
                print('')
                print((random.choice(possible_results).result))
                print('')
        except:
            user_text == 'Q'

# Call Magic_Ball
def main():
    Magic_Ball()

# Call main
if __name__ == '__main__':
    main()
















