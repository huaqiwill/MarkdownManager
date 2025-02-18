from PySide6.QtWidgets import QMainWindow
from app.components.menubar import MenuBar
from app.components.toolbar import ToolBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,800,600)
        self.setWindowTitle("Markdown管理工具")

        menubar = MenuBar()
        self.setMenuBar(menubar)

        toolbar = ToolBar()
        self.addToolBar(toolbar)
