def new_game():
    guesses = list()
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("#------------------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        question_num += 1
        guess = input("A or B or C, Your answer: ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
    dispaly_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct answer")
        return 1
    else:
        print("Wrong answer")
        return 0


def dispaly_score(correct_guesses, guesses):
    print("##########\nRESULTS: ",end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("GUESSES: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    print("Your Score is :"+str(int((correct_guesses/len(questions))*100)))

def play_agian():
    cont = input("Do you want to play again? (yes/no): ")
    if cont == "yes":
        return True
    return False


questions = {"SQL window function to get the first value? ": "B",
             "Does nested loops is a join algorithm? ":
                 "A", "Analyzer of the Query Engine takes 'parse....' from the Parser? ": "A"}
options = [["A. MIN()", "B. FIRST_VALUE", "C. INTIAL_VALUE"], ["A. Yes", "B. NO"], ["A. Tree", "B. File", "C. Object"]]

new_game()
while play_agian():
    new_game()
print("Finsih Game!")