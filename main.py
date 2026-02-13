
# User Management
from users import users, add_user, remove_user

# Dummy names
add_user("Kenway")
add_user("John")
add_user("Arthur")
add_user("Edward")
add_user("Deacon")


# APPLICATION STATE

import Utils
app_state = {"app_status": "initialized", "users": 0, "quizzes": 0, "score":0}
# Entry point of the application
app_state["users"] = len(users)
def start_app():
    print("Welcome to Quiz Engine")
 # Take inputs from the user (username as key, score as value)
    user_name = input("Enter username: ").strip()
    score = input("Enter score (integer): ")

# Call the function from utils
    updated_board = Utils.update_score(user_name,score)


# Set app_state["scores"] to the score of the user you just updated
    app_state["scores"] = Utils.score_board.get(user_name, 0)

    print("Welcome to Quiz Engine")
    print("Score:", app_state["score"])

