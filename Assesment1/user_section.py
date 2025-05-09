class UserSection:
    def __init__(self, username):
        self.username = username

    def menu(self):
        while True:
            print(f"\nUser Menu ({self.username}):")
            print("1. View/Change info")
            print("2. Change password")
            print("3. Logout")
            choice = input("Choose: ")

            if choice == '1':
                self.view_or_change_info()
            elif choice == '2':
                self.change_password()
            elif choice == '3':
                break
            else:
                print("Invalid choice.")

    def view_or_change_info(self):
        # Show current info and prompt for change
        pass

    def change_password(self):
        # Change user's password
        pass