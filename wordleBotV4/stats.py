import main
import multiprocessing
import time

def solve_one(hidden_word):
    textfile = open(".possibleAnswers.txt", "r")
    main.answers = textfile.readline().split()
    textfile.close()
    textfile = open(".guessables.txt", "r")
    main.guessables = textfile.readline().split()
    textfile.close()

    guess = "aesir"
    for guess_num in range(6):
        feedback = main.get_feedback(guess, hidden_word)
        main.remove(guess, feedback)
        if feedback == "ggggg":
            return ["Success", guess_num]
        elif len(main.answers) == 0:
            return ["Fail", hidden_word]
        elif guess_num == 5:
            return ["Defeat", hidden_word]
        guess = main.optimal_guess(main.answers)

if __name__ == "__main__":
    successful = [0, 0, 0, 0, 0, 0]
    unsuccessful = []
    failed = []

    start_time = time.time()
    count = 0
    possible_answers = open(".possibleAnswers.txt", "r").readline().split()
    with multiprocessing.Pool() as pool:#Parallel Processing to make it faster. For even faster, use pypy3 instead of python3. Total time abt 10 min
        for res in pool.imap_unordered(solve_one, possible_answers):
            count += 1
            if res[0] == "Fail":
                failed.append(res[1])
            elif res[0] == "Success":
                successful[res[1]] += 1
            elif res[0] == "Defeat":
                unsuccessful.append(res[1])

            if count % 50 == 0:
                print(f"{count} done in {time.time() - start_time} seconds")

    print(f"{count} done in {time.time() - start_time} seconds")
    with open("stats.txt", "w") as stats_file:
        stats_file.writelines([f"Solved in:\n1 guess: {successful[0]}\n2 guesses: {successful[1]}\n3 guesses: {successful[2]}\n4 guesses: {successful[3]}\n5 guesses: {successful[4]}\n6 guesses: {successful[5]}\n", f"\n Words that ran out of guesses: {unsuccessful}\n", f"\nWords that failed the logic: {failed}\n", f"\nAvg. guesses per word: {(successful[0]*1+successful[1]*2+successful[3]*4+successful[4]*5+successful[5]*6)/sum(successful)}"])
