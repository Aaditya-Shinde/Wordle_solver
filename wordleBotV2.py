textfile = open("possibleAnswers.txt", "r")
words = textfile.readline().split()
textfile.close()

def remove(guess, feedback):
    global words
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
    
    temp_words = copy.copy(words)
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
            words.remove(word)

def optimalGuess(possibilities):
    return possibilities[len(possibilities)//2]    #Choosing a guess in the middle of possibilities at random. Doesn't really make a differnece if you chose any other guess

guess = input("What do you want your first guess to be? ")
for guess_num in range(6):
    print(guess.upper())
    feedback = input(": ").lower()
    if feedback == "ggggg":
        print(f"Yes! It only took me {guess_num + 1} tries")
        break
    elif len(words) == 0:
        print("fail in the logic")
        break
    elif guess_num == 5:
        print("😵")
        break
    remove(guess, feedback)
    guess = optimalGuess(words)
    print(words)
    print()
