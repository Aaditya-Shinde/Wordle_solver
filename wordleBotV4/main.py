import copy
from collections import defaultdict

def remove(guess, feedback):
    global answers
    
    temp_words = copy.copy(answers)
    for word in temp_words:
        if get_feedback(guess, word) != feedback:
            answers.remove(word)

def get_feedback(guess, hidden_word):
    feedback = ['b', 'b', 'b', 'b', 'b']

    letter_count = defaultdict(int)
    for i in hidden_word:
        letter_count[i] += 1
    curr_count = defaultdict(int)
    for i in range(5):
        if guess[i] in hidden_word and letter_count[guess[i]]-curr_count[guess[i]] > 0:
            curr_count[guess[i]] += 1
            feedback[i] = 'y'
    for i in range(5):
        if guess[i] == hidden_word[i]:
            curr_count[guess[i]] += 1
            feedback[i] = 'g'

    return ''.join(feedback)

def optimal_guess(possibilities):
    global count
    global guessables
    
    if len(possibilities) <= 2: 
            return possibilities[0]
    best_score = float('inf')   
    final_guess = ""
    for guess in guessables:
        groups = defaultdict(int)
        for hidden_word in possibilities:
            groups[get_feedback(guess, hidden_word)] += 1
        if max(groups.values()) < best_score or (max(groups.values()) == best_score and guess in possibilities):
            best_score = max(groups.values())
            final_guess = guess

    guessables.remove(final_guess)    
    return final_guess

def main():
    guess = input("What would you like your first guess to be? ").lower()#aesir is optimalGuess
    for guess_num in range(6):
        print(guess.upper())
        feedback = input(": ").lower()[:5]
        remove(guess, feedback)
        if feedback == "ggggg":
            print(f"Yes! It only took me {guess_num + 1} tries")
            break
        elif len(answers) == 0:
            print("fail in the logic")
            break
        elif guess_num == 5:
            print("😵")
            break
        guess = optimalGuess(answers)
        print(answers)

if __name__ == "__main__":
    textfile = open("../possibleAnswers.txt", "r")
    answers = textfile.readline().split()
    guessFile = open("../guessables.txt", "r")
    guessables = guessFile.readline().split()
    textfile.close()
    guessFile.close()
    
    main()
