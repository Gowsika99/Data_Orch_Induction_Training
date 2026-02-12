users = []

# Add user 
def add_user(name: str) -> list[str]:
    try:
        if name.lower().startswith("adm"):
            raise ValueError("Usernames starting with 'adm' are not allowed.")
        else:
            return users.append(name)

    except ValueError as e:
        print(f"Invalid username '{name}': {e}")


# Remove User
def remove_user(users):      
    if not users:              # Empty list
        return None, users

    removed = users.pop()      # Remove last user
    return removed, users      # Return removed item + updated list
  
    

