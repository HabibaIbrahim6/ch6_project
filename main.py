# ============================================================================
# Imports
# ============================================================================
from login_and_register import login, register_user, current_user
from user_menu import user_menu
from admin_menu import admin_menu
# ====================================================================================================
# ============================================================================
# Login and Registration
# ============================================================================
print("Welcome to  Workshops & Learning Events Planner!")
print("1-->Register")
print("2-->Login")

while True:
    try:
            choice1 = int(input("Enter your choice (1-2): "))
            if choice1 == 1:
                register_user()
            elif choice1 == 2:
                current_user = login()
                break
            else:
                print("Please enter a number between 1 and 2.")
    except ValueError:
            print("Invalid choice! Please enter a number between 1 and 2.")
            continue

def main():
    if current_user is None:
        print("Please enter your login credentials.")
        exit()

    if current_user['role'] == "admin":
        admin_menu()
    elif current_user['role'] == "user":
        user_menu()
if __name__ == "__main__":
    main()