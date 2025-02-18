from PySide6.QtWidgets import QApplication,QMainWindow
import sys
from app.view.main_window import MainWindow

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
