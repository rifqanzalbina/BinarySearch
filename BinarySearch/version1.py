import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
# The GUI Using PyQt5 or if you want use PyQt6 its still good :D

# The class That we Set a GUI To BinarySearch

class BinarySearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Binary Search")
        self.setGeometry(300, 300, 400, 200)

        self.label_list = QLabel("Enter a list of numbers (comma-separated):", self)
        self.label_list.move(20, 20)

        self.entry_list = QLineEdit(self)
        self.entry_list.setGeometry(200, 20, 150, 30)

        self.button_generate = QPushButton("Generate List", self)
        self.button_generate.setGeometry(200, 60, 150, 30)
        self.button_generate.clicked.connect(self.generate_sorted_list)

        self.label_search = QLabel("Enter a number to search:", self)
        self.label_search.move(20, 100)

        self.entry = QLineEdit(self)
        self.entry.setGeometry(200, 100, 150, 30)

        self.button = QPushButton("Search", self)
        self.button.setGeometry(200, 140, 150, 30)
        self.button.clicked.connect(self.search)

        self.show()

    def generate_sorted_list(self):
        input_list = self.entry_list.text().split(",")
        input_list = [int(num.strip()) for num in input_list if num.strip()]
        self.sorted_list = sorted(input_list)

    def search(self):
        target = int(self.entry.text())
        result = self.binary_search(self.sorted_list, target)

        if result != -1:
            QMessageBox.information(self, "Result", f"Element {target} found at index {result}.")
        else:
            QMessageBox.information(self, "Result", f"Element {target} not found.")

    def binary_search(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    binary_search_app = BinarySearchApp()
    sys.exit(app.exec_())
