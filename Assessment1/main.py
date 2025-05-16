from database import create_user_table
from user_m import register_account, sign_in, delete_user
from admin_m import (
    admin_add_user,
    admin_change_user,
    admin_view_user,
    admin_search_user,
    admin_delete_user
)

# Admin credentials
admin_name = "admin"
admin_password = "adminpassword"

def menu():
    print("\n==== Welcome to MSE800 Car Rental Long Range System ====")
    print("1. Register User")
    print("2. Sign in")
    print("3. Delete Account")
    print("4. Exit")

def main():
    create_user_table()
    while True:
        menu()
        choice = input("Select an option (1-4): ")

        if choice == '1':  # Register User
            user_id = input("Enter User ID: ")
            password1 = input("Enter password: ")
            password2 = input("Confirm password: ")
            if password1 != password2:
                print("Passwords do not match. Please try again.")
                continue
            name = input("Enter name-surname: ")
            email = input("Enter email: ")
            telephone = input("Enter telephone: ")
            address = input("Enter address: ")
            if not user_id or not password1 or not name or not email:
                print("All fields are required. Please try again.")
                continue
            register_account(user_id, password1, name, email, telephone, address)

        elif choice == '2':  # Sign in
            while True:
                user_id = input("Enter User ID: ")
                password = input("Enter password: ")
                if not user_id or not password:
                    print("User ID and password are required. Please try again.")
                    continue
        
                # Verify credentials
                if sign_in(user_id, password):
                    print("Sign in successful.")
                    # You may break the loop here if sign-in is successful
                    break
                else:
                    print("Incorrect user ID or password. Please try again.")

        elif choice == '3':  # Delete account
            user_id = input("Enter User ID: ")
            password = input("Enter password: ")
            if not sign_in(user_id, password):
                print("Incorrect user ID or password.")
                continue
            confirmation = input("Do you want to delete this account? (yes/no): ").lower()
            if confirmation in ('yes', 'y'):
                delete_user(user_id)
                print("Account deleted.")
            else:
                print("Deletion canceled.")

        elif choice == '4':  # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
