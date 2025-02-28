# database.py

from PyQt6.QtSql import QSqlDatabase, QSqlQuery


def init_db(db_name):
    """
    Initialize the SQLite database connection.

    Args:
        db_name (str): Path to the database file

    Returns:
        bool: True if database was successfully initialized, False otherwise
    """
    # Create a database connection to SQLite
    database = QSqlDatabase.addDatabase("QSQLITE")
    database.setDatabaseName(db_name)
    if not database.open():
        return False

    # Create expenses table if it doesn't exist
    query = QSqlQuery()
    query.exec("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            description TEXT
        )
    """)
    return True


def fetch_expenses():
    """
    Retrieve all expense records from the database.

    Returns:
        list: List of expense records ordered by date (newest first)
    """
    query = QSqlQuery("SELECT * FROM expenses ORDER BY date DESC")
    expenses = []
    while query.next():
        expenses.append([query.value(i) for i in range(5)])
    return expenses


def add_expense_to_db(date, category, amount, description):
    """
    Add a new expense to the database.

    Args:
        date (str): Date of the expense in YYYY-MM-DD format
        category (str): Expense category
        amount (float): Expense amount
        description (str): Description of the expense

    Returns:
        bool: True if expense was successfully added, False otherwise
    """
    query = QSqlQuery()
    query.prepare("""
        INSERT INTO expenses (date, category, amount, description)
        VALUES (?, ?, ?, ?)
    """)
    query.addBindValue(date)
    query.addBindValue(category)
    query.addBindValue(amount)
    query.addBindValue(description)
    return query.exec()


def delete_expense_from_db(expense_id):
    """
    Delete an expense from the database.

    Args:
        expense_id (int): ID of the expense to delete

    Returns:
        bool: True if expense was successfully deleted, False otherwise
    """
    query = QSqlQuery()
    query.prepare("DELETE FROM expenses WHERE id = ?")
    query.addBindValue(expense_id)
    return query.exec()
