import random
 
def pick_door():
    return random.randint(1,3)
 
class MontyHall:
    def __init__(self):
        self.prize_door = pick_door()
        self.selected_door = None
        self.removed_door = None
 
    def select_door(self):
        self.selected_door = pick_door()
 
    def remove_door(self):
        d = pick_door()
        while d == self.selected_door or d == self.prize_door:
            d = pick_door()
        self.removed_door = d
 
    def switch_choice(self):
        self.selected_door = 6 - self.selected_door - self.removed_door

    def user_wins(self):
        if self.selected_door == self.prize_door:
            return True
        else:
            return False
 
    def run_game(self, switch=True):
        self.select_door()
        self.remove_door()
        if switch:
            self.switch_choice()
        return self.user_wins()
    
wins, losses = 0, 0
for i in range(1000000):
    # make an instance of the game, call it 'm'
    m = MontyHall()
    # run the game and switch choice of door.
    if m.run_game(switch=True):
        # a return value of True means we've won
        wins += 1
    else:
        # a return value of False means we've lost
        losses += 1
 
# Now that the game has been run one million times, compute/display stats.
perc_win = 100.0*wins / (wins+losses)
 
print ("One million Monty Hall games (with switching):")
print ("won:", wins, "games")
print ("lost:", losses, "games")
print (f"odds: {round(perc_win,2)}% winning percentage",'\n')
 
 
# Now, we'll run the game one million times and always stick to our original
# door selection every single time.
 
wins, losses = 0, 0
for i in range(1000000):
    # make an instance of the game, call it 'm'
    m = MontyHall()
    # run the game and switch choice of door.
    if m.run_game(switch=False):
        # a return value of True means we've won
        wins += 1
    else:
        # a return value of False means we've lost
        losses += 1
 
# Now that the game has been run one million times, compute/display stats.
perc_win = 100.0*wins / (wins+losses)
 
print ("One million Monty Hall games (staying with original choice):")
print ("won:", wins, "games")
print ("lost:", losses, "games")
print (f"odds: {round(perc_win,2)}% winning percentage")