# expense_app.py

from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit, QTableWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import QDate, Qt
from database import fetch_expenses, add_expense_to_db, delete_expense_from_db


class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_table_data()

    def init_ui(self):
        self.setWindowTitle("Expense-Tracker")
        self.resize(550, 500)

        # Initialize Widgets
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.add_button = QPushButton("Add Expense")
        self.delete_button = QPushButton("Delete Expense")

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(
            ["Id", "Date", "Category", "Amount", "Description"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Connect Buttons to Methods
        self.add_button.clicked.connect(self.add_expense)
        self.delete_button.clicked.connect(self.delete_expense)

        # Setup Layouts
        self.setup_layout()

        # Populate Dropdown Categories
        self.populate_dropdown()

        # Apply Styling
        self.apply_styles()

    def setup_layout(self):
        layout = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()

        # Row 1
        row1.addWidget(QLabel("Date:"))
        row1.addWidget(self.date_box)
        row1.addWidget(QLabel("Category:"))
        row1.addWidget(self.dropdown)

        # Row 2
        row2.addWidget(QLabel("Amount:"))
        row2.addWidget(self.amount)
        row2.addWidget(QLabel("Description:"))
        row2.addWidget(self.description)

        # Row 3 (Buttons)
        row3.addWidget(self.add_button)
        row3.addWidget(self.delete_button)

        # Add rows to main layout
        layout.addLayout(row1)
        layout.addLayout(row2)
        layout.addLayout(row3)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def populate_dropdown(self):
        categories = ["Food", "Transportation", "Rent",
                      "Shopping", "Entertainment", "Bills", "Other"]
        self.dropdown.addItems(categories)

    def apply_styles(self):
        self.setStyleSheet
    ("""
    
    /* Base styling */
QWidget { 
    background-color: #2c3e50; 
    font-family: 'Segoe UI', Arial, sans-serif; 
    font-size: 14px; 
    color: #ecf0f1; 
} 

/* Headings for labels */ 
QLabel { 
    font-size: 15px; 
    color: #3498db; 
    font-weight: bold; 
    padding: 5px; 
    text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.3); 
} 

/* Styling for input fields */ 
QLineEdit, QComboBox, QDateEdit { 
    background-color: #34495e; 
    font-size: 14px; 
    color: #ecf0f1; 
    border: 1px solid #3498db; 
    border-radius: 5px; 
    padding: 8px; 
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.3); 
} 

QLineEdit:hover, QComboBox:hover, QDateEdit:hover { 
    border: 1px solid #1abc9c; 
    background-color: #2c3e50; 
} 

QLineEdit:focus, QComboBox:focus, QDateEdit:focus { 
    border: 2px solid #1abc9c; 
    background-color: #2c3e50; 
    box-shadow: 0 0 5px rgba(26, 188, 156, 0.5); 
} 

/* Dropdown styling */
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 25px;
    border-left: 1px solid #3498db;
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
}

QComboBox::down-arrow {
    image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTEyIDRsLTUgNS01LTUiIHN0cm9rZT0iI2VjZjBmMSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz48L3N2Zz4=);
}

QComboBox QAbstractItemView {
    border: 1px solid #3498db;
    background-color: #34495e;
    border-radius: 5px;
    padding: 5px;
    selection-background-color: #1abc9c;
}

/* Table styling */ 
QTableWidget { 
    background-color: #34495e; 
    alternate-background-color: #2c3e50; 
    gridline-color: #3498db; 
    selection-background-color: #1abc9c; 
    selection-color: white; 
    font-size: 14px; 
    border: 1px solid #3498db; 
    border-radius: 5px; 
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3); 
} 

QHeaderView::section { 
    background-color: #16a085; 
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1abc9c, stop:1 #16a085); 
    color: white; 
    font-weight: bold; 
    padding: 8px; 
    border: none; 
    border-right: 1px solid #2c3e50;
    border-bottom: 1px solid #2c3e50;
} 

QTableView::item {
    padding: 6px;
    border-bottom: 1px solid #2c3e50;
}

QTableView::item:selected {
    background-color: #1abc9c;
    color: #ecf0f1;
}

/* Scroll bar styling */ 
QScrollBar:vertical { 
    width: 14px; 
    background-color: #2c3e50; 
    border: none; 
    border-radius: 7px; 
    margin: 0px;
} 

QScrollBar::handle:vertical { 
    background-color: #3498db; 
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #3498db, stop:1 #2980b9); 
    min-height: 30px; 
    border-radius: 7px; 
} 

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1abc9c, stop:1 #16a085);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { 
    background: none; 
    height: 0px;
} 

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

/* Buttons */ 
QPushButton { 
    background-color: #3498db; 
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #3498db, stop:1 #2980b9); 
    color: white; 
    padding: 10px 15px; 
    border-radius: 5px; 
    font-size: 14px; 
    font-weight: bold; 
    border: none; 
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3); 
} 

QPushButton:hover { 
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1abc9c, stop:1 #16a085); 
    box-shadow: 0 3px 5px rgba(0, 0, 0, 0.4); 
} 

QPushButton:pressed { 
    background: #16a085; 
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.4); 
} 

QPushButton:disabled { 
    background-color: #7f8c8d; 
    color: #bdc3c7; 
    box-shadow: none; 
} 

/* Delete button special styling */
QPushButton#delete_button {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e74c3c, stop:1 #c0392b);
}

QPushButton#delete_button:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #c0392b, stop:1 #a33025);
}

QPushButton#delete_button:pressed {
    background: #a33025;
}

/* Tooltip styling */ 
QToolTip { 
    background-color: #34495e; 
    color: #ecf0f1; 
    border: 1px solid #3498db; 
    font-size: 12px; 
    padding: 5px; 
    border-radius: 4px; 
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4); 
    opacity: 220;
}

/* Calendar popup styling */
QCalendarWidget {
    background-color: #34495e;
    color: #ecf0f1;
}

QCalendarWidget QToolButton {
    color: #ecf0f1;
    background-color: #2c3e50;
    padding: 5px;
    border-radius: 3px;
}

QCalendarWidget QMenu {
    background-color: #34495e;
    color: #ecf0f1;
}

QCalendarWidget QSpinBox {
    background-color: #34495e;
    color: #ecf0f1;
    border: 1px solid #3498db;
    border-radius: 3px;
}

QCalendarWidget QTableView {
    background-color: #34495e;
    selection-background-color: #1abc9c;
    selection-color: #ecf0f1;
    border: none;
}

QCalendarWidget QAbstractItemView:enabled {
    color: #ecf0f1;
}

QCalendarWidget QAbstractItemView:disabled {
    color: #7f8c8d;
}
""")

    def load_table_data(self):
        expenses = fetch_expenses()
        self.table.setRowCount(0)
        for row_idx, expense in enumerate(expenses):
            self.table.insertRow(row_idx)
            for col_idx, data in enumerate(expense):
                self.table.setItem(
                    row_idx, col_idx, QTableWidgetItem(str(data)))

    def add_expense(self):
        date = self.date_box.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText()
        amount = self.amount.text()
        description = self.description.text()

        if not amount or not description:
            QMessageBox.warning(self, "Input Error",
                                "Amount and Description cannot be empty!")
            return

        if add_expense_to_db(date, category, amount, description):
            self.load_table_data()
            self.clear_inputs()
        else:
            QMessageBox.critical(self, "Error", "Failed to add expense")

    def delete_expense(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection",
                                "Please select an expense to delete.")
            return

        expense_id = int(self.table.item(selected_row, 0).text())
        confirm = QMessageBox.question(self, "Confirm", "Are you sure you want to delete this expense?",
                                       QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if confirm == QMessageBox.StandardButton.Yes and delete_expense_from_db(expense_id):
            self.load_table_data()

    def clear_inputs(self):
        self.date_box.setDate(QDate.currentDate())
        self.dropdown.setCurrentIndex(0)
        self.amount.clear()
        self.description.clear()
