from database import (
    create_table,
    add_transaction,
    view_transactions,
    total_spending,
    category_spending,
    monthly_spending,
    view_by_month,
    plot_category_spending,
    plot_monthly_spending
)

# Create database table
create_table()


while True:
    print("\n=== Personal Finance Analyzer ===")
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. Total Spending")
    print("4. Category-wise Spending")
    print("5. Monthly Spending")
    print("6. View Transactions by Month")
    print("7. Show Category Chart")
    print("8. Show Monthly Chart")
    print("9. Exit")

    choice = input("Enter choice: ")

    # 🔹 Add Transaction
    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        add_transaction(date, amount, category, description)
        print("Transaction saved successfully!")

    # 🔹 View All Transactions
    elif choice == "2":
        data = view_transactions()
        print("\n--- All Transactions ---")
        for row in data:
            print(row)

    # 🔹 Total Spending
    elif choice == "3":
        total = total_spending()
        print("Total Spending:", total)

    # 🔹 Category-wise Spending
    elif choice == "4":
        data = category_spending()
        print("\nCategory Breakdown:")
        for cat, amt in data:
            print(cat, ":", amt)

    # 🔹 Monthly Spending
    elif choice == "5":
        month = input("Enter month (01-12): ")
        total = monthly_spending(month)
        print("Total spending for month:", total)

    # 🔹 View by Month
    elif choice == "6":
        month = input("Enter month (01-12): ")
        data = view_by_month(month)

        print("\nTransactions in selected month:")
        for row in data:
            print(row)

    # 🔹 Category Chart
    elif choice == "7":
        plot_category_spending()

    # 🔹 Monthly Chart2
    elif choice == "8":
        plot_monthly_spending()

    # 🔹 Exit
    elif choice == "9":
        print("Exiting program...")
        break

    # 🔹 Invalid input
    else:
        print("Invalid choice, please try again.")