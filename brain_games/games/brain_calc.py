from brain_games.cli import welcome_user
import random


def correct_answer(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    else:
        return num1 - num2


def wrong_answer_message(user_answer, correct_answer, user_name):
    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.\n"
          f"Let's try again, {user_name}!")


def main():
    user = welcome_user()
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
            correct_answers_count += 1
        else:
            wrong_answer_message(
                user_answer,
                correct_answer(num1, num2, operator),
                user
            )
            break
    if correct_answers_count == 3:
        print(f"Congratulations, {user}!")


if __name__ == "__main__":
    main()
