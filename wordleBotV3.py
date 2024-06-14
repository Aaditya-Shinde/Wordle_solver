import random

textfile = open("possibleAnswers.txt", "r")
answers = textfile.readline().split()
guessFile = open("guessables.txt", "r")
guessables = guessFile.readline().split()
textfile.close()
guessables.close()

count = {'c': 446, 'i': 646, 'g': 299, 'a': 906, 'r': 835, 'e': 1053, 'b': 266, 'u': 456, 't': 667, 's': 617, 'y': 416, 'h': 377, 'm': 298, 'p': 345, 'w': 193, 'k': 202, 'l': 645, 'f': 206, 'o': 672, 'v': 148, 'd': 370, 'n': 548, 'q': 29, 'j': 27, 'x': 37, 'z': 35}
#these values are from the original guessables file before we tamper with it.

def remove(guess, feedback):
    global answers
    global count
    import copy

    def hasBlack(word, black):    #checking if word has a grey letter
        for letter in black:
            if letter in word:
                return True
        return False

    def notAllRequired(green, yellow, word):    #checking if word doesn't have all yellow and green letters
        for i in green:
            if not i in word:
                return True
        for j in yellow:
            if not j in word:
                return True
        return False

    def yellowWrongPlace(yellow, word):    #checking if the yellow letters are in the wrong place
        for idx in range(5):
            letter = word[idx]
            if letter in yellow and idx in yellow[letter]:
                return True
        return False

    def greenNotInRightPlace(green, word):    #checking if the green letters are in the wrong place
        for required in green:
            if word[green[required]] != required:
                return True
        return False
    
    temp_words = copy.copy(answers)
    black = set()
    yellow = {}
    green = {}
    for idx in range(5):
        if feedback[idx] == 'b':
            black.add(guess[idx])
        elif feedback[idx] == 'y':
            if guess[idx] in yellow:
                yellow[guess[idx]].add(idx)
            else:
                yellow.update({guess[idx]:{idx}})
        elif feedback[idx] == 'g':
            green.update({guess[idx]:idx})

    for word in temp_words:
        if hasBlack(word, black) or notAllRequired(green, yellow, word) or yellowWrongPlace(yellow, word) or greenNotInRightPlace(green, word):
            answers.remove(word)
            for idx in range(5):
                letter = word[idx]
                if not letter in word[:idx]:
                    count[letter] -= 1

def optimalGuess(possibilities):
    global count
    global guessables
    
    if len(possibilities) <= 2: #If there are three possibilities then there's really no use in doing the computing, it's a 50/50 
        return random.choice(possibilities)
    best_score = 9999999999    #impossible to reach but needs to be defined before hand
    final_guess = ""
    for guess in guessables:
        score = 0
        for idx in range(5):
            letter = guess[idx]
            score += abs(count[letter]-(len(possibilities)//2))    #the least score is the best because it eliminates the closest to half of the answers.
        if score < best_score:
            best_score = score
            final_guess = guess

    guessables.remove(final_guess)    #because we will be guessing it and it will have to be removed(unless of course it's the answer in which case it doesn't matter because the programm will exit)
    return final_guess

guess = input("What would you like your first guess to be? ").lower()
for guess_num in range(6):
    print(guess.upper())
    feedback = input(": ").lower()
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
