users = []


def add_user(name: str) -> list[str]:
    try:
        if name.lower().startswith("adm"):
            raise ValueError("Usernames starting with 'adm' are not allowed.")
        else:
            return users.append(name)

    except ValueError as e:
        print(f"Invalid username '{name}': {e}")



    # Adds a user to the users list and returns the updated list
    

