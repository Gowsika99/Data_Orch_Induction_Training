quizzes = []

def add_quiz(question, answers, correct_ans, score):
    quiz_item = {
        "question": question,
        "answers": answers,
        "correct_ans": correct_ans,
        "score": score
    }
    quizzes.append(quiz_item)
    return quizzes

add_quiz(
    "What is the capital of India?",
    ["Delhi", "Mumbai", "Chennai", "Kolkata"],
    "Delhi",
    10
)
add_quiz(
    "Who wrote the Harry Potter series?",
    ["J.K. Rowling", "Enid Blyton", "C.S. Lewis", "George Orwell"],
    "J.K. Rowling",
    8
)