from brain_games.cli import welcome_user
import random


def is_even(number):
    return number % 2 == 0


def wrong_answer_message(user_answer, correct_answer, user_name):
    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.\n"
          f"Let's try again, {user_name}!")


def main():
    user = welcome_user()
    correct_answers_count = 0
    while correct_answers_count < 3:
        question_number = random.randint(1, 100)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print(f"Question: {question_number}")
        user_answer = input("Your answer: ")
        correct_answer = 'yes' if is_even(question_number) else 'no'
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
