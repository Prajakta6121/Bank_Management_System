accounts = {}

def create_account():
    username = input("Enter a username: ")
    if username in accounts:
        print("❌ Username already exists!\n")
        return
    password = input("Set a password: ")
    balance = float(input("Initial deposit amount: ₹"))
    accounts[username] = {
        "password": password,
        "balance": balance,
        "transactions": [f"Account created with ₹{balance}"]
    }
    print("✅ Account created successfully!\n")

def login():
    username = input("Enter username: ")
    if username not in accounts:
        print("❌ Account does not exist!\n")
        return None

    for attempt in range(3):
        password = input("Enter password: ")
        if accounts[username]["password"] == password:
            print("✅ Login successful!\n")
            return username
        else:
            print(f"❌ Incorrect password. Attempts left: {2 - attempt}")
    
    print("🚫 Too many incorrect attempts. Access denied.\n")
    return None

def deposit(username):
    amount = float(input("Enter amount to deposit: ₹"))
    accounts[username]["balance"] += amount
    accounts[username]["transactions"].append(f"Deposited ₹{amount}")
    print("✅ Deposit successful!\n")

def withdraw(username):
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount > accounts[username]["balance"]:
        print("❌ Insufficient funds!\n")
    else:
        accounts[username]["balance"] -= amount
        accounts[username]["transactions"].append(f"Withdrew ₹{amount}")
        print("✅ Withdrawal successful!\n")

def view_balance(username):
    balance = accounts[username]["balance"]
    print(f"💰 Current balance: ₹{balance:.2f}\n")

def view_transactions(username):
    print("📜 Transaction History:")
    for txn in accounts[username]["transactions"]:
        print(f"- {txn}")
    print()

def user_menu(username):
    while True:
        print(f"\n👤 Welcome, {username}!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. Logout")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            deposit(username)
        elif choice == "2":
            withdraw(username)
        elif choice == "3":
            view_balance(username)
        elif choice == "4":
            view_transactions(username)
        elif choice == "5":
            print("👋 Logged out.\n")
            break
        else:
            print("❌ Invalid option. Try again.\n")

def main_menu():
    while True:
        print("=== BANK MANAGEMENT SYSTEM ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            user = login()
            if user:
                user_menu(user)
        elif choice == "3":
            print("👋 Thank you for using the Bank System!")
            break
        else:
            print("❌ Invalid option. Try again.\n")

main_menu()
