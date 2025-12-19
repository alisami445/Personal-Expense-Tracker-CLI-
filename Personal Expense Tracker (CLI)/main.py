from datetime import date
import csv
def Menu_view():
    print("\n1. Add Data")
    print("2. View Data")
    print("3. Filter Data")
    print("4. Show Statistics")
    print("5. Exit")
def Menu_sel():
    menu_options = input("pick ur menu option(1-5): ")
    while not(menu_options.isnumeric() and 1<=int(menu_options)<=5):
        menu_options = input("pick ur menu option(1-5): ")
    return int(menu_options)
def AddData(filename):
    while True:
        try:
            day=int(input("\n Enter the day: "))
            month=int(input(" Enter the month: "))
            year=int(input(" Enter the year: "))
            Date = date(year, month, day)
            break
        except ValueError:
            print(" Invalid date. Please re-enter.")      

    Type=input(" Enter the type of data (income/expense): ")
    while Type =="" or not(Type=="income" or Type=="expense"):
        print(" Invalid type. Please re-enter.")
        Type=input("Enter the type of data (income/expense):")
    
    category=input(" Enter the category(food, rent, transport...): ")
    while category=="":
        print(" Invalid category. Please re-enter.")
        category=input(" Enter the category(food, rent, transport...): ")
    
    while True :
        amount=input(" Enter the amount: ")
        try:
            amount=float(amount)
            if amount>0:
                break
            else:
                print(" Amount must be positive. Please re-enter.")
        except ValueError:
            print(" Invalid amount. Please enter a numeric value.")

    note=input(" Enter any notes (optional): ")   

    print(f" Date entered: {day:02d}/{month:02d}/{year}")
    print(f"type of data entered:{Type}")
    print(f" category entered: {category}")
    print(f" amount entered: {amount}")
    print(f" note entered: {note}")
    with open(filename,"a",newline="") as csvfile:
        csvfile_writer=csv.writer(csvfile)
        csvfile_writer.writerow([f"{day:02d}/{month:02d}/{year}",Type,category,amount,note])
        print(" Data added successfully.")  
def ViewData():
    with open("DATA.csv","r") as csvfile:
        csvfile_reader=csv.reader(csvfile)
        csvfile_header=next(csvfile_reader)
        print("\n"+"-"*50)
        print(f"{csvfile_header[0]}| {csvfile_header[1]} | {csvfile_header[2]} | {csvfile_header[3]} | {csvfile_header[4]}")
        print("\n"+"-"*50)
        for row in csvfile_reader:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
        print("-"*50)
def FilterData():
    while True:
        filter_type=input("\n Filter by (date/type/category): ")
        try:
            if filter_type=="date":
                while True:
                    try:
                        month=int(input(" Enter the month (1-12): "))
                        if 1<=month<=12:
                            break
                    except ValueError:
                        print(" Invalid month. Please re-enter.")
                with open("DATA.csv","r") as csvfile:
                    csvfile_reader=csv.reader(csvfile)
                    csv_file_header=next(csvfile_reader)
                    print("\n"+"-"*50)
                    print(f"{csv_file_header[0]}| {csv_file_header[1]} | {csv_file_header[2]} | {csv_file_header[3]} | {csv_file_header[4]}")
                    print("\n"+"-"*50)
                    for row in csvfile_reader:
                        if int(row[0].split("/")[1])==month:
                            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
                    break
            elif filter_type=="type":
                type_value=input(" Enter the type to filter by (income/expense): ")
                while type_value=="" or not(type_value=="income" or type_value=="expense"):
                    print(" Invalid type. Please re-enter.")
                    type_value=input(" Enter the type to filter by (income/expense): ")
                with open("DATA.csv","r") as csvfile:
                    csvfile_reader=csv.reader(csvfile)
                    csv_file_header=next(csvfile_reader)
                    print("\n"+"-"*50)
                    print(f"{csv_file_header[0]}| {csv_file_header[1]} | {csv_file_header[2]} | {csv_file_header[3]} | {csv_file_header[4]}")
                    print("\n"+"-"*50)
                    for row in csvfile_reader:
                        if row[1]==type_value:
                            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
                    break
            elif filter_type=="category":
                category_value=input(" Enter the category to filter by: ")
                while category_value=="":
                    print(" Invalid category. Please re-enter.")
                    category_value=input(" Enter the category to filter by: ")
                with open("DATA.csv","r") as csvfile:
                    csvfile_reader=csv.reader(csvfile)
                    csv_file_header=next(csvfile_reader)
                    print("\n"+"-"*50)
                    print(f"{csv_file_header[0]}| {csv_file_header[1]} | {csv_file_header[2]} | {csv_file_header[3]} | {csv_file_header[4]}")
                    print("\n"+"-"*50)
                    for row in csvfile_reader:
                        if row[2]==category_value:
                            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
                    break
        except ValueError:
            print(" Invalid filter type. Please re-enter.")
def ShowStats():
    total_income=0
    total_expenses=0
    Net_balance=0
    with open("DATA.csv","r") as csvfile:
        csvfile_reader=csv.reader(csvfile)
        for row in csvfile_reader:
            if row[1]=="income":
                total_income+=float(row[3])
            elif row[1]=="expense":
                total_expenses+=float(row[3])
    Net_balance=total_income - total_expenses
    print(f"\n Total Income: {total_income}")
    print(f" Total Expenses: {total_expenses}")
    print(f" Net Balance: {Net_balance}")
    category_totals = {}
    with open("DATA.csv", "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            if row["type"] == "expense":
                category = row["category"]
                amount = float(row["amount"])
                if category not in category_totals:
                    category_totals[category] = amount
                else:
                    category_totals[category] += amount
        
    sorted_categories = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
    top3 = sorted_categories[:3]
    print("\nTop 3 Expense Categories:")
    i = 1
    for item in top3:
        cat = item[0] 
        total = item[1]
        print(str(i) + ". " + cat + " — " + str(total))
        i = i + 1

filename="DATA.csv"
while True:
    Menu_view()
    choice=Menu_sel()
    if choice == 1:
        AddData(filename)
    elif choice == 2:
        ViewData()
    elif choice == 3:
        FilterData()
    elif choice == 4:
        ShowStats()
    elif choice == 5:
        print("Exiting the program.")
        break