import json
from PySide6.QtCore import QAbstractListModel, QSize, Qt

class TaskModel(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.tasks = []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.tasks[index.row()]
    
    def rowCount(self, index):
        return len(self.tasks)


    