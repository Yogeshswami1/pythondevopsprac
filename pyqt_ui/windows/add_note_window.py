from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QMessageBox
from services.api_service import add_note

class AddNoteWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Note")
        self.setGeometry(250, 250, 300, 200)

        layout = QVBoxLayout()

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Enter title")
        layout.addWidget(self.title_input)

        self.content_input = QTextEdit()
        self.content_input.setPlaceholderText("Enter content")
        layout.addWidget(self.content_input)

        self.save_btn = QPushButton("Save Note")
        self.save_btn.clicked.connect(self.save_note)
        layout.addWidget(self.save_btn)

        self.setLayout(layout)

    def save_note(self):
        title = self.title_input.text()
        content = self.content_input.toPlainText()

        if add_note(title, content):
            QMessageBox.information(self, "Success", "Note added successfully")
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Failed to add note")
