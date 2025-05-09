class AdminSection:
    def __init__(self, username):
        self.username = username

    def menu(self):
        while True:
            print(f"\nAdmin Menu ({self.username}):")
            print("1. View all users")
            print("2. Change user info")
            print("3. Change own password")
            print("4. Logout")
            choice = input("Choose: ")

            if choice == '1':
                self.view_all_users()
            elif choice == '2':
                self.change_user_info()
            elif choice == '3':
                self.change_password()
            elif choice == '4':
                break
            else:
                print("Invalid choice.")

    def view_all_users(self):
        # Load and display users
        pass

    def change_user_info(self):
        # Select user and modify info
        pass

    def change_password(self):
        # Change admin's password
        pass
