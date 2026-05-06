import sqlite3
import matplotlib.pyplot as plt


# 🔹 Connect to database
def connect():
    return sqlite3.connect("finance.db")


# 🔹 Create table
def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            amount REAL,
            category TEXT,
            description TEXT
        )
    """)

    conn.commit()
    conn.close()


# 🔹 Add transaction
def add_transaction(date, amount, category, description):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions (date, amount, category, description)
        VALUES (?, ?, ?, ?)
    """, (date, amount, category, description))

    conn.commit()
    conn.close()


# 🔹 View all transactions
def view_transactions():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()

    conn.close()
    return rows


# 🔹 Total spending
def total_spending():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM transactions")
    total = cursor.fetchone()[0]

    conn.close()
    return total if total else 0


# 🔹 Category-wise spending
def category_spending():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM transactions
        GROUP BY category
    """)

    data = cursor.fetchall()
    conn.close()
    return data


# 🔹 Monthly spending
def monthly_spending(month):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount)
        FROM transactions
        WHERE strftime('%m', date) = ?
    """, (month,))

    total = cursor.fetchone()[0]

    conn.close()
    return total if total else 0


# 🔹 View transactions by month
def view_by_month(month):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM transactions
        WHERE strftime('%m', date) = ?
    """, (month,))

    rows = cursor.fetchall()
    conn.close()
    return rows


# 🔹 Plot category spending (Bar Chart)
def plot_category_spending():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM transactions
        GROUP BY category
    """)

    data = cursor.fetchall()
    conn.close()

    if not data:
        print("No data to display")
        return

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.bar(categories, amounts)
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()


# 🔹 Plot monthly spending (Line Chart)


def plot_monthly_spending():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT strftime('%m', date) as month, SUM(amount)
        FROM transactions
        WHERE date IS NOT NULL
        GROUP BY month
        ORDER BY month
    """)

    data = cursor.fetchall()
    conn.close()

    if not data:
        print("No data to display")
        return

    # 🔥 filter out bad values (VERY IMPORTANT)
    months = []
    amounts = []

    for row in data:
        if row[0] is not None and row[1] is not None:
            months.append(row[0])
            amounts.append(row[1])

    plt.plot(months, amounts, marker='o')
    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.show()