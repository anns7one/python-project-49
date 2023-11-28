from brain_games.cli import welcome_user
import random


def correct_answer(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    else:
        return num1 - num2


def wrong_answer_message(user_answer, correct_answer):
    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.")


def main():
    welcome_user()
    print("What is the result of the expression?")
    correct_answers_count = 0
    while correct_answers_count < 3:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operator = random.choice(['+', '-', '*'])
        print(f"Question: {num1} {operator} {num2}")
        user_answer = int(input("Your answer: "))
        if user_answer == correct_answer(num1, num2, operator):
            print("Correct!")
        else:
            wrong_answer_message
            (user_answer, correct_answer(num1, num2, operator))
            print("Let's try again!")
        correct_answers_count += 1
    print("Congradulations!"
          "You've answered correctly 3 times.")


if __name__ == "__main__":
    main()
