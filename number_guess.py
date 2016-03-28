range_lo, range_hi = (1, 100)
number_range = (range_lo, range_hi)

def number_guess(p=None):
    global number_range
    if p is None:
        p=range_hi/2
    reply = raw_input("Is your number {0}? Reply with 'yes,' 'higher,' or 'lower.'".format(p))
    if reply == "yes":
        print "Cool! I'm the best."
        return
    if reply == "higher":
        number_range = (p + 1, number_range[1])
    if reply == "lower":
        number_range = (number_range[0], p)
    midway = number_range[0] + (number_range[1] - number_range[0]) / 2
    number_guess(int(midway))



def rawr_cute():
    return "You look lovely today!"

print """Welcome to the Numbers Guessing Game! {0}
To get started, think of a whole number between {1} and {2}. When you're
ready to play, press 'Enter.'""".format(rawr_cute(), range_lo, range_hi)

raw_input()

number_guess()