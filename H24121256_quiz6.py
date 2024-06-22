import random
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def get_user_guess():
	while  True:
		guess = str(input("Guess the lowercase alphabet: "))
		if guess in alphabet:
			return guess
		else:
			print("Please enter a lowercase alphabet: ")	

def player_guess():
	answer = random.choice(alphabet)
	guesses = []
	while True:
		user_guess = get_user_guess()
		guesses.append(user_guess)
		if alphabet[user_guess] < alphabet[answer]:
			print("The answer you are looking for is alphabetically lower.")
		elif alphabet[user_guess] > alphabet[answer]:
			print("The answer you are looking for is alphabetically higher.")
		else:
			print("Congratulations! You guessed the alphabet",user_guess,"in",len(guesses),"tries")
			# Create histogram of guesses.
			 
			print("Guess Histogram: ")



