from brain_games.cli import welcome_user


def main():
    user = welcome_user()
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    answers_count = 0
    correct_answers_count = 0
    while answers_count < 3:
        
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
