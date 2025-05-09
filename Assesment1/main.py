from admin_section import AdminSection
from user_section import UserSection

def main():
    while True:
        print("=== Welcome to System ===")
        print("1. Login")
        print("2. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            username, is_admin = login()  # implement login function
            if username:
                if is_admin:
                    admin = AdminSection(username)
                    admin.menu()
                else:
                    user = UserSection(username)
                    user.menu()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

def login():
    # Implement login logic here,
    # Return username and boolean is_admin
    pass

if __name__ == '__main__':
    main()