print("Welcome to the Expense Tracker!")
expenses = {}
op=0
print("Enter name of file to save expenses:")
filename = input()
file=open(filename, 'w')
file.write("Expenses Log\n")
while op!=4:
    try:
        print("1.Add new expense.\n2.View all expenses.\n3.View total expenses.\n4.Exit.\nEnter your choice:")
        op=int(input())
        if op==1:
            print("Enter expense description:")
            description=input()
            print("Enter expense amount:")
            amount=float(input())
            expenses[description] = amount
            file.write(f"{description}: {amount:.2f}\n")
            print("Expense added.")
        elif op==2:
            print("All expenses:")
            for expense in expenses:
                print(f"{expense}: {expenses[expense]}")
        elif op==3:
            total = sum(expenses.values())
            print(f"Total expenses: {total:.2f}")
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print("Exiting Expense Tracker. Goodbye!")
file.close()