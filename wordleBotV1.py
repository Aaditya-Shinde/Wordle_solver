textfile = open("possibleAnswers.txt", "r")
words = textfile.readline().split()
textfile.close()

def hasBlack(word, black):#checking if word has a grey letter
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

def greenWrongPlace(green, word):    #checking if the green letters are in the wrong place
    for idx in range(5):
        letter = word[idx]
        if letter in green and idx != green[letter]:
            return True
    return False

def remove(guess, feedback):    #shortens the possible answers through feedback
    global words
    import copy

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
        if hasBlack(word, black) or notAllRequired(green, yellow, word) or yellowWrongPlace(yellow, word) or greenWrongPlace(green, word):
            words.remove(word)

letters = ["GLENT", "BRICK", "JUMPY", "WAQFS", "VOZHD"]    #covers 25 out of 26 letters in the alphabet
for guess_num in range(5):
    guess = letters[guess_num]
    print(guess.upper())
    feedback = input(": ")
    if feedback == "ggggg":
        print(f"Yes! It only took me {guess_num + 1} tries")
        break
    remove(guess, feedback)
    print(words)
    print()

guess = words[0]
print(guess.upper())
feedback = input(": ").lower()
if feedback == "ggggg":
    print(f"Yes! I got it!")
else:
    print("😵")    #The method is not perfect and doesn't always get it in 6 tries

#THIS DOESN'T ACCOUNT FOR DOUBLE LETTERS. The program is still usable but YOU HAVE TO MANIPULATE THE FEEDBACK
#i.e. if the word you guess is "HELLO" and the result is "BBGBB" then your feedback should be "BBGYB"
