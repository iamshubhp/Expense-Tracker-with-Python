import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from database import init_db  # Import at the top as usual
from app import ExpenseApp


def main():
    """
    Main entry point of the application.
    Initializes the database and launches the expense tracker app.
    """
    # Initialize the application
    app = QApplication(sys.argv)

    # Initialize Database after QApplication instance is created
    # This ensures QApplication is ready before any database operations
    if not init_db("expense.db"):
        QMessageBox.critical(None, "Error", "Could not open your database")
        sys.exit(1)  # Exit with error code if database initialization fails

    # Create and show the main window
    window = ExpenseApp()
    window.show()

    # Start the application's event loop
    # This keeps the application running until the user closes it
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
