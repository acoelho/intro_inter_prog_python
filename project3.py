# template for "Stopwatch: The Game"
import simplegui
import time



# define global variables
time_elapse = 0 
message1 = "00:00:00.0"
wins = 0
tries = 0
running = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    u = t
    hrs = "00"
    mins = "00"
    secs = "00"
    if u >= 36000 :
        h = (u - (u % 36000)) / 36000
        if h < 10 : 
            hrs = "0" + str(h)
        else :
            hrs = str(h)
        u = u - h * 36000
    if u >= 600 :
        m = (u - (u % 600)) / 600
        u = u - m * 600
        if m < 10 : 
            mins = "0" + str(m)
        else :
            mins = str(m)
    if u >= 10 :
        s = (u - (u % 10)) / 10
        u = u - s * 10
        if s < 10 : 
            secs = "0" + str(s)
        else :
            secs = str(s)
    ms = u
    return hrs + ":" + mins + ":" + secs + "." + str(ms) 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    # start 
    global running
    running = 1
    timer.start()


def stop():
    #   
    global wins, tries, running
    timer.stop()
    if (time_elapse % 10 == 0) :
        if running == 1 :
            wins += 1
    if running == 1 :
        tries += 1
    running = 0
    
def reset():
    #
    global time_elapse, wins, tries, running, message1
    timer.stop()
    wins = 0
    tries = 0
    time_elapse = 0
    running = 0
    message1 = "00:00:00.0"
    

# define event handler for timer with 0.1 sec interval
def update():
    global time_elapse, message1 
    time_elapse += 1
    message1 = format(time_elapse)


# define draw handler
def draw(canvas):
    canvas.draw_text(message1, [50,75], 46, "Red")
    canvas.draw_text(str(wins), [45,142], 28, "Red")  
    canvas.draw_text(str(tries), [190,142], 28, "Red")
    canvas.draw_text("Wins", [45,172], 28, "Red")  
    canvas.draw_text("Tries", [190,172], 28, "Red")
 
            
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
    
# register event handlers
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)


frame.set_draw_handler(draw)


timer = simplegui.create_timer(100, update)

# start frame
frame.start()

# Please remember to review the grading rubric