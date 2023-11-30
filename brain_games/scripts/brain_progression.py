from brain_games.cli import welcome_user
import random


def main():
    user = welcome_user()
    print("What number is missing in the progression?")
    answers_count = 0
    correct_answers_count = 0
    result = []
    while answers_count < 3:
        step = random.randint(1, 5)
        first_element = random.randint(1, 10)
        progression_length = random.randint(5, 10)
        for num in range(progression_length):
            progression = first_element + num * step
            result.append(str(progression))
            index_colon = random.randint(0, len(result) - 1)
        correct_result = result[index_colon]
        result[index_colon] = '..'
        print(' '.join(result))
        result.clear()
        user_answer = int(input("Your answer: "))
        if user_answer == int(correct_result):
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_result}'.")
            print(f"Let's try again! {user}")
        answers_count += 1
    if correct_answers_count == 3:
        print(f"Congradulations! {user}")


if __name__ == "__main__":
    main()
