
# User Management
from users import users, add_user

def latest_user():
    return users[-1]

# Dummy names
add_user("Kenway")
add_user("John")
add_user("Arthur")
add_user("Edward")
add_user("Deacon")


# APPLICATION STATE
app_state = {"status": "initialized", "users": 0, "quizzes": 0}
app_state["users"] = len(users)
def start_app():
    print("App Status:", app_state["status"])
    print(f"Hello {latest_user} , welcome to the app")

start_app()





