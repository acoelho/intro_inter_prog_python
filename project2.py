# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

max_range = 100
max_guess = 7
message1 = "Welcome"
message2 = "Guess the Number"

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global game_range, game_guess, secret_number
    global message1, message2
    game_range = max_range
    game_guess = max_guess
    secret_number = random.randrange(0,game_range)
    print "Guess the number from 1 to " + str(game_range)
    print "You have " + str(game_guess) + " guesses"
    message1 = "Guess a Number"
    message2 = str(game_guess) + " Guesses Left"


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global max_range, max_guess
    max_range = 100
    max_guess = 7
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global max_range, max_guess
    max_range = 1000
    max_guess = 10
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global game_guess, message1, message2
    n_guess = int(guess)
    print "You guessed " + guess
    if (n_guess == secret_number ) :
        print "You win!"
        print
        new_game()
    else :
        game_guess -= 1
        if (game_guess < 1) :
            print "Sorry, you lose. The number was " + str(secret_number)
            print
            new_game()
        else :
            if (n_guess > secret_number) :
                print "Lower!"
                message1 = "Lower!"
            else :
                print "Higher!"
                message1 = "Higher!"
                
            print "You have " + str(game_guess) + " guesses left"
            message2 = str(game_guess) + " guesses left"
            
            
def draw(canvas):
    canvas.draw_text(message1, [30,72], 38, "Red")  
    canvas.draw_text(message2, [40,152], 30, "Red")  
            
    
# create frame
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Guess the Number", 300, 200)
frame.add_button("[0-100)", range100)
frame.add_button("[0-1000)", range1000)
frame.add_input("Enter your guess", input_guess, 50)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric