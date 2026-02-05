print("Welcome to the Expense Tracker!")
def add_expense():
    print("Enter expense description:")
    description=input()
    while description.strip() == '':
        print("Description cannot be empty. Please enter a valid description:")
        description=input()
    print("Enter expense amount:")
    amount=float(input())
    if amount<=0:
        raise ValueError()
    expenses[description] = expenses.get(description, 0) + amount
    print("Expense added.")
    return
def display():
    if not expenses:
        print("No expenses recorded.")
        return
    print("All expenses:")
    for expense in expenses:
        print(f"{expense}: {expenses[expense]:.2f}")
def total_expenses():
    total = sum(expenses.values())
    print(f"Total expenses: {total:.2f}")
    return
op=0
print("Enter name of file to save expenses:")
filename = input()
file=open(filename, 'a+')
file.seek(0)
expenses = {}
if file.read() == '':
    pass
else:
    file.seek(0)
    file.readline()
    text=file.readlines()
    for line in text:
        l= line.strip().split(": ")
        desc=l[0]
        amt=l[1]
        expenses[desc] = expenses.get(desc, 0) + float(amt)
file.close()
while op!=4:
    try:
        print("1.Add new expense.\n2.View all expenses.\n3.View total expenses.\n4.Exit.\nEnter your choice:")
        op=int(input())
        if op==1:
            add_expense()
        elif op==2:
            display()
        elif op==3:
            total_expenses()
        elif op==4:
            break
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print("Exiting Expense Tracker. Goodbye!")
file=open(filename, 'w')
file.write("Expenses Log:\n")
for expense in expenses:
    file.write(f"{expense}: {expenses[expense]:.2f}\n")
file.close()