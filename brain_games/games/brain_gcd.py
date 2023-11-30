from brain_games.cli import welcome_user
import math
import random


def wrong_answer_message(user_answer, correct_answer, user_name):
    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.\n"
          f"Let's try again, {user_name}!")


def main():
    user = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    correct_answers_count = 0
    while correct_answers_count < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_answer = math.gcd(num1, num2)
        print(f"Question: {num1} {num2}")
        user_answer = int(input("Your answer: "))
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            wrong_answer_message(user_answer, correct_answer, user)
            break
    if correct_answers_count == 3:
        print(f"Congratulations, {user}!")


if __name__ == "__main__":
    main()
