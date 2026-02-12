# APPLICATION STATE
app_state = {"status": "initialized", "users": 0, "quizzes": 0}
def start_app():
    print("App Status:", app_state["status"])

from quiz_data import add_quiz, quizzes

app_state["quizzes"] = len(quizzes)

print(app_state)

from quiz_data import quizzes  # we only need the data to display

# Task 8 

from quiz_data import quizzes

def start_app():
    print("Welcome user. Today’s quiz is:")

    # take the first quiz from the list
    first_quiz = quizzes[0]

    # print question
    print(f"<1. {first_quiz['question']}>")

    # print options as a, b, c...
    answers = first_quiz["answers"]
    option_letters = ["a", "b", "c", "d", "e", "f"]

    for i, option in enumerate(answers):
        print(f"<{option_letters[i]}. {option}>")


start_app()