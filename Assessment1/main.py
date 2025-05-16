from database import create_user_table
from user_m import register_account,delete_user
from admin_m import admin_add_user, admin_change_user, admin_view_user, admin_search_user, admin_delete_user

admin_name = "admin"                                                                        #Determine admin_name is "admin" for the admin user 
admin_password = "adminpassword"                                                            #Determine admin_password is "admin_password" for the admin user

def menu():
    print("\n==== Welcome to MSE800 Car rental long range system ====")
    print("1. Register User")
    print("2. Sign in")
    print("3. Delete account")
    print("4. Exit ")


def main():                                                                                 #user_id, name, email, password, telephone, address
    create_user_table()                                                                                      
    while True:
        menu()
        choice = input("Select an option (1-4): ")
        if choice == '1':
            user_id = input("Enter User ID: ")
            password1 = input("Enter password: ")
            password2 = input("Confirm password: ")
            if password1 != password2:
                print("Passwords do not match. Please try again.")
                continue
            password = password1
            name = input("Enter name: ")
            email = input("Enter email: ")
            telephone = input("Enter telephone: ")
            address = input("Enter address: ")
            if not user_id or not name or not email or not password1 or not telephone or not address:
                print("All fields are required. Please try again.")
                continue
        
        elif choice == '2':
            user_id = input("Enter User ID: ")
            password = input("Enter password: ")

            if user_id == admin_name and password == admin_password:                        #admin login
                continue
            print("Admin login successful.")                                                #login successful (admin_name, admin_password)

            if not user_id or not password:
                print("User ID and password are required. Please try again.")
                continue
            print("Sign in successful.") #login successful (user_id, password)

        elif choice == '3':
            user_id = input("Enter User ID: ")
            password = input("Enter password: ")
            if not user_id or not password:
                print("User ID and password are required. Please try again.")
                continue
            print("Do you want to delete your account? (yes/no)")
            confirm = input("Enter your choice: ")  
            delete_user(user_id)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")                   

if __name__ == "__main__":                                              
    main()
