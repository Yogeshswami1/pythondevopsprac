import sys
from PyQt5.QtWidgets import QApplication
from windows.notes_list_window import NotesListWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotesListWindow()
    window.show()
    sys.exit(app.exec_())
