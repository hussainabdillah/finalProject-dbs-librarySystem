# mainMenu
def main_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Login as Member")
    print("2. Login as Admin")
    print("3. Exit")


# member menu
def login_member_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Borrow a Book")
    print("2. Return a Book")
    print("3. Display Borrowed Book")
    print("4. Exit")


# admin menu
def login_admin_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Display Book List")
    print("4. Logout")


# member
def borrow_book_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Borrow a Book")
    print("2. Back to Member Menu")
    print("3. Exit")


def return_book_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Return a Book")
    print("2. Back to Member Menu")
    print("3. Exit")


def display_borrowed_book_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Display Borrowed Book")
    print("2. Back to Member Menu")
    print("3. Exit")


# admin
def add_book_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Add a Book")
    print("2. Back to Admin Menu")
    print("3. Exit")


def remove_book_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Remove a Book")
    print("2. Back to Admin Menu")
    print("3. Exit")


def display_book_list_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Display Book List")
    print("2. Back to Admin Menu")
    print("3. Exit")


# Main Program
run_program = True
run_admin = True

while run_program:
    main_menu()

    main_input = input("Enter your choice: ")

    # member login logic
    if main_input == "1":
        print("Login as Member")

    # admin login logic
    elif main_input == "2":
        while run_admin:
            login_admin_menu()

            admin_input = input("Enter your choice: ")

            if admin_input == "1":
                print("Add a Book")
            elif admin_input == "2":
                print("Remove a Book")
            elif admin_input == "3":
                print("Display Book List")
            elif admin_input == "4":
                print("Logging out...")
                run_admin = False

    # exit logic
    elif main_input == "3":
        print("Exiting program...")
        run_program = False

    # invalid input logic
    else:
        print("Invalid Input, exiting program...")
        run_program = False
