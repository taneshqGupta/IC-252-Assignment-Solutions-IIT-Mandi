import random

testcases = 1000000
cards = [('red', 'black'), ('red', 'red'), ('black', 'black')]

red_count = 0
black_count = 0

for _ in range(testcases):
    card = random.choice(cards) 
    if card == ('red', 'black'):
        upturned_side = random.choice(['red', 'black'])  
    else:
        upturned_side = card[0]

    if upturned_side == 'red':  
        red_count += 1
        if card == ('red', 'black'):  
            black_count += 1

prob = black_count / red_count if red_count else 0

print(prob) 


