import tkinter
import tkmacosx
import main

def change_color(button_num):
    letters[button_num].configure(bg=colors[(colors.index(letters[button_num]["bg"])+1)%3])

def feedback_to_string():
    global feedback
    global flag

    feedback = ""
    for letter in letters:
        feedback += ['b', 'y', 'g'][colors.index(letter["bg"])]
    print(feedback)
    flag = True
    return feedback

root = tkinter.Tk()
root.title("Wordler")
root.geometry("500x70")
root.eval('tk::PlaceWindow . center')
root.attributes('-topmost', True)

frame = tkinter.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

colors = ["#403c3c", "#b89c3c", "#40743c"]
letters = [
           tkmacosx.Button(frame, text = "B", bg = "#b89c3c", fg = "#ffffff", command = lambda: change_color(0)), 
           tkmacosx.Button(frame, text = "B", bg = "#403c3c", fg = "#ffffff", command = lambda: change_color(1)), 
           tkmacosx.Button(frame, text = "B", bg = "#40743c", fg = "#ffffff", command = lambda: change_color(2)), 
           tkmacosx.Button(frame, text = "B", bg = "#40743c", fg = "#ffffff", command = lambda: change_color(3)), 
           tkmacosx.Button(frame, text = "B", bg = "#40743c", fg = "#ffffff", command = lambda: change_color(4))
           ]

letters[0].grid(column=0, row=0)
letters[1].grid(column=1, row=0)
letters[2].grid(column=2, row=0)
letters[3].grid(column=3, row=0)
letters[4].grid(column=4, row=0)

letters[0].config(text="A")
letters[1].config(text="E")
letters[2].config(text="S")
letters[3].config(text="I")
letters[4].config(text="R")

submit = tkmacosx.Button(frame, text = "Submit", bg = "#000000", fg = "#ffffff", command = feedback_to_string)
submit.grid(column=2, row=1)

textfile = open(".possibleAnswers.txt", "r")
main.answers = textfile.readline().split()
textfile.close()
textfile = open(".guessables.txt", "r")
main.guessables = textfile.readline().split()
textfile.close()

flag = False
feedback = ""
guess = "aesir"
for guess_num in range(6):
    for i in range(5):
        letters[i].configure(text=guess.upper()[i])
    while not flag:
        letters[0].grid(column=0, row=0)
        letters[1].grid(column=1, row=0)
        letters[2].grid(column=2, row=0)
        letters[3].grid(column=3, row=0)
        letters[4].grid(column=4, row=0)
        submit.grid(column=2, row=1)
        root.update()
    flag = False
    main.remove(guess, feedback)
    if feedback == "ggggg":
        print(f"Yes! It only took me {guess_num + 1} tries")
        break
    elif len(main.answers) == 0:
        print("fail in the logic")
        break
    elif guess_num == 5:
        print("😵")
        break
    guess = main.optimalGuess(main.answers)
    # print(main.answers)
