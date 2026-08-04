print("welcome to expense tracker")
expense = []
print("========MENUE========")

while (True):
    print("1. add expense")
    print("2. view all expenses")
    print("3. view total expenses")
    print("4.exit")

    choice = int(input("enter your choice"))

    if choice == 1:
        item = input("enter the item")
        amount = int(input("enter the amount"))
        date = input("enter the date(dd/mm/yyyy):")
        expense.append(item)
        expense.append(amount)
        expense.append(date)
        print("expense added successfully")
    elif choice == 2:
        for i in expense:
            print(i)
    elif choice == 3:
        totalexpense = int(input("enter the total expense(sum of all expenses):"))
        print("total expense:", totalexpense)
    elif choice == 4:
        print("exit")
        break
    else:
        print("invalid choice")
                            
