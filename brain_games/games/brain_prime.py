from brain_games.cli import welcome_user
import random


def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


def main():
    user = welcome_user()
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    answers_count = 0
    correct_answers_count = 0
    while answers_count < 3:
        num = random.randint(1, 3571)
        print(f"Question: {num}")
        user_answer = input("Your answer: ")
        if (user_answer == 'yes' and is_prime(num)) or \
           (user_answer == 'no' and not is_prime(num)):
            print("Correct!")
            correct_answers_count += 1
        else:
            correct_answer = 'yes' if is_prime(num) else 'no'
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again! {user}")
        answers_count += 1
    if correct_answers_count == 3:
        print(f"Congradulations! {user}")


if __name__ == "__main__":
    main()
