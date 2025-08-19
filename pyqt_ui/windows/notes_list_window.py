from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QMessageBox
from services.api_service import get_notes
from windows.add_note_window import AddNoteWindow

class NotesListWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Notes")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.refresh_btn = QPushButton("Refresh Notes")
        self.refresh_btn.clicked.connect(self.load_notes)
        layout.addWidget(self.refresh_btn)

        self.add_btn = QPushButton("Add Note")
        self.add_btn.clicked.connect(self.open_add_note_window)
        layout.addWidget(self.add_btn)

        self.setLayout(layout)
        self.load_notes()

    def load_notes(self):
        self.list_widget.clear()
        notes = get_notes()
        if notes:
            for note in notes:
                self.list_widget.addItem(f"{note['title']} - {note['content']}")
        else:
            QMessageBox.information(self, "Info", "No notes found")

    def open_add_note_window(self):
        self.add_window = AddNoteWindow(self)
        self.add_window.show()
