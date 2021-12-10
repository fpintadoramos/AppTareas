from io import FileIO
import sys
import json
from PySide6 import QtGui
from PySide6.QtCore import QAbstractListModel, QSize, Qt

from PySide6.QtCore import QAbstractListModel, QSize
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow
from TaskModel import TaskModel

from ui_designmodel import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        listView = self.listView
        self.model = TaskModel()
        listView.setModel(self.model)

        self.t = self.lineEdit
        PBAdd = self.PBAdd
        PBDel = self.PBDel

        PBAdd.clicked.connect(self.add)
        PBDel.clicked.connect(self.dele)

        self.a = self.actionA_adir
        self.a.triggered.connect(self.add)

        self.d = self.actionEliminar
        self.d.triggered.connect(self.dele)

        try:
            with open("tareas2.json") as f:
                self.model.tasks = json.load(f)
        except Exception:
            self.model.tasks = []

    def add(self):
        self.model.tasks.append(self.t.text())
        with open("tareas2.json" , "w") as f:
            json.dump(self.model.tasks, f)
        self.model.layoutChanged.emit()
        
    def dele(self):
        check = self.listView.selectedIndexes()[0].row()
        del self.model.tasks[check]
        with open("tareas2.json" , "w") as f:
            json.dump(self.model.tasks, f)
        self.model.layoutChanged.emit()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()