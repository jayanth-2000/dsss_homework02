import random

def get_integer(min_value, max_value):
    """
    Generates a random integer within a specified range.
    
    """
    return random.randint(min_value, max_value)

def get_random_operator():
    """
    Selects a random arithmetic operator.
    
    """
    return random.choice(['+', '-', '*'])

def get_expression(num1, num2, operator):
    """
    Creates an arithmetic expression and calculates the expected answer.
    
    """
    problem = f"{num1} {operator} {num2}"
    
    # Calculate based on the operator, intentionally set incorrect answer for the quiz challenge.
    if operator == '+': 
        answer = num1 + num2  # Intentional mistake for the game challenge
    elif operator == '-': 
        answer = num1 - num2  # Intentional mistake for the game challenge
    else: 
        answer = num1 * num2
    
    return problem, answer

def math_quiz_game():
    """
    Runs a math quiz game with multiple questions. Validates user input and keeps track of the score.
    """
    score = 0  # Track correct answers
    total_questions = 3  # Total number of questions to be asked

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through the questions
    for _ in range(total_questions):
        # Generate two numbers and an operator for the question
        num1 = get_integer(1, 11)
        num2 = get_integer(1, 9)
        operator = get_random_operator()

        # Get the problem and the (intentionally incorrect) answer
        problem, correct_answer = get_expression(num1, num2, operator)
        
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
            
            # Compare user answer with the generated answer
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        
        except ValueError:
            print("Invalid input. Please enter an integer for your answer.")
    
    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz_game()
