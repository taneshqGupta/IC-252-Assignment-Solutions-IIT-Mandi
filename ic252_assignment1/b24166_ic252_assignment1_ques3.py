import random

n = 10000
player1_wins = 0
player2_wins = 0
ties = 0

for i in range(n):
	player1_dice1 = random.randint(1, 6)
	player1_dice2 = random.randint(1, 6)

	player2_dice1 = random.randint(1, 6)
	player2_dice2 = random.randint(1, 6)
	player2_dice3 = random.randint(1, 6)

	player1_score = player1_dice1 + player1_dice2
	player2_score = player2_dice1 + player2_dice2 + player2_dice3

	if (player1_score > player2_score): player1_wins += 1
	if (player2_score > player1_score): player2_wins += 1
	if (player1_score == player2_score): ties += 1


prob_player1_wins = player1_wins/n
prob_player2_wins = player2_wins/n
prob_ties = ties/n

print(f"Probability of:\nPlayer1 winning = {prob_player1_wins}\nPlayer2 winning = {prob_player2_wins}\nTies = {prob_ties}\n\n")

