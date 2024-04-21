import random

# Questions and their corresponding correct answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Berlin", "D. Rome"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. J.K. Rowling", "B. Harper Lee", "C. George Orwell", "D. Charles Dickens"],
        "answer": "B"
    },
    {
        "question": "What is the powerhouse of the cell?",
        "options": ["A. Mitochondria", "B. Nucleus", "C. Ribosome", "D. Endoplasmic reticulum"],
        "answer": "A"
    }
    # Add more questions here if needed
]


def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    return answer


def kbc_game(questions):
    random.shuffle(questions)  # Shuffle the questions
    total_questions = len(questions)
    correct_answers = 0
    for i, question in enumerate(questions, start=1):
        print(f'\nQuestion {i}/{total_questions}:')
        answer = display_question(question)
        if answer == question["answer"]:
            print("Correct answer!")
            correct_answers += 1
        else:
            print("Wrong answer!")
            break  # End the game if the answer is wrong
    # Calculate the amount based on correct answers
    amount = correct_answers * 10000  # Assuming each correct answer wins Rs. 10,000
    return amount


def main():
    print("Welcome to Kaun Banega Crorepati!")
    print("Answer the following questions to win money.")
    print("You will win Rs. 10,000 for each correct answer.")
    print("Let's start!\n")

    total_amount = kbc_game(questions)

    print("\nCongratulations on completing the game!")
    print(f"You won a total amount of Rs. {total_amount:,}!")
    print("Thank you for playing!")


if __name__ == "__main__":
    main()
