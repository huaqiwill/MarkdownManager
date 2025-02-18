from PySide6.QtWidgets import QToolBar, QMainWindow
from PySide6.QtGui import QAction, QIcon


class ToolBar(QToolBar):

    def __init__(self):
        super().__init__("主工具条")

        # 创建打开动作
        open_action = QAction(QIcon("open.png"), "打开", self)
        open_action.triggered.connect(self.on_open)
        self.addAction(open_action)

        # 创建保存动作
        save_action = QAction(QIcon("save.png"), "保存", self)
        save_action.triggered.connect(self.on_save)
        self.addAction(save_action)

        # 添加分隔符
        self.addSeparator()

        # 创建退出动作
        exit_action = QAction(QIcon("exit.png"), "退出", self)
        exit_action.triggered.connect(self.on_close)
        self.addAction(exit_action)

    def on_open(self):
        print("打开文件")

    def on_save(self):
        print("保存文件")

    def on_close(self):
        print("关闭程序")
